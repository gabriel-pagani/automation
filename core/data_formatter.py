from constants.abbreviations import abbreviations
from constants.municipalities import municipalities
import re


def name_formatter(text: str) -> str:
    capitalized_text = text.title().strip()

    for key, value in abbreviations.items():
        capitalized_text = re.sub(r'\b{}\b'.format(re.escape(key)), value, capitalized_text)

    capitalized_text = re.sub(r'\b\d+\b', '', capitalized_text) # remove numbers from string

    result = capitalized_text.strip().replace('.', ' ').replace('-', ' ').replace(',', ' ').replace('/', ' ').replace('&', 'e')
    return ' '.join(result.split())


def municipality_formatter(text: str) -> str:
    capital_text = text.upper()

    for key, value in municipalities.items():
        if capital_text == key:
            capital_text = value
            break

    result = capital_text.strip().title()
    return result


def street_formatter(text: str) -> list:
    street = text.strip().split()
    street_type = {
        'AV': ['Avenida', re.sub('AV ', '', text)],
        'ROD': ['Rodovia', re.sub('ROD ', '', text)],
        'EST': ['Estrada', re.sub('EST ', '', text)],
        'AL': ['Alameda', re.sub('AL ', '', text)],
    }

    if street[0].upper() in street_type:
        return street_type[street[0].upper()]
    else:
        return ['Rua', re.sub('R ', '', text)]


def district_formatter(text: str) -> list:
    district = text.strip().split()
    district_type = {
        'JARDIM': 'Jardim',
        'VILA': 'Vila',
        'ZONA': 'Zona',
        'PARQUE': 'Parque',
        'RESIDENCIAL': 'Residencial',
        'SITIO': 'Sitio',
        'NUCLEO': 'Nucleo',
        'LOTEAMENTO': 'Loteamento',
        'HORTO': 'Horto',
        'GLEBA': 'Gleba',
        'FAZENDA': 'Fazenda',
        'DISTRITO': 'Distrito',
        'CONJUNTO': 'Conjunto',
        'CHACARA': 'Chacara',
        'BOSQUE': 'Bosque',
        'SRV': 'Servidao'
    }

    if district[0].upper() in district_type:
        type = district_type[district[0].upper()]
        name = re.sub(f'{district[0].upper()} ', '', text)
        return [type, name]
    else:
        return ['Bairro', re.sub('BAIRRO ', '', text)]


def suffix_remover(text: str) -> str:
    text = re.sub(r'\bLtda\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\bSa\b', '', text, flags=re.IGNORECASE)
    result = text.strip()
    return result


def data_formatter(extracted_data: dict) -> dict:
    formatted_data = {}

    formatted_data['Nome Empresarial'] = name_formatter(extracted_data['Nome Empresarial'])

    if '*' in extracted_data['Nome Fantasia'] or extracted_data['Nome Fantasia'] == extracted_data['Nome Empresarial']:
        formatted_data['Nome Fantasia'] = suffix_remover(formatted_data['Nome Empresarial'])
    else:
        formatted_data['Nome Fantasia'] = suffix_remover(name_formatter(extracted_data['Nome Fantasia']))

    formatted_data['Cnpj'] = extracted_data['Cnpj'].strip()

    formatted_data['Cep'] = extracted_data['Cep'].replace('-', '').replace('.', '').strip()

    street_info = street_formatter(extracted_data['Logradouro'])
    formatted_data['Tipo Rua'] = street_info[0]
    formatted_data['Nome Rua'] = street_info[1].title()

    if not re.search(r'\d', extracted_data['Numero']):
        formatted_data['Numero'] = ''
    else:
        formatted_data['Numero'] = extracted_data['Numero'].upper().strip()

    if '*' in extracted_data['Complemento']:
        formatted_data['Complemento'] = ''
    else:
        formatted_data['Complemento'] = extracted_data['Complemento'].title().strip()

    district_info = district_formatter(extracted_data['Bairro'])
    formatted_data['Tipo Bairro'] = district_info[0]
    formatted_data['Nome Bairro'] = district_info[1].title()

    formatted_data['Uf'] = extracted_data['Uf'].upper().strip()

    formatted_data['Municipio'] = municipality_formatter(extracted_data['Municipio'])

    phone = extracted_data['Telefone'].replace('(', '').replace(')', '').replace('-', '').replace(' ', '').strip()

    formatted_data['Celular1'] = phone
    formatted_data['Celular2'] = ''

    if '/' in phone:
        formatted_data['Celular1'], formatted_data['Celular2'] = phone.split('/')

    if formatted_data['Celular2'] and all(char == '0' for char in formatted_data['Celular2']):
        formatted_data['Celular2'] = ''

    if formatted_data['Celular2'] == formatted_data['Celular1']:
        formatted_data['Celular2'] = ''

    if '@' not in extracted_data['Email']:
        formatted_data['Email'] = ''
    else:
        formatted_data['Email'] = extracted_data['Email'].strip().lower()

    formatted_data['Situacao'] = extracted_data['Situacao'].strip()
    return formatted_data
