ZERO_DIVISION = "ERROR: You cannot divide by 0."
UNDEF_SYM = "ERROR: Undefined symbol."

class Calculator:

    def add(a, b):
        return a + b

    def sub(a, b):
        return a - b

    def mul(a, b):
        return a * b

    def div(a, b):
        return a / b if b != 0 else ZERO_DIVISION

    def parse(txt):
        try:
            txt = str(txt)
            arr = txt.split()

            nums = []
            operations = []

            for i in arr:
                if i.isnumeric():
                    nums.append(float(i))
                elif i in ('+', '-', '*', '/'):
                    operations.append(i)
                else:
                    raise UNDEF_SYM
        finally:
            return nums, operations
        
    def calculate(self, txt):
        nums, operations = self.parse(txt)
        res = nums[0]

        for i in range(1, len(nums)):
            op = operations[i-1]

            if op == '+':
                res = self.add(res, nums[i])
            elif op == '-':
                res = self.sub(res, nums[i])
            elif op == '*':
                res = self.mul(res, nums[i])
            else:
                res = self.div(res, nums[i])
        
        return res

C = Calculator

while True:
    txt = input("Enter the expression or Q to quit: ")

    if txt.capitalize() == 'Q':
        break

    print(C.calculate(C, txt))