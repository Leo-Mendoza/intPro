def repx3(str):
    print(str,str,str,)

def promX2(a,b):
    return (a+b)/2

def promX3(a,b,c):
    return (a+b+c)/3

def AbsVal(a):
    if a < 0:
        return a * -1
    else:
        return a

def elevarAlCubo(a):
    return a**3

def divisores(a):
    if a > 0:
        for i in range(1,a+1):
            if a % i == 0:
                print(f"{i} es divisor de {a}")
    else:
        for i in range(1,(a*-1)+1,):
            if a % i == 0:
                print(f"{i} es divisor de {a}")

def esPrimo(a):
    if a > 0:
        div = 0
        for i in range(1,a+1):
            if a % i == 0:
                div += 1
        if div > 2:
            print(f"{a} no es primo")
        else: 
            print(f"{a} es primo ")
    else: 
        print(f"{a} no es primo")

def esPrimo_pura(a):
    return "es primo" if divisores(a) > 2 else "no es primo"
