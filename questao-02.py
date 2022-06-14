#o numero verificado é definido pela variavel "num"

from pickle import FALSE


num = 10
v = []


def fibonacci(n):
    a=1
    b=1
    if n==1:
        v.append(1)
    elif n==2:
        v.append(0)
        v.append(1)
    else:
        v.append('0')
        v.append(a)
        v.append(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            v.append(total)
            #print(total)
         
fibonacci(num)


x = len(v)
cont = 0
verificador = 0


while cont < x:
    if v[cont] != num:    
        cont = cont + 1
    else:
        print('O número informado pertence a sequência.')
        break

print('O número informado não pertence a sequência.')
