#Реализуйте проверку ввода на число.
#Программа должна выводить “Correct”, если введено целое
# или вещественное число (в качестве разделителя
#должна использоваться одна точка).
#Во всех остальных случаях должно выводиться “Wrong”.

nn1 = input('Введите число... ')
c1 = len(nn1)
b = 0
b2 = 0
while c1-1 >= 0:
    c1 = c1 - 1
    if nn1[c1] == '.':
        b = b + 1
        if b == 2:
            print(nn1, 'Wrong')
            break
    elif nn1[c1] == '-':
        b2 = b2 + 1
        if b2 == 2:
            print(nn1, 'Wrong')
            break
    elif nn1[c1].isdigit() == False:
        print(nn1, 'Wrong')
        break
    elif c1 == 0:
        print(nn1, 'Correct')



