from mysql.connector import connect
import os
from constantesEParametros import Constantes
from constantesEParametros import intervalosConcentracao
from constantesEParametros import tabelaQualidadeAr
from constantesEParametros import valorDaQualidade
from constantesEParametros import opcoesDicionario


def obtemConexaoComMySQL(servidor="127.0.0.1", usuario="root", senha="MilenaCapelli05@", bd="projetointegrador"):
    if obtemConexaoComMySQL.conexao == None:
        obtemConexaoComMySQL.conexao = \
            connect(host=servidor, user=usuario, passwd=senha, database=bd)
    return obtemConexaoComMySQL.conexao


obtemConexaoComMySQL.conexao = None

conexao = obtemConexaoComMySQL()
cursor = conexao.cursor()


def calculaIndice(concetracaoColetada, elemento, qualidadeAr):
    indiceInicial = tabelaQualidadeAr[elemento][qualidadeAr]["indiceInicial"]
    indiceFinal = tabelaQualidadeAr[elemento][qualidadeAr]["indiceFinal"]
    concentracaoInicial = tabelaQualidadeAr[elemento][qualidadeAr]["concentracaoInicial"]
    concentracaoFinal = tabelaQualidadeAr[elemento][qualidadeAr]["concentracaoFinal"]
    if qualidadeAr == Constantes.PESSIMA.value:
        return indiceInicial + (indiceInicial/concentracaoInicial) * (concetracaoColetada - concentracaoInicial)
    else:
        return indiceInicial + ((indiceFinal - indiceInicial) / (concentracaoFinal - concentracaoInicial)) * (concetracaoColetada - concentracaoInicial)


def descobrirQualidade(index):
    match index:
        case 0:
            return Constantes.BOA.value
        case 1:
            return Constantes.MODERADA.value
        case 2:
            return Constantes.RUIM.value
        case 3:
            return Constantes.MUITO_RUIM.value


def retornaQualidade(concetracaoColetada, elemento):
    intervalos = intervalosConcentracao[elemento]
    for i in range(0, len(intervalos)):
        if i != 4:
            if concetracaoColetada >= intervalos[i][0] and concetracaoColetada <= intervalos[i][1]:
                return descobrirQualidade(i)
            continue
        elif concetracaoColetada >= intervalos[i][0]:
            return Constantes.PESSIMA.value


def retornaInformaçõesElemento(concentracaoColetada, elemento, qualidadeFinal, indiceFinal):
    qualidade = retornaQualidade(concentracaoColetada, elemento)
    indice = calculaIndice(concentracaoColetada, elemento, qualidade)
    informacoesElemento = {
        "qualidade": qualidade,
        "indice": indice
    }

    if valorDaQualidade[qualidade] >= valorDaQualidade[qualidadeFinal]:
        return informacoesElemento, qualidade, indice
    else: 
        return informacoesElemento, qualidadeFinal, indiceFinal

