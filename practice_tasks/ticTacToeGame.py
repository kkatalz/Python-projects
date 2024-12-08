def gameField():
    field = {
        "separator": "---+---+---",
        "row0": "   |   |   ",
        "row1": "   |   |   ",
        "row2": "   |   |   "
    }
    return field

def fieldLook(field):
    print("\n"+ field["separator"])
    print(field["row0"])
    print(field["separator"])
    print(field["row1"])
    print(field["separator"])
    print(field["row2"])
    print(field["separator"] +"\n")

def fillField(field, player):

    while True:
        while True:
            row = input("Enter the row (0-2): ")
            try:
                row = int(row)
                if row<0 or row>2:
                    print("Invalid input")
                    continue
            except ValueError:
                print("Invalid input")
                continue
            break
        
        while True:
            column = input("Enter the column (0-2): ")
            try:
                column = int(column)
                if column<0 or column>2:
                    print("Invalid input")
                    continue
            except ValueError:
                print("Invalid input")
                continue
            break

        if row == 0:
            row = "row0"
        elif row == 1:
            row = "row1"
        elif row == 2:
            row = "row2"

        row_parts = field[row].split("|")

        if row_parts[column].strip() == "":  
            row_parts[column] = f" {player} "
            
            break

        elif row_parts[column].strip() == "X" or row_parts[column].strip() == "Y":
            print("That spot is already taken. Try again!")
            continue  
        # check if all spots are taken
        elif all([x.strip() != "" for x in row_parts]):
            print("All spots are taken. Game over!")
            break

    field[row] = "|".join(row_parts)
    fieldLook(field)

def main():
    firstPlayer = "X"
    secPlayer = "Y"

    print("Welcome to Tic Tac Toe!")
    field = gameField()

    fieldLook(field)


    print(f"Player {firstPlayer}'s turn")
    fillField(field, firstPlayer)

    print(f"Player {secPlayer}'s turn")
    fillField(field, secPlayer)

# TODO: Add logic to check is someone won the game
# TODO: Add logic to check if the game is a tie
# TODO: Add logic to check if the game is over



if __name__ == "__main__":
    main()