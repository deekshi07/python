# lists= [ 1,2,4,5,6,7,8,8,7,6,6,5,4,3]
# lists = iter(lists)

# print(next(lists))

# print(lists.__next__())






class pow_of_two():
    
    def __init__(self,max=0):
        self.max = max
        
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2**self.n
            self.n += 1
            return result
        else:
            raise StopIteration
        
p = pow_of_two(5)
p_iter = iter(p)
print(next(p_iter))
print(next(p_iter))
print(next(p_iter))
print(next(p_iter))

