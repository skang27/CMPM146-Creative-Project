import time
import random
import json

# Calculate the utility of an option given a state
def utility(opt, state):
    value = 0
    index = 0

    # Possible trait values for an option
    #traits: Patience, Curiosity, Honesty, Empathy, Decisiveness, Cynicism

    # opt_traits = (random.randint(0, 10), \
    #               random.randint(0, 10), \
    #               random.randint(0, 10), \
    #               random.randint(0, 10), \
    #               random.randint(0, 10), \
    #               random.randint(0, 10))

    opt_traits = []
    opt_traits.append(opt["Patience"])
    opt_traits.append(opt["Curiosity"])
    opt_traits.append(opt["Honesty"])
    opt_traits.append(opt["Empathy"])
    opt_traits.append(opt["Decisiveness"])
    opt_traits.append(opt["Cynicism"])

    for trait in state:
        value += (trait * opt_traits[index])
        index += 1

    return value

# Rank options given a state
def rank_options(options, state):
    ranked_opts = []
    orig_index = 0

    for opt in options:
        ranked_opts.append((utility(opt["Stats"], state), opt["Option"], orig_index))
        orig_index += 1

    ranked_opts.sort(reverse=True)

    return ranked_opts

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # is_option = False
    # switch = "-\n"

    # Possible options for a scenario
    # options = {1: ["We have kids.", "We're ok.", "Chill out, lady.", "..."]}

    # Possible traits for the NPC
    npc_state = (1, 2, 3, 4, 5, 6)

    script_filename = 'script.json'
    with open(script_filename) as f:
        data = json.load(f)

    while True:
        for scene_dict in data:
            options_list = scene_dict["Options"]
            if len(options_list) == 0: #if there are no options, then it is just a scene
                next_to_print = scene_dict["Scene"] 
                print(next_to_print, "\n")

                #pause to let the player read the text printed by a period of time depending on how many words are in the string
                time.sleep(len(next_to_print) / 25)
            else:
                # print("**options found**\n")
                # TODO: Use utility functions to weigh each option (should have a dictionary with options).
                #       Should also print selected option in this if statement.
                ranked_opts = rank_options(scene_dict["Options"], npc_state)

                for util, opt, index in ranked_opts:
                    print("Value:", util, "~ Option:", opt)
                    print("index:", index)
            
                print("")

                #choose the top ranked option
                print("NPC chose this option: ", ranked_opts[0][1])


                print("")



                # TODO: Figure out how we're going to set up options along with their trait values
                #       Finalize state
                #       Add player input and the part that changes state according to the player's input
                print("How favorable is this action from -5 to 5? ", end = '')
                favorability = input()

                print("")
                #after the player says how favorable the NPC's choice was, 
                #print the rest of the script that follows the option the NPC chose
                #get the index of the chosen from the original list index stored in the rank option function
                next_to_print = options_list[ranked_opts[0][2]]["Result"] 

                print(next_to_print)

                # if len(next_to_print) < 5:
                #     time.sleep()
                #pause to let the player read the text printed by a period of time depending on how many words are in the string
                time.sleep(len(next_to_print) / 25)

                print("")

        input("To go back to the beginning of the script\nPress any key ")

        # time.sleep(1)

    # with open('script.txt') as file:
    #     scenario = 1

    #     for line in file:
    #         # The script contains a hyphen, "-", whenever it's the NPC's turn to choose an option.
    #         # This if statement switches the boolean value whenever it encounters the hyphen,
    #         # printing the rest of the script otherwise.
    #         if switch == line:
    #             is_option = not is_option
    #         elif not is_option:
    #             print(line)
    #             # time.sleep(0.5) # optional delay in text output

    #         # If a hyphen was found, executes the utility calculations for NPC option selection.
    #         if is_option:
    #             # TODO: Use utility functions to weigh each option (should have a dictionary with options).
    #             #       Should also print selected option in this if statement.

    #             ranked_opts = rank_options(options[scenario], state)

    #             for util, opt in ranked_opts:
    #                 print(util, opt, sep="  ")

    #             # This lets me iterate
    #             input()

    #             # TODO: Figure out how we're going to set up options along with their trait values
    #             #       Finalize state
    #             #       Add player input and the part that changes state according to the player's input

    #             # input_str = input() # replace these with NPC response
    #             # print(input_str)
    #             is_option = not is_option # switches boolean value back after finishing NPC response