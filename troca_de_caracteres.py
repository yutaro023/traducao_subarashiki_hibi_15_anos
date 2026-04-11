# -*- coding: utf-8 -*-

def substituir_caracteres(texto):
    mapa = {
        "ã": "ｧ",
        "á": "ｦ",
        "é": "ｧ",
        "í": "ｨ",
        "õ": "ｫ",
        "ç": "｢",
        # adicione aqui todos os outros mapeamentos necessários
    }
    resultado = ""
    for char in texto:
        if char in mapa:
            resultado += mapa[char]
        else:
            resultado += char
    return resultado

def processar_arquivo(entrada, saida):
    with open(entrada, "r", encoding="utf-8") as f:
        conteudo = f.read()
    novo_conteudo = substituir_caracteres(conteudo)
    with open(saida, "w", encoding="utf-8") as f:
        f.write(novo_conteudo)

# Exemplo de uso:
# processar_arquivo("entrada.txt", "saida.txt")

processar_arquivo("2_0717_saviour.txt", "saida.txt")