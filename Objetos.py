class Cachorro():
    patas = 4
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return "Este é o cachorro de nome " + self.nome

    def __repr__(self):
        return self.nome

    def latir(self):
        print("\"Au-au\"")
        print("{}, de {} anos, está enchendo o saco...".format(self.nome, self.idade))

class Filhote(Cachorro):
    def __init__(self, nome, idade, nome_do_dono):
       super().__init__(nome, idade)
       self.dono = nome_do_dono

    def __str__(self):
        return super().__str__() + ". Ele não é fofinho??"

    def latir(self):
        print("\"Au-au\"")
        print("{}, de {} anos, está sendo muito fofo...".format(self.nome, self.idade))

'''
Brincar com hierarquia de classes
Estudar funções padrão como str, init e repr
'''