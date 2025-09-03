import numpy as np

def _validar_participantes(participantes):
    """Valida a lista de participantes conforme os testes negativos."""
    if not isinstance(participantes, list):
        raise TypeError("Participantes deve ser uma lista")
    if not participantes:
        raise ValueError("A lista de participantes está vazia")
    for p in participantes:
        if not isinstance(p, str):
            raise TypeError("Participantes devem ser strings")
        if not p.strip():
            raise ValueError("Participante inválido (vazio ou espaços)")

def sortear_participante(participantes):
    """Sorteia 1 participante da lista."""
    _validar_participantes(participantes)
    indice = np.random.randint(0, len(participantes))
    return indice, participantes[indice]

def sortear_varios(participantes, qtd):
    """Sorteia vários participantes, sem repetição."""
    if not isinstance(qtd, int):
        raise TypeError("Quantidade deve ser inteira")
    _validar_participantes(participantes)
    if qtd > len(participantes):
        raise ValueError("Quantidade maior que o número de participantes")
    if qtd <= 0:
        raise ValueError("Quantidade deve ser positiva")

    # Impede casos em que não existem participantes únicos suficientes
    if len(set(participantes)) < qtd:
        raise ValueError("Quantidade maior que o número de participantes únicos")

    indices = np.random.choice(len(participantes), size=qtd, replace=False)
    return [(i, participantes[i]) for i in indices]

def salvar_resultado(arquivo, resultado):
    """Salva o resultado do sorteio em um arquivo de texto."""
    with open(arquivo, "w", encoding="utf-8") as f:
        for indice, vencedor in resultado:
            f.write(f"Número sorteado: {indice}\n")
            f.write(f"O vencedor do sorteio é: {vencedor}\n\n")

def main():
    participantes = []
    print("Digite os nomes dos participantes (digite 'fim' para encerrar):")
    while True:
        nome = input("Nome: ").strip()
        if nome.lower() == "fim":
            break
        participantes.append(nome)

    if not participantes:
        print("Nenhum participante foi adicionado. Encerrando programa.")
        return

    # Pergunta quantos vencedores sortear
    if len(participantes) > 1:
        try:
            qtd = int(input("\nQuantos vencedores você quer sortear? "))
            resultado_varios = sortear_varios(participantes, qtd)

            print("\nResultado do sorteio:")
            for i, (indice, nome) in enumerate(resultado_varios, start=1):
                print(f"{i} vencedor(a) - {nome} [{indice}]")

            salvar_resultado("resultado.txt", resultado_varios)
        except (ValueError, TypeError) as e:
            print(f"Erro: {e}")
    else:
        # Se só tiver 1 participante, sorteia 1
        indice, vencedor = sortear_participante(participantes)
        print(f"\n1 vencedor(a) - {vencedor} [{indice}]")
        salvar_resultado("resultado.txt", [(indice, vencedor)])

if __name__ == "__main__":
    main()