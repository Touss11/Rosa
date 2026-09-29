def get_numeric_list_from_user(prompt_message="Please enter numerical values separated by spaces: "):

    while True:
        user_input = input(prompt_message)
        try:
            numeric_list = [float(item) for item in user_input.split()]
            return numeric_list
        except ValueError:
            print("Invalid input. Please enter only numerical values separated by spaces.")

my_numbers = get_numeric_list_from_user("Enter your numbers: ")
print(f"You entered: {my_numbers}")