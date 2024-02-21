import hashlib # importando biblioteca hash

def gerawordlist()-> list: # gera a lista de palavras
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

def descriptografa(wordlist:list, senha_cript:str)-> str:# descriptografa
    for valor in wordlist: # para cada valor na lista
        tentativa = hashlib.md5(f"{valor}".encode("utf-8")).hexdigest()
    if tentativa == senha_cript:
        print(f'o hash md5 {tentativa} e equivalente a {valor}')


senha = "fa246d0262c3925617b0c72bb20eeb1d" # recebe a senha hash md5

descriptografa(gerawordlist(), senha) # retorna o resultado