import re

def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read()
    return txt

def parse_position(string, positions): 
    for j, i in enumerate(range(1, len(string),4), start=1): 
        if j not in positions.keys(): positions[j] = []
        if string[i] != ' ': positions[j].insert(0, string[i])

def parse_movement(string): 
    string = string.split()
    return (int(string[1]), int(string[3]),int(string[5]))

def change_positions(movement, positions, mode=0): 
    n_movement,  from_pos , to_pos,= movement[0], movement[1], movement[2] 
    if mode == 0: 
        for i in range(n_movement):
            positions[to_pos].append(positions[from_pos][-1])
            positions[from_pos].pop()
    else:
        #try:  
        aux = positions[from_pos][-n_movement:]
        for element in aux: 
            positions[to_pos].append(element)
            positions[from_pos].pop()
        # except IndexError: 
        #     print('error')
        
def main(): 
    input = read_file('input.txt').splitlines()
    positions = {}
    movements = []
    pattern2 = r'move \d+ from \d to \d'

    # parse 
    for line in input:
        
        if '[' in line : parse_position(line, positions)
          
        value2 = re.findall(pattern2, line)
        if value2: movements.append(parse_movement(line))

    # change mode     
    for movement in movements: 
        change_positions(movement, positions, mode=1)
    
    final_str = ''
    
    for n  in positions.keys(): 
        if positions[n]: final_str += positions[n][-1]
    
    print(f'{final_str}')
if __name__ == '__main__':  
    main()