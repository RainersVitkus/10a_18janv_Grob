ievade=str(input("Ievadi savu tekstu, tas tiks ievietots teksts.txt failā"))
print(ievade)

def lasit_datni():
    try:
        with open("teksts.txt", 'w', encoding="utf8") as ff:
            ff.write(ievade)

    except FileNotFoundError:
        print("Datne nav atrasta")

if __name__=="__main__":
    lasit_datni()