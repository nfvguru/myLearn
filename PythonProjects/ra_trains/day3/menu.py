def get_user_choice(*args):
    while True:
        choice = input(f"Enter {'/'.join(sorted(args))}: ")
        if choice in args:
            return choice
        print(f"{choice} is not valid; try again")
