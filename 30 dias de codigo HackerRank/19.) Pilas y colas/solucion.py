class Solution:
    def __init__(self):
        self.queue = []
        self.stack = []
        self.stackTopValue = None
        self.queueFirstValue = None
        
        
    # Stack
    def pushCharacter(self,l):
        self.stack.append(l)
            
    def popCharacter(self):
        self.stackTopValue = self.stack[-1]
        self.stack.pop()
        return self.stackTopValue
        
    
    # Queue    
    def enqueueCharacter(self,l):
        self.queue.append(l)
            
    def dequeueCharacter(self):
        self.queueFirstValue = self.queue[0]
        self.queue.pop(0)
        return self.queueFirstValue
        
# read the string s
s=input()
#Create the Solution class object
obj=Solution()  

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+ s +", is a palindrome.")
else:
    print("The word, "+ s +", is not a palindrome.")
