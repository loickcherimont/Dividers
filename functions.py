# main function of the app
def divider_list(user_entry=input("Please enter a positive integer: ")):
    # init dividers list to empty list:
    list_of_div = []

    # check if entry is an positive int

    # core of the function:
    # casting user_entry into int
    user_entry = int(user_entry)

    match user_entry:
    # if user_entry == 0 -> return "INFINITE NUMBER"
        case 0:
            print("INFINITE NUMBER")
        # elif user_entry == 1 -> return "1"
        case 1:
            print(user_entry)
        # else user_entry > 1
        case _:
            list_of_div = [str(i) for i in range(1,user_entry+1) if user_entry % i == 0]
            list_of_div = " - ".join(list_of_div)
            print(list_of_div)

# test
divider_list()
