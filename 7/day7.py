from filesystem import FileSystem, Dir

def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read()
    return txt

def main(): 
    input = read_file('input.txt').splitlines()
    fs = FileSystem()

    for line in input: 
        line = line.split()
        if line[0] == '$': 
            if line[1] == 'cd' and line[2] != '..':
                fs.change_current_dir(line[2])
            elif line[1] == 'cd' and line[2] == '..':
                fs.level_down()
                
        else:
            if line[0] == 'dir':
                fs.add_dir_current_dir(line[1])
            else:
                fs.add_file_current_dir(int(line[0]), line[1])
            
    #p1
    print(fs.at_most_n(100000))
    
    #p2
    print(fs.free_n_space(30000000))
    
    #fs.print_path()

if __name__ == '__main__':  
    main()