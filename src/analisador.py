import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


class AnalisadorDados:
    def __init__(self, caminho_arquivo):
        self.df = pd.read_csv(caminho_arquivo)
        self.df.dropna(inplace=True)
        self.df.drop_duplicates(inplace=True)
        self.df['data'] = pd.to_datetime(self.df['data'])
        self.df['faturamento'] = self.df['quantidade'] * self.df['preco_unitario']
        sns.set_theme(style="whitegrid")

    def exibir_resumo_estatistico(self):
        print("\n--- RESUMO ESTATISTICO GERAL ---")
        print(f"Total de Registros Validos: {len(self.df)}")
        print(f"Faturamento Total: R$ {self.df['faturamento'].sum():,.2f}")
        print(f"Ticket Medio por Venda: R$ {self.df['faturamento'].mean():,.2f}")
        print(f"Quantidade Total de Itens Vendidos: {self.df['quantidade'].sum()}")
        print(f"Avaliacao Media dos Produtos: {self.df['avaliacao'].mean():.2f} / 5.00")
        print("\nEstatisticas Descritivas (Numericas):")
        print(self.df[['quantidade', 'preco_unitario', 'faturamento', 'avaliacao']].describe().round(2))

    def agrupar_por_categoria(self):
        print("\n--- FATURAMENTO E QUANTIDADE POR CATEGORIA ---")
        agrupado = self.df.groupby('categoria').agg(
            total_itens=('quantidade', 'sum'),
            faturamento_total=('faturamento', 'sum'),
            avaliacao_media=('avaliacao', 'mean')
        ).sort_values(by='faturamento_total', ascending=False)
        print(agrupado.round(2))
        return agrupado

    def filtrar_por_regiao(self, regiao):
        filtrado = self.df[self.df['regiao'].str.lower() == regiao.strip().lower()]
        if filtrado.empty:
            print(f"\nNenhum registro encontrado para a regiao '{regiao}'.")
            print(f"Regioes disponiveis: {', '.join(self.df['regiao'].unique())}")
        else:
            print(f"\n--- VENDAS NA REGIAO: {regiao.upper()} ---")
            print(filtrado[['data', 'categoria', 'produto', 'quantidade', 'faturamento']].to_string(index=False))
            print(f"Subtotal da Regiao: R$ {filtrado['faturamento'].sum():,.2f}")

    def grafico_barras_categoria(self):
        dados_cat = self.df.groupby('categoria')['faturamento'].sum().sort_values(ascending=False).reset_index()
        plt.figure(figsize=(9, 5))
        sns.barplot(data=dados_cat, x='categoria', y='faturamento', hue='categoria', palette='viridis', legend=False)
        plt.title('Faturamento Total por Categoria de Produto')
        plt.xlabel('Categoria')
        plt.ylabel('Faturamento (R$)')
        plt.tight_layout()
        plt.show()

    def grafico_linha_evolucao_temporal(self):
        dados_tempo = self.df.sort_values('data').groupby('data')['faturamento'].sum().reset_index()
        plt.figure(figsize=(10, 5))
        sns.lineplot(data=dados_tempo, x='data', y='faturamento', marker='o', color='royalblue', linewidth=2.5)
        plt.title('Evolucao Diaria do Faturamento')
        plt.xlabel('Data da Venda')
        plt.ylabel('Faturamento (R$)')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    def grafico_dispersao_preco_avaliacao(self):
        plt.figure(figsize=(9, 5))
        sns.scatterplot(
            data=self.df,
            x='preco_unitario',
            y='avaliacao',
            hue='categoria',
            size='quantidade',
            sizes=(60, 300),
            alpha=0.85
        )
        plt.title('Relacao entre Preco Unitario, Quantidade e Avaliacao')
        plt.xlabel('Preco Unitario (R$)')
        plt.ylabel('Avaliacao do Cliente (0 a 5)')
        plt.legend(bbox_to_anchor=(1.02, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
