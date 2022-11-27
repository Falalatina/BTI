

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


def rozdzielenie_tych_samych(text):
    index =0
    while (index<len(text)):
        z1 = text[index]
        if index == len(text) -1:
            text = text + 'X'
            index += 2
            continue
        z2 = text[index + 1]
        if z1 ==z2:
            #cos tam: index+1 dodaj X od tego miejsca:cos tam
            text = text[:index +1] + "x" + text[index+1:] #by pomijalo znak na index+1 i dawalo tam X 
            index += 2
    return text        

#to idzie tak długo aż znajdzie odpowiedni row
def indexznaku(znak, tabela):
    for i in range(5):
        try:
            index = tabela[i].index(znak)    # tu go szuka
            return(i,index)
        except:
            continue #az znajdzie XD

#kodowanie i odkodowanie
def playfair(key, text, kodowanie=False):
    inc = 1
    if kodowanie==False:
        inc = -1
        tabela = tworze_tabele(key)
        text = text.upper()
        text = text.replace(' ', '')
        text = rozdzielenie_tych_samych(text)
        kodowany_text = ''
    for (z1, z2) in zip(text[::2], text[1::2]):
        row1,col1 = indexznaku(z1,tabela)
        row2,col2 = indexznaku(z2, tabela)
        if row1 ==row2:
            kodowany_text += tabela[row1][(col1 + inc)%5] + tabela[row2][(col2 + inc)%5] 
        elif col1==col2:
            kodowany_text += tabela[(row1 + inc)%5][col1] + tabela[(row2 + inc)%5][row2]   
        else:
            kodowany_text += tabela[row1][col1] + tabela[row2][col2]     
    return kodowany_text

if __name__ =='__main__':
    print('kodowanie: ')     
    sekretna = input("podaj sekretna wiadomość: ")  
    klucz = input("Podaj klucz: ") 
    print(playfair(klucz, sekretna))
    print('Odkodowanie: ')
    odkoduj = input("Podaj kod do odkodowania: ")
    print(playfair(klucz, odkoduj, False))

#no i nie działa :<<<<<<<<<<
