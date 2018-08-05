
if __name__ == "__main__":
    from isolation import Board
    from sample_players import *
    from tournament import *
    import webbrowser
    import urllib
    import urllib.parse
    import urllib.request
    from selenium import webdriver
    import os

    print()
    print("###############################")
    print("Game Playing Agent - Isolation")
    print("###############################")

    print()
    print("Select one of the following options (1, 2, etc):")
    print("     1 - Analise AI")
    print("     2 - Play the Game")
    print()

    optionChosen = input("Option: ")
    if optionChosen == "1":
        print()
        print()
        print("Analysing....")
        print()
        print()
        main()

    if optionChosen == "2":
        print()
        print()

        print("Select the kind of player you want the AI to play against: ")
        print("     1 - Random Player")
        print("     2 - Greedy Player")
        print("     3 - Human Player")
        print("     4 - AlphaBeta Player")
        print("     5 - Minimax Player")
        print()
        print()

        chosenPlayer = input("Selected player: ")
        if chosenPlayer == "1":
            enemy = RandomPlayer()
        elif chosenPlayer == "2":
            enemy = GreedyPlayer()
        elif chosenPlayer == "3":
            enemy = HumanPlayer()
        elif chosenPlayer == "4":
            enemy = game_agent.AlphaBetaPlayer()
        elif chosenPlayer == "5":
            enemy = game_agent.MinimaxPlayer()

        print()
        print()
        print()

        # create an isolation board (by default 7x7)
        player1 = RandomPlayer()
        player2 = enemy
        game = Board(player1, player2)

        game.apply_move((2, 3))
        game.apply_move((0, 5))
        print(game.to_string())

        assert (player1 == game.active_player)
        print(game.get_legal_moves())

        new_game = game.forecast_move((1, 1))
        assert (new_game.to_string() != game.to_string())
        print("\nOld state:\n{}".format(game.to_string()))
        print("\nNew state:\n{}".format(new_game.to_string()))

        winner, history, outcome = game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(game.to_string())
        print("Move history:\n{!s}".format(history))
        print()

        result = history
        print("#############################")
        print("Copy the following result")
        print(result)
        print("#############################")

        print()
        print()
        print("Do you want to see the result in a WebBrowser? (yes/no):")
        openInBrowser = input("Open in Browser: ")
        if openInBrowser == "yes":
            #webbrowser.open("http://pablo.creativossinideas.com/isoviz/display.html", new=2)

            driver = webdriver.Chrome(os.getcwd() +'/chromedriver')  # Optional argument, if not specified will search path.
            driver.get('http://pablo.creativossinideas.com/isoviz/display.html');
            search_box = driver.find_element_by_name('moves')
            resultsAsText = str(result)
            search_box.send_keys(resultsAsText)
            search_box.submit()

        elif openInBrowser == "no":
            print("#############################")
            print("Please try it at: http://pablo.creativossinideas.com/isoviz/display.html")
            print("Ok, finished!")
            print("Thank you very much")
