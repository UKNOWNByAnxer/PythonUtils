import os
import shutil

def organize_files():
    # Get the current working directory path
    source_path = os.getcwd()

    # Create destination folders if they don't exist
    folders = ["Images", "Documents", "Videos", "Music", "Programming", "Organized Files"]
    for folder in folders:
        folder_path = os.path.join(source_path, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    
    # Get a list of all files in the source folder
    files = os.listdir(source_path)
    
    # Organize files into destination folder based on their extensions
    for file in files:
        # Ignore hidden folders and files
        if not file.startswith('.'):
            # Get the file extension
            _, extension = os.path.splitext(file)
            extension = extension.lower()  # Convert to lowercase
            
            # Define destination folder based on extension
            if extension in ['.jpg', '.jpeg', '.png', '.gif', 
                             '.bmp', '.tiff', '.svg', '.webp', 
                             '.ico', '.psd','.ai', '.eps', 
                             '.raw', '.cr2', '.nef', '.orf',
                             '.sr2', '.heic', '.tif', '.jpe']:
                destination_folder = os.path.join(source_path, "Images")
            elif extension in ['.doc', '.docx', '.pdf', '.txt', 
                               '.rtf', '.odt', '.docm', '.dotx',
                               '.dotm', '.xlsx', '.xlsm', '.xltx',
                               '.xltm', '.xlsb', '.xlam', '.pptx',
                               '.pptm', '.potx', '.potm', '.ppam',
                               '.ppsx', '.ppsm', '.sldx', '.sldm',
                               '.onetoc', '.onepkg']:
                destination_folder = os.path.join(source_path, "Documents")
            elif extension in ['.mp4', '.mov', '.avi', '.mkv', 
                               '.avi', '.mp4', '.wmv', '.wma', '.mov',
                               '.flv', '.rm', '.rmvb', '.mkv', 
                               '.3gp', '.h.264', '.mpg', '.webm']:
                destination_folder = os.path.join(source_path, "Videos")
            elif extension in ['.py', '.java', '.cpp', '.c', '.html', '.css', '.js', '.php', '.rb', '.swift',
                                '.kt', '.scala', '.ts', '.asm', '.pl', '.go', '.lua', '.sh', '.dart', '.r',
                                '.sql', '.json', '.xml', '.sass', '.scss', '.less', '.coffee', '.ejs', '.tsx',
                                '.jsx', '.vue', '.swiftui', '.groovy', '.jsp', '.jspf', '.jspf', '.pl', '.asmx',
                                '.ashx', '.axd', '.aspx', '.ascx', '.master', '.cshtml', '.vbhtml', '.asax', '.cs',
                                '.vb', '.fsharp', '.fs', '.pas', '.dpr', '.lpr', '.sc', '.clj', '.cljs', '.rkt',
                                '.ss', '.scm', '.pl', '.r', '.rmd', '.jl', '.tex', '.cls', '.sty', '.bib', '.md',
                                '.markdown', '.rdoc', '.yaml', '.yml', '.ini', '.cfg', '.conf', '.env', '.properties',
                                '.bat', '.cmd', '.ps1', '.vbs', '.ahk', '.reg', '.csv', '.tsv', '.xls', '.xlsx',
                                '.ods', '.db', '.sql', '.sqlite', '.mdf', '.accdb', '.bak', '.json', '.xml', '.yaml',
                                '.yml', '.pcs']:
                destination_folder = os.path.join(source_path, "Programming")
            elif extension in ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', 
                               '.m4a', '.aiff', '.ape', '.alac', '.opus', '.mid', 
                               '.midi', '.ac3', '.amr', '.au', '.ra', '.rm', 
                               '.mpc', '.mp2', '.spx']:
                destination_folder = os.path.join(source_path, "Music")
            else:
                destination_folder = os.path.join(source_path, "Organized Files")
            
            # Move the file to the destination folder
            shutil.move(os.path.join(source_path, file), destination_folder)

    print("Files organized successfully.")

def main():
    organize_files()

if __name__ == "__main__":
    main()
