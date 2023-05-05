from mysql.connector import connect
import os

def obtemConexaoComMySQL (servidor = "127.0.0.1", usuario = "root", senha = "MilenaCapelli05@", bd = "projetointegrador"):
    if obtemConexaoComMySQL.conexao == None:
        obtemConexaoComMySQL.conexao = \
        connect(host = servidor, user = usuario, passwd = senha, database = bd)
    return obtemConexaoComMySQL.conexao
obtemConexaoComMySQL.conexao = None 

conexao = obtemConexaoComMySQL()
cursor = conexao.cursor()

while True:

    while True:

        try:
            cursor.execute("select mp10 from qualidadedoar;")
            dados = cursor.fetchall()
            tamanho = len(dados)
            somatoria = 0 
            while len(dados) != 0:
                somatoria += dados.pop()[0]
            mp10 = somatoria / tamanho
            
            cursor.execute("select mp25 from qualidadedoar;")
            dados = cursor.fetchall()
            tamanho = len(dados)
            somatoria = 0 
            while len(dados) != 0:
                somatoria += dados.pop()[0]
            mp25 = somatoria / tamanho
           
            cursor.execute("select o3 from qualidadedoar;")
            dados = cursor.fetchall()
            tamanho = len(dados)
            somatoria = 0 
            while len(dados) != 0:
                somatoria += dados.pop()[0]
            o3 = somatoria / tamanho 

            cursor.execute("select co from qualidadedoar;")
            dados = cursor.fetchall()
            tamanho = len(dados)
            somatoria = 0 
            while len(dados) != 0:
                somatoria += dados.pop()[0]
            co = somatoria / tamanho

            cursor.execute("select no2 from qualidadedoar;")
            dados = cursor.fetchall()
            tamanho = len(dados)
            somatoria = 0 
            while len(dados) != 0:
                somatoria += dados.pop()[0]
            no2 = somatoria / tamanho

            cursor.execute("select so2 from qualidadedoar;")
            dados = cursor.fetchall()
            tamanho = len(dados)
            somatoria = 0 
            while len(dados) != 0:
                somatoria += dados.pop()[0]
            so2 = somatoria / tamanho

            os.system('cls')

        except:

            print("\n A qualidade do ar deve ser numérica; tente novamente!")

        else:

            if mp10 < 0 or mp25 < 0 or o3 < 0 or co < 0 or no2 < 0 or so2 < 0:

                print("\n Os números devem ser positivos; tente novamente!")

            else:

                break

    # Indice mp10

    if mp10 >= 0 and mp10 <= 50:

        qualiademp10 = "BOM"

        mp10ind = 0 + ((40-0) / (50-0)) * (mp10 - 0)

    elif mp10 > 50 and mp10 <= 100:

        qualiademp10 = "MODERADO"

        mp10ind = 41 + ((80-41) / (100-50)) * (mp10 - 50)

    elif mp10 > 100 and mp10 <= 150:

        qualiademp10 = "RUIM"

        mp10ind = 81 + ((120-81) / (150-100)) * (mp10 - 100)

    elif mp10 > 150 and mp10 <= 250:

        qualiademp10 = "MUITO RUIM"

        mp10ind = 121 + ((200-121) / (250-150)) * (mp10 - 150)

    elif mp10 > 250:

        qualiademp10 = "PÉSSIMO"

        mp10ind = 201 + (201/250) * mp10 - 250

    # Indice mp2.5

    if mp25 >= 0 and mp25 <= 25:

        qualiademp25 = "BOM"

        mp25ind = 0 + ((40-0) / (25-0)) * (mp25 - 0)

    elif mp25 > 25 and mp25 <= 50:

        qualiademp25 = "MODERADO"

        mp25ind = 41 + ((80-41) / (50-25)) * (mp25 - 25)

    elif mp25 > 50 and mp25 <= 75:

        qualiademp25 = "RUIM"

        mp25ind = 81 + ((120-81) / (75-50)) * (mp25 - 50)

    elif mp25 > 75 and mp25 <= 125:

        qualiademp25 = "MUITO RUIM"

        mp25ind = 121 + ((200-121) / (125-75)) * (mp25 - 75)

    elif mp25 > 125:

        qualiademp25 = "PÉSSIMO"

        mp25ind = 201 + (201/125) * (mp25 - 125)

    # Indice 03

    if o3 >= 0 and o3 <= 100:

        qualiadeo3 = "BOM"

        o3ind = 0 + ((40-0) / (100-0)) * (o3 - 0)

    elif o3 > 100 and o3 <= 130:

        qualiadeo3 = "MODERADO"

        o3ind = 41 + ((80-41) / (130-100)) * (o3 - 100)

    elif o3 > 130 and o3 <= 160:

        qualiadeo3 = "RUIM"

        o3ind = 81 + ((120-81) / (160-130)) * (o3 - 130)

    elif o3 > 160 and o3 <= 200:

        qualiadeo3 = "MUITO RUIM"

        o3ind = 121 + ((200-121) / (200-160)) * (o3 - 160)

    elif o3 > 200:

        qualiadeo3 = "PÉSSIMO"

        o3ind = 201 + (201/200) * (o3 - 200)

    # Indice CO

    if co >= 0 and co <= 9:

        qualiadeco = "BOM"

        coind = 0 + ((40-0) / (9-0)) * (co - 0)

    elif co > 9 and co <= 11:

        qualiadeco = "MODERADO"

        coind = 41 + ((80-41) / (11-9)) * (co - 9)

    elif co > 11 and co <= 13:

        qualiadeco = "RUIM"

        coind = 81 + ((120-81) / (13-11)) * (co - 11)

    elif co > 13 and co <= 15:

        qualiadeco = "MUITO RUIM"

        coind = 121 + ((200-121) / (15-13)) * (co - 13)

    elif co > 15:

        qualiadeco = "PÉSSIMO"

        coind = 201 + (201/15) * (co - 15)

    # Indice no2

    if no2 >= 0 and no2 <= 200:

        qualiadeno2 = "BOM"

        no2ind = 0 + ((40-0) / (200-0)) * (no2 - 0)

    elif no2 > 200 and no2 <= 240:

        qualiadeno2 = "MODERADO"

        no2ind = 41 + ((80-41) / (240-200)) * (no2 - 200)

    elif no2 > 240 and no2 <= 320:

        qualiadeno2 = "RUIM"

        no2ind = 81 + ((120-81) / (320-240)) * (no2 - 240)

    elif no2 > 320 and no2 <= 1130:

        qualiadeno2 = "MUITO RUIM"

        no2ind = 121 + ((200-121) / (1130-320)) * (no2 - 320)

    elif no2 > 1130:

        qualiadeno2 = "PÉSSIMO"

        no2ind = 201 + (201/125) * (no2 - 125)

    # Indice so2

    if so2 >= 0 and so2 <= 20:

        qualiadeso2 = "BOM"

        so2ind = 0 + ((40-0) / (20-0)) * (so2 - 0)

    elif so2 > 20 and so2 <= 40:

        qualiadeso2 = "MODERADO"

        so2ind = 41 + ((80-41) / (40-20)) * (so2 - 20)

    elif so2 > 40 and so2 <= 365:

        qualiadeso2 = "RUIM"

        so2ind = 81 + ((120-81) / (365-40)) * (so2 - 40)

    elif so2 > 365 and so2 <= 800:

        qualiadeso2 = "MUITO RUIM"

        so2ind = 121 + ((200-121) / (800-365)) * (so2 - 365)

    elif so2 > 800:

        qualiadeso2 = "PÉSSIMO"

        so2ind = 201 + (201/800) * (so2 - 800)

    result = 1

    # Calculo de mp10

    if mp10 >= 0 and mp10 <= 50:

        ind = mp10ind

        result = 1

    elif mp10 > 50 and mp10 <= 100:

        ind = mp10ind

        result = 2

    elif mp10 > 100 and mp10 <= 150:

        ind = mp10ind

        result = 3

    elif mp10 > 150 and mp10 <= 250:

        ind = mp10ind

        result = 4

    elif mp10 > 250:

        ind = mp10ind

        result = 5

        # Calculo mp25

    if mp25 >= 0 and mp25 < 25 and result == 1:

        if mp25ind > mp10ind and mp25ind > coind and mp25ind > o3ind and mp25ind > no2ind and mp25ind > so2ind:

            ind = mp25ind

            result = 1

    elif mp25 >= 25 and mp25 <= 50 and result <= 2:

        if mp25ind > mp10ind and mp25ind > coind and mp25ind > o3ind and mp25ind > no2ind and mp25ind > so2ind:

            ind = mp25ind

            result = 2

    elif mp25 > 50 and mp25 <= 75 and result <= 3:

        if mp25ind > mp10ind and mp25ind > coind and mp25ind > o3ind and mp25ind > no2ind and mp25ind > so2ind:

            ind = mp25ind

            result = 3

    elif mp25 > 75 and mp25 <= 125 and result <= 4:

        if mp25ind > mp10ind and mp25ind > coind and mp25ind > o3ind and mp25ind > no2ind and mp25ind > so2ind:

            ind = mp25ind

            result = 4

    elif mp25 > 125 and result <= 5:

        if mp25ind > mp10ind and mp25ind > coind and mp25ind > o3ind and mp25ind > no2ind and mp25ind > so2ind:

            ind = mp25ind

            result = 5

            # Calculo O3

    if o3 >= 0 and o3 < 100 and result == 1:

        if o3ind > mp10ind and o3ind > mp25ind and o3ind > coind and o3ind > no2ind and o3ind > so2ind:

            ind = o3ind

            result = 1

    elif o3 >= 100 and o3 <= 130 and result <= 2:

        if o3ind > mp10ind and o3ind > mp25ind and o3ind > coind and o3ind > no2ind and o3ind > so2ind:

            ind = o3ind

            result = 2

    elif o3 > 130 and o3 <= 160 and result <= 3:

        if o3ind > mp10ind and o3ind > mp25ind and o3ind > coind and o3ind > no2ind and o3ind > so2ind:

            ind = o3ind

            result = 3

    elif o3 > 160 and o3 <= 200 and result <= 4:

        if o3ind > mp10ind and o3ind > mp25ind and o3ind > coind and o3ind > no2ind and o3ind > so2ind:

            ind = o3ind

            result = 4

    elif o3 > 200 and result <= 5:

        if o3ind > mp10ind and o3ind > mp25ind and o3ind > coind and o3ind > no2ind and o3ind > so2ind:

            ind = o3ind

            result = 5

            # Calculo co

    if co >= 0 and co <= 9 and result == 1:

        if coind > mp10ind and coind > mp25ind and coind > o3ind and coind > no2ind and coind > so2ind:

            ind = coind

            result = 1

    elif co >= 9 and co <= 11 and result <= 2:

        if coind > mp10ind and coind > mp25ind and coind > o3ind and coind > no2ind and coind > so2ind:

            ind = coind

            result = 2

    elif co > 11 and co <= 13 and result <= 3:

        if coind > mp10ind and coind > mp25ind and coind > o3ind and coind > no2ind and coind > so2ind:

            ind = coind

            result = 3

    elif co > 13 and co <= 15 and result <= 4:

        if coind > mp10ind and coind > mp25ind and coind > o3ind and coind > no2ind and coind > so2ind:

            ind = coind

            result = 4

    elif co > 15 and result <= 5:

        if coind > mp10ind and coind > mp25ind and coind > o3ind and coind > no2ind and coind > so2ind:

            ind = coind

            result = 5

            # Calculo NO2

    if no2 >= 0 and no2 <= 200 and result == 1:

        if no2ind > mp10ind and no2ind > mp25ind and no2ind > o3ind and no2ind > coind and no2ind > so2ind:

            ind = no2ind

            result = 1

    elif no2 >= 200 and no2 <= 240 and result <= 2:

        if no2ind > mp10ind and no2ind > mp25ind and no2ind > o3ind and no2ind > coind and no2ind > so2ind:

            ind = no2ind

            result = 2

    elif no2 > 240 and no2 <= 320 and result <= 3:

        if no2ind > mp10ind and no2ind > mp25ind and no2ind > o3ind and no2ind > coind and no2ind > so2ind:

            ind = no2ind

            result = 3

    elif no2 > 320 and no2 <= 1130 and result <= 4:

        if no2ind > mp10ind and no2ind > mp25ind and no2ind > o3ind and no2ind > coind and no2ind > so2ind:

            ind = no2ind

            result = 4

    elif no2 > 1130 and result <= 5:

        if no2ind > mp10ind and no2ind > mp25ind and no2ind > o3ind and no2ind > coind and no2ind > so2ind:

            ind = no2ind

            result = 5

            # Calculo so2

    if so2 >= 0 and so2 <= 20 and result == 1:

        if so2ind > mp10ind and so2ind > mp25ind and so2ind > o3ind and so2ind > coind and so2ind > no2ind:

            ind = so2ind

            result = 1

    elif so2 >= 20 and so2 <= 40 and result <= 2:

        if so2ind > mp10ind and so2ind > mp25ind and so2ind > o3ind and so2ind > coind and so2ind > no2ind:

            ind = so2ind

            result = 2

    elif so2 > 40 and so2 <= 365 and result <= 3:

        if so2ind > mp10ind and so2ind > mp25ind and so2ind > o3ind and so2ind > coind and so2ind > no2ind:

            ind = so2ind

            result = 3

    elif so2 > 365 and so2 <= 800 and result <= 4:

        if so2ind > mp10ind and so2ind > mp25ind and so2ind > o3ind and so2ind > coind and so2ind > no2ind:

            ind = so2ind

            result = 4

    elif so2 > 800 and result <= 5:

        if so2ind > mp10ind and so2ind > mp25ind and so2ind > o3ind and so2ind > coind and so2ind > no2ind:

            ind = so2ind

        result = 5

    # Mostrar resultado

    if result == 1:

        print("\n Mp10 - Sua qualidade é classificada como", qualiademp10, "e seu indice é de", mp10ind, " \n Mp25 - Sua qualidade é classificada como", qualiademp25, "e seu indice é de", mp25ind, " \n O3- Sua qualidade é classificada como", qualiadeo3, "e seu indice é de", o3ind, "\n Co - Sua qualidade é classificada como",
              qualiadeco, "e seu indice é de", coind, " \n So2 - Sua qualidade é classificada como", qualiadeso2, "e seu indice é de", so2ind, "\n No2 - Sua qualidade é classificada como", qualiadeno2, "e seu indice é de", no2ind, "\n\n A qualidade do ar é BOA \n\n Seu indice é de %.2f" % ind)

    elif result == 2:

        print("\n Mp10 - Sua qualidade é classificada como", qualiademp10, "e seu indice é de", mp10ind, " \n Mp25 - Sua qualidade é classificada como", qualiademp25, "e seu indice é de", mp25ind, " \n O3- Sua qualidade é classificada como", qualiadeo3, "e seu indice é de", o3ind, "\n Co - Sua qualidade é classificada como", qualiadeco, "e seu indice é de", coind, " \n So2 - Sua qualidade é classificada como",
              qualiadeso2, "e seu indice é de", so2ind, "\n No2 - Sua qualidade é classificada como", qualiadeno2, "e seu indice é de", no2ind, "\n\n A qualidade do ar é MODERADA \n\n Seu indice é de %.2f \n\n Significado: Pessoas de grupos sensiveis (crianças, idosos e \n pessoas com doenças respiratoria e cardiacas) podem apresentar \n sintomas como  tosse seca e cansaço. A população, em geral, não\n é afetada. " % ind)

    elif result == 3:

        print("\n Mp10 - Sua qualidade é classificada como", qualiademp10, "e seu indice é de", mp10ind, " \n Mp25 - Sua qualidade é classificada como", qualiademp25, "e seu indice é de", mp25ind, " \n O3- Sua qualidade é classificada como", qualiadeo3, "e seu indice é de", o3ind, "\n Co - Sua qualidade é classificada como", qualiadeco, "e seu indice é de", coind, " \n So2 - Sua qualidade é classificada como", qualiadeso2, "e seu indice é de",
              so2ind, "\n No2 - Sua qualidade é classificada como", qualiadeno2, "e seu indice é de", no2ind, "\n\n A qualidade do ar é RUIM \n\n Seu indice é de %.2f \n\n Significado: Toda a população pode apresentar sintomas como\n tosse seca, cansaço, ardor nos olhos, nariz e garganta.\n Pessoas de grupos sensiveis (crianças, idosos e pessoas\n com doenças respiratorias e cardiacas) podem apresentar efeitos\n mais sérios na saúde. " % ind)

    elif result == 4:

        print("\n Mp10 - Sua qualidade é classificada como", qualiademp10, "e seu indice é de", mp10ind, " \n Mp25 - Sua qualidade é classificada como", qualiademp25, "e seu indice é de", mp25ind, " \n O3- Sua qualidade é classificada como", qualiadeo3, "e seu indice é de", o3ind, "\n Co - Sua qualidade é classificada como", qualiadeco, "e seu indice é de", coind, " \n So2 - Sua qualidade é classificada como", qualiadeso2, "e seu indice é de", so2ind,
              "\n No2 - Sua qualidade é classificada como", qualiadeno2, "e seu indice é de", no2ind, "\n\n A qualidade do ar é MUITO RUIM \n\n Seu indice é de %.2f \n\n Significado: Toda a população pode apresentar agravamento dos\n sintomas como tosse seca, cansaço, ardor nos olhos, nariz e\n garganta e ainda falta de ar e respiração ofegante. Efeitos\n ainda mas graves à saúde de grupos sensíveis (crianças, idosos\n e pessoas com doenças respiratórias e cardíacas." % ind)

    else:

        print("\n Mp10 - Sua qualidade é classificada como", qualiademp10, "e seu indice é de", mp10ind, " \n Mp25 - Sua qualidade é classificada como", qualiademp25, "e seu indice é de", mp25ind, " \n O3- Sua qualidade é classificada como", qualiadeo3, "e seu indice é de", o3ind, "\n Co - Sua qualidade é classificada como", qualiadeco, "e seu indice é de", coind, " \n So2 - Sua qualidade é classificada como",
              qualiadeso2, "e seu indice é de", so2ind, "\n No2 - Sua qualidade é classificada como", qualiadeno2, "e seu indice é de", no2ind, "\n\n A qualidade do ar é PÉSSIMA \n\n Seu indice é de %.2f \n\n Significado: Toda a população pode apresentar sérios riscos\n de manifestaçoes de doenças respiratórias e cardiovasculares.\n Aumento de mortes prematuras em pessoas de grupos sensiveis" % ind)

    while True:

        resp = input("\n Deseja consultar mais índices (S/N)? ") . upper()

        if resp != "S" and resp != "N":

            print("\n A resposta tem que ser S ou N; tente novamente!!")

        else:

            break

    os.system('cls')

    if resp in ["N"]:

        break
