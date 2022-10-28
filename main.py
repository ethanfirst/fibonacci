def main():
   
    if input("cached? (y/n) ") == "y": # added line
        my_fib = FibCached() # added line
    else: # added line
        my_fib = Fib() # added line

   
    print(my_fib.fib(10)) 
 
class Fib:
    beginning_nums = (0, 1, 1, 2, 3, 5, 8) 
    beginning_nums = (0, 1, 1) 
    def fib(self, in_num):
        
        if in_num < 3:
            return self.beginning_nums[in_num] 
        return self.fib(in_num - 1) + self.fib(in_num - 2) 
      
class FibCached(Fib): # added line
    def __init__(self): # added line
        self.cache = {} # added line
    def fib(self, in_num): # added line
        if in_num not in self.cache: # added line
            self.cache[in_num] = super().fib(in_num) # added line
        return self.cache[in_num] # added line


