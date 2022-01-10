
def palindrom_python(data):
    # if s == s[::-1]:
    #     return True
    # else:
    #     return False
    original_string = data
    reverse_string = reverse(data)

    if original_string == reverse_string:
        return True
    return False



def reverse(data):
    #Convert a string into a array
    data = list(data)
    startPoint = 0
    endPoint = len(data) - 1
    while endPoint > startPoint:
        data[startPoint], data[endPoint] = data[endPoint], data[startPoint]
        startPoint = startPoint + 1
        endPoint = endPoint - 1

    #Covert a array into string
    return  ''.join(data)


if __name__ == '__main__':
    print(palindrom_python('cvcs'))
