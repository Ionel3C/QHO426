with open("harry.txt") as h:
    with open("john.txt") as j:
        h_lines = h.readlines()
        j_lines = j.readlines()

for i in range (len(j_lines)):
    print(f"\033[90mJohn: {j_lines[i]}", end = "")
    print(f"\033[96mHarry: {h_lines[i]}", end = "")