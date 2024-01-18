ievade=str(input("Ievadiet savu vārdu: "))
#Naiet
if type(ievade) != str:
    print("Lūdzu ievadīt tikai tekstu")


ievade1=str(input("Ievadiet savu mīļāko suņu šķirni: "))
#Naiet
if type(ievade1) != str:
    print("Lūdzu ievadīt tikai tekstu")

tests="tests"

def funkcija():
    try:
        with open("lietotaji.txt", 'w', encoding="utf8") as ff:
            ff.write(ievade+ievade1)

    except FileNotFoundError:
        print("Datne nav atrasta")

if __name__=="__main__":
    funkcija()




def parbaude():
    try:
        with open("lietotaji.txt",'r', encoding='utf8') as datne:
            saturs=datne.read()
            if saturs==ievade+ievade1:
                print("Viss ir oki doki!")
            else:
                print("Kaut kas nogāja greizi, aizejiet pajautāt programmēšanas skolotājai :)")

    except FileNotFoundError:
        print("Kaut kas nogāja greizi, aizejiet pajautāt programmēšanas skolotājai :)")

if __name__=="__main__":
    parbaude()