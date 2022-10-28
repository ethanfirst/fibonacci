def main():
    my_fib = Fib()
    print(my_fib.fib(4))

class Fib:
    beginning_nums = (0, 1, 1, 2, 3, 5, 8)
    def fib(self, in_num):
        return self.beginning_nums[in_num]

main()
