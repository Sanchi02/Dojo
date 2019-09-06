def myCompare():
    class K(object):
        def __init__(self, obj):
            self.obj = obj
        def __lt__(self, other):
            a, b = str(self.obj), str(other.obj)
            ab = a + b
            ba = b + a
            return (((int(ba) > int(ab)) - (int(ba) < int(ab))) < 0 )
    return K

# driver code 
if __name__ == "__main__": 
	a = [4,2,3,1] 
	sorted_array = sorted(a, key=myCompare()) 
	number = "".join([str(i) for i in sorted_array]) 
	print(number) 


