# EXO_STATI

from collections import Counter
# coding:utf-8
A = [7, 13	, 8	, 10	, 9	, 12	, 10, 8,	9, 10, 6, 14, 7, 15,	9,	11,	12,	11,	12,	5,	14,	11,	8,	10,	14,
     12,	8, 5, 7,	13,	12,	16,	11,	9,	11,	11,	12,	12,	15,	14,	5,	14,	9,	9,	14,	13,	11,	10,	11,	12,	9, 15]
print(A)
compte = Counter(A)


print(compte)
list_vite = []
som = 0
for elt in compte.values():
    list_vite.append(elt)
    som += elt

print(som)
print(list_vite)

for cle, elt in compte.items():
    s = elt/som
    print("la cle est {} frequence {:.2f}".format(cle, s))
