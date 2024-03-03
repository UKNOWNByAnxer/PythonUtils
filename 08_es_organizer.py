import os
import shutil

def organizar_archivos():
    # Obtener la ruta actual del directorio de trabajo
    ruta_origen = os.getcwd()

    # Crear las carpetas de destino si no existen
    carpetas = ["Imagenes", "Documentos", "Videos", "Musica", "Programacion", "Archivos Organizados"]
    for carpeta in carpetas:
        ruta_carpeta = os.path.join(ruta_origen, carpeta)
        if not os.path.exists(ruta_carpeta):
            os.makedirs(ruta_carpeta)
    
    # Obtener una lista de todos los archivos en la carpeta de origen
    archivos = os.listdir(ruta_origen)
    
    # Organizar los archivos en la carpeta de destino basándose en sus extensiones
    for archivo in archivos:
        # Ignorar carpetas y archivos ocultos
        if not archivo.startswith('.'):
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(archivo)
            extension = extension.lower()  # Convertir a minúsculas
            
            # Definir la carpeta de destino según la extensión
            if extension in ['.jpg', '.jpeg', '.png', '.gif', 
                             '.bmp', '.tiff', '.svg', '.webp', 
                             '.ico', '.psd','.ai', '.eps', 
                             '.raw', '.cr2', '.nef', '.orf',
                               '.sr2', '.heic', '.tif', '.jpe']:
                carpeta_destino = os.path.join(ruta_origen, "Imagenes")
            elif extension in ['.doc', '.docx', '.pdf', '.txt', 
                               'rtf', '.odt', 'docm', 'dotx',
                                 'dotm','xlsx','xlsm','xltx',
                                 'xltm','xlsb','xlam','pptx',
                                 'pptm','potx','potm','ppam',
                                 'ppsx','ppsm','sldx', 'sldm',
                                 'onetoc', 'onepkg']:
                carpeta_destino = os.path.join(ruta_origen, "Documentos")
            elif extension in ['.mp4', '.mov', '.avi', '.mkv', 
                               'avi', 'mp4', 'wmv','wma', 'mov',
                                 'flv', 'rm', 'rmvb', 'mkv', 
                                 '3gp', 'h.264', 'mpg', 'webm']:
                carpeta_destino = os.path.join(ruta_origen, "Videos")
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
                                '.yml', 'pcs']:
                carpeta_destino = os.path.join(ruta_origen, "Programacion")
            elif extension in ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma', 
                               '.m4a', '.aiff', '.ape', '.alac','.opus', '.mid', 
                               '.midi', '.ac3', '.amr', '.au', '.ra', '.rm', 
                               '.mpc', '.mp2', '.spx']:
                carpeta_destino = os.path.join(ruta_origen, "Musica")
            else:
                carpeta_destino = os.path.join(ruta_origen, "Archivos Organizados")
            
            # Mover el archivo a la carpeta de destino
            shutil.move(os.path.join(ruta_origen, archivo), carpeta_destino)

    print("Archivos organizados correctamente.")

def main():
    organizar_archivos()

if __name__ == "__main__":
    main()
