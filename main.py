import time
import random

# Calculate the utility of an option given a state
def utility(opt, state):
    value = 0
    index = 0

    # Possible trait values for an option
    opt_traits = (random.randint(0, 10), \
                  random.randint(0, 10), \
                  random.randint(0, 10), \
                  random.randint(0, 10), \
                  random.randint(0, 10), \
                  random.randint(0, 10))

    for trait in state:
        value += (trait * opt_traits[index])
        index += 1

    return value

# Rank options given a state
def rank_options(options, state):
    ranked_opts = []

    for opt in options:
        ranked_opts.append((utility(opt, state), opt))

    ranked_opts.sort(reverse=True)

    return ranked_opts

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    is_option = False
    switch = "-\n"

    # Possible options for a scenario
    options = {1: ["We have kids.", "We're ok.", "Chill out, lady.", "..."]}

    # Possible traits for the NPC
    state = (1, 2, 3, 4, 5, 6)

    with open('script.txt') as file:
        scenario = 1

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

                ranked_opts = rank_options(options[scenario], state)

                for util, opt in ranked_opts:
                    print(util, opt, sep="  ")

                # This lets me iterate
                input()

                # TODO: Figure out how we're going to set up options along with their trait values
                #       Finalize state
                #       Add player input and the part that changes state according to the player's input

                # input_str = input() # replace these with NPC response
                # print(input_str)
                is_option = not is_option # switches boolean value back after finishing NPC response




