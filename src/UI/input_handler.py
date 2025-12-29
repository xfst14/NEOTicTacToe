class InputHandler:
    
    @staticmethod
    def get_move():
        while True:
            try:
                inp = int(input("Choose a cell (1 - 9): "))
                if 1 <= inp <= 9:
                    return inp - 1
                print("Invalid input. Please choose between 1 and 9.")
            except ValueError:
                print("Invalid input. Please choose between 1 and 9.")

    @staticmethod
    def get_game_mode():
        print("Game modes:")
        print("1. Human vs Human ")
        print("2. Human vs Bot (Easy) ")
        print("3. Human vs Bot (Hard).")
        while True:
            try:
                game_mode = int(input("Choose game mode: "))
                if 1 <= game_mode <= 3:
                    return game_mode
                else:
                    print("\nInvalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("\nInvalid input. Please enter a number between 1 and 3.")