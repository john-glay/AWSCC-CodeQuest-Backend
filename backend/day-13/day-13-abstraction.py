class Calculator:
    def sum(self, numlist: list):
        _sum = 0
        for num in numlist:
            _sum += num

        return _sum

    def minus(self, numlist: list):
        # Initialize with the first element
        _minus = numlist[0] if numlist else 0
        # Subtract the rest of the elements
        for num in numlist[1:]:
            _minus -= num
        return _minus

numlist = [5, 10, 15, 20, 25]
new_calculator = Calculator()
sum = new_calculator.sum(numlist)
minus = new_calculator.minus(numlist)
print(sum)
print(minus)