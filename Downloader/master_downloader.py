import TrafficDataAcadian
import TrafficDataCollege
import TrafficDataCityplace
import TrafficDataLA1
import TrafficDataLA415
import TrafficDataNicholson
from multiprocessing import Process

if __name__ == "__main__":
    p1 = Process(target=TrafficDataAcadian.printAcadianDrive)
    p1.start()
    
    p2 = Process(target=TrafficDataCollege.printCollegeDrive)
    p2.start()
    
    p3 = Process(target=TrafficDataCityplace.printCityplace)
    p3.start()
    
    p4 = Process(target=TrafficDataLA1.printLA1)
    p4.start()
    
    p5 = Process(target=TrafficDataLA415.printLA415)
    p5.start()
    
    p6 = Process(target=TrafficDataNicholson.printNicholson)
    p6.start()
    
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()
