import networkx as nx
import matplotlib.pyplot as pt

class Princesa:
    grafo = nx.DiGraph()
    lectura =(("9 10 2"), ("9 1"),( "8 5"),("1 2 3"),("1 3 2"),("2 3 4"),("2 6 1"),("3 8 1"),("8 6 5"),("4 5 2"),("3 4 2"),("3 6 2"),("6 9 3"))


    escritura = ""
    aristas= []
    def crear(self):
        txt = self.lectura[0].split(" ")
        if(int(txt[0])>=2 and int(txt[0])<100000 and int(txt[1])>=0 and int(txt[1])<=600000 and int(txt[2])>=0 and int(txt[2])<=100):
            c =  int(txt[0])
            s = int(txt[1])
            d = int(txt[2])
            txt= self.lectura[1].split(" ")
            if int(txt[0])<=c and int(txt[1])>=1 :
                cf = int(txt[0])
                cm = int(txt[1])
            txt= self.lectura[2].split(" ")
            if(len(txt)==d):
                dragones = txt

            for i in range(0,c) :
                aver= str(i+1)
                self.grafo.add_node(aver)



            for x in range(0,s):
                    txt= self.lectura[3+x].split(" ")
                    xd= (txt[0],txt[1],int(txt[2]))
                    self.aristas.append(xd)
            self.grafo.add_weighted_edges_from(self.aristas)
            
        try:
            escritura=nx.dijkstra_path(self.grafo, '1', '9')
            interceptado = 0
            for sd in range(0, len(escritura)):
               for dn in range(0, len(dragones)):
                  if(escritura[sd]==dragones[dn]):
                      print("Has sido Interceptado por los dragones MUAJAJAA")
                      interceptado = 1
            if(interceptado==0):
                print(chr(27)+"[1;32m"+"¡¡¡Lograste salvar a la Princesa Felicitaciones!!!")
            
                  
            print("\x1b[0;00m"+"El camino mas corto por Dijkstra seria: " , escritura)
            print("los dragones estan en: %s" % (dragones))
        except nx.exception.NetworkXNoPath as err:
          print("No hay camino")

        
            
        
        nx.draw(self.grafo, pos=nx.circular_layout(self.grafo),node_color='greenyellow', edge_color='black', with_labels=True)

        pt.show()

pr = Princesa()
pr.crear()
