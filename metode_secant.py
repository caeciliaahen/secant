fx = list(map(float, input("Masukkan variabel persamaan: ").split(',')))
x1 = float(input("Masukkan x-1: "))
x2 = float(input("Masukkan x0: "))
x = [x1, x2]
suku = int(input("Masukkan jumlah iterasi maksimal: "))
pangkat = len(fx)

print("\n[Persamaan]\nf(x) =", end=' ')
for i in reversed(range(pangkat)):
    if i == (pangkat - 1):
        if fx[i] != 0:
            if fx[i] == 1:
                print("x^" + str(i), end=' ')
            else:
                print(str(fx[i]) + "x^" + str(i), end=' ')
    elif i == 1:
        if (fx[i] > 0):
            print("+", str(fx[i]) + "x", end=' ')
        elif (fx[i] < 0):
            print(str(fx[i]) + "x", end=' ')
    elif i == 0:
        if (fx[i] > 0):
            print("+", str(fx[i]), end='\n\n')
        elif (fx[i] < 0):
            print(str(fx[i]), end='\n\n')
    else:
        if (fx[i] > 0):
            print("+", str(fx[i]) + "x^" + str(i), end=' ')
        elif (fx[i] < 0):
            print(str(fx[i]) + "x^" + str(i), end=' ')

print("[Asumsi]")
for i in range(len(x)):
    print("x"+str(i-1),"=",x[i])

def f(n):
    hasil = []
    for i in range(len(fx)):
        hasil.append(fx[i]*(n**i))
    return sum(hasil)

i=2
while i==2 or (ea!=0 and i<=(suku+1)):
    x.append(x[i-1] - (f(x[i-1])*(x[i-1]-x[i-2])/(f(x[i-1])-f(x[i-2]))))
    ea = abs((x[i]-x[i-1])/x[i])*100
    print("\nIterasi",str(i-1)+":")
    print("x"+str(i-1),"=",x[i])
    print("|∈a| =",str(ea)+"%")
    i+=1

print("\n[END] Perhitungan berhenti pada iterasi ke-"+str(i-2),"dengan |∈a| =", str(ea) + "%")