# #taks4:
#This function determines if a character in string is 'T' or not. if it's 'T', it will be replaced with  'U'.
def dna_to_rna(dna): #the function name is 'dna_to_rna' and it has 1 parameter(dna)
    rna = "" # created a new empty string named- rna
    for char in dna: #for loop in dna
        if char == 'T': #check if the char(character) in 'dna'(string) equals to 'T'
            rna += 'U' #if statement below is true, rna will be encreased with character 'U'
        else:
            rna += char# if statement in 48th line is false, rna will be encreased with char
    return rna #function returns rna varibale 

print(dna_to_rna("TTTT"))# calling function and passing 'TTTT'  as a parameter