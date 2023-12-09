#write functions here, don't add input('') statements here!

class Stock():
    __symbol = None
    __company_name = None
    def __init__(self, symbol, company):
        self.__symbol = symbol
        self.__company_name = company

    def get_symbol(self):
        return self.__symbol
    
    def get_company_name(self):
        return self.__company_name
    
def get_stock_list(file_name):
    stock_dictionary = {}
    in_file = open(file_name, 'r')
    for line in in_file:
        symbol, company_name = line.strip().split(' ', 1)
        stock = Stock(symbol, company_name)
        stock_dictionary[symbol] = stock
    return stock_dictionary

def write_stock_file(file):
    out_file = open(file, 'w')
    symbols = ['APPL','CAT','EK','GOOG','MSFT']
    companies = ['Apple Inc','Caterpillar','Eastman Kodak','Google','Microsoft']
    for i in range(len(symbols)):
        out_file.write(symbols[i] + ' ' + companies[i] + '\n')
    out_file.close()