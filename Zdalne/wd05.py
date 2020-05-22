## ZADANIE 7 ##

# class ZwrocParzyste:
    
#     def __init__(self, n):
#         self.n = n
#         self.i = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.n == self.i:
#             raise StopIteration

#         self.i += 1
#         if self.i % 2 == 0:
#             return self.i
#         else:
#             return False
# print([a for a in ZwrocParzyste(20)])

## ZADANIE 8 ##
# class samogloski:
#     def __init__(self, data):
#         self. data = data
#         self.index = len(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         samogloski = 'aeiou'
#         for a in self.data:
#             if a in samogloski:
#                 return a
# zdanie = 'Ala ma kota a kot ma Ale'
# print(samogloski(zdanie))

## ZADANIE 9 ##

# def parzyste():
#     for n in range(21):
#         if n % 2 == 0:
#             yield n

# for liczba in parzyste():
#     print(liczba)

## ZADANIE 10 ##
# import itertools as it
# a = [2,4,4,4,5,6,6,7,8,9]
# print(set(it.combinations(a,3)))

## ZADANIE 11 ##

# def Fibonacci():
#     a, b = 1,1
#     yield a
#     yield b
#     while True:
#         a,b = b, a+b
#         yield b
# gen = Fibonacci()        
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

## ZADANIE 12 ##

    



    


        
        

