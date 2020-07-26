# Design and implement a data structure for a compressed string iterator. It should support the following operations: next and hasNext.

# The given compressed string will be in the form of each letter followed by a positive integer representing the number of this letter existing in the original uncompressed string.

# next() - if the original string still has uncompressed characters, return the next letter; Otherwise return a white space.
# hasNext() - Judge whether there is any letter needs to be uncompressed.

# Note:
# Please remember to RESET your class variables declared in StringIterator, as static/class variables are persisted across multiple test cases. Please see here for more details.

# Example:

# StringIterator iterator = new StringIterator("L1e2t1C1o1d1e1");

# iterator.next(); // return 'L'
# iterator.next(); // return 'e'
# iterator.next(); // return 'e'
# iterator.next(); // return 't'
# iterator.next(); // return 'C'
# iterator.next(); // return 'o'
# iterator.next(); // return 'd'
# iterator.hasNext(); // return true
# iterator.next(); // return 'e'
# iterator.hasNext(); // return false
# iterator.next(); // return ' '

class StringIterator:
    
    def __init__(self, compressedString: str):
        self.compressedString = compressedString
        self.alpha = []
        self.counts = []
        ptr = 0
        while(ptr!=len(compressedString)):
            tmp = ''
            if(compressedString[ptr].isalpha()):
                self.alpha.append(compressedString[ptr])
                ptr += 1
                while(ptr!=len(compressedString) and compressedString[ptr].isdigit()):
                    tmp = tmp + compressedString[ptr]
                    ptr += 1
                # print("tmp = {}".format(tmp))
                self.counts.append(int(tmp))
#         print(self.alpha)
#         print(self.counts)
        
    def next(self) -> str:
        if(len(self.alpha)==0):
            return ' '
        tmp = self.alpha[0]
        self.counts[0] -= 1
        if(self.counts[0]==0):
            self.alpha.pop(0)
            self.counts.pop(0)
        # print("From next = {}".format(self.alpha))
        # print("From next = {}".format(self.counts))
        return tmp
