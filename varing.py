import csv
from stringer import Stringer
import subprocess as sp; sp.call('cls', shell=True)

stringer = Stringer()

stringer.raw_data = stringer.load_raw_data('./one of classes.txt')
stringer.formated_str = stringer.format_converter(stringer.raw_data)
print(stringer.formated_str)




# comment before git
#=========================================
# with open("./one of classes.txt", mode='r') as file:
#     data2 = file.read()
#     data_splited = data2.split(r"درس(ت):",) # reasul like this ==> ['', ' ۱۴۰۴/۰۷/۲۱ ۱۱:۰۰-۱۴:۰۰، ', ' ۱۴۰۴/۰۷/۲۸ ۱۱:۰۰-۱۴:۰۰، ', ' ۱۴۰۴/۰۸/۰۵ ۱۱:۰۰-۱۴:۰۰، ', ' ۱۴۰۴/۰۸/۱۲ ۱۱:۰۰-۱۴:۰۰، ', ' ۱۴۰۴/۰۸/۱۹ ۱۱:۰۰-۱۴:۰۰، ', ' ۱۴۰۴/۰۸/۲۶ ۱۱:۰۰-۱۴:۰۰، ', ' ۱۴۰۴/۰۹/۱۰ ۱۱:۰۰-۱۴:۰۰، امتحان(۱۴۰۴/۱۰/۲۱) ساعت : ۱۳:۳۰-۱۵:۳۰']

# def formated_str(raw):
#     return raw.replace(r"/", '-').replace(r"،", ',').replace(r"۱",'1').replace(r"۲",'2').replace(r"۳",'3').replace(r"۴",'4').replace(r"۵",'5').replace(r"۶",'6').replace(r"۷",'7').replace(r"۸",'8').replace(r"۹",'9').replace(r"۹",'9').replace(r"۰",'0').replace(r")",')').replace(r"(",'(').replace(r"(",'(').replace(r"-",'-').replace(r"امتحان",'\nEXAM ==>').replace(r"ساعت",'').replace(r":", ':').strip()
    
# end_result= []
# for item in data_splited:
#     formated = formated_str(item)
#     # end_result.append(formated.replace(' ', ','))
#     end_result.append(formated)

# end_result.remove('')
# print(end_result)
# # print(end_result[-1])

# # moshti_nemone = end_result[0]
# # print(moshti_nemone.replace(' ', ','))
# with open('end_result.csv', mode='w') as file:
#     file.writelines(end_result)