def mostraInfoSobreAr(concentracaoMp10, concentracaoMp25, concentracaoO3, concentracaoCo, concentracaoNo2, concentracaoSo2):
    mp10Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(
        concentracaoMp10, Constantes.MP10.value, Constantes.BOA.value, 0)

    mp25Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(
        concentracaoMp25, Constantes.MP25.value, qualidadeFinal, indiceFinal)

    coInfo, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(
        concentracaoCo, Constantes.CO.value, qualidadeFinal, indiceFinal)

    no2Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(
        concentracaoNo2, Constantes.NO2.value, qualidadeFinal, indiceFinal)

    so2Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(
        concentracaoSo2, Constantes.SO2.value, qualidadeFinal, indiceFinal)

    o3Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(
        concentracaoO3, Constantes.O3.value, qualidadeFinal, indiceFinal)

    match qualidadeFinal:
        case Constantes.BOA.value:
            print(f"\n Mp10 - Sua qualidade é classificada como {mp10Info['qualidade']} e seu indice é de {mp10Info['indice']} \n Mp25 - Sua qualidade é classificada como {mp25Info['qualidade']} e seu indice é de {mp25Info['indice']} \n O3- Sua qualidade é classificada como {o3Info['qualidade']} e seu indice é de {o3Info['indice']} \n Co - Sua qualidade é classificada como {coInfo['qualidade']} e seu indice é de {coInfo['indice']} \n So2 - Sua qualidade é classificada como {so2Info['qualidade']} e seu indice é de {so2Info['indice']} \n No2 - Sua qualidade é classificada como {no2Info['qualidade']} e seu indice é de {no2Info['indice']} \n\n A qualidade do ar é BOA \n\n Seu indice é de %.2f" % indiceFinal)

        case Constantes.MODERADA.value:
            print(f"\n Mp10 - Sua qualidade é classificada como {mp10Info['qualidade']} e seu indice é de {mp10Info['indice']} \n Mp25 - Sua qualidade é classificada como {mp25Info['qualidade']} e seu indice é de {mp25Info['indice']} \n O3- Sua qualidade é classificada como {o3Info['qualidade']} e seu indice é de {o3Info['indice']} \n Co - Sua qualidade é classificada como {coInfo['qualidade']} e seu indice é de {coInfo['indice']} \n So2 - Sua qualidade é classificada como {so2Info['qualidade']} e seu indice é de {so2Info['indice']} \n No2 - Sua qualidade é classificada como {no2Info['qualidade']} e seu indice é de {no2Info['indice']} \n\n A qualidade do ar é MODERADA \n\n Seu indice é de %.2f \n\n Significado: Pessoas de grupos sensiveis (crianças, idosos e \n pessoas com doenças respiratoria e cardiacas) podem apresentar \n sintomas como  tosse seca e cansaço. A população, em geral, não\n é afetada. " % indiceFinal)

        case Constantes.RUIM.value:
            print(f"\n Mp10 - Sua qualidade é classificada como {mp10Info['qualidade']} e seu indice é de {mp10Info['indice']} \n Mp25 - Sua qualidade é classificada como {mp25Info['qualidade']} e seu indice é de {mp25Info['indice']} \n O3- Sua qualidade é classificada como {o3Info['qualidade']} e seu indice é de {o3Info['indice']} \n Co - Sua qualidade é classificada como {coInfo['qualidade']} e seu indice é de {coInfo['indice']} \n So2 - Sua qualidade é classificada como {so2Info['qualidade']} e seu indice é de {so2Info['indice']} \n No2 - Sua qualidade é classificada como {no2Info['qualidade']} e seu indice é de {no2Info['indice']} \n\n A qualidade do ar é RUIM \n\n Seu indice é de %.2f \n\n Significado: Toda a população pode apresentar sintomas como\n tosse seca, cansaço, ardor nos olhos, nariz e garganta.\n Pessoas de grupos sensiveis (crianças, idosos e pessoas\n com doenças respiratorias e cardiacas) podem apresentar efeitos\n mais sérios na saúde. " % indiceFinal)

        case Constantes.MUITO_RUIM.value:
            print(f"\n Mp10 - Sua qualidade é classificada como {mp10Info['qualidade']} e seu indice é de {mp10Info['indice']} \n Mp25 - Sua qualidade é classificada como {mp25Info['qualidade']} e seu indice é de {mp25Info['indice']} \n O3- Sua qualidade é classificada como {o3Info['qualidade']} e seu indice é de {o3Info['indice']} \n Co - Sua qualidade é classificada como {coInfo['qualidade']} e seu indice é de {coInfo['indice']} \n So2 - Sua qualidade é classificada como {so2Info['qualidade']} e seu indice é de {so2Info['indice']} \n No2 - Sua qualidade é classificada como {no2Info['qualidade']} e seu indice é de {no2Info['indice']} \n\n A qualidade do ar é MUITO RUIM \n\n Seu indice é de %.2f \n\n Significado: Toda a população pode apresentar agravamento dos\n sintomas como tosse seca, cansaço, ardor nos olhos, nariz e\n garganta e ainda falta de ar e respiração ofegante. Efeitos\n ainda mas graves à saúde de grupos sensíveis (crianças, idosos\n e pessoas com doenças respiratórias e cardíacas." % indiceFinal)

        case Constantes.PESSIMA.value:
            print(f"\n Mp10 - Sua qualidade é classificada como {mp10Info['qualidade']} e seu indice é de {mp10Info['indice']} \n Mp25 - Sua qualidade é classificada como {mp25Info['qualidade']} e seu indice é de {mp25Info['indice']} \n O3- Sua qualidade é classificada como {o3Info['qualidade']} e seu indice é de {o3Info['indice']} \n Co - Sua qualidade é classificada como {coInfo['qualidade']} e seu indice é de {coInfo['indice']} \n So2 - Sua qualidade é classificada como {so2Info['qualidade']} e seu indice é de {so2Info['indice']} \n No2 - Sua qualidade é classificada como {no2Info['qualidade']} e seu indice é de {no2Info['indice']} \n\n A qualidade do ar é PÉSSIMA \n\n Seu indice é de %.2f \n\n Significado: Toda a população pode apresentar sérios riscos\n de manifestaçoes de doenças respiratórias e cardiovasculares.\n Aumento de mortes prematuras em pessoas de grupos sensiveis" % indiceFinal)


