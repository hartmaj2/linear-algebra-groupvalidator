# VSTUP: Ctvercova tabulka n x n, kde n je pocet prvku v grupe
# jednotlive radky zadavame jako prvky oddelene mezerou, konec radku znacime stiskem klavesy enter
# tato tabulka popisuje, jake jsou vysledky grupovych operaci jednotlivych prvku

# VYSTUP: Informace o tom, jestli matematicka struktura dana touto tabulkou splnuje:
#   1. Axiom asociativity
#   2. Jaky je neutralni prvek, pokud vubec existuje (ten muze byt jen jeden, over si sam proc :)
#   3. Pokud existuje neutralni prvek, tak ke kazdemu prvku priradi jeho odpovidajici inverzni prvek 

def nactiTabulku():
    t = []
    t.append([int(x) for x in input().split()])

    for i in range(1,len(t[0])):
        t.append([int(x) for x in input().split()])
    
    return t

def vypisTabulku(t):

    for i in range(0,len(t)):
        for cislo in t[i]:
            print(cislo,end=" ")
        print()
    print()

def zkontrolujAsociativitu(tabulka):

    def op(a,b):
        return tabulka[a][b]

    asociativni = True
    for i in range(0,len(tabulka)):
        for j in range(0,len(tabulka)):
            for k in range(0,len(tabulka)):
                prvni = op(i,op(j,k))
                druhy = op(op(i,j),k)
                symbol = "o"
                print(f"{i} {symbol} ({j} {symbol} {k}) = {prvni}",end = "     ")
                print(f"({i} {symbol} {j}) {symbol} {k} = {druhy}",end="")
                
                if prvni != druhy:
                    asociativni = False
                    print("    TATO OPERACE NENI ASOCIATIVNI!")

                
                else:
                    print()
                
    return asociativni

# vrati index neutralniho prvku nebo None pokud neexistuje
def vratNeutralniPrvek(tabulka):

    neutprvek = None

    for i in range(0,len(tabulka)):

        neutralni = True

        # nyni budeme prochazet jednotlive sloupce ci radky podle toho, jaky prvek je zafixovany
        for j in range(0,len(tabulka)):

            if tabulka[i][j] != j or tabulka[j][i] != j:
                neutralni = False
            
        if neutralni:
            neutprvek = i
            break

    return neutprvek

# pokud na vstupu prijme jako neutralni prvek None, tak vrati rovnou None
def najdiInverzniPrvky(tabulka, neutprvek):

    if neutprvek == None:
        return None

    seznam = [None] * len(tabulka)

    for i in range (0,len(tabulka)):

        for j in range (0,len(tabulka)):
            
            if (tabulka[i][j] == neutprvek and tabulka[j][i] == neutprvek):
                seznam[i] = j
            

    return seznam

def vytiskniVystup(asociativita, neutralniPrvek, inverzniPrvky, tabulka):
    print(f"Asociativita: {asociativita}")
    print(f"Neutralni prvek: {neutralniPrvek}")
    if inverzniPrvky != None:
        print("Inverzni prvky:")
        for i in range(0,len(tabulka)):
            print(f"{i} -> {inverzniPrvky[i]}")

def main():

    tabulka = nactiTabulku()

    asociativita = zkontrolujAsociativitu(tabulka)
    neutralniPrvek = vratNeutralniPrvek(tabulka)
    inverzniPrvky = najdiInverzniPrvky(tabulka,neutralniPrvek)

    vytiskniVystup(asociativita, neutralniPrvek, inverzniPrvky, tabulka)     

main()