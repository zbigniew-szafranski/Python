# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
# for char in reverse('golf'):
#     print(char)
#
# print(sum(i*i for i in range(10)))
#
# for element in [1,2,3]:
#     print(element)
#
# for element in (1,2,3):
#     print(element)
#
# for key in {'one': 1, 'two':2}:
#     print(key)
# for char in "123":
#     print(char)
#
# for line in open("products.txt"):
#     print(line, end='')

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self
    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]
rev = Reverse('spam')
iter(rev)
for char in rev:
    print(char)
