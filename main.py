def main():
    my_fib = Fib()
   
    print(my_fib.fib(10)) 
 
class Fib:
    beginning_nums = (0, 1, 1, 2, 3, 5, 8) 
    beginning_nums = (0, 1, 1) 
    def fib(self, in_num):
        
        if in_num < 3:
            return self.beginning_nums[in_num] 
        return self.fib(in_num - 1) + self.fib(in_num - 2) 


