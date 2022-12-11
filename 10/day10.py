def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read().strip()
    return txt

def main(): 
    instructions = read_file('input.txt').splitlines()
   
    n = 0 #number of instruction 
    a = 0 # add to x

    flag = 0
    X = 1
    
    CRT_screen = ''
    sprite = [0, 1, 2]

    sum_signal_strength = 0

    for i in range(240): #iterate over every cycle
        j = i
        i = i % 40

        if i == 0: 
            CRT_line = ''
        
        if i == 19: #sum signal strengths # p1
            print(j, X)
            sum_signal_strength +=  (j+1) *  X 

        if i in sprite: 
            CRT_line += '#'
        else: 
            CRT_line += '.'

        if i == 39: 
            CRT_line = CRT_line + '\n'
            CRT_screen += CRT_line  
               
    
        if flag == 1: # addx -> second cycle. 
            flag = 0
            X += a
            sprite = [X - 1, X, X + 1]
            n += 1
            continue

         # read instruction

        instruction = instructions[n].split()
        if instruction[0] == 'noop': 
            n += 1 
        else:
            a = int(instruction[1]) 
            flag = 1 # to skip one cycle 

    
    with open("output.txt", "w") as f:
        f.write(CRT_screen)
    
    print(CRT_screen)
    print(sum_signal_strength)

if __name__ == '__main__':  
    main()
