#!/usr/bin/python
# À mon avis, il y a plus simple.

nb_user = int(input("Entrez un nombre entier en 0 et 15 : "))

bit1 = nb_user // (2**3)
bit2 = (nb_user - bit1 * 2**3) // (2**2)
bit3 = (nb_user - bit1 * 2**3 - bit2 * 2**2) // (2**1)
bit4 = (nb_user - bit1 * 2**3 - bit2 * 2**2 - bit3 * 2**1) 

print("{}{}{}{}".format(bit1, bit2, bit3, bit4))