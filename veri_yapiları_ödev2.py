# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 23:51:03 2020

@author: ugur_
"""

count = 0
giris = open("giris.txt", "r")
cikis = open("cikis.txt", "w+")

for satir in giris: 
    if '{' in satir:
        cikis.write(  ( count * "\t" ) + satir ) 
        count += 1
        
    elif '}' in satir:
        count -= 1
        cikis.write(  ( count * "\t" ) + satir )  
    else:
        cikis.write(  ( count * "\t" ) + satir )

giris.close()
cikis.close()