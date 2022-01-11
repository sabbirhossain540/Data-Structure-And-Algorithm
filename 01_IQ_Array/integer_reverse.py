
def reverse_integer(n):
    reversed = 0
    reminder = 0

    while n > 0:
        reminder = n % 10
        reversed = reversed*10 + reminder
        n = n//10
    return  reversed

if __name__ == '__main__':
    print(reverse_integer(125))

