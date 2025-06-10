import fitz
import re


def data_extractor(file_path: str) -> dict:
    document = fitz.open(file_path)
    data = document.load_page(0).get_text()

    patterns = {
        "Cnpj": r"NÚMERO DE INSCRIÇÃO\n([^\n]+)",
        "Nome Empresarial": r"NOME EMPRESARIAL\n([^\n]+)",
        "Nome Fantasia": r"TÍTULO DO ESTABELECIMENTO \(NOME DE FANTASIA\)\n([^\n]+)",
        "Logradouro": r"LOGRADOURO\n([^\n]+)",
        "Numero": r"NÚMERO\n([^\n]+)",
        "Complemento": r"COMPLEMENTO\n([^\n]+)",
        "Cep": r"CEP\n([^\n]+)",
        "Bairro": r"BAIRRO/DISTRITO\n([^\n]+)",
        "Municipio": r"MUNICÍPIO\n([^\n]+)",
        "Uf": r"UF\n([^\n]+)",
        "Email": r"ENDEREÇO ELETRÔNICO\n([^\n]+)",
        "Telefone": r"TELEFONE\n([^\n]+)",
        "Situacao": r"SITUAÇÃO CADASTRAL\n([^\n]+)"
    }

    extracted_data = {}
    for key, pattern in patterns.items():
        correspondence = re.search(pattern, data)
        if correspondence:
            extracted_data[key] = correspondence.group(1).strip()
        else:
            extracted_data[key] = ""

    return extracted_data
