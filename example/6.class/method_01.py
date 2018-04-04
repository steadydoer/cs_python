class CounterManager:
    insCount = 0#인스턴스가 하나도 없더라도 속성이 메모리에 위치함 
    def __init__(self):
        CounterManager.insCount += 1
    def staticPrintCount():
        print("Instance Count: ", CounterManager.insCount)
    SPrintCount = staticmethod(staticPrintCount)

    def classPrintCount(cls):
        print("Instance Count: ", CounterManager.insCount)
    CPrintCount = classmethod(classPrintCount)
    #def printInstaceCount():
    #    print("Instance Count: ", CounterManager.insCount)


A, b, c = CounterManager(), CounterManager(), CounterManager()
#CounterManager.printInstaceCount()
#b.printInstaceCount()

CounterManager.SPrintCount()
b.SPrintCount()

CounterManager.CPrintCount()
b.CPrintCount()

#
