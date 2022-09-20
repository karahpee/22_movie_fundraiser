def yes_no(question):

    error = "Question requires a yes or no response."

    valid = False
    while not valid:

        # ask question but put response in a lowercase return
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print(error)

# main routine goes below here

for item in range (0, 6):
    want_snacks = yes_no("Would you like to order snacks?")
    print("You said:", want_snacks)
    print()
