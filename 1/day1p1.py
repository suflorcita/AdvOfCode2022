def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read()
    return txt

def sum_calories(lst): 
    total_calories = [sum(l) for l in lst]
    return total_calories

def main(): 
    input = read_file('input.txt').strip().replace("\n", 't').split('tt')
    input = [element.split('t') for element in input]
    input = [list(map(int, elf)) for elf in input]
    
    most = max(sum_calories(input))
    print(most)
    
if __name__ == '__main__':
    main()
