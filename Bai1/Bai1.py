import math

def ktNgto( _n ):
    if _n<2:
        return False
    for i in range(2, math.trunc(math.sqrt(_n))+1):
        if _n%i == 0:
            return False
    else:
        return True

if __name__ == "__main__":
    n = int(input('Nhap so nguyen duong n: '))
    for i in range(2,n+1):
        if ktNgto(i) == True:
            print(i)