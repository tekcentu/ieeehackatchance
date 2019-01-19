# -*- coding: utf-8 -*-
"""
Created on Sat Jan 19 20:11:31 2019

@author: Oguz
"""

def idBulma(ilacIsim):
    ilacID = ilacVeriTabani.execute("SELECT id FROM ilaclar WHERE isim=?", (ilacIsim,)).fetchall()
    return(ilacID[0][0])

def kullanma(ilacIsim):
    ilacID = idBulma(ilacIsim)
    ilac = ilacVeriTabani.execute("SELECT kullanma FROM ilaclar").fetchall()
    ilacStr = "".join(ilac[ilacID-1][0])
    ilacStr = ilacStr.split(",")
    return(ilacStr)

def ilacBilgi(ilacIsim):
    ilacID = idBulma(ilacIsim)
    ilacIsimleri = ilacVeriTabani.execute("SELECT isim FROM ilaclar").fetchall()
    hamile = ilacVeriTabani.execute("SELECT hamile FROM ilaclar").fetchall()
    return(ilacIsimleri[ilacID-1][0], kullanma(ilacID), hamile[ilacID-1][0])
    
def ilacIsimleri():
    isimDatabase = ilacVeriTabani.execute("SELECT isim FROM ilaclar").fetchall()
    isimler = []
    for i in range(0, len(isimDatabase)):
        isimler.append(isimDatabase[i][0])
    print(isimler)
    
def kullanilan(hastaID):
    hasta = hastaVeriTabani.execute("SELECT kullanilan FROM hastalar").fetchall()
    hastaStr = "".join(hasta[hastaID-1][0])
    hastaStr = hastaStr.split(",")
    return(hastaStr)
    
def hastaBilgi(hastaId):
    hastaIsim = hastaVeriTabani.execute("SELECT isim FROM hastalar").fetchall()
    hamile = hastaVeriTabani.execute("SELECT hamile FROM hastalar").fetchall()
    return(hastaIsim[hastaId-1][0], kullanilan(hastaId), hamile[hastaId-1][0])
    

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

import sqlite3

ilacBaglanti = sqlite3.connect("ilaclar.db")
hastaBaglanti = sqlite3.connect("hastalar.db")

if(ilacBaglanti):
    print('Ilaclar baglantisi basarili!')
else:
    print('Ilaclar baglantisi basarisiz!')
    
if(hastaBaglanti):
    print('Hastalar baglantisi basarili!')
else:
    print('Hastalar baglantisi basarisiz!')
    
    
    
ilacVeriTabani = ilacBaglanti.cursor()
hastaVeriTabani = hastaBaglanti.cursor()


#drugId = ilacVeriTabani.execute("SELECT id FROM ilaclar").fetchall()
#drugId[0][0]
#
#drugName = ilacVeriTabani.execute("SELECT isim FROM ilaclar").fetchall()
#
#drug = ilacVeriTabani.execute("SELECT kullanma FROM ilaclar").fetchall()
#drugStr = "".join(drug[0][0])
#drugStr = drugStr.split(",")



print(hastaBilgi(1))

ilacBaglanti.commit()
ilacBaglanti.close()

hastaBaglanti.commit()
hastaBaglanti.close()

