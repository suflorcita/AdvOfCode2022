def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read().strip()
    return txt

def parse_input(input): 
    clean_input = []
    for line in input: 
        elf1, elf2 = line.split(',')
        elf1 = tuple(map(int, elf1.split('-')))
        elf2 = tuple(map(int, elf2.split('-')))
        clean_input.append([elf1, elf2])
        elf1, elf2 = (), ()
    return clean_input

def pair_into_pair(pair1, pair2): 
    # para un lado (pair1 en pair2)
    if pair1[0] >= pair2[0] and pair1[1] <= pair2[1]:  
        return True  
    # para el otro lado (pair2 en pair1)
    elif pair2[0] >= pair1[0] and pair2[1] <= pair1[1]:  
        return True 
    return False  

def overlap(pair1, pair2): 
    set1 = set(range(pair1[0], pair1[1] + 1))
    set2 = set(range(pair2[0], pair2[1] + 1))
    # si la interseccion entre los dos conjuntos tiene más de un elemento es true
    return bool(set1 & set2)

def main(): 
    input = parse_input(read_file('input.txt').splitlines())
    
    sum1 = 0
    sum2 = 0 

    for line in input: 
        pair_elf1, pair_elf2= line
        sum1 += pair_into_pair(pair_elf1, pair_elf2)
        sum2 += overlap(pair_elf1, pair_elf2)

    print(sum1, sum2)
if __name__ == '__main__':  
    main()