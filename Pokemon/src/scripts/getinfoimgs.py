from csv import reader

def getinfo(path):
    arquivo = []
    with open(path) as map:
        layout = reader(map, delimiter=',')
        for row in layout:
            arquivo.append(list(row))
        return arquivo