def niente_e(elenco):
    '''  
    no_e = False
    for c in parola:
        no_e = True if c != "e" else False
        
    if no_e: 
        return True
    else:
        return False 
    '''
    n_par = 0
    for parola in elenco:
        e_pres = False
        for c in parola:
            if c == "e" and e_pres == False:
                n_par += 1
                print(parola)
                e_pres = True
    num_par = (n_par/len(elenco))*100
    return num_par
                
    
def main():
    elenco = ["ciao", "gatto", "cane", "moto", "pesce", "esca"]
    print(niente_e(elenco))
    
if __name__ == "__main__":
    main()