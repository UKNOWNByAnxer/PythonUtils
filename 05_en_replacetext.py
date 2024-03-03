import os

def search_remplaz_text(archive, Text_Seach, Text_remplaze):
    try:
        with open(archive, 'r') as file:
            content = file.read()
        
        Modified_content = content.replace(Text_Seach, Text_remplaze)
        
        with open(archive, 'w') as file:
            file.write(Modified_content)
        
        print(f"The text '{Text_Seach}' has been replaced by '{Text_remplaze}' in the File {archive}")
    except FileNotFoundError:
        print("The specified file was not found.")

def main():
    archive = input("Enter the name of the file you want to search and replace text: ")
    if not os.path.isfile(archive):
        print("The specified file was not found.")
        return
    
    Text_Seach = input("Enter the text you want to search for: ")
    Text_remplaze = input("Enter the text with which you want to replace: ")

    search_remplaz_text(archive, Text_Seach, Text_remplaze)

if __name__ == "__main__":
    main()
    input('\n')