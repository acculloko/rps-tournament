# Encoded tournament
tournament_sample = [
    [
        [
            ["Armando", "P"],["Dave", "S"]
        ],
        [
            ["Richard", "R"],["Michael", "S"]
        ]
    ],[
        [
            ["Allen", "S"],["Omer", "P"]
        ],
        [
            ["David E.", "R"],["Richard X.", "P"]
        ]
    ]
]


# Checks move validity
def rps_strat_checker(move):
    if move.casefold() != "r" and move.casefold() != "p" and move.casefold() != "s":
        raise Exception("NoSuchStrategyError")


# Method that determines the winner in a rock-paper-scissors match
def rps_game_winner(players):

    # Guarantees that the list contains two elements
    if len(players) != 2:
        raise Exception("WrongNumberOfPlayersError")
    
    l_move = players[0][1].upper()
    r_move = players[1][1].upper()

    rps_strat_checker(l_move)
    rps_strat_checker(r_move)

    # Rock-Paper-Scissors logic
    if ((l_move == "R" and r_move == "P") or (l_move == "P" and r_move == "S") or (l_move == "S" and r_move == "R")):
        print(players[1][0] + " beats " + players[0][0])
        return players[1]
    else: 
        print(players[0][0] + " beats " + players[1][0])
        return players[0]


# Method that determines the winner of the tournament
def rps_tournament_winner(tournament):

    left = tournament[0]
    right = tournament[1]

    # Recursive logic
    if not isinstance(left[0], str):
        left = rps_tournament_winner(left)
    if not isinstance(right[0], str):
        right = rps_tournament_winner(right)
    
    return(rps_game_winner([left,right]))


print(rps_tournament_winner(tournament_sample)[0] + " wins the tournament!")