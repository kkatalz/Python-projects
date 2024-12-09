ROW0 = "row0"
ROW1 = "row1"
ROW2 = "row2"
firstPlayer = "X"
secPlayer = "Y"

def gameField():
    field = {
        "separator": "---+---+---",
        ROW0: "   |   |   ",
        ROW1: "   |   |   ",
        ROW2: "   |   |   "
    }
    return field

def fieldLook(field):
    print("\n"+ field["separator"])
    print(field[ROW0])
    print(field["separator"])
    print(field[ROW1])
    print(field["separator"])
    print(field[ROW2])
    print(field["separator"] +"\n")

def winner(player, row_parts, firstColumn_part, secColumn_part, thirdColumn_part, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal):
  
    playerWinner = all(el.strip() == player for el in row_parts) or \
                   all(el.strip() == player for el in firstColumn_part) or \
                   all(el.strip() == player for el in secColumn_part) or \
                   all(el.strip() == player for el in thirdColumn_part) or \
                   all(el.strip() == player for el in leftTopToRightBottomDiagonal) or \
                   all(el.strip() == player for el in rightTopToLeftBottomDiagonal)
    return playerWinner



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
            row = ROW0
        elif row == 1:
            row = ROW1
        elif row == 2:
            row = ROW2

        gameIsOver = False

        row_parts = field[row].split("|")


        
         # fill the spot 
        if row_parts[column].strip() == "":  
            row_parts[column] = f" {player} "

            field[row] = "|".join(row_parts)
            fieldLook(field)       

            all_spots = field[ROW0].split("|") + field[ROW1].split("|") + field[ROW2].split("|")
            firstColumn_part = [field[ROW0].split("|")[0].strip(), field[ROW1].split("|")[0].strip(), field[ROW2].split("|")[0].strip()]
            secColumn_part = [field[ROW0].split("|")[1].strip(), field[ROW1].split("|")[1].strip(), field[ROW2].split("|")[1].strip()]
            thirdColumn_part = [field[ROW0].split("|")[2].strip(), field[ROW1].split("|")[2].strip(), field[ROW2].split("|")[2].strip()]
            leftTopToRightBottomDiagonal = [field[ROW0].split("|")[0].strip(), field[ROW1].split("|")[1].strip(), field[ROW2].split("|")[2].strip()]
            rightTopToLeftBottomDiagonal = [field[ROW0].split("|")[2].strip(), field[ROW1].split("|")[1].strip(), field[ROW2].split("|")[0].strip()]
            
        elif row_parts[column].strip() == "X" or row_parts[column].strip() == "Y":
            print("That spot is already taken. Try again!")
            continue    

        tieCondition = winner(firstPlayer, row_parts, firstColumn_part, secColumn_part, thirdColumn_part, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal) and winner(secPlayer, row_parts, firstColumn_part, secColumn_part, thirdColumn_part, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal)     

        if tieCondition: 
            print("That's a tie!")
            gameIsOver = True

        elif winner(player, row_parts, firstColumn_part, secColumn_part, thirdColumn_part, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal):
            print(f"Player {player} won!")
            gameIsOver = True

        elif all([spot.strip() != "" for spot in all_spots]):
            print("All spots are taken. Game over!")
            gameIsOver = True        

        if gameIsOver:
            return True
    
        break

        
def main():

    print("Welcome to Tic Tac Toe!")
    field = gameField()
    fieldLook(field)

    players = [firstPlayer, secPlayer]
    while True:
        for player in players:
            print(f"Player {player}'s turn")

            if fillField(field, player):
                exit()
            else:
                continue


if __name__ == "__main__":
    main()