import networkx as nx
import matplotlib.pyplot as pt

grafo = nx.DiGraph()
lectura = open("princesa/entrada.in","r")
escritura = open("princesa/salida.out", "w")
aristas= []
def crear():
    txt = lectura.readline().split(" ")
    if(int(txt[0])>=2 and int(txt[0])<100000 and int(txt[1])>=0 and int(txt[1])<=600000 and int(txt[2])>=0 and int(txt[2])<=100):
        c =  int(txt[0])
        s = int(txt[1])
        d = int(txt[2])
        txt= lectura.readline().split(" ")
        if int(txt[0])<=c and int(txt[1])>=1 :
            cf = int(txt[0])
            cm = int(txt[1])
        txt= lectura.readline().split(" ")
        if(len(txt)==d):
         dragones = txt  
          
        for i in range(0,c) :
            aver= str(i+1)
            grafo.add_node(aver)
           

        
        for x in range(0,s):
                txt= lectura.readline().split(" ")
                xd= (txt[0],txt[1],int(txt[2]))
                aristas.append(xd)
        grafo.add_weighted_edges_from(aristas)
    print("dijkstra")

    print(nx.dijkstra_path(grafo, '1', '9'))

    nx.draw(grafo, pos=nx.circular_layout(grafo), node_color='greenyellow', edge_color='black', with_labels=True)   

    pt.show()

crear()
