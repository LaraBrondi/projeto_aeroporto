voos = {}
passageiros = {}

def cadastrar_voo():
    codigo = input("Código do voo: ")
    origem = input("Origem: ")
    destino = input("Destino: ")
    preco = int(input("Preço: "))
    lugares = int(input("Quantidade de lugares: "))
    escala = int(input("Número de escalas: "))
    if codigo in voos:
        print("Código de voo já cadastrado.")
        return
    voos[codigo] = {"origem": origem, "destino": destino, "preco": preco, "lugares": lugares, "escala": escala, "passageiros": []}
    print(f"Voo cadastrado com sucesso com o código {codigo}.")

def exibir_voos_codigo():
    codigo = input("Digite o código do voo: ")
    if codigo:
        if codigo in voos:
            voo = voos[codigo]
            print(f"Código: {codigo}, Origem: {voo['origem']}, Destino: {voo['destino']}, Preço: R${voo['preco']}, Lugares: {voo['lugares']}, Escalas: {voo['escala']}")
        else:
            print("Voo não encontrado.")
    return

def buscar_voos_por_cidade():
    cidade = input("Digite a cidade: ")
    print(f"\nVoos relacionados à cidade {cidade}:")
    if cidade:
        encontrados = False
        for codigo, voo in voos.items():
            if voo["origem"].lower() == cidade.lower() or voo["destino"].lower() == cidade.lower():
                print(f"Código: {codigo}, Origem: {voo['origem']}, Destino: {voo['destino']}, Preço: R${voo['preco']}, Lugares: {voo['lugares']}, Escalas: {voo['escala']}")
                encontrados = True
        if not encontrados:
            print("Nenhum voo encontrado para esta cidade.")


def vender_passagem():
    cpf = input("CPF: ")
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    codigo = input("Código do voo: ")
    if codigo in voos:
        voo = voos[codigo]
        if voo["lugares"] > 0:
            if cpf in passageiros:
                print("CPF já cadastrado.")
                return
            if cpf not in passageiros:
                passageiros[cpf] = {"nome": nome, "telefone": telefone}
            voo["passageiros"].append(cpf)
            voo["lugares"] -= 1
            print(f"Passagem vendida para {nome} no voo {codigo}.")
        else:
            print("Não há lugares disponíveis.")
    else:
        print("Voo não encontrado.")

def cancelar_passagem():
    cpf = input("CPF: ")
    codigo = input("Código do voo: ")
    if cpf in passageiros and codigo in voos:
        voo = voos[codigo]
        if cpf in voo["passageiros"]:
            voo["passageiros"].remove(cpf)
            voo["lugares"] += 1
            print(f"Passagem cancelada para o CPF {cpf} no voo {codigo}.")
        else:
            print("Passagem não encontrada para este CPF.")
    else:
        print("CPF ou código de voo inválido.")

def exibir_passageiros_voo():
    codigo = input("Digite o código do voo: ")
    if codigo in voos:
        voo = voos[codigo]
        if voo["passageiros"]:
            print(f"Passageiros no voo {codigo}:")
            for cpf in voo["passageiros"]:
                if cpf in passageiros:
                    print(f"CPF: {cpf}, Nome: {passageiros[cpf]['nome']}, Telefone: {passageiros[cpf]['telefone']}")
        else:
            print("Nenhum passageiro cadastrado neste voo.")
    else:
        print("Voo não encontrado.")

def exibir_voos_disponiveis():
    print("\n--- Voos Disponíveis ---")
    if not voos:
        print("Nenhum voo cadastrado.")
        return
    for codigo, voo in voos.items():
        print(f"Código: {codigo}, Origem: {voo['origem']}, Destino: {voo['destino']}, Preço: R${voo['preco']}, Lugares: {voo['lugares']}, Escalas: {voo['escala']}")

def menu():
    opcao = "S"
    while opcao == "S":
        print("\n--- Menu ---")
        print("1. Cadastrar voo")
        print("2. Exibir voos por código")
        print("3. Buscar voos por cidade")
        print("4. Vender passagem")
        print("5. Cancelar passagem")
        print("6. Mostrar passageiros de um voo")
        print("7. Exibir voos disponíveis")
        print("8. Sair")

        opcaoEscolha = input("Escolha uma opção: ")

        if opcaoEscolha == "1":
            cadastrar_voo()
        elif opcaoEscolha == "2":
            exibir_voos_codigo()
        elif opcaoEscolha == "3":
            buscar_voos_por_cidade()
        elif opcaoEscolha == "4":
            vender_passagem()
        elif opcaoEscolha == "5":
            cancelar_passagem()
        elif opcaoEscolha == "6":
            exibir_passageiros_voo()
        elif opcaoEscolha == "7":
            exibir_voos_disponiveis()
        elif opcaoEscolha == "8":
            opcao = "N"
            print("Saindo do sistema...")
        else:
            print("Opção inválida.")

menu()