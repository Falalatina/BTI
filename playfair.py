

def tworze_tabele(key):
    key = key.upper()
    tabela =[[0 for i in range(5)] for j in range(5)]
    dodawanie_liter = []
    row = 0
    col = 0
    for znak in key:
        if znak not in dodawanie_liter:
            tabela[row][col] = znak
        else:
            continue    #to nam pomija 1 iteracje
        if(col==4):
            col = 0
            row += 1    
        else:
            col +=1    

#wiemy, że ord('A')= 65 a ord('Z')=91 i ord('J') = 74 wiec pomijamy do chr(75) = I
    for znak in range(65,91):
        if znak == 74:
            continue
        if chr(znak) not in dodawanie_liter:
            dodawanie_liter.append(chr(znak))
 #///////////
    poz = 0
    for i in range(5):
        for j in range(5):
            tabela[i][j] = dodawanie_liter[poz]
            poz += 1
    return tabela