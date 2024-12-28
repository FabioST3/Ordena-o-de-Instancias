import os
import time
import argparse

def ordenacao_selecao(arr):
    n = len(arr)
    for i in range(n - 1):
        indice_minimo = i
        for j in range(i + 1, n):
            if arr[j] < arr[indice_minimo]:
                indice_minimo = j
        arr[i], arr[indice_minimo] = arr[indice_minimo], arr[i]

def ordenacao_insercao(arr):
    n = len(arr)
    for i in range(1, n):
        chave = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > chave:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave

def ler_instancia(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo:
            return [int(numero) for numero in arquivo.read().split()]  
    except Exception as e:
        print(f"Erro ao ler o arquivo {caminho_arquivo}: {e}")
        return []

def processar_arquivo(caminho_arquivo):
    print(f"Processando arquivo: {caminho_arquivo}")

    dados = ler_instancia(caminho_arquivo)
    if not dados:
        return

    # Ordenação por Seleção
    inicio_tempo = time.perf_counter()
    ordenacao_selecao(dados[:])  
    tempo_selecao = time.perf_counter() - inicio_tempo
    print(f"Tempo Selecao: {tempo_selecao:.6f} segundos")

    # Ordenação por Inserção
    inicio_tempo = time.perf_counter()
    ordenacao_insercao(dados[:])  
    tempo_insercao = time.perf_counter() - inicio_tempo
    print(f"Tempo Insercao: {tempo_insercao:.6f} segundos")

    # Comparação dos Tempos
    diferenca = abs(tempo_selecao - tempo_insercao)
    if tempo_selecao < tempo_insercao:
        print(f"A seleção foi {diferenca:.6f} segundos mais rápida.")
    elif tempo_insercao < tempo_selecao:
        print(f"A inserção foi {diferenca:.6f} segundos mais rápida.")
    else:
        print("Ambos os métodos tiveram o mesmo tempo.")

def principal():
    parser = argparse.ArgumentParser(description="Processa arquivos de instâncias para ordenação.")
    parser.add_argument("-d", "--diretorio", type=str, default="instancias", help="Caminho do diretório com os arquivos de instâncias.")
    args = parser.parse_args()

    if not os.path.exists(args.diretorio):
        print(f"Erro: Diretório '{args.diretorio}' não existe.")
        return

    for entrada in os.scandir(args.diretorio):  
        if entrada.is_file():
            processar_arquivo(entrada.path)

if __name__ == "__main__":
    principal()
