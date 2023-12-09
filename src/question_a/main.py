#add import
from question_a import validate_string1, validate_substring, get_most_likely_ancestor_consensus

def run_main():
    while True:
        dna_string = input("Please enter a DNA string that is 8 to 16 characters long: ")
        if not validate_string1(dna_string):
            print("Invalid string. Try again...")
            continue

        dna_substring = input("Please enter a DNA substring that is exactly 4 characters long: ")
        if not validate_substring(dna_substring):
            print("Invalid DNA substring length. Please try again.") 
            continue

        result_positions = get_most_likely_ancestor_consensus(dna_string, dna_substring)
        print(f"Result: {result_positions}")

        user_input = input("Create another string? : Yes or No...").lower()
        if user_input == 'Yes' or user_input == 'yes':
            run_main()
            break
        elif user_input == 'No' or user_input == 'no':
            print('Now exiting the program...Goodbye!')
            break
        else:
            print('Invalid. Type Yes or No... ')

if __name__ == "__main__":
    run_main()