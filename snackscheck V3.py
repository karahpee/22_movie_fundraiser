# function goes below
def string_check(choice, options):

    global is_valid
    for var_list in options:

        # if snack is in one of the stated lists, return full answer
        if choice in var_list:

            # get full name of snack and put it in the title when outputted
            chosen = var_list[0].title()
            is_valid = "yes"
            break

        # if chosen option is not valid, set is_valid to no
        else:
            is_valid = "no"

    # if snack is not OK, ask the question again
    if is_valid == "yes":
        return chosen
    else:
        return "invalid choice"


# valid snacks and holds the list for all the snacks
# each item in valid snacks are the valid options


valid_snacks = [
    ["popcorn", "p", "corn", "a"],
    ["M&Ms", "m&ms", "m", "b"],
    ["pita chips", "chips", "pc", "pita", "c"],
    ["orange juice", "juice", "orange", "oj", "d"],
    ["water", "w", "e"],
]

# valid options for yes or no questions
yes_no = [
    ["yes", "y"],
    ["no", "n"]
]

check_snack = "invalid choice."
while check_snack == "invalid choice":
    want_snack = input("Do you want to order any snacks? ").lower()
    check_snack = string_check(want_snack, yes_no)

# looping 6 times to get testing to go faster
for item in range(0, 6):

    # ask user for desired snack and put it in lowercase
    desired_snack = input("Snack: ").lower()

    # check if snack input is valid
    snack_choice = string_check(desired_snack, valid_snacks)
    print("Snack choice: ", snack_choice)
