from collections import Counter
from math import *
#coding:utf-8
b=inf
a=inf
list_interval=[800,1000,1400,1600,b,2400,a]
a =min(list_interval)+3200
print(a)


budget_x={(800,1000):0.08,(1000,1400):0.18,(1400,1600):0.34,(1600,b):0.64,(b,2400):0.73,(2400,a):1}
print(budget_x)

dict_freq={}
som_desc=0
for cle, elt in budget_x.items():
    
    som_desc = elt -som_desc
    som_desc=round(som_desc,2)
    dict2={cle:som_desc}
    
    dict_freq.update(dict2)
    #print("la cle est {} a pour frequence {:.2f}".format(cle, s))


print("les frequences  du tableau statistiques est le dictionnaire =>",dict_freq)

budget_c={}
for cle in budget_x.keys():
    s=sum(cle)/2
    s=round(s,2)
    dist_c={cle:s}
    budget_c.update(dist_c)
print(budget_c)
   
    