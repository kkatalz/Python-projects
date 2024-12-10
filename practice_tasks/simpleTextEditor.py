import os

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))

    while True:
        file = input("Enter the file name to open or create: ").strip()
        file_path = os.path.join(script_directory, file)

        try:
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    print("File opened.")   
                    print(f.read())
                    
            else:
                with open(file_path, "w") as f: 
                    print("File created.")
            break 

        except OSError:
            print("Error opening file.")
            return
      
                

    with open(file_path, "a") as f:
        print("\nEnter your text (type SAVE on a new line to save and exit the file):")
        while True:
            text = input()
            if text.strip().lower() == "save":
                print("File saved.")
                break
            f.write(text + "\n")       

if __name__ == "__main__":
    main()
