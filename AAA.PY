print(ord('J'))
print(ord('I'))
print(chr(74))


#probuje w palni z pamieci pojechac
def table_tw(key):
    key = key.upper()
    row= 0
    col=0
    tabela = [[0 for i in range(5)] for j in range(5)]
    dodawanie_zn = []
    #tutaj tworze tabelki
    #ponizej robie tak, ze jak znaku ni ma w dodawanych to wchodzi tam jak jest to pomijamy

    for znak in key:
        if znak not in dodawanie_zn:
            tabela[row][col] = znak
        else:
            continue
    #tutaj ladnie slicznie by mi przechodzilo    
        if col == 4:
            col = 0
            row +=1
        else:
            col += 1            
    #dobra tu bylo bardziej komplikejted bo dla znaku w odrebie (65,91) dodajemy znak i pomijamy 74 bo to j xd

    for znak in range(65,91):
        if znak == 74:
            continue
        if  chr(znak) not in dodawanie_zn:
            dodawanie_zn.append(chr(znak))
    #teraz kaj wyswietlanie
    poz = 0
    for i in range(5):
        for j in range(5):
            tabela[i][j] = dodawanie_zn[poz]
            poz+=1
    return tabela        

tab = [[0 for i in range(5)] for j in range(5)]
print(tab)