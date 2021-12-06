import time
import random
import json


# Calculate the utility of an option given a state
def utility(opt, state):
    value = 0
    index = 0

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


def change_state(state, value):
    for i in range(6):
        state[i] += (value * state[i])

    return state


# Rank options given a state
def rank_options(options, state):
    ranked_opts = []
    orig_index = 0

    for opt in options:
        ranked_opts.append((utility(opt["Stats"], state), opt["Option"], orig_index))
        orig_index += 1

    ranked_opts.sort(reverse=True)

    return ranked_opts


if __name__ == '__main__':
    # Possible traits for the NPC
    npc_state = [1, 2, 3, 4, 5, 6]

    not_done = True

    script_filename = 'script.json'
    with open(script_filename) as f:
        data = json.load(f)

    while not_done:
        for scene_dict in data:
            options_list = scene_dict["Options"]
            if len(options_list) == 0:  # if there are no options, then it is just a scene
                next_to_print = scene_dict["Scene"]
                print(next_to_print, "\n")
            else:
                # print("**options found**\n")
                # TODO: Use utility functions to weigh each option (should have a dictionary with options).
                #       Should also print selected option in this if statement.
                ranked_opts = rank_options(scene_dict["Options"], npc_state)

                for util, opt, index in ranked_opts:
                    print("Value:", round(util, 2), "~ Option:", opt)
                    print("index:", index)

                print("")

                # choose the top ranked option
                print("NPC chose this option: ", ranked_opts[0][1])

                print("")

                # TODO: Figure out how we're going to set up options along with their trait values
                #       Finalize state
                #       Add player input and the part that changes state according to the player's input
                favorability = input("How favorable is this action from -5 to 5? ")

                print("")

                npc_state = change_state(npc_state, int(favorability))

                # after the player says how favorable the NPC's choice was,
                # print the rest of the script that follows the option the NPC chose
                # get the index of the chosen from the original list index stored in the rank option function
                next_to_print = options_list[ranked_opts[0][2]]["Result"]

                print(next_to_print)

                # if len(next_to_print) < 5:
                #     time.sleep()

                print("")

        finish = input("Would you like to restart the script with the current traits? (Y/N) ")
        if finish == "N" or finish == "n":
            not_done = False
