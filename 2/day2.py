def read_file(filename):
    with open(filename, 'r') as f: 
        txt = f.read().strip()
    return txt


def main(): 
    input = read_file('input.txt').splitlines()
    jugadas = []

    for jugada in input: 
        jugada = tuple(jugada.replace(" ", ""))
        jugadas.append(jugada)
    
    lista_puntos = []
    punto = 0

    dict_points = {'X':1, 'Y':2, 'Z':3}
    
    dict_res = { ('A', 'Y'): 6, ('B', 'Z'):6, ('C', 'X'):6,
                 ('A', 'X'): 3, ('B', 'Y'):3, ('C', 'Z'):3,
                 ('A', 'Z'): 0, ('B', 'X'): 0, ('C', 'Y'):0
    }
    lista_puntos = []
    punto = 0

    #p1
    for jug in jugadas: 
        
        #sumo por jugada
        punto += dict_points[jug[1]]

        #sumo por resultado 
        punto += dict_res[jug]
        
        lista_puntos.append(punto)
        punto = 0

    print(sum(lista_puntos)) 

    #p2
    lista_puntos2 = []
    punto2 = 0
    
    dict_perdedoras = {'A':'Z', 'B':'X', 'C':'Y'}
    dict_empates = {'A':'X', 'B':'Y', 'C':'Z'}
    dict_ganadoras = {'A':'Y', 'B':'Z', 'C':'X'}

    for jug in jugadas: 
        #sumo por resultado
        if jug[1] == 'X': 
            punto2 += 0
            punto2 += dict_points[dict_perdedoras[jug[0]]]
        elif jug[1] == 'Y': 
            punto2 += 3
            punto2 += dict_points[dict_empates[jug[0]]]
        else: 
            punto2 += 6
            punto2 += dict_points[dict_ganadoras[jug[0]]]
        
        lista_puntos2.append(punto2)
        punto2 = 0

    print(sum(lista_puntos2))
    
if __name__ == '__main__':
    main()
