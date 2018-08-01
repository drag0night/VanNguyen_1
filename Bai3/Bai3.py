import random as rd

class Point:  
    def __init__(self,_x,_y):
        self.x = _x
        self.y = _y
    def __hash__(self):
        hash = 3
        hash = 71 * hash + self.x
        hash = 71 * hash + self.y
        return hash
    def __eq__(self,other):
        return ( self.x == other.x and self.y == other.y and self.__class__ == other.__class__)

if __name__ == "__main__":
    set_collection = set()
    i=0
    while i<1000:
        x = rd.randint(0,50)
        y = rd.randint(0,50)
        temp = Point(x,y)
        if temp not in set_collection:
            i+=1
            set_collection.add(temp)
    
    i=1
    fw = open("output.txt","w")
    for elem in set_collection:
        s = "-Point %d: (%d,%d)\n" % ( i,elem.x,elem.y )
        fw.write(s)
        i+=1
    fw.close()