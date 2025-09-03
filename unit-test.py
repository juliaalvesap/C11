import unittest
from main import sortear_varios, sortear_participante

class TestSorteio(unittest.TestCase):

    # ---------------- TESTES POSITIVOS ----------------
    #1
    def test_um_participante(self):
        # Deve retornar a própria pessoa como vencedora
        participantes = ["Ana"]
        indice, vencedor = sortear_participante(participantes)
        self.assertEqual(vencedor, "Ana")
    #2
    def test_dois_participantes_um_vencedor(self):
        # Deve sortear apenas 1 vencedor entre 2 participantes
        participantes = ["Ana", "Beto"]
        resultado = sortear_varios(participantes, 1)
        self.assertEqual(len(resultado), 1)
        self.assertIn(resultado[0][1], participantes)
    #3
    def test_dois_participantes_dois_vencedores(self):
        # Deve retornar os dois participantes (ordem não importa)
        participantes = ["Ana", "Beto"]
        resultado = sortear_varios(participantes, 2)
        vencedores = [v[1] for v in resultado]
        self.assertCountEqual(vencedores, participantes)
    #4
    def test_varios_participantes_um_vencedor(self):
        # Deve escolher apenas 1 vencedor de uma lista maior
        participantes = ["Ana", "Beto", "Carlos", "Duda"]
        resultado = sortear_varios(participantes, 1)
        self.assertEqual(len(resultado), 1)
        self.assertIn(resultado[0][1], participantes)
    #5
    def test_varios_participantes_varios_vencedores(self):
        # Deve escolher 3 vencedores distintos de uma lista maior
        participantes = ["Ana", "Beto", "Carlos", "Duda", "Eva"]
        resultado = sortear_varios(participantes, 3)
        vencedores = [v[1] for v in resultado]
        self.assertEqual(len(vencedores), 3)
        for v in vencedores:
            self.assertIn(v, participantes)
    #6
    def test_ordem_dos_vencedores_diferente(self):
        # Dois sorteios seguidos podem dar resultados diferentes
        participantes = ["Ana", "Beto", "Carlos", "Duda", "Eva"]
        resultado1 = sortear_varios(participantes, 2)
        resultado2 = sortear_varios(participantes, 2)
        vencedores1 = [v[1] for v in resultado1]
        vencedores2 = [v[1] for v in resultado2]
        self.assertTrue(vencedores1 != vencedores2 or vencedores1 == vencedores2)
    #7
    def test_sem_repeticao_vencedores(self):
        # Nenhum nome pode se repetir dentro dos vencedores
        participantes = ["Ana", "Beto", "Carlos", "Duda"]
        resultado = sortear_varios(participantes, 3)
        vencedores = [v[1] for v in resultado]
        self.assertEqual(len(vencedores), len(set(vencedores)))
    #8
    def test_todos_sao_vencedores(self):
        # Quando a quantidade de vencedores é igual ao total de participantes
        participantes = ["Ana", "Beto", "Carlos", "Duda"]
        resultado = sortear_varios(participantes, 4)
        vencedores = [v[1] for v in resultado]
        self.assertCountEqual(vencedores, participantes)
    #9
    def test_lista_grande(self):
        # Teste de performance: 100 participantes, 10 vencedores
        participantes = [f"Pessoa{i}" for i in range(100)]
        resultado = sortear_varios(participantes, 10)
        vencedores = [v[1] for v in resultado]
        self.assertEqual(len(vencedores), 10)
    #10
    def test_nome_duplicado(self):
        # Lista com nomes duplicados ainda deve funcionar
        participantes = ["Ana", "Ana", "Beto", "Carlos"]
        resultado = sortear_varios(participantes, 2)
        vencedores = [v[1] for v in resultado]
        self.assertEqual(len(vencedores), 2)
        for v in vencedores:
            self.assertIn(v, participantes)

    # ---------------- TESTES NEGATIVOS ----------------
    #1
    def test_lista_vazia(self):
        # Não pode sortear vencedores de uma lista vazia
        participantes = []
        with self.assertRaises(ValueError):
            sortear_varios(participantes, 1)
    #2
    def test_numero_vencedores_zero(self):
        # Não pode haver sorteio com zero vencedores
        participantes = ["Ana", "Beto"]
        with self.assertRaises(ValueError):
            sortear_varios(participantes, 0)
    #3
    def test_numero_vencedores_negativo(self):
        # Número de vencedores negativo deve falhar
        participantes = ["Ana", "Beto"]
        with self.assertRaises(ValueError):
            sortear_varios(participantes, -1)
    #4
    def test_numero_vencedores_maior_que_lista(self):
        # Não pode pedir mais vencedores que o total de participantes
        participantes = ["Ana", "Beto", "Carlos"]
        with self.assertRaises(ValueError):
            sortear_varios(participantes, 5)
    #5
    def test_participante_invalido_none(self):
        # Não pode haver participante None
        participantes = ["Ana", None, "Carlos"]
        with self.assertRaises(TypeError):
            sortear_varios(participantes, 2)
    #6
    def test_participante_invalido_numero(self):
        # Não pode haver participante numérico
        participantes = ["Ana", 123, "Carlos"]
        with self.assertRaises(TypeError):
            sortear_varios(participantes, 2)
    #7
    def test_qtd_float(self):
        # Quantidade deve ser inteira
        participantes = ["Ana", "Beto"]
        with self.assertRaises(TypeError):
            sortear_varios(participantes, 1.5)
    #8
    def test_qtd_string(self):
        # Quantidade não pode ser string
        participantes = ["Ana", "Beto"]
        with self.assertRaises(TypeError):
            sortear_varios(participantes, "dois")
    #9
    def test_participante_vazio(self):
        # Não pode haver participante vazio
        participantes = ["Ana", " ", "Carlos"]
        with self.assertRaises(ValueError):
            sortear_varios(participantes, 2)
    #10
    def test_todos_iguais(self):
        # Se todos são iguais e precisa de mais de 1 vencedor, deve falhar
        participantes = ["Ana", "Ana", "Ana"]
        with self.assertRaises(ValueError):
            sortear_varios(participantes, 2)

if __name__ == '__main__':
    unittest.main()
