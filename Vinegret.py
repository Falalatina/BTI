
tekst = 'mops' #by odszyfrować tu dac to co wyszło
key = 'tajny'

alphabet = 'ABCDEFGHIJKLMNOPRSTUWXYZ'

def enkrypt(tekst, key, alphabet):
    message = ''
    tekst = tekst.upper()
    key = key.upper()
    key_len = len(key)

    for i in range(len(tekst)):
        if tekst[i] in alphabet:
           tekst_index = alphabet.find(tekst[i])
           key_index = alphabet.find(key[i % key_len])
           c = (tekst_index + key_index) % len(alphabet) #by odszyfrować tu dać minusik
           message += alphabet[c]
        else:
            message += tekst[i]
    return message



def dekrypt(tekst, key, alphabet):
    reversed_key = ''
    for c in key.upper():
        key_index = (len(alphabet) - alphabet.find(c)) % len(alphabet)
        reversed_key += alphabet[key_index]
    return enkrypt(tekst, reversed_key, alphabet)    


cipher_text = enkrypt(tekst, key, alphabet)
print(cipher_text)
print(dekrypt(cipher_text, key, alphabet))
#uwu