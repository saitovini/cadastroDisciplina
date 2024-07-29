import sys

MAX = 100

class Disciplina:
    def __init__(self):
        self.codigo = 0
        self.nome = ""
        self.professor = ""
        self.creditos = 0
        self.ano = 0
        self.semestre = 0
        self.nota1 = 0.0
        self.nota2 = 0.0

    def getCodigo(self):
        return self.codigo

    def getNome(self):
        return self.nome

    def getProfessor(self):
        return self.professor

    def getCreditos(self):
        return self.creditos

    def getAno(self):
        return self.ano

    def getSemestre(self):
        return self.semestre

    def getMedia(self):
        return (self.nota1 + 2.0 * self.nota2) / 3.0

    def ler(self):
        self.codigo = int(input("Código: "))
        self.nome = input("Nome: ")
        self.professor = input("Professor: ")
        self.creditos = int(input("Créditos: "))
        self.ano = int(input("Ano: "))
        self.semestre = int(input("Semestre: "))
        self.nota1 = float(input("Nota 1: "))
        self.nota2 = float(input("Nota 2: "))


class Historico:
    def __init__(self):
        self.vet = []
        self.qtd = 0

    def obterIndice(self, codigo):
        for i in range(self.qtd):
            if self.vet[i].getCodigo() == codigo:
                return i
        return -1

    def existe(self, codigo):
        return self.obterIndice(codigo) > -1

    def inserir(self, d):
        self.vet.append(d)
        self.qtd += 1

    def remover(self, codigo):
        pos = self.obterIndice(codigo)
        if pos > -1:
            self.vet.pop(pos)
            self.qtd -= 1
            return True
        else:
            return False

    def alterar(self, codigo, d):
        pos = self.obterIndice(codigo)
        if pos > -1:
            self.vet[pos] = d

    def listar(self):
        print(f"{'Cod.':<4} {'Nome':<50} {'Cred':<4} {'Ano/S':<6} {'Media':<5}")
        for d in self.vet:
            print(f"{d.getCodigo():04} {d.getNome():<50} {d.getCreditos():<4} {d.getAno()}/{d.getSemestre():<5} {d.getMedia():.2f}")

    def listar_por_semestre_ano(self, semestre, ano):
        print(f"{'Cod.':<4} {'Nome':<50} {'Cred':<4} {'Ano/S':<6} {'Media':<5}")
        for d in self.vet:
            if d.getSemestre() == semestre and d.getAno() == ano:
                print(f"{d.getCodigo():04} {d.getNome():<50} {d.getCreditos():<4} {d.getAno()}/{d.getSemestre():<5} {d.getMedia():.2f}")

    def listar_por_parte(self, parte):
        print(f"{'Cod.':<4} {'Nome':<50} {'Cred':<4} {'Ano/S':<6} {'Media':<5}")
        for d in self.vet:
            if parte in d.getNome() or parte in d.getProfessor():
                print(f"{d.getCodigo():04} {d.getNome():<50} {d.getCreditos():<4} {d.getAno()}/{d.getSemestre():<5} {d.getMedia():.2f}")

    def historico(self):
        self.listar()
        print(f"{'Coeficiente de Rendimento':<68} {self.cr():.2f}")

    def cr(self):
        s = sum(d.getMedia() * d.getCreditos() for d in self.vet)
        creditos = sum(d.getCreditos() for d in self.vet)
        return 0 if creditos == 0 else s / creditos


def menu():
    while True:
        print("1 - Inserir nova disciplina")
        print("2 - Remover disciplina pelo código")
        print("3 - Alterar disciplina pelo código")
        print("4 - Listar todas as disciplinas")
        print("5 - Listar disciplinas de um ano/semestre")
        print("6 - Listar disciplinas pelo nome/professor")
        print("7 - Histórico")
        print("8 - Sair")
        opc = int(input("Entre com a sua opção: "))
        if 1 <= opc <= 8:
            return opc


def esperarOk():
    while input() != "Ok":
        pass


def main():
    h = Historico()
    terminou = False

    while not terminou:
        opc = menu()
        if opc == 1:  # Inserir
            ficha = Disciplina()
            ficha.ler()
            h.inserir(ficha)
            print("Disciplina inserida com sucesso!")
        elif opc == 2:  # Remover
            codigo = int(input("Código: "))
            if h.remover(codigo):
                print("Disciplina removida com sucesso!")
            else:
                print("Disciplina não encontrada!")
        elif opc == 3:  # Alterar
            codigo = int(input("Código: "))
            if h.existe(codigo):
                ficha = Disciplina()
                ficha.ler()
                h.alterar(codigo, ficha)
                print("Disciplina alterada com sucesso!")
            else:
                print("Disciplina não encontrada!")
        elif opc == 4:  # Listar tudo
            h.listar()
            esperarOk()
        elif opc == 5:  # Filtrar por semestre/ano
            ano = int(input("Ano: "))
            semestre = int(input("Semestre: "))
            h.listar_por_semestre_ano(semestre, ano)
            esperarOk()
        elif opc == 6:  # Filtrar por nome/professor
            parteNome = input("Parte do nome ou professor: ")
            h.listar_por_parte(parteNome)
            esperarOk()
        elif opc == 7:  # Histórico
            h.historico()
            esperarOk()
        elif opc == 8:  # Sair
            print("Obrigado por utilizar o programa de cadastro, volte sempre!")
            terminou = True


if __name__ == "__main__":
    main()

