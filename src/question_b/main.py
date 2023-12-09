import question_b

question_b.write_stock_file("stocklist.txt")
stock_dict = question_b.get_stock_list("stocklist.txt")

while True:
    print("MENU:")
    print("1-Display Stock Purchase History")
    print("2-Exit")
    option = str(input("Select option 1 or 2... "))
    while option not in ('1','2'):
        option = str(input("Invalid. Select option 1 or 2... "))
    if option == '1':
        print("\nStock Purchase History")
        print("Stock\t      Report")
        for symbol, stocks in stock_dict.items():
            print(f"{str(stocks.get_company_name()).ljust(14)}{stocks.get_symbol()}")
        print("")
    elif option == '2':
        print("Now exiting the program...Goodbye!")
        break