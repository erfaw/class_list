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


#DONE: make a csv formate file with columns : ['date', 'duration']
#TODO: in program vaghti arzesh peyda mikne ke beshe bahash to Google Calendar event set kard, felan bedarde khasi nemikhore,
#TODO: fix kardane vaghti ke data filed 'makan' dare 
#TODO: add kardane mechanism khondan va sakhtan az roye chand file
#TODO: ezafe kardane TITLE ba jahayi az file haye output ke lazeme
