def gen_pass(k):
    g = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    passw = ''
    for a in g[0:]:
        for b in g[1:]:
            if a >= b:
                continue
            ps = a + b

            if k % ps == 0 :
                 passw += str(a) + str(b)


    return passw
k = int(input('Введи значение ребуса от 3 до 20: ',))
if 3<= k <=20:
    rez = gen_pass(k)
    print(rez)
else:
    print('Не то число, брат')









    





