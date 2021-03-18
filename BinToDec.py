# -*- coding: utf-8 -*-

def bin_to_dec_standard(binaerstring):
    result = 0
    ziffern = len(binaerstring)
    for i in binaerstring:
        result = result + int(i) * 2 ^ ziffern
        ziffern -= 1
    return result

# aus Weitz, Edmund (2021): Konkrete Mathematik (nicht nur) für Informatiker. Springer Nature 2018, 2021
# Unterschied zu oben liegt bei der Multiplikation des Ergebnisses auch wenn 0(Bin).
# Weswegen auch eine Division am Endergebnis getätigt wird.
def bin_to_dec_addition(binaerstring):
    result = 0
    for i in reversed(binaerstring):
        result = result + int(i)
        result = result * 2
    result = result / 2


    return result