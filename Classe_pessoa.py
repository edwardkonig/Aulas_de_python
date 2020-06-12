class Person:
    def __init__(self,nome, idade, cidade, sexo, profissao):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade
        self.sexo = sexo
        self.profissao = profissao

    def __str__(self):
        return self.textoNome()

    def textoNome(self):
        return "Esse é o " + self.nome

    def textoIdade(self):
        return "Ele tem " + self.idade + " anos."
    
    def meResponda(self, pergunta):
        for word in pergunta.split():
            if word in dir(self):
                return self.__getattribute__(word)
            # if word == "nome":
            #     return "Meu nome é {}.".format(self.nome)
            # if word == "idade":
            #     return "Eu tenho {} anos.".format(self.idade)
            # if word == "cidade":
            #     return "Eu moro em {}".format(self.cidade)
            # if word == "sexo":
            #     return "Eu me identifico como {}".format(self.sexo)
            # if word == "profissao":
            #     return "Eu trabalho como {}".format(self.profissao)

        return "Não entendi sua pergunta..."
        

'''
Utilizando o que aprendemos sobre Classes, crie uma classe Pessoa com propriedades típicas de uma pessoa. Um objeto dessa classe deverá ser capaz de responder as seguintes perguntas: - Qual seu nome?
- Qual sua idade?
- Qual sua cidade?
- Qual seu sexo?
'''

'''
Nivel de possibilidade que a pergunta não precise ser estrita
Como vc se chama/qual o seu nome - input mesmo resultado
Dica: Procurar se palavra chave aparece na pergunta
Será que consigo fazer isso para todas as propriedades?
Estudar getattribute - getters and setters
'''