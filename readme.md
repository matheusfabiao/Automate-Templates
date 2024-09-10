# Gerador de Contratos Automático

Este projeto é uma aplicação simples para gerar contratos automaticamente utilizando Python, Streamlit e DocxTemplate. A interface permite que o usuário insira os dados necessários para o contrato e gere um documento Word (.docx) com as informações preenchidas.

## Estrutura do Projeto

O projeto é organizado da seguinte maneira:

```
automate_templates/
│
├── .venv/                      # Ambiente virtual (não incluído no repositório)
├── output/                     # Pasta para armazenar os contratos gerados
├── Templates/                  # Modelos de documentos
│   └── modelo_contrato_teste.docx    # Modelo de contrato Word
├── main.py                     # Arquivo principal com o código Python
└── requirements.txt            # Dependências do projeto
```

### `main.py`

Este é o código principal da aplicação. Ele utiliza o Streamlit para criar uma interface web, onde o usuário pode preencher os dados do contrato e gerar o documento final. O código faz uso da biblioteca `DocxTemplate` para substituir as variáveis no modelo de contrato (.docx) pelos valores inseridos pelo usuário.

### Modelo de Contrato

O arquivo `modelo_contrato_teste.docx` contém o modelo de contrato com variáveis que serão preenchidas pela aplicação. Exemplo de variáveis no modelo:

- `{{nome_cliente}}`
- `{{nome_parte}}`
- `{{cidade}}`
- `{{data_contrato}}`

Essas variáveis serão substituídas pelos dados fornecidos através da interface da aplicação.

## Funcionalidades

- Interface web para entrada de dados usando Streamlit.
- Geração automática de contratos com base em um modelo `.docx` utilizando a biblioteca `DocxTemplate`.
- Armazenamento dos contratos gerados na pasta `output/`.

## Como Executar

### 1. Clonar o Repositório

Clone o repositório para o seu ambiente local:

```bash
git clone https://github.com/seu-usuario/automate-templates.git
cd automate-templates
```

### 2. Criar um Ambiente Virtual

Recomenda-se criar um ambiente virtual para o projeto. Use os seguintes comandos para criar e ativar o ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate        # Linux/MacOS
.\.venv\Scripts\activate         # Windows
```

### 3. Instalar as Dependências

Instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

Para executar a aplicação, use o comando:

```bash
streamlit run main.py
```

Isso abrirá a interface da aplicação no navegador, onde você pode preencher os dados e gerar o contrato.

## Requisitos

- Python 3.8 ou superior
- Bibliotecas: `Streamlit`, `python-docx`, `docxtpl`, entre outras listadas no `requirements.txt`

## Funcionalidade Principal

Ao abrir a interface da aplicação no navegador, você poderá:

1. Preencher o nome do cliente.
2. Preencher o nome da outra parte envolvida no contrato.
3. Selecionar a cidade e a data do contrato.
4. Gerar o contrato clicando no botão "Enviar", e o documento será salvo na pasta `output/` com o nome correspondente.

## Contribuição

Sinta-se à vontade para abrir issues ou enviar pull requests. Todas as contribuições são bem-vindas.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---
