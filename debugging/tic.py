#!/usr/bin/python3

# Fonction pour afficher le plateau
def print_board(board):
    for row in board:
        print(" | ".join(row))       # Affiche les cases séparées par |
        print("-" * 5)              # Affiche une ligne de séparation

# Fonction pour vérifier si quelqu'un a gagné
def check_winner(board):
    # Vérifie les lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérifie les colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérifie la diagonale principale
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    # Vérifie la diagonale secondaire
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

# Fonction pour vérifier si le plateau est plein (égalité)
def board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# Fonction principale du jeu
def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]  # Crée un plateau 3x3 vide
    player = "X"                         # Commence avec le joueur X

    while True:
        print_board(board)

        # Demande à l'utilisateur de saisir la ligne
        try:
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        except ValueError:
            print("Invalid input. Please enter numbers 0, 1, or 2.")
            continue  # Redemande si ce n'est pas un nombre

        # Vérifie que les coordonnées sont dans le plateau
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Coordinates out of range. Try again.")
            continue

        # Vérifie que la case est libre
        if board[row][col] != " ":
            print("That spot is already taken! Try again.")
            continue

        # Place le symbole du joueur
        board[row][col] = player

        # Vérifie si le joueur a gagné
        if check_winner(board):
            print_board(board)
            print("Player " + player + " wins!")
            break

        # Vérifie si le plateau est plein (égalité)
        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Change de joueur
        player = "O" if player == "X" else "X"

# Lancer le jeu
tic_tac_toe()
