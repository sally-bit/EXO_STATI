from collections import Counter
from math import *
#coding:utf-8

note_A={8:2,9:2,10:1,11:1}
note_B={6:2,8:2,9:2,13:1,14:1}

eff_to_A=sum(note_A.values())

eff_to_B=sum(note_B.values())

som_A=0
for cle,val in note_A.items():
    s=cle*val
    som_A +=s

moy_A=som_A/eff_to_A
print("la moyenne du groupe A => {:.2f}".format(moy_A)) 
var_A=0
for cle ,val in note_A.items():
    s= val * (moy_A- cle)**2
    var_A += s
    
ecart_A=sqrt(var_A)
print("l'ecart type du groupe A => {:.2f}".format(ecart_A)) 

print("****************** groupe B ***************************")

som_B=0
for cle,val in note_B.items():
    s=cle*val
    som_B +=s

moy_B=som_B/eff_to_B
print("la moyenne du groupe B => {:.2f}".format(moy_B)) 
var_B=0
for cle ,val in note_B.items():
    s= val * (moy_B- cle)**2
    var_B += s
    
ecart_B=sqrt(var_B)
print("l'ecart type du groupe A => {:.2f}".format(ecart_B)) 

print("on constat ici que la moyenne du groupe A est superieur aux groupe B mais que l'ecart-type du groupe B est eleve par rapport aux groupe A")