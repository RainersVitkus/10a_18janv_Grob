import _json
import csv


ievade_fnos=str(input("Ievadi faila nosaukumu"))
ievade_fpap=str(input("Ievadi teksta failu paplašinājumu"))

faila_nos=ievade_fnos+ievade_fpap
#print(faila_nos)

if ievade_fpap == ".txt":
    def galvfunkcija():
        try:
            with open(faila_nos,'r', encoding='utf8') as datne:
                saturs=datne.read()
                print(saturs)

        except FileNotFoundError:
            print("Datne nav atrasta")
"""
if ievade_fpap ==".CSV":
    def galvfunkcija1():
        try:
            with open(faila_nos,'r', encoding='utf8') as datne:
                saturs=datne.read()
                print(saturs)

        except FileNotFoundError:
            print("Datne nav atrasta")
    if __name__=="__main__":
    galvfunkcija1()
"""

if __name__=="__main__":
    galvfunkcija()
