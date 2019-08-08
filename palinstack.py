class Stack:
    def __init__(self):
      self.items=[]

    def isEmpty(self):
      return self.items==[]

    def push(self,data):
      self.items.append(data)

    def size(self):
      return len(Self.items)

    def show(self):
      print (self.items)

    def peek(self):
      return self.items[len(self.items)-1]

    def pop(self):
      assert not self.isEmpty()
      return self.items.pop()

a= input(" ")

s=Stack()

for i in a:
    s.push(i)
    list1 = s.pop()

if(list1 == a):
    print("not")
else:
    print("yes")
    
    