def inserirNoBanco(mp10, mp25, o3, co, no2, so2):
    cursor.execute(
        f"insert into qualidadedoar (mp10, mp25, o3, co, no2, so2) values ({mp10}, {mp25}, {o3}, {co}, {no2}, {so2})")
    conexao.commit()


def consultarIndices():
    while True:
        try:
            cursor.execute("select id from qualidadedoar")
            dados = cursor.fetchall()
            for i in dados:
                print(f"Id = {i[0]}")
            consulta = int(
                input("Insira o ID do índice que deseja consultar: "))
        except ValueError:
            print("Deve-se digitar apenas IDs válidos, tente novamente!")
        else:
            if consulta <= 0:
                print(
                    "Deve-se digitar IDs maiores e diferentes de zero, tente novamente!")
            else:
                break
    cursor.execute(f"select * from qualidadedoar where id = {consulta}")
    dados = cursor.fetchall()
    for linha in dados:
        mostraInfoSobreAr(linha[1], linha[2], linha[3], linha[4], linha[5], linha[6])
    while True:
        resp = input("\n Deseja consultar mais índices (S/N)? ").upper()
        if resp != "S" and resp != "N":
            print("\n A resposta tem que ser S ou N; tente novamente!!")
        else:
            break


def deletarIndice():
    while True:
        try:
            id = int(input("Insira o ID do Índice que deseja deletar: "))
        except ValueError:
            print("Deve-se digitar apenas IDs válidos, tente novamente!")
        else:
            if id <= 0:
                print(
                    "Deve-se digitar apenas IDs maiores e diferentes de zero, tente novamente!")
            else:
                break
    cursor.execute(f"delete from qualidadedoar where id = {id}")
    conexao.commit()
    while True:
        resp = input("\n Deseja deletar mais índices (S/N)? ").upper()
        if resp != "S" and resp != "N":
            print("\n A resposta tem que ser S ou N; tente novamente!!")
        else:
            break


def mostraIndice(id):
    cursor.execute(f"select * from qualidadedoar where id = {id}")
    linha = cursor.fetchone()
    print(f"id: {linha[0]}")
    print(f"mp10: {linha[1]}")
    print(f"mp25: {linha[2]}")
    print(f"o3: {linha[3]}")
    print(f"co: {linha[4]}")
    print(f"no2: {linha[5]}")
    print(f"so2: {linha[6]}")
    print()


def atualizarIndice(listaDeIndices, id):
    dicionarioDeIndices = {}
    for indice in listaDeIndices:
        while True:
            try:
                valor = float(input(f"Digite aqui seu índice do {indice}: "))
            except ValueError:
                print("Deve-se digitar apenas números, tente novamente!")
            else:
                if valor < 0:
                    print("Deve-se digitar apenas números positivos, tente novamente!")
                else:
                    break
        dicionarioDeIndices[indice] = valor

    comando = "update qualidadedoar set "
    for i in range(0, len(listaDeIndices)):
        if i == 0:
            comando += f"{listaDeIndices[i]} = {dicionarioDeIndices[listaDeIndices[i]]}"
        else:
            comando += f", {listaDeIndices[i]} = {dicionarioDeIndices[listaDeIndices[i]]}"

    comando += f" where id = {id}"

    cursor.execute(comando)
    conexao.commit()

