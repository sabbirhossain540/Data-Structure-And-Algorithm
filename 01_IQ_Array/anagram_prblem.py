
def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False

    return True

if __name__ == '__main__':
    st1 = "restful"
    st2 = "luftser"

    print(is_anagram(st1, st2))