import numpy as np

def main():
    participantes = ["Anna", "Bianca", "Julia", "Mavi", "Mary"]

    # Sorteia um índice válido na lista
    indice_sorteado = np.random.randint(0, len(participantes))

    # Usa o índice para pegar o vencedor
    vencedor = participantes[indice_sorteado]

    print(f"Número sorteado: {indice_sorteado}")
    print(f"O vencedor do sorteio é: {vencedor}")

    # Gera o arquivo de texto com o resultado
    with open("resultado.txt", "w", encoding="utf-8") as f:
        f.write(f"Número sorteado: {indice_sorteado}\n")
        f.write(f"O vencedor do sorteio é: {vencedor}\n")

if __name__ == "__main__":
    main()
