import csv
from stringer import Stringer
import subprocess as sp; sp.call('cls', shell=True)
import pandas as pd 

stringer = Stringer()

stringer.raw_data = stringer.load_raw_data('./one of classes.txt')
stringer.formated_str = stringer.format_converter(stringer.raw_data)

stringer.en_formated_text_output()

stringer.dataframe = stringer.make_DataFrame()
print(stringer.dataframe)

stringer.dataframe.to_csv('end_result.csv')
stringer.dataframe.to_excel('end_result.xlsx')


#TODO: make a csv formate file with columns : ['date', 'duration']
#TODO:
