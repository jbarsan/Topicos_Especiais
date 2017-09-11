from .models import Cargo, Cidade, Bairro


def PopulaBanco():
    cargos = open('cargos.txt')
    for cargo in cargos:
        Cargo.objects.create(descricao=cargo)
    cargos.close()

    cidades = open('cidades.txt')
    for cidade in cidades:
        Cidade.objects.create(nome_cidade=cidade, estado='PI')
    cidades.close()

    the = Cidade.objects.get(id=216)
    bairros = open('bairros_the.txt')
    for bairro in bairros:
        Bairro.objects.create(nome_bairro=bairro, cidade=the)
    bairros.close()
