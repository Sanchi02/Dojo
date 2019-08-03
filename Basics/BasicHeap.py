       
class Heap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def heapify(self,index):
        while(index//2 > 0):
            if (self.heapList[index] > self.heapList[index//2]):
                self.heapList[index], self.heapList[index//2] = self.heapList[index//2], self.heapList[index]
            index = index//2
    
    def insert(self,data):
        self.heapList.append(data)
        self.currentSize = self.currentSize + 1
        self.heapify(self.currentSize)
        
    def getMinChild(self,i):
        if i * 2 + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i*2] > self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1
        
    def afterExtract(self,i):
        while (i * 2) <= self.currentSize:
            minChild = self.getMinChild(i)
            if self.heapList[i] < self.heapList[minChild]:
                self.heapList[i], self.heapList[minChild] = self.heapList[minChild], self.heapList[i]
            i = minChild
            
    def extractMax(self):
        max = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize = self.currentSize - 1
        self.heapList.pop()
        self.afterExtract(1)
        return max
  
    def printer(self):
        print(self.heapList)
        
heaper = Heap()
list1 = [3,23,7,75,19,2,1]
for i in list1:
    heaper.insert(i)
heaper.printer()
print(heaper.extractMax())
heaper.printer()
            
