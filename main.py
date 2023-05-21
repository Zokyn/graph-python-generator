import random
from graph_theory import Graph 

MAX_NODES = int(6)

def generateGraphs(graph_list):
    question = input("Quantos grafos serão gerados: ")
    graph_count = int(question)

    question = input("Serão permitidos multigrafos? [y (Sim)]:")
    multigraph = True if question == 'y' else False 

    graph_list = []
    for _ in range(graph_count):

        V = []; E = []
        n = 0
        
        for n in range(1, random.randint(1, MAX_NODES), 1):
            V.append(n)

        if(n >= 2):
            m = int((n * (n-1))/2)
            for _ in range(1, random.randint(1, m), 1):
                v = random.randint(1, n)
                w = random.randint(1, n)
                if(multigraph == False): 
                    while(w == v or [v, w] in E or [w, v] in E):
                        w = random.randint(1, n)
                E.append([v, w])

        print("\n\n")
        new_graph = Graph(V, E); new_graph.show() 
        graph_list.append(new_graph)
        print("\n\n")
def main():

    menu_flag = True
    graph_list = []

    while(menu_flag):

        print("-"*50)
        print("Escolha uma opção: ")
        print("1. Gere uma lista inicial de grafos.")
        print("2. Mostre a lista completa de grafos.")
        print("0. Saia.")
        
        option = int(input(">>> OPÇÃO: "))
        print("\n\n")
        
        if option == 1: 
            generateGraphs(graph_list)
        
        elif option == 2:
            for i in range(len(graph_list)):
                print(graph_list[i])
                # graph.show()
        
        elif option == 0:
            menu_flag = False

if __name__ == '__main__':
    main()