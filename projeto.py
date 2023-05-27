from mysql.connector import connect
import os
from constantesEParametros import Constantes
from constantesEParametros import intervalosConcentracao
from constantesEParametros import tabelaQualidadeAr
from constantesEParametros import valorDaQualidade

def obtemConexaoComMySQL (servidor = "127.0.0.1", usuario = "root", senha = "MilenaCapelli05@", bd = "projetointegrador"):
    if obtemConexaoComMySQL.conexao == None:
        obtemConexaoComMySQL.conexao = \
        connect(host = servidor, user = usuario, passwd = senha, database = bd)
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
    mp10Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(concentracaoMp10, Constantes.MP10.value, Constantes.BOA.value, 0)

    mp25Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(concentracaoMp25, Constantes.MP25.value, qualidadeFinal, indiceFinal)
    
    coInfo, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(concentracaoCo, Constantes.CO.value, qualidadeFinal, indiceFinal)

    no2Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(concentracaoNo2, Constantes.NO2.value, qualidadeFinal, indiceFinal)

    so2Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(concentracaoSo2, Constantes.SO2.value, qualidadeFinal, indiceFinal)

    o3Info, qualidadeFinal, indiceFinal = retornaInformaçõesElemento(concentracaoO3, Constantes.O3.value, qualidadeFinal, indiceFinal)

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

def funcaoPrincipal():
    while True:
        cursor.execute("select mp10 from qualidadedoar;")
        dados = cursor.fetchall()
        mp10 = dados
                
        cursor.execute("select mp25 from qualidadedoar;")
        dados = cursor.fetchall()
        mp25 = dados
        
        cursor.execute("select o3 from qualidadedoar;")
        dados = cursor.fetchall()
        o3 = dados

        cursor.execute("select co from qualidadedoar;")
        dados = cursor.fetchall()
        co = dados

        cursor.execute("select no2 from qualidadedoar;")
        dados = cursor.fetchall()
        no2 = dados

        cursor.execute("select so2 from qualidadedoar;")
        dados = cursor.fetchall()
        so2 = dados # [(0,), (1,), (2,)]

        for i in range(0, len(dados)):
            mostraInfoSobreAr(mp10[i][0], mp25[i][0], o3[i][0], co[i][0], no2[i][0], so2[i][0])
        
        while True:
            resp = input("\n Deseja consultar mais índices (S/N)? ").upper()
            if resp != "S" and resp != "N":
                print("\n A resposta tem que ser S ou N; tente novamente!!")
            else:
                break

        os.system('cls')

        if resp in ["N"]:
            break


funcaoPrincipal()