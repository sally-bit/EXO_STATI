from collections import Counter
from math import *
#coding:utf-8

A = [7, 13 , 8 , 10 , 9 , 12 , 10, 8, 9, 10, 6, 14, 7, 15, 9, 11, 12, 11, 12, 5, 14, 11, 8, 10, 14, 12, 8, 5, 7, 13, 12, 16, 11, 9, 11, 11, 12, 12, 15, 14, 5, 14, 9, 9, 14, 13, 11, 10, 11, 12, 9, 15]
A.sort()
mod=[]
eff=[]
freq=[]
N=[]
F=[]

print("Tableau statistique => ",A)
compte=dict(Counter(A))

print("L' effectives du tableau statistiques est le dictionnaire =>",compte)


dict_freq={}
for cle, elt in compte.items(): 
    mod.append(cle)
    eff.append(elt)
    s = round(elt/52,2)
    freq.append(s)
    dict2={cle:s}
    dict_freq.update(dict2)
    #print("la cle est {} a pour frequence {:.2f}".format(cle, s))


print("les frequences  du tableau statistiques est le dictionnaire =>",dict_freq)

dict_eff_cum={}
sec=0
for cle, elt in compte.items(): 
    sec +=elt
    N.append(sec)
    dict2={cle:sec}
    dict_eff_cum.update(dict2)

print("les effectives cumules  du tableau statistiques est le dictionnaire =>",dict_eff_cum)


dict_freq_cum={}
sfc=0
for cle, elt in dict_freq.items(): 
    sfc +=elt
    sfc=round(sfc,2)
    F.append(sfc)
    dict2={cle:sfc}
    dict_freq_cum.update(dict2)

print("les frequences cumules  du tableau statistiques est le dictionnaire =>",dict_freq_cum)



list_fx=[]

for cle, elt in dict_freq_cum.items():
    list_fx.append((cle,elt))

print("la fonction Fx ==> ",list_fx)


print("Calculer le mode Mo ")

for cle, elt in compte.items():
    if elt==max(compte.values()):
        print("le mode est égal à {} qui correspondant au plus grand effectif qui est {}".format(cle,elt))
        break



som_my=0
for cle, elt in compte.items():
    s=cle*elt
    som_my += s
moy=som_my/52
print("la moyenne arithmétique x  est ==> {:.2f}".format(moy))
    
    
for cle, elt in dict_freq_cum.items(): 
    if elt >= 0.5:
        print("la mediane de x est Me==>",cle," pour x=> ",elt)
        break
        

print("Calculer la variance et l’écart-type")

var=0
for cle ,val in dict_freq.items():
    s=val *(moy-cle)**2
    var +=s
    
print("la variance est =>{:.2f}".format(var))

ecart=sqrt(var)
print("l'ecart-type est =>{:.2f}".format(ecart))

print("")

print(mod)
print(eff)
print(freq)
print(N)
print(F)