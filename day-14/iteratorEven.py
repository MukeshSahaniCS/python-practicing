class EvenNumbers:
    def __init__(self,maxVal):
        self.maxVal = maxVal
        self.current = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current>self.maxVal:
            raise StopIteration
        even_num = self.current
        self.current+=2
        return even_num
max_val = int(input())
even_num = EvenNumbers(max_val)
for num in even_num:
    print(num)