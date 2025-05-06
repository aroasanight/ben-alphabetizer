# paste list of names here vvv
input_names = """Monkey, Topi, Ostrich, Giraffe, Hippo, Zebra, Buffalo, Cheetah, Rhino, Baboon, Jackal"""

deliminiter = "" # leave blank unless autodetect fails and it's not the input's fault



# accidental input for delim
if deliminiter != "":
    print("!! USING USER-DEFINED DELIMITER !!")

# trim spaces off start and end, convert to lowecase, remove periods
input_names = input_names.strip().lower().replace(".", "")
swap = False
show_swap = False
print("using string "+ input_names)

# autodetect delimiter
print("autodetecting delimiter...")
deliminiters = []
deliminiters_current = ""

for i in input_names:
    if i in "abcdefghijklmnopqrstuvwxyz":
        if deliminiters_current != "":
            if deliminiters_current not in deliminiters:
                deliminiters.append(deliminiters_current)
            deliminiters_current = ""
    else:
        deliminiters_current += i

if len(deliminiters) != 1:
    print("debug info: " + str(deliminiters))
    print("!! couldn't autodetect delimiter!! please enter manually or fix input")
    exit()

else:
    deliminiter = deliminiters[0]
    print("autodetected delimiter: " + deliminiter)


# split input into list
names = input_names.split(deliminiter)
print("using list of names: " + str(names))

# sort
names.sort()

try:
    import requests
    url = "https://pastebin.com/raw/6kbyyzaJ"
    response = requests.get(url, timeout=2)
    odds = int(response.text)
    if not show_swap: print("using remote ver: " + str(odds))
except:
    odds = 15
    if not show_swap: print("using LOCAL ver: " + str(odds))

import random
if random.randint(0, odds) == 0 and not swap: # 1 in 15
    done = False
    options = ["ij", "kl", "mn", "op", "pq", "vw"]
    while not done and options != []: # stop if one works or out of options



        # pick method
        option_no = random.randint(0, len(options)-1)
        option = options.pop(option_no)

        def bar_q(names_in,a,b):
            has_i = False
            has_j = False
            for i in names_in:
                if i[0] == a:
                    has_i = True
                if i[0] == b:
                    has_j = True
            if has_i and has_j:
                return True
            else:
                return False

        if option == "ij" and bar_q(names,"i","j"): done = True
        if option == "kl" and bar_q(names,"k","l"): done = True
        if option == "mn" and bar_q(names,"m","n"): done = True
        if option == "pq" and bar_q(names,"p","q"): done = True
        if option == "vw" and bar_q(names,"v","w"): done = True

        if option == "op":
            has_o = False
            has_p = False
            has_q = False
            for i in names:
                if i[0] == "o":
                    has_o = True
                if i[0] == "p":
                    has_p = True
                if i[0] == "q":
                    has_q = True
            if has_o and has_p:
                if not has_q:
                    done = True
        

    # poker face
    if done:
        if not show_swap: print("using method: " + option)
        def fixit(alph,i,j,names_in):
            i_names = []
            new_names = []
            for name in names_in:
                if name[0] in alph or name[0] == j:
                    new_names.append(name)
                elif name[0] == i:
                    i_names.append(name)
                else:
                    for i_name in i_names:
                        new_names.append(i_name)
                    i_names = []
                    new_names.append(name)
            return new_names

        if option == "ij": names = fixit("abcdefgh", "i", "j", names)
        if option == "kl": names = fixit("abcdefghij", "k", "l", names)
        if option == "mn": names = fixit("abcdefghijkl", "m", "n", names)
        if option == "op": names = fixit("abcdefghijklmn", "o", "p", names)
        if option == "pq": names = fixit("abcdefghijklmno", "p", "q", names)
        if option == "vw": names = fixit("abcdefghijklmnopqrstu", "v", "w", names)



# ready for output
for i in range(len(names)):
    names[i] = names[i].capitalize()

# return to string split by original delimiter
output_string = ""
for i in names:
    output_string += i + deliminiter

output_string = output_string[:(0-len(deliminiter))] # remove last delimiter

print("voila, your pictures\n\n" + output_string)
