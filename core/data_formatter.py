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


def data_formatter(extracted_data: dict) -> dict:
    ...