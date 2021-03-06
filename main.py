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


def change_trait(state, value, opt_traits, has_autonomy):
    for i in range(6):
        if value != 0:
            empathyVal = 0
            cynicismVal = 0
            if state[3] > 0:
                empathyVal = state[3]
            if state[5] > 0:
                cynicismVal = state[5]
            if has_autonomy == True:
                # print("has autonomy")
                state[i] += (opt_traits[i]/value) * (1 + ( (empathyVal - cynicismVal) / 5)) #use the empathy and cynicism traits
            else:
                state[i] += (opt_traits[i]/value)
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


def print_traits(npc_state):
    print("\nHere are your NPC's traits:")
    print("Patience:", round(npc_state[0], 2))
    print("Curiosity:", round(npc_state[1], 2))
    print("Honesty:", round(npc_state[2], 2))
    print("Empathy:", round(npc_state[3], 2))
    print("Decisiveness:", round(npc_state[4], 2))
    print("Cynicism:", round(npc_state[5], 2))
    print("")


if __name__ == '__main__':
    # Possible traits for the NPC
    npc_state = []

    for i in range(6):
        npc_state.append(random.randint(-5, 5))

    is_done = False

    script_filename = 'script.json'
    with open(script_filename) as f:
        data = json.load(f)

    while not is_done:
        cynicalNPC = False
        autonomy = input("\nWould you like the NPC to have some autonomy? (Y/N) ")

        if autonomy == "Y" or autonomy == "y":
            cynicalNPC = True

        print_traits(npc_state)
        for scene_dict in data:
            options_list = scene_dict["Options"]
            if len(options_list) == 0:  # if there are no options, then it is just a scene
                next_to_print = scene_dict["Scene"]
                print(next_to_print, "\n")
            else:
                ranked_opts = rank_options(scene_dict["Options"], npc_state)

                for util, opt, index in ranked_opts:
                    print("Value:", round(util, 2), "~ Option:", opt)
                    # print("index:", index)

                print("")

                # choose the top ranked option
                print("NPC chose this option: ", ranked_opts[0][1])

                print("")

                favorability = input("How favorable is this action from -5 to 5? ")

                print("")

                opt = find_opt(scene_dict["Options"], ranked_opts[0][1])
                npc_state = change_trait(npc_state, int(favorability), opt, cynicalNPC)

                next_to_print = options_list[ranked_opts[0][2]]["Result"]

                print(next_to_print)

                # if len(next_to_print) < 5:
                #     time.sleep()

        print_traits(npc_state)
        finish = input("Would you like to restart the script with the current traits? (Y/N) ")
        if finish == "N" or finish == "n":
            is_done = True
