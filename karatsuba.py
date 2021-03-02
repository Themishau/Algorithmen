# -*- coding: utf-8 -*-

 

def karatsuba_mul(a, b):
    if a==0 or b==0:
        return 0
    m=max(a.bit_length(), b.bit_length())
    if m<=8:
        return a*b
    else:
        k=m//2
        print(m)
        print(k)
        a1=a>>k # a / pow(2,k) 
        print(a)
        print(a1)
        print(a>>k)
        a0=a & (1<<k)-1 
        print(a0)
        print(a & (1<<k)-1) 
        b1=b>>k
        print(b)
        print(b1)
        print(b>>k)
        b0=b & (1<<k)-1
        print(b0)
        print(b & (1<<k)-1) 


        p2=karatsuba_mul(a1, b1)
        p1=karatsuba_mul(a1+a0, b1+b0)
        p0=karatsuba_mul(a0, b0)
        c2=p2 << 2*k
        c1=p1-p2-p0 << k
        c0=p0
        return c2+c1+c0

if __name__ == '__main__':
    print("start")

    a=100000000
    b=100000000
    print(1 >> 1)
    print(bin(1>>1))
    print (1 << 1)
    print(bin(1<<1))  

    print(8 >> 1)
    print(bin(8>>1))
    print (8 << 1)
    print(bin(8<<1)) 

    print (a, b)
    print (a*b)
    print (karatsuba_mul(a, b))
   # gtfsMenu = Controller()
   # gtfsMenu.run()
