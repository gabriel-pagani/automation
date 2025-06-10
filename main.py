from core.data_extractor import data_extractor
from core.data_formatter import data_formatter

x = (data_formatter(data_extractor(r'pdfs/sinasc.pdf')))

for k, v in x.items():
    print(f'{k}: {v}')