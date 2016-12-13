import os

current_dir = os.path.dirname(os.path.realpath(__file__))
repeat = int(raw_input("How many pictures to take? "))
wait = int(raw_input("How long inbetween? (secs) "))

with open(current_dir + "/config.txt", "w") as configfile:
    configfile.write(str(repeat) + "\n" + str(wait) + "\n")
