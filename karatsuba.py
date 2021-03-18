# -*- coding: utf-8 -*-


def karatsuba_mul(zahla, zahlb):
    #negative Eingaben erstmal ignoriert
    if zahla == 0 or zahlb == 0:
        return 0

    max_bit = max(zahla.bit_length(), zahlb.bit_length())
    if max_bit <= 8:
        return zahla * zahlb
    # auf Basis der Dezimalzahl auch möglich. 
    #m=min(zahla, zahlb)
    #if m == 1:
    #    return zahla * zahlb
    


    else:
        mitte = max_bit//2
        print(max_bit)
        print(mitte)
        zahla_shifted = zahla >> mitte # zahla / pow(2,mitte) 
        print(zahla)
        print(zahla_shifted)
        print(zahla >> mitte)
        zahla_shifted_b = zahla & ( 1 << mitte ) -1 
        print(zahla_shifted_b)
        print(zahla & ( 1 << mitte ) -1 ) 

        zahlb_shifted = zahlb >> mitte
        print(zahlb)
        print(zahlb_shifted)
        print(zahlb >> mitte)
        zahlb_shifted_b = zahlb & ( 1 << mitte ) -1
        print(zahlb_shifted_b)
        print(zahlb & ( 1 << mitte ) -1 ) 

        #rekursion 
        p2=karatsuba_mul(zahla_shifted, zahlb_shifted)
        p1=karatsuba_mul(zahla_shifted + zahla_shifted_b, zahlb_shifted + zahlb_shifted_b )
        p0=karatsuba_mul(zahla_shifted_b, zahlb_shifted_b)
        
        c2=p2 << 2* mitte
        
        c1=p1-p2-p0 << mitte
        #carry bit
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
    print (1 & 1)
    print(bin(1&1)) 
    print("######")
    print(8 >> 1)
    print(bin(8>>1))
    print (8 << 1)
    print(bin(8<<1)) 
    print (8 & 10)
    print(bin(8&1)) 

    print (a, b)
    print (a*b)
    print (karatsuba_mul(a, b))
   # gtfsMenu = Controller()
   # gtfsMenu.run()
