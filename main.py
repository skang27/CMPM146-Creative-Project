import time
import random
import json


# Calculate the utility of an option given a state
def utility(opt, state):
    value = 0
    index = 0

    opt_traits = create_opt_traits(opt)

    for trait in state:
        value += (trait * opt_traits[index])
        index += 1

    return value


def change_trait(state, value, opt_traits):
    for i in range(6):
        if value != 0:
            state[i] += opt_traits[i]/value
            if state[i] > 5:
                state[i] = 5
            elif state[i] < -5:
                state[i] = -5

    return state


def find_opt(options, to_find):
    for opt in options:
        if to_find == opt["Option"]:
            return create_opt_traits(opt["Stats"])


def create_opt_traits(opt):
    opt_traits = [opt["Patience"], opt["Curiosity"], opt["Honesty"], opt["Empathy"], opt["Decisiveness"],
                  opt["Cynicism"]]

    return opt_traits


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
    npc_state = [2, 2, 2, 2, 2, 2]

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

                opt = find_opt(scene_dict["Options"], ranked_opts[0][1])
                npc_state = change_trait(npc_state, int(favorability), opt)

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
            print("\nHere are your NPC's traits:")
            print("Patience:", round(npc_state[0],2))
            print("Curiosity:", round(npc_state[1],2))
            print("Honesty:", round(npc_state[2],2))
            print("Empathy:", round(npc_state[3],2))
            print("Decisiveness:", round(npc_state[4],2))
            print("Cynicism:", round(npc_state[5],2))
            not_done = False
