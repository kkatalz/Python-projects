ROW0 = "row0"
ROW1 = "row1"
ROW2 = "row2"
firstPlayer = "X"
secPlayer = "Y"
gameIsOver = False

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

        row_parts = field[row].split("|")
        firstColumn_part = (field[ROW0].split("|")[0] + field[ROW1].split("|")[0] + field[ROW2].split("|")[0]).replace(" ", "")
        secColumn_part = (field[ROW0].split("|")[1] + field[ROW1].split("|")[1] + field[ROW2].split("|")[1]).replace(" ", "")
        thirdColumn_part = (field[ROW0].split("|")[2] + field[ROW1].split("|")[2] + field[ROW2].split("|")[2]).replace(" ", "")
        # print("First column: ", firstColumn_part)

        if row_parts[column].strip() == "":  
            row_parts[column] = f" {player} "
            break

        elif row_parts[column].strip() == "X" or row_parts[column].strip() == "Y":
            print("That spot is already taken. Try again!")
            continue  

        elif all([x.strip() != "" for x in row_parts]):
            print("All spots are taken. Game over!")
            gameIsOver = True
            
        
        elif all([x.strip() == firstPlayer for x in row_parts]) or all(el == firstPlayer for el in firstColumn_part) or all(el == firstPlayer for el in secColumn_part) or all(el == firstPlayer for el in thirdColumn_part):
            print(f"Player {firstPlayer} won!")
            gameIsOver = True
            
        elif all([y.strip() ==secPlayer for y in row_parts]) or all(el == secPlayer for el in firstColumn_part) or all(el == secPlayer for el in secColumn_part) or all(el == secPlayer for el in thirdColumn_part):
            print(f"Player {secPlayer} won!")
            gameIsOver = True
            
        
        else:
            print("That's a tie!")
            gameIsOver = True
            
        if gameIsOver:
            break
            



    field[row] = "|".join(row_parts)
    fieldLook(field)

def main():

    print("Welcome to Tic Tac Toe!")
    field = gameField()
    fieldLook(field)

    # do{}


    while True:
    
        print(f"Player {firstPlayer}'s turn")
        
        if not fillField(field, firstPlayer):
            continue 

        print(f"Player {secPlayer}'s turn")
        if not fillField(field, secPlayer):
            continue



if __name__ == "__main__":
    main()