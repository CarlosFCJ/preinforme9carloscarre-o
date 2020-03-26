# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:49:05 2020

@author: carlos carreño
"""
#%% 1
X1 = int(input("Ingrese el numero que va en la posicion X1: "))
X2 = int(input("Ingrese el numero que va en la posicion X2: "))
Y1 = int(input("Ingrese el numero que va en la posicion y1: "))
Y2 = int(input("Ingrese el numero que va en la posicion y2: "))

R = (((X1-X2)**2)+((Y1-Y2)**2))
D = R**(1/2)

print("la distancia euclidiana entre los dos puntos es :" )
print(D)

#%% 2
N = int(input("Ingrese el numero: "))
P1 = N//1000
N = N-(P1*1000)
P2 = N//100
N = N-(P2*100)
P3 = N//10
P4 = N-(P3*10)

print(str(P4)+str(P3)+str(P2)+str(P1))

#%% 3
n1 = float(input("Ingrese nota 1: "))
n2 = float(input("Ingrese nota 2: "))
n3 = float(input("Ingrese nota 3: "))
n4 = float(input("Ingrese nota 4: "))
n5 = float(input("Ingrese nota 5: "))

NF = float(input("ingrese NF"))

if NF<2.0 :
    print("el estudiante no puede habilitar, su nota es : " + str(NF))
elif NF<3.0:
    print("el estudiante reprobo, su nota es : " + str(NF))
elif NF>=3.0 and NF<4.6:
    print("el estudiante aprobo, su nota es : " + str(NF))
else :
    print("el estudiante aprobo mas de 4.5, felicidades , su nota es:" + str(NF))

#%% 4
f = int(input("Ingrese el numero de filas : "))
co = 1
fo = f+2
for c in range(2,fo,1):
    print(str(co))
    co = str(co) + str(c)
    int(c)
