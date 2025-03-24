import random
from os import system, name

class Forca:
    def __init__(self):
        self.niveis = {
            "Facil": 8,
            "Medio": 6,
            "Dificil": 4
        }
        self.chances = 0

    def definir_nivel(self, dificuldade):
        if dificuldade in self.niveis:
            self.chances = self.niveis[dificuldade]
            print(f"Nível escolhido: {dificuldade.capitalize()} ({self.chances} chances)")
        else:
            print("Nível inválido! Escolha entre: Facil, Medio ou Dificil.")

    def tentar(self):
        if self.chances > 0:
            self.chances -= 1
            print(f"Tentativa registrada! Chances restantes: {self.chances}")
        else:
            print("Você já ultrapassou o número de chances!")

    def desenho(self, chances):
        stages = [
            '''
              ------
              |    |
              |    O
              |   /|\\
              |   / \\
             ---
            ''',
            '''
              ------
              |    |
              |    O
              |   /|\\
              |   / 
             ---
            ''',
            '''
              ------
              |    |
              |    O
              |   /|\\
              |    
             ---
            ''',
            '''
              ------
              |    |
              |    O
              |   /|
              |    
             ---
            ''',
            '''
              ------
              |    |
              |    O
              |    |
              |    
             ---
            ''',
            '''
              ------
              |    |
              |    O
              |    
              |    
             ---
            ''',
            '''
              ------
              |    |
              |    
              |    
              |    
             ---
            '''
        ]
        print(stages[chances])

def limpa_tela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

def game():
    limpa_tela()
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    categorias = {
        "Frutas": ['banana', 'abacate', 'uva', 'morango', 'laranja'],
        "Animais": ['camelo', 'elefante', 'cachorro', 'gato', 'cobra'],
        "Paises": ['brasil', 'canada', 'india', 'japao', 'argentina']
    }

   
    print("Escolha uma categoria:")
    opcoes = list(categorias.keys())
    for i, categoria in enumerate(opcoes, 1):
        print(f"{i} - {categoria}")

    try:
        escolha = int(input("Digite o número da categoria desejada: ")) - 1
        if escolha < 0 or escolha >= len(opcoes):
            raise ValueError
        categoria_escolhida = opcoes[escolha]
    except ValueError:
        print("Opção inválida! Tente novamente.")
        return

    palavras = categorias[categoria_escolhida]
    palavra = random.choice(palavras)

    letras_descobertas = ['_' for _ in palavra]
    chances = 6
    letras_erradas = []

    while chances > 0:
        print("\n" + " ".join(letras_descobertas))
        print(f"\nChances restantes: {chances}")
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("Você já tentou essa letra! Tente outra.")
            continue

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if tentativa == letra:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print(f"\nUhuul! Você venceu! A palavra era: {palavra}")
            break

    if "_" in letras_descobertas:
        print(f"\nQue pena, você perdeu! A palavra era: {palavra}")

if __name__ == "__main__":
    game()
