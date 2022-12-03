import string

def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read().strip()
    return txt

def letter_in_string(string1, string2):
    for letter in string1: 
        if letter in string2: 
            return letter
    return None

def letter_in_three_strings(string1, string2, string3): 
    for letter in string1: 
        if letter in string2 and letter in string3: 
            return letter
    return None

def priority(character): 
    #priority
    lowercase = {v:k for k,v in enumerate(string.ascii_lowercase, start=1)}
    uppercase = {v:k for k,v in enumerate(string.ascii_uppercase, start=27)}

    if character.islower():
       return lowercase[character]
    else: 
       return uppercase[character]  

def main(): 
    input = read_file('input.txt').splitlines()
    sum_1 = 0
    sum_2 = 0

    #p1
    for line in input: 
        str1 = line[0:len(line)//2]
        str2 = line[len(line)//2:]

        character = letter_in_string(str1, str2)

        sum_1 += priority(character)
    print(sum_1 )
       
    #p2

    # divide into groups
    groups = [[input[i], input[i+1], input[i+2]] for i in range(0, len(input), 3)]
    
    for group in groups: 
        str1, str2, str3 = group[0], group[1], group[2]
        character = letter_in_three_strings(str1, str2, str3)
        
        sum_2 += priority(character)
    print(sum_2) 

if __name__ == '__main__':
    main()
