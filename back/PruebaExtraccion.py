from back import DataExtractor
from back.PruebaComplicada import process_and_generate_plots_from_extractor

# Extraer los datos sísmicos del archivo
times_rel, times_abs, data, start_time = DataExtractor.extract_data('xa.s12.00.mhz.1970-01-19HR00_evid00002.csv',
                                                                    'data/lunar/training/data/S12_GradeA/')

# Generar las imágenes usando los datos extraídos
output_directory = process_and_generate_plots_from_extractor(times_rel, times_abs, data, start_time)


