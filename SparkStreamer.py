from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit, udf,current_timestamp
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, BinaryType, ArrayType, IntegerType
from PIL import Image
import tensorflow as tf
import numpy as np
import io

spark = SparkSession \
    .builder \
    .master("local") \
    .appName("Image Streaming") \
    .getOrCreate()

image_schema = StructType([
    StructField("image", StructType([
        StructField("origin", StringType(), True),
        StructField("height", IntegerType(), True),
        StructField("width", IntegerType(), True),
        StructField("nChannels", IntegerType(), True),
        StructField("mode", IntegerType(), True),
        StructField("data", BinaryType(), True)
    ]), True)
])

model = tf.keras.models.Sequential([
  tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(240, 352, 3)),  
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)), 
  tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),  
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),  
  tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),  
  tf.keras.layers.MaxPooling2D(pool_size=(2, 2)), 
  tf.keras.layers.Flatten(),  
  tf.keras.layers.Dense(128, activation='relu'), 
  tf.keras.layers.Dropout(0.2),  
  tf.keras.layers.Dense(2, activation='softmax')  
])
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.load_weights('cnn_weights.weights.h5')


def to_rgb(data):
    image = Image.open(io.BytesIO(data))
    print(image)
    image = image.resize((352, 240))
    rgb_values = np.array(image)
    
    return rgb_values

to_rgbUDF = udf(to_rgb, ArrayType(ArrayType(IntegerType())))

initDF = (
    spark
    .readStream
    .format("image")
    .schema(image_schema)
    .option("path", "s3://bucket-michaels/dev/CollegeStreamData/")
    .load()
)
print(initDF.isStreaming)

resultDF = initDF.withColumn("pixel_size", col("image.height") * col("image.width")) \
                 .withColumn("Camera Name", lit( "I-10 @ College Drive")) \
                 .withColumn("rgb_values", to_rgbUDF(col("image.data")))\
                 .withColumn("timestamp", current_timestamp())\
                 .withColumn("traffic", lit(model.predict(col('rgb_values'))))

resultDF \
    .select( "Camera Name", "timestamp", "traffic") \
    .writeStream \
    .outputMode("append") \
    .option("truncate", False) \
    .format("console") \
    .start() \
    .awaitTermination()




