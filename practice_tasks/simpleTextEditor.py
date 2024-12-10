def main():

    while True:
        file = input("Enter the file name to open or create (.txt): ")
        
        if file.endswith(".txt"):
            try:
                with open(file, "r+") as f:
                    print("File opened.")   
                    print(f.read())
                     
            except FileNotFoundError:
                with open(file, "w+") as f: 
                    print("File created.")
            break
        else:
            print("Invalid file name.")
                

    with open(file, "a") as f:
        print("\nEnter your text (type SAVE on a new line to save and exit the file):")
        while True:
            text = input()
            if text.strip().lower() == "save":
                print("File saved.")
                break
            f.write(text + "\n")       

if __name__ == "__main__":
    main()
