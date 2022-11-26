

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

#wiemy, że ord('A')= 65 a ord('Z')=91 i ord('J') = 74 wiec pomijamy chr(75) = I
