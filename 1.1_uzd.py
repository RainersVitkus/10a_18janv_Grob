def lasit_datni():
    try:
        with open("pteksts.txt",'r', encoding='utf8') as datne:
            saturs=datne.read()
            print(saturs)
        with open("jteksts.txt", 'w', encoding="utf8") as ff:
            ff.write(saturs)

    except FileNotFoundError:
        print("Datne nav atrasta")

if __name__=="__main__":
    lasit_datni()