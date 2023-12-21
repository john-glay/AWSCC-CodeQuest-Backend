class BasicCalculator:
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

class ComplexCalculator(BasicCalculator):
    pass

basic = BasicCalculator()
complex = ComplexCalculator()

print(basic.sum([1, 2, 3]))
print(complex.sum([1, 2, 3]))

print(basic.minus([1, 2, 3]))
print(complex.minus([1, 2, 3]))