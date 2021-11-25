import time

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_option = False
    switch = "-\n"

    with open('script.txt') as file:
        for line in file:
            # The script contains a hyphen, "-", whenever it's the NPC's turn to choose an option.
            # This if statement switches the boolean value whenever it encounters the hyphen,
            # printing the rest of the script otherwise.
            if switch == line:
                is_option = not is_option
            elif not is_option:
                print(line)
                # time.sleep(0.5) # optional delay in text output

            # If a hyphen was found, executes the utility calculations for NPC option selection.
            if is_option:
                # TODO: Use utility functions to weigh each option (should have a dictionary with options).
                #       Should also print selected option in this if statement.
                # input_str = input() # replace these with NPC response
                # print(input_str)
                is_option = not is_option # switches boolean value back after finishing NPC response




