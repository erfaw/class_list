import csv
from stringer import Stringer
import subprocess as sp; sp.call('cls', shell=True)

stringer = Stringer()

stringer.raw_data = stringer.load_raw_data('./one of classes.txt')
stringer.formated_str = stringer.format_converter(stringer.raw_data)

stringer.en_formated_text_output()
