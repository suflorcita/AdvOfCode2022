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
    
    
    calories = sum_calories(input)
    calories.sort(reverse=True)  
    sum_top_three = calories[0] + calories[1] + calories[2]
    print(sum_top_three)
    
if __name__ == '__main__':
    main()
