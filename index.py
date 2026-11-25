Projeto Python
escolha = ""

print ("\n")

def escolha_valor(escolha):
    
    ap = 700
    casa = 900
    estudio = 1200
    valor_vaga = 60

    #----------------------------------------------------------------------------------------------------------
    while True:
        try:
            print (end="\n\n" "O contrato imobiliário é de R$2.000,00 divididos em até 5 vezes""\n""\n")

            escolha =  int(input ("locaçoes:""\n\n""(1) Apartamentos R$700,00 + contrato imobiliário" "\n" "(2) Casa R$900,00 + contrato imobiliário""\n""(3) Estudio R$1200,00 + contrato imobiliário""\n"))

        except ValueError:
            print("\n""Escolha de 1 a 3!""\n")
            continue


        if escolha == 1: #Retorna valor final do apartamento
            
            quarto_ap = int(input(f"(1) 1 Quarto R${int(ap)}\n(2) 2 Quartos R${int(ap)} + R$200\n"))
            if quarto_ap == 2:
                ap += 200

            vaga = int(input(f"(1) Incluir vaga de garagem R${ap} + R$300""\n"f"(2) Nao incluir vaga de garagem R${ap}""\n"))
            if vaga == 1:
                ap += 300
            (print("Oferecemos um desconto de 5% para pessoas sem crianças"))
            crianças = int(input("(1) Com criança""\n""(2) Sem criança""\n"))
            if crianças == 2:
                ap = ap - (ap * 5 / 100)
        
            return ap
        #----------------------------------------------------------------------------------------------------------
        elif escolha == 2:

            quarto_casa = int(input ("(1) 1 Quarto R$900""\n""(2) 2 Quartos R$900 + R$250""\n"))
            if quarto_casa == 2:
                casa += 250
            vaga = int(input(f"(1) Incluir vaga de garagem R${casa} + R$300""\n"f"(2) Nao incluir vaga de garagem R${casa}""\n"))
            if vaga == 1:
                casa += 300
            return casa
        #----------------------------------------------------------------------------------------------------------
        elif escolha == 3:
            
            vaga = int(input(f"(1) Nao incluir vaga de garagem R${estudio}""\n"f"(2) Incluir 2 vaga de garagem R${estudio} + R$250""\n"))
            if vaga == 2:
                estudio += 250
                vaga_extra = int(input("(1) Acrescentar mais vagas no valor de R$ 60,00""\n""(2) Nao acrescentar mais vagas""\n"))
                if vaga_extra == 1:
                    qnt_vagas = int(input("Quantas vagas?""\n"))
                    estudio += valor_vaga * qnt_vagas

            return estudio
        #----------------------------------------------------------------------------------------------------------
        else:
            print("\n""Escolha de 1 a 3!")
            continue
        

orçamento = escolha_valor(escolha)

print (f"valor do aluguel e R${float(orçamento):.2f} + R$2000 do contrato (em ate 5 vezes)")
contrato = 2000
parcelas_contrato = 5
valor_parcela_contrato = contrato / parcelas_contrato
valor_total_primeiros_5_meses = orçamento + valor_parcela_contrato


import csv # Geração do arquivo CSV com as 12 parcelas do orçamento


parcelas_totais = 12

with open("parcelas_orcamento.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Mês", "Valor aluguel (R$)", "Contrato (R$)", "Total do mês (R$)"])

    for mes in range(1, parcelas_totais + 1):
        if mes <= parcelas_contrato:
            total_mes = orçamento + valor_parcela_contrato
            escritor.writerow([mes, f"{orçamento:.2f}", f"{valor_parcela_contrato:.2f}", f"{total_mes:.2f}"])
        else:
            total_mes = orçamento
            escritor.writerow([mes, f"{orçamento:.2f}", "0.00", f"{total_mes:.2f}"])

print("\nArquivo 'parcelas_orcamento.csv' gerado com sucesso!")
print("As 12 parcelas do orçamento foram salvas no arquivo CSV.")
