from core.data_extractor import data_extractor
from core.data_formatter import data_formatter
from core.bot import bot


formatted_data = (data_formatter(data_extractor(r'assets\pdfs\sinasc.pdf')))

bot(formatted_data=formatted_data, clifor='C19000', insc_est='1234567890')