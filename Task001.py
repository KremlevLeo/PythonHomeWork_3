# 3.10 Вводим с клавиатуры десятичное число. Необходимо перевести его в шестнадцатиричную систему счисления.
def hexaceteric(num):
    result = ''
    while num >= 1:
        res = math.floor(num % 16)
        if res == 10:
            res = 'A'
        elif res == 11:
            res = 'B'
        elif res == 12:
            res = 'C'
        elif res == 13:
            res = 'D'
        elif res == 14:
            res = 'E'
        elif res == 15:
            res = 'F'
        result += str(res)
        num //= 16
    return result

num = int(input("Введите целое число: "))
result = hexaceteric(num)
print(result[-1::-1])
