#add import

from question_d import create_multiplication_table, display_multiplication_table

def try_again():
    while True:
        option = input("Nice going! Would you like to make another one? Type yes or no: ")
        if option == 'Yes' or option == 'yes':
            run_main()
            break
        elif option == 'No' or option == 'no':
            print('Now exiting the program...Goodbye!')
            break
        else:
            print('Invalid. Type Yes or No... ')

def run_main():
        while True:
            try:
                rows = int(input("Enter the number of rows you'd like your multiplication table to have: "))
                columns = int(input("Enter the number of columns you'd like your multiplication table to have: "))
            except ValueError:
                 print('Please enter numerical values for rows and columns.')
                 continue
            multi_table = create_multiplication_table(rows, columns)

            display_multiplication_table(multi_table)
            print()
            try_again()
            break
        
print("Hi, let's create a multiplication table!")
run_main()