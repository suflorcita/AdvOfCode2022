import re

def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read().strip()
    return txt

def n_distinct_char_in_str(string, N):  
    aux = []
    first=0; end=N

    while True: 
        aux = string[first:end]
        if len(set(aux)) == N: break
        first += 1
        end +=1
    
    return end 
        
def main(): 
    input = read_file('input.txt')


    print(n_distinct_char_in_str(input, 4))
    print(n_distinct_char_in_str(input, 14))
    
    
if __name__ == '__main__':  
    main()