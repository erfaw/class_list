import csv
from stringer import Stringer
import subprocess as sp; sp.call('cls', shell=True)
import pandas as pd 

stringer = Stringer()

stringer.raw_data = stringer.load_raw_data('./one of classes.txt')
stringer.formated_str = stringer.format_converter(stringer.raw_data)

stringer.en_formated_text_output()

our_list = []
for line in stringer.en_formated_list:
    if line != stringer.en_formated_list[-1]:
        nothing = line.split()
    else:
        nothing = line.split()
        nothing.remove('time')
        nothing[1] = nothing[0].replace("EXAM(",'').replace(')','')
        nothing[0] = 'EXAM:'

    our_list.append(nothing)



my_df = pd.DataFrame(our_list, index=[i for i in range(1, len(our_list)+1)], columns=['', 'DATE', 'TIME'])
print(my_df)


#TODO: make a csv formate file with columns : ['date', 'duration']
#TODO:
