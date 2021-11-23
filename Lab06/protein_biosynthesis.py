def dna_to_rna(dna) :
    len_dna = len(dna)
    rna_out = ''
    for i in range(len_dna) :
        if dna[i] == 'A' :
            rna_out += 'U'
        if dna[i] == 'T' :
            rna_out += 'A'
        if dna[i] == 'C' :
            rna_out += 'G'            
        if dna[i] == 'G' :
            rna_out += 'C'
    return rna_out

def nub_amino(rna_out) :
    len_rna = len(rna_out)
    start_codon = 'AUG'
    stop_codon = ['UAA','UGA','UAG']
    i,nub = 0,0
    check = 0
    while i != len_rna :
        if rna_out[i:i+3] == start_codon :
            nub += 1
            check = 1
            i += 3
        if check == 1 :
            if rna_out[i:i+3] not in stop_codon :
                nub += 1
                i += 3
            else :
                break
        if check == 0 :
            i += 1
    return nub


    
dna = input('DNA: ')
# dna = 'CGTCGTCCTACAGCATGAGCATCATCAGCCCATTGTCATGC'
rna = dna_to_rna(dna)
count = nub_amino(rna)
# print(rna)
print(f'{count} Amino acid(s)')
        