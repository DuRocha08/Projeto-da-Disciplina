import os
from src.analisador import AnalisadorDados


def exibir_menu():
    print("\n" + "=" * 45)
    print("   SISTEMA DE ANALISE DE DADOS - CLI")
    print("=" * 45)
    print("1. Exibir Resumo Estatistico Geral")
    print("2. Exibir Agrupamento por Categoria")
    print("3. Filtrar Vendas por Regiao")
    print("4. Grafico de Barras: Faturamento por Categoria")
    print("5. Grafico de Linhas: Evolucao do Faturamento")
    print("6. Grafico de Dispersao: Preco vs Avaliacao")
    print("0. Sair")
    print("=" * 45)


def main():
    caminho_csv = os.path.join('data', 'vendas_kaggle.csv')
    if not os.path.exists(caminho_csv):
        print(f"Erro: Arquivo '{caminho_csv}' nao encontrado.")
        return

    analisador = AnalisadorDados(caminho_csv)

    while True:
        exibir_menu()
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            print("\nEntrada invalida! Digite apenas numeros inteiros correspondentes ao menu.")
            continue

        if opcao == 1:
            analisador.exibir_resumo_estatistico()
        elif opcao == 2:
            analisador.agrupar_por_categoria()
        elif opcao == 3:
            regiao = input("Digite o nome da regiao (ex: Sudeste, Sul, Norte, Nordeste, Centro-Oeste): ")
            analisador.filtrar_por_regiao(regiao)
        elif opcao == 4:
            analisador.grafico_barras_categoria()
        elif opcao == 5:
            analisador.grafico_linha_evolucao_temporal()
        elif opcao == 6:
            analisador.grafico_dispersao_preco_avaliacao()
        elif opcao == 0:
            print("\nEncerrando o sistema. Ate logo!")
            break
        else:
            print("\nOpcao inexistente! Escolha um numero entre 0 e 6.")


if __name__ == '__main__':
    main()
