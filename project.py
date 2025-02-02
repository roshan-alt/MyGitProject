# Stack Implementation from group Member.
"""
Roshan: Make push method and len method.
Rishi: Make pop method.
Syed: Make peek method or make print method.
"""
class Stack:
    def __init__(self):
        self.arr = []
        self.size = 0
    
    # Implementation of push method of Stack.
    def push(self,item):
        if (self.size+1 > len(self.arr)):
            self.arr.append(item)
        else:
            self.arr[self.size] = item
        self.size+=1



    # Implementation of print method
    def __str__(self):
        return f"{[self.arr[i] for i in range(self.size)]}"


def Main():
    st = Stack()
    st.push(10)
    st.push(20)
    st.push(30)
    print(st)
if __name__ == "__main__":
    Main()
