
## Requisitos Técnicos Obrigatórios (O que será avaliado)

1. **O Menu Interativo (`main.py`):**
O sistema deve rodar em um loop contínuo (`while True`). O menu numérico deve ser protegido com bloco `try/except` capturando `ValueError`. O programa não pode "dar tela de erro" se o usuário digitar uma letra.
2. **Motor de Dados (`analisador.py`):**
Uso exclusivo do Pandas para ler o `.csv`. A equipe deve aplicar pelo menos uma técnica de limpeza (`dropna()` ou `fillna()`) no construtor da classe. Antes de gerar um gráfico, a equipe deve utilizar comandos como `groupby` ou filtros booleanos.
3. **Arquitetura (Orientação a Objetos):**
A manipulação de dados e a geração de imagens **não podem** ser feitas soltas no `main.py`. A lógica de negócios deve ser inteiramente modelada como atributos e métodos (Ex: `self.df`) dentro da Classe no arquivo `analisador.py`.
4. **Inteligência Visual (Dashboards):**
O menu deve acionar métodos que gerem, no mínimo, **3 gráficos diferentes** (ex: Linha, Barras, Histograma, Dispersão). **Regra de Ouro:** Nenhum gráfico pode ser plotado sem título (`plt.title`) e nomes nos eixos (`plt.xlabel` e `plt.ylabel`).

---

## Como Entregar (Fluxo Git/GitHub)

Para simular o mercado de trabalho real de desenvolvimento de software, a entrega não será um arquivo compactado `.zip`, mas sim um **Pull Request (PR)** oficializado nesta plataforma.

1. Faça o **Fork** (ou Clone) deste repositório para a conta de um dos integrantes ou acesse o repositório gerado pela atividade.
2. É proibido programar diretamente na branch de produção. Crie a branch da equipe: `git checkout -b dev-nome-da-equipe`.
3. Escrevam o código nos arquivos disponibilizados fazendo `commits` frequentes. Dividam o trabalho!
4. Terminada a implementação, subam a branch para o servidor: `git push origin dev-nome-da-equipe`.
5. Abram um **Pull Request (PR)** apontando da branch de vocês para a `main`. O professor corrigirá e fará o merge deste PR.

---

## Instalação e Execução Local

Para testar o projeto no laboratório ou no computador de casa, abra o terminal e execute:

```bash
# 1. Instalar todas as dependências do projeto (Pandas, Matplotlib, Seaborn)
# 2. Iniciar o Menu Interativo
python main.py

```

---

# 📝 Formulário Oficial de Entrega (Preenchimento Obrigatório)

### 👥 Integrantes da Equipe

- Eduardo Rocha Campos 
- Matheus Amaro 
- Kauê Amorim 
- Cauã Rodrigues 
- Pedro Augusto

### 🗂️ Sobre o Dataset Escolhido

- **Tema Geral:** Vendas de E-commerce
- **Fonte de Dados (URL):** https://www.kaggle.com/
- **Motivação:** Analisar o comportamento de vendas por categoria e região para identificar os produtos mais rentáveis, avaliar o desempenho temporal do faturamento e otimizar estratégias comerciais.

### 🏗️ Arquitetura e Estruturação (O que vocês codaram)

- **Módulos / Classes Criadas:** Classe `AnalisadorDados` estruturada em `src/analisador.py`, responsável por carregar a base de dados via Pandas, executar a limpeza técnica, calcular estatísticas descritivas, realizar agrupamentos (`groupby`), filtragens por região e renderizar os gráficos analíticos.
- **Limpeza de Dados:** Aplicação de `.dropna()` para remover valores nulos e `.drop_duplicates()` para eliminação de registros duplicados diretamente no construtor da classe.

### 📊 Gráficos Desenvolvidos

Descreva detalhadamente as 3 visualizações construídas:

1. **Visão 1:** Gráfico de barras indicando o faturamento total acumulado por categoria de produto.
2. **Visão 2:** Gráfico de linhas exibindo a evolução diária do faturamento ao longo do tempo.
3. **Visão 3:** Gráfico de dispersão analisando a relação entre o preço unitário e a avaliação dos clientes, segmentado por categoria e dimensionado por quantidade de itens.
