class FileSystem: 
    def __init__(self):
        self.current_level = 0
        self.current_dir = Dir('/') 
        self.path = {0:[self.current_dir]} #path dictionary. level:[list of dirs(object Dir)]
        pass
    
    def change_current_dir(self, name_dir): 
        '''Change current dir and append the new dir to the path'''
        for dir in self.current_dir.dirs:
            if dir.name == name_dir: 
                self.level_up()
                self.path[self.current_level].append(dir)
                self.current_dir = dir
                
    
    def add_dir_current_dir(self, name_dir):
        '''Add a directory to the current directory'''
        
        if not (self.current_level + 1) in self.path.keys(): #if next level doesnt exist 
            self.path[self.current_level + 1] = []

        for dir in self.current_dir.dirs: # search in list of current dir's dirs
            if dir.name == name_dir: 
                return None 

        new_dir = Dir(name_dir, self.current_dir)
        self.current_dir.add_dir(new_dir)
        

    def add_file_current_dir(self, size_file, name_file):
        '''Add a file to the current directory'''
        self.current_dir.add_file(size_file, name_file)
               
        dir = self.current_dir

        while dir != None: 
            dir.size += size_file     
            dir = dir.parent
        
       
    def level_up(self):
        '''Change a level up the current level'''
        self.current_level += 1

        if not self.current_level in self.path.keys():
            self.path[self.current_level] = []
        
    def level_down(self):
        '''Change a level down the current level'''
        self.current_level -= 1
        if self.current_dir.parent != None:
            self.current_dir = self.current_dir.parent
        
    
    def print_path(self): 
        '''Print path and the sum of the element in the path'''
        for level in self.path: 
            for dir in self.path[level]: 
                print(f'In level {level} dir "{dir.name}"')
                try:
                    print(f'The dir {dir.name} with parent {dir.parent.name}')
                except AttributeError:
                    print(f'The dir is {dir.name}')
                print(f'With a size of {dir.size}')    

    def at_most_n(self, n): 
        sum = 0 
        for level in self.path: 
            for dir in self.path[level]:
                if dir.size <= n: 
                    sum += dir.size
                    continue
        return sum 

    def free_n_space(self, n): 
        used_space = self.path[0][0].size #size of dir '/'
        unused_space = 70000000 - used_space
        size_files = n - unused_space 
        files = []

        #print(f'Se usó un total de {used_space} y necesito liberar archivos de al menos{size_files}')
        
        for level in self.path: 
            for dir in self.path[level]:
                if dir.size >= size_files:
                    files.append(dir.size)
        
        return min(files)
         
class Dir: 
    '''The dir class represent each directory of the system '''
    def __init__(self, name, parent=None): 
        self.name = name
        self.files = {} # dictionary of files. name_file : size
        self.dirs = [] # list of dirs 
        self.parent = parent # Directory parent
        self.size = 0
       
    def add_file(self, size_file, name): 
        '''Add a file to the directory'''
        self.files[name] = size_file
        

    def add_dir(self, dir): 
        '''Add a directory to the directory
        Directory is class Dir'''        
        self.dirs.append(dir)
