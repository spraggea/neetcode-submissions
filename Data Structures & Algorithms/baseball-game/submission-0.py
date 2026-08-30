class Solution:
    def calPoints(self, operations: List[str]) -> int:

        
        record = [] #create stack to keep record
       


        for i in operations:
    
            if i == "+":
                record.append(int (record[-1]) + int(record[-2]))
            elif i == "D":
                    record.append(2 * int (record[-1]))
            elif i == "C":
                    record.pop()
            else:
                record.append(int (i))
        return sum(record)








            





        
        