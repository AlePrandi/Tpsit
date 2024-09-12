import os

def trova_file_con_estensione(directory, estensione):
   
    file_paths = []
    for radice, _, file_names in os.walk(directory):
        for file_name in file_names:
            if file_name.lower().endswith(estensione):
                file_paths.append(os.path.join(radice, file_name))
    return file_paths

def confronta_file(file1, file2):
    
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        while True:
            chunk1 = f1.read(4096)
            chunk2 = f2.read(4096)

            if chunk1 != chunk2:
                return False

            if not chunk1: 
                return True

def trova_duplicati(directory, estensione):
    
    file_paths = trova_file_con_estensione(directory, estensione)
    duplicati = []

    while file_paths:
        file1 = file_paths.pop(0)
        for file2 in file_paths[:]:
            if confronta_file(file1, file2):
                duplicati.append((file1, file2))
                file_paths.remove(file2)

    return duplicati

def main():
    duplicati = trova_duplicati('../', '.txt')
    for dup in duplicati:
        print(f"File duplicati: {dup[0]} e {dup[1]}")

if __name__ == "__main__":
    main()
