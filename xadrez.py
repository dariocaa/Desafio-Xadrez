class Tabuleiro:
    def __init__(self):
        self.tabuleiro = self.criar_tabuleiro()

    def criar_tabuleiro(self):
        return [[" " for _ in range(8)] for _ in range(8)]

    def posicionar_peca(self, linha, coluna, peca):
        self.tabuleiro[linha][coluna] = peca

    def mover_peca(self, linha_ori, col_ori, linha_dest, col_dest):
        peca = self.tabuleiro[linha_ori][col_ori]
        if peca == " ":
            print("Não há peça na posição de origem.")
            return
        self.tabuleiro[linha_dest][col_dest] = peca
        self.tabuleiro[linha_ori][col_ori] = " "

    def exibir(self):
        print("  A B C D E F G H")
        for i in range(8):
            linha = [self.tabuleiro[i][j] for j in range(8)]
            print(f"{8-i} {' '.join(linha)} {8-i}")
        print("  A B C D E F G H")

# Função principal
def main():
    tab = Tabuleiro()
    tab.posicionar_peca(7, 4, "R")  # Rei branco em E1
    tab.posicionar_peca(0, 4, "r")  # Rei preto em E8
    tab.posicionar_peca(6, 3, "P")  # Peão branco em D2
    tab.posicionar_peca(1, 3, "p")  # Peão preto em D7

    print("Tabuleiro inicial:")
    tab.exibir()

    print("\nMovendo peão branco de D2 para D4")
    tab.mover_peca(6, 3, 4, 3)
    tab.exibir()

if __name__ == "__main__":
    main()
