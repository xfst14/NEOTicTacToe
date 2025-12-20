from game_flow import Game

if __name__ == '__main__':
    # MAIN MENU LOOP: after each game ends, return to main menu (mode selection)
    while True:
        game = Game()  # Choose game mode
        game.run()     # Play one full game with that mode

        # Ask if the player wants to go back to the main menu (choose mode again)
        while True:
            choice = input("\nReturn to main menu and play again? (y/n): ").strip().lower()
            if choice in ['y', 'n']:
                break
            else:
                print("Invalid input. Please enter 'y' or 'n'.")

        if choice != 'y':
            print("\nThanks for playing NEO TIC-TAC-TOE!")
            break