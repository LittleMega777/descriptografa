import hashlib

def gerawordlist():
    wordlist = []
    for word in range(0, 10000):
        if word <= 9:
            wordlist.append(f'000{word}')
        elif 10 <= word <= 99:
            wordlist.append(f'00{word}')
        elif 100 <= word <= 999:
            wordlist.append(f'0{word}')
        else:
            wordlist.append(f'{word}')
    return wordlist

senha = "" # coloque a senha hash aqui

word_list = gerawordlist()

for numero in word_list:
    tentativa = hashlib.md5(f"{numero}".encode("utf-8")).hexdigest()
    if tentativa == senha:
        print(f'o hash md5 {tentativa} e equivalente a {numero}')