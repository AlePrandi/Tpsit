def sed(modello, sostituzione, file_input, file_output):

    with open(file_input, 'r', encoding='utf-8') as f_in:
        testo = f_in.read()

    testo_modificato = testo.replace(modello, sostituzione)

    with open(file_output, 'w', encoding='utf-8') as f_out:
        f_out.write(testo_modificato)

def main():
    sed('stai', 'gatto', 'input.txt', 'output.txt')

if __name__ == "__main__":
    main()
