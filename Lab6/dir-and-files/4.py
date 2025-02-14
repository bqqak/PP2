with open("Home/KBTU/Lab6/dir-and-files/s.txt", "r") as file:

    num_lines = sum(1 for line in file)

print("Total number of lines:", num_lines)
