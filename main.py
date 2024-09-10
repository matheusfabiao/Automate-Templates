import main as st
from pathlib import Path
from docxtpl import DocxTemplate

document_path = Path(__file__).parent / 'templates/modelo_contrato_teste.docx'
doc = DocxTemplate(document_path)

st.title('Gerador de Contrato')

client = st.text_input('Nome do Cliente:', placeholder='João da Silva')
party = st.text_input('Nome da Parte:', placeholder='Maria da Silva')
city = st.selectbox(
    'Cidade:',
    [
        'João Pessoa',
        'Campina Grande',
        'São Paulo',
        'Rio de Janeiro',
        'Porto Alegre',
        'Brasília',
    ],
)
today = st.date_input('Selecione uma data:', format='DD/MM/YYYY')

context = {
    'nome_cliente': client,
    'nome_parte': party,
    'cidade': city,
    'data_contrato': today.strftime('%d/%m/%Y'),
}

if st.button('Enviar'):
    doc.render(context)
    output_path = Path(__file__).parent / f'output/{party} - Contrato.docx'
    doc.save(output_path)
