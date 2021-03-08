# -*- coding: utf-8 -*-
import math
from bitstring import BitArray

def karatsuba_mul(zahla, zahlb):
    #negative Eingaben erstmal ignoriert
    if zahla == 0 or zahlb == 0:
        return 0

    max_bit = max(zahla.bit_length(), zahlb.bit_length())
    """
    print("zahla zahlb")
    print(zahla.bit_length())
    print(zahlb.bit_length())
    print(max_bit)
    print("######")
    print(math.log(zahla + 1))
    print(math.log(zahlb + 1))
    print("######")
    print(math.ceil(zahla))
    print(math.ceil(zahlb))
    print("######")
    print(math.ceil(math.log10(zahla + 1)))
    print(math.ceil(math.log10(zahlb + 1)))
    print("######")
    print(zahla >> 2)
    print(zahlb >> 2)
    print("######")
    print((zahla >> 2)+(zahlb >> 2))
    print((zahla >> 2)+(zahlb >> 2) << 2)
    print("###### ende ######")
    """
    if max_bit <= 2:
        return zahla * zahlb
    # auf Basis der Dezimalzahl auch möglich. 
    #m=min(zahla, zahlb)
    #if m == 1:
    #    return zahla * zahlb
    


    else:
        print("###### bearbeitung ######")
        mitte = max_bit//2
        print("###### max_bit/mitte ######")
        print(max_bit)
        print(mitte)
        zahla_shifted = zahla >> mitte # zahla / pow(2,mitte) 
        print("###### zahla_shifted ######")
        print("zahla " + str(zahla))
        print("zahla_shifted " + str(zahla_shifted))
        print("zahla >> mitte " + str(zahla >> mitte))
        zahla_shifted_b = zahla & ( 1 << mitte ) -1 
        print("###### zahla_shifted_b ######")
        print("zahla_shifted_b " + str(zahla_shifted_b))
        print("( 1 << mitte ) -1 ) " + str(( 1 << mitte ) -1 )) 
        c = BitArray(hex=str(zahla))
        c2 = BitArray(hex=str(( 1 << mitte ) -1 ))
        print(c.bin)
        print(c2.bin)
        zahlb_shifted = zahlb >> mitte
        print("###### zahlb_shifted ######")
        print("zahlb " + str(zahlb))
        print("zahlb_shifted " + str(zahlb_shifted))
        print("zahlb >> mitte " + str(zahlb >> mitte))
        zahlb_shifted_b = zahlb & ( 1 << mitte ) -1
        print("###### zahlb_shifted_b ######")
        print("zahlb_shifted_b " + str(zahlb_shifted_b))
        print("( 1 << mitte ) -1  " + str(( 1 << mitte ) -1 ) )

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

    a=10
    b=100
    print("######")

    print (a, b)
    print (a*b)
    print (karatsuba_mul(a, b))
   # gtfsMenu = Controller()
   # gtfsMenu.run()
