class Stringer(str):
    def __init__(self):
        super().__init__()
        self.raw_data = None
        self.formated_str = None

    def load_raw_data(self, address):
        """opens txt file of date details in not formated string from base file, address is file path"""
        with open(address, mode='r') as file:
            return file.read()
    
    def format_converter(self, string):
        """catch a not formated string and replace letters with what we want. and return it"""
        return string.replace(r"/", '-').replace(r"،", ',').replace(r"۱",'1').replace(r"۲",'2').replace(r"۳",'3').replace(r"۴",'4').replace(r"۵",'5').replace(r"۶",'6').replace(r"۷",'7').replace(r"۸",'8').replace(r"۹",'9').replace(r"۹",'9').replace(r"۰",'0').replace(r")",')').replace(r"(",'(').replace(r"(",'(').replace(r"-",'-').replace(r"امتحان",'EXAM').replace(r"ساعت",'time').replace(r"درس(ت)", 'class').replace(r":", ':').strip()

    def split_with_comma(self, string):
        """catch a string, split it with ',' and return it"""
        return string.split(',')