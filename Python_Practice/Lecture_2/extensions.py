'''
This program is supposed to recieve a file name and,
depending on the extension it has, output the media
type of the file (web's interpretation of the file)
'''
def main():
    file=input("File name: ")
    
    def get_Extension(file):
        file_Parts=file.split('.')
        match file.split('.'):
            case f , extension:
                return extension.lower() if extension else exit(2)
            case _:
                print('No added extension')
                exit(1)
        
        
    def get_MIME(file):
        match get_Extension(file):
            case 'txt':
                return 'text/plain'
            case 'pdf' | 'zip' as extension:
                return f'aplication/{extension}'
            case 'gif' | 'png' | 'jpeg' as extension:
                return f'image/{extension}'
            case 'jpg':
                return 'image/jpeg'
            case _:
                return 'application/octet-stream'
 
    
    print("Media type:", get_MIME(file))
    

main()