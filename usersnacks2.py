# string checks function and takes in question for valid responses
def string_checker(question, to_check):

    valid = False
    while not valid:

        response = input(question).lower()

        if response in to_check:
            return response

        else:
            for item in to_check:
                # checks response in first letter
                # makes sure is item of list
                if response == item[0]:
                    # note: returns entire response
                    # rather than just one letter
                    return item

        print("That is not a valid response.")

# main routine will start below
for item in range(0, 6):
    want_snacks = string_checker("Would you like "
                                 "Snacks?", ["yes", "no"])
    print("You said:", want_snacks)
    print()
