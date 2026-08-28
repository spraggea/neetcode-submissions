from collections import deque
class MyStack:


    def __init__(self):
        self.q1 = deque() #Main queue
        self.q2 = deque() #Temp help Queue

    def push(self, x: int) -> None:
     #Push: add to top 
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft())

        self.q1, self.q2 = self.q2, self.q1

     


    def pop(self) -> int:
    #remove from top
        return self.q1.popleft()

    def top(self) -> int:
    #return top value 
        return self.q1[0]

    def empty(self) -> bool:
       #is empty func 
       return len(self.q1) == 0


#Idea: We use two queues
#q1 (main queue) and q2 temp queue
#Simulate stack behavior we need to reverse the order of elements
#for Push add the new elements to q2 (empty queue)
#Move all elements from q1 to q2 one by one
#Swap names of q1 and q2
#Ensures newest elemet is always the last front of q1

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()