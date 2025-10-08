class Stringer(str):
    def __init__(self):
        super().__init__()
        self.raw_data = None
        self.formated_str = None
        self.csv_output = None
        self.en_formated_list = []

    def load_raw_data(self, address):
        """opens txt file of date details in not formated string from base file, address is file path"""
        with open(address, mode='r') as file:
            return file.read()
    
    def format_converter(self, string):
        """catch a not formated string and replace letters with what we want. and return it"""
        return string.replace(r"/", '-').replace(r"،", ',').replace(r"۱",'1').replace(r"۲",'2').replace(r"۳",'3').replace(r"۴",'4').replace(r"۵",'5').replace(r"۶",'6').replace(r"۷",'7').replace(r"۸",'8').replace(r"۹",'9').replace(r"۹",'9').replace(r"۰",'0').replace(r")",')').replace(r"(",'(').replace(r"(",'(').replace(r"-",'-').replace(r"امتحان",'EXAM').replace(r"ساعت",'time').replace(r"درس(ت)", 'class').replace(r":", ':').strip()

    def split_with_comma(self, string):
        """catch a string, split it with ',' and return it"""
        r_list = string.split(',')
        e_list = [x.strip() for x in r_list]
        return e_list
    
    def en_formated_text_output(self):
        """make a text output file name: en_formated_text_of_classes_and_exam.txt"""
        with open('./en_formated_text_of_classes_and_exam.txt', mode='w') as file:
            for index in self.split_with_comma(self.formated_str):
                file.write(index)
                self.en_formated_list.append(index)
                file.write('\n')