def mostraDados():
    cursor.execute("select * from qualidadedoar")
    dados = cursor.fetchall()
    for i in dados:
        print(f"Id = {i[0]}")
        print(f"Mp10 = {i[1]}")
        print(f"Mp2,5 = {i[2]}")
        print(f"O3 = {i[2]}")
        print(f"CO = {i[3]}")
        print(f"NO2 = {i[4]}")
        print(f"SO2 = {i[5]}")
        print()

def editarIndice():
    while True:
        try:
            id = float(input("Insira o ID do Índice que deseja alterar: "))
        except ValueError:
            print("Deve-se digitar apenas números naturais, tente novamente!")
        else:
            if id <= 0:
                print(
                    "Deve-se digitar apenas IDs maiores e diferentes de zero, tente novamente!")
            else:
                break
    mostraIndice(id)
    print("Selecione os índices que deseja atualizar: ")
    print("1 - MP10 \n2 - MP2,5 \n3 - O3 \n4 - CO \n5 - NO2 \n6 - SO2 \n7 - Atualizar todos")
    print("Exemplo: 1, 2, 6 \nQualquer formato diferente será inválido!")

    elementosParaAtualizar = []

    while True:
        try:
            opcoes = input("Insira suas opções: ")
            if len(opcoes) == 1:
                if int(opcoes) == 7:
                    atualizarIndice(list(opcoesDicionario.values()), id)
                else:
                    elementosParaAtualizar.append(opcoesDicionario[opcoes])
            else:
                opcoesNumericas = opcoes.replace(", ", "-").split("-")
                for opcao in opcoesNumericas:
                    int(opcao)
                    elementosParaAtualizar.append(opcoesDicionario[opcao])
        except ValueError:
            print("Deve-se digitar apenas números naturais, tente novamente!")
        else:
            if len(opcoes) <= 0:
                print("Deve-se digitar pelo menos uma opção, tente novamente!")
            else:
                break

    if len(opcoes) != 0:
        atualizarIndice(elementosParaAtualizar, id)

    while True:
        resp = input("\n Deseja editar mais índices (S/N)? ").upper()
        if resp != "S" and resp != "N":
            print("\n A resposta tem que ser S ou N; tente novamente!!")
        else:
            break


def adicionarIndice():
    while True:
        while True:
            try:
                mp10 = float(input("Digite aqui seu índice do Mp10: "))

                mp25 = float(input("Digite aqui seu índice do Mp2,5: "))

                o3 = float(input("Digite aqui seu índice do O3: "))

                co = float(input("Digite aqui seu índice do CO: "))

                no2 = float(input("Digite aqui seu índice do NO2: "))

                so2 = float(input("Digite aqui seu índice do SO2: "))
            except ValueError:
                print("Deve-se digitar apenas números, tente novamente!")
            else:
                if mp10 < 0 or mp25 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:
                    print("Deve-se digitar apenas números positivos, tente novamente!")
                else:
                    break

        mostraInfoSobreAr(mp10, mp25, o3, co, no2, so2)
        inserirNoBanco(mp10, mp25,  o3, co, no2, so2)

        while True:
            resp = input("\n Deseja adicionar mais índices (S/N)? ").upper()
            if resp != "S" and resp != "N":
                print("\n A resposta tem que ser S ou N; tente novamente!!")
            else:
                break
        os.system('cls')
        if resp in ["N"]:
            break


def menu():
    while True:
        print("Programa para calcular a qualidade do ar!\n")
        print("Menu inicial")
        print("1 - Adicionar Índices \n2 - Editar Índices \n3 - Deletar Índices \n4 - Consultar Índices \n5 - Encerrar o programa!")
        try:
            escolha = int(
                input("Digite o número da ação que deseja realizar: "))
        except ValueError:
            print("Deve-se digitar opções válidas! \nExemplo: 1 \nTente novamente!")
        else:
            if escolha <= 0:
                print("Deve-se digitar opções válidas! \nExemplo: 1 \nTente novamente!")
            elif escolha == 1:
                adicionarIndice()
            elif escolha == 2:
                mostraDados()
                editarIndice()
            elif escolha == 3:
                mostraDados()
                deletarIndice()
            elif escolha == 4:
                consultarIndices()
            else:
                break
    print("Obrigado por usar nosso programa de cálculo da qualidade do ar!")

menu()
