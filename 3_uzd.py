def lasit_datni():
    try:
        with open("teksts_3uzd.txt",'r', encoding='utf8') as datne:
            saturs=datne.read()
            print(saturs)

    except FileNotFoundError:
        print("Datne nav atrasta")

if __name__=="__main__":
    lasit_datni()