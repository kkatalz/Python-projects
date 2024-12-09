from colorama import Fore, Style

ROW0 = "row0"
ROW1 = "row1"
ROW2 = "row2"
rows = [ROW0, ROW1, ROW2]
firstPlayer = f"{Fore.GREEN}X{Style.RESET_ALL}"
secPlayer = f"{Fore.BLUE}O{Style.RESET_ALL}"

def gameField():
    field = {
        "separator": "---+---+---",
        ROW0: "   |   |   ",
        ROW1: "   |   |   ",
        ROW2: "   |   |   "
    }
    return field

def fieldLook(field):
    print("\n")
    for row in rows:
        print(field["separator"])
        print(field[row])
    print(field["separator"] +"\n")

def helperForWinner(player, fieldPlace):
    return all(el.strip() == player for el in fieldPlace) 

def winner(player, row_parts, firstColumn, secColumn, thirdColumn, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal):
  
    playerWinner = helperForWinner(player, row_parts) or \
                    helperForWinner(player, firstColumn) or \
                    helperForWinner(player, secColumn) or \
                    helperForWinner(player, thirdColumn) or \
                    helperForWinner(player, leftTopToRightBottomDiagonal) or \
                    helperForWinner(player, rightTopToLeftBottomDiagonal)
    return playerWinner


def fieldnputCheck(rowColoumn):
    while True:
            element = input(f"Enter the {rowColoumn} (0-2): ")
            try:
                element = int(element)
                if element <0 or element >2:
                    print("Invalid input")
                    continue
            except ValueError:
                print("Invalid input")
                continue
            break
    return element

def columsValue(field, column, row0 = ROW0, row1 = ROW1, row2 = ROW2):
    return [field[row0].split("|")[column].strip(), field[row1].split("|")[column].strip(), field[row2].split("|")[column].strip()]


def fillField(field, player):

    while True:
        row = fieldnputCheck("row")
        column = fieldnputCheck("column")

        row = [ROW0, ROW1, ROW2] [row] #current row
        row_parts = field[row].split("|")

        gameIsOver = False

         # fill the spot 
        if row_parts[column].strip() == "":  
            row_parts[column] = f" {player} "

            field[row] = "|".join(row_parts)
            fieldLook(field)       

            all_spots = field[ROW0].split("|") + field[ROW1].split("|") + field[ROW2].split("|")

            firstColumn = columsValue(field, 0)
            secColumn = columsValue(field, 1)
            thirdColumn = columsValue(field, 2)
            
            leftTopToRightBottomDiagonal = [field[ROW0].split("|")[0].strip(), field[ROW1].split("|")[1].strip(), field[ROW2].split("|")[2].strip()]
            rightTopToLeftBottomDiagonal = [field[ROW0].split("|")[2].strip(), field[ROW1].split("|")[1].strip(), field[ROW2].split("|")[0].strip()]
            
        elif row_parts[column].strip() == firstPlayer or row_parts[column].strip() == secPlayer:
            print("That spot is already taken. Try again!")
            continue    

        tieCondition = winner(firstPlayer, row_parts, firstColumn, secColumn, thirdColumn, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal) and winner(secPlayer, row_parts, firstColumn, secColumn, thirdColumn, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal)     

        if tieCondition: 
            print("That's a tie!")
            gameIsOver = True

        elif winner(player, row_parts, firstColumn, secColumn, thirdColumn, leftTopToRightBottomDiagonal, rightTopToLeftBottomDiagonal):
            print(f"{Fore.LIGHTMAGENTA_EX}Player {player} won!{Style.RESET_ALL}")
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