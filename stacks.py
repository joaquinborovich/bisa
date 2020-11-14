

class Stack():
    """
    stack dynamic set implementation,
    n (max ammount of elements)
    """
    def __init__(self, max):
        self.__top = 0
        self.array = []
        # for i in range(length): self.array.append(None)
        self.__max = max

    def push(self, value):
        if self.get_top() == (self.get_length() - 1):
            # array is full
            raise Exception('Stack Overflow, array is full')
        else:
            # set the top position to the value
            self.array.append(value)
            self.__top += 1

    def pop(self):
        if self.__top > 0:
            del self.array[self.__top - 1]
            self.__top -= 1 
        else:
            # there is no elements in the array
            raise Exception('Stack Underflow, empty stack')

    def get_top(self):
        return self.__top   

    def get_length(self):
        return self.__max

    def __str__(self):
        return f'{self.array}, max={self.__max}, top={self.__top}'


if __name__ == "__main__":
    s = Stack(max=10)
    s.push('hola')
    print(s)
    s.push('dos')
    print(s)
    s.pop()
    print(s)
    s.pop()
    print(s)
    s.pop()

    