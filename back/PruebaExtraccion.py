from back import DataExtractor
from back.DataExtractor import extract_data
from back.PruebaComplicada import process_seismic_data_from_csv

# Ejemplo de uso
csv_file_path = './data/lunar/training/data/S12_GradeA/xa.s12.00.mhz.1975-06-26HR00_evid00198.csv'
output_directory = process_seismic_data_from_csv(csv_file_path)
print(f"Imágenes guardadas en: {output_directory}")
