# start loop

# make it so loop runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "xxx" and count < MAX_TICKETS:
    print("You have {} tickets"
          "left".format(MAX_TICKETS - count))

    # get hold of them specific details
    name = input("Name: ")
    count += 1
    print()

if count == MAX_TICKETS:
    print("There are no longer any tickets available>")
else:
    print("You have {} tickets.   \n"
    "There are still {} tickets still availble"
    .format(count, MAX_TICKETS - count))
