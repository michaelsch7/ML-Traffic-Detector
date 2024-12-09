from TrainingLoader import *

yes, no = load_arrays_from_pics()
X_train, X_test, y_train, y_test = create_train_data_from_array(yes, no)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

import tensorflow as tf

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

model.fit(X_train, y_train, epochs=10)