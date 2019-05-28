import random
import operator

#classe para passar os valores para os processos
class Processo(object):
        def __init__(self, nome,burst,tcheg):
            self.nome = nome
            self.burst = burst
            self.tcheg = tcheg
        
        def setNome(nome):
            self.nome = nome

        def setBurst(burst):
            self.burst = burst
        
        def setTcheg(tcheg):
            self.tcheg = tcheg
#função para ordenar pelo tempo de chegada
def ftchegada(lista, n):
    print("\nORDENADOS PELO TEMPO DE CHEGADA")
    lista.sort(key=operator.attrgetter("tcheg"),reverse=False)
    print ("proc","burst","tcheg")
    for i in lista:
        print(i.nome," ", i.burst," ",i.tcheg)
    #codigo para o waiting time
    print("\nWaiting time")
    w=0
    i=0
    q=0
    r=0
    c=0
    a=0
    print(lista[i].nome, " ", w)
    while(n>i):
        q+=w
        w+=lista[i].burst
        i+=1   
        if(n>i):
                print(lista[i].nome, " ", w)
        else:
            break
    print("\nWaiting time medio")
    print(int(q/n))
    #codigo do turnaround
    print("\nTurnaround")    
    while(n>c):
        r+=lista[c].burst
        a+=r
        if(n>c):
                print(lista[c].nome, " ", r)
                c+=1   
        else:
                break  
    print("\nTurnaround medio")
    a=a/n
    print(("%.2f" %a))

    

#função para ordenar pelo burst
def fburst(lista, n):
    print(" ")
    print("OBJETOS ORDENADOS PELO BURST")
    lista.sort(key=operator.attrgetter("burst"),reverse=False)
    print ("proc","burst")
    for i in lista:
        print(i.nome," ", i.burst)
    #codigo para o waiting time
    print("Waiting time")
    w=0
    i=0
    q=0
    r=0
    c=0
    a=0
    print(lista[i].nome, " ", w)
    while(n>i):
        q+=w
        w+=lista[i].burst
        i+=1
        if(n>i):
            print(lista[i].nome, " ", w)
        else:
            break
    print("Waiting time medio")
    print(int(q/n))
    #codigo do turnaround
    print("\nTurnaround")    
    while(n>c):  
        r+=lista[c].burst
        a+=r
        if(n>c):
                print(lista[c].nome, " ", r)
                c+=1   
        else:
                break  
    print("\nTurnaround medio")
    a=a/n
    print(("%.2f" %a))

#função para ordenar por prioridade    
def fprioridade(lista, n):
    print(" ")
    print("ORDENADOS POR PRIORIDADE")
    lista.sort(key=operator.attrgetter("tcheg"),reverse=False)
    print ("proc","burst","tcheg")
    atual = 0
    prox = 1
    count = lista[atual].tcheg
    lista2 = []
    burst = []
    process = []
    tcheg = []
    lista2.append(lista[atual])
    print(lista2[atual].nome," ",lista2[atual].burst," ",count)
    while(atual < n):
        if (prox < n and count==lista[prox].tcheg):
            lista2.append(lista[prox])
            lista2.sort(key=operator.attrgetter("burst"),reverse=False)
            process.append(lista2[atual].nome)
            burst.append(lista2[atual].burst)
            tcheg.append(lista2[atual].tcheg)
            print(lista2[atual].nome," ",lista2[atual].burst," ",count)
            prox+=1          
        elif(lista2[atual].burst==0):
            atual+=1
            prox+=1
            if (atual<len(lista2)):
                process.append(lista2[atual].nome)
                burst.append(lista2[atual].burst)
                tcheg.append(lista2[atual].tcheg)
                print(lista2[atual].nome," ",lista2[atual].burst," ",count)
            else:
                break
        else:
            lista2[atual].burst-=1
            count+=1
    #codigo para o waiting time
    print("Waiting time")
    w=0
    i=0
    q=0
    n=len(burst)
    print(lista2[i].nome, " ", w)
    while(n>i):
        q+=w
        if(n>i):
            w+=burst[i]
            print(process[i], " ", w)
            i+=1
        else:
            break
    print("Waiting time medio")
    print(int(q/n))
    #codigo do turnaround
    r=0
    c=0
    a=0
    n=len(burst)
    print("\nTurnaround")    
    while(n>c):
        r+=burst[c]
        a+=r
        if(n>c):
                print(process[c], " ", r)
                c+=1   
        else:
                break  
    print("\nTurnaround medio")
    a=a/n
    print(("%.2f" %a))
    
#funcao para ordenar pelo quantum
def fquantum(comando, lista, n):
    if (comando == "M" or comando =="m"):
        q = int(input("Quantidade do QUANTUM: "))
    else:
        q = random.randrange(1, 101)
    print(" ")
    print("ORDENADOS PELO QUANTUM")
    print("Ovalor do quanto é: ", q)
    lista.sort(key=operator.attrgetter("tcheg"),reverse=False)
    print ("proc","burst","tcheg")
    atual = 0
    prox = 1
    count = lista[atual].tcheg
    lista2 = []
    burst = []
    tcheg = []
    process = []
    aux = 0
    lista2.append(lista[atual])
    while(True):
    #verifica o tempo de chegada dos processos para poder executa-lo
        if (prox < n and count>=lista[prox].tcheg):
            lista2.append(lista[prox])
            process.append(lista2[atual].nome)
            burst.append(lista2[atual].burst)
            tcheg.append(lista2[atual].tcheg)
            prox+=1
        elif(atual<len(lista2) and lista2[atual].burst<=0):
            del lista2[atual]
            atual+=1
            aux+=1
            if (aux==n):
                break
            else:
                atual=0 
        else:
            process.append(lista2[atual].nome)
            burst.append(lista2[atual].burst)
            tcheg.append(lista2[atual].tcheg)
            print(lista2[atual].nome," ",lista2[atual].burst," ",count)
            if (lista2[atual].burst <= q):
                count+=lista2[atual].burst
                lista2[atual].burst -= lista2[atual].burst
            else:
                count+=q
                lista2[atual].burst-=q
            atual+=1
            if (atual>=len(lista2)):
                atual=0
    #codigo para o waiting time          
    print("Waiting time")
    w=0
    i=0
    q=0
    a=0
    print(len(burst))
    print(lista[i].nome, " ", w, "")
    while(n>i):
        q+=w
        w+=burst[i]
        i+=1
        a+=1
        if(n>i):
            w-=tcheg[i]
            print(a, " ", w)
        else:
            break
    print("\nWaiting time medio")
    print(int(q/n))
    #codigo do turnaround
    r=0
    c=0
    a=0
    i=0
    print("\nTurnaround")    
    while(n>c):
        r+=burst[c]
        a+=r
        i+=1
        if(n>c):
                print(i, " ", r)
                c+=1   
        else:
                break  
    print("\nTurnaround medio")
    a=a/n
    print(("%.2f" %a))


#funcao multinivel de niveis
def fmult(lista, n):
    lista.sort(key=operator.attrgetter("tcheg"),reverse=False)
    print("\nORDENADOS POR MULTINÍVEL :")
    aux=n
    lista1=[]
    lista2 = []
    count = 0
    for i in lista:
        lista1.append(lista[count])
        if(aux==n):
                    fquantum(comando,lista1,len(lista1))
                    aux+=1
                    count+=1
                    lista2.append(lista[count])
        else:
                ftchegada(lista2, len(lista2))
        
            
#menu dos processos
while True:
    
    print("\nEscolha o Escalonamento")
    opcao = int(input("1 - FCFS\n2 - SJF\n3 - SRTF\n4 - ROUND ROBIN\n5 - MULTINÍVEL\n6 - SAIR\n"))
    if (opcao == 6):
        print("Escalonamento encerrado.")
        break

    n = int(input("Qual a quantidede de processos?"))
    lista = []
    #menu para escolher manual ou nao
    while (True):
        comando = input("Burst manual ou aleatório(M/A)?")
        if comando == "A" or comando == "M" :
            break
        elif comando == "a" or comando == "m" :
            break
        else:
            print("por vafor digite um comando valido\n")
            
    if comando == "A" or comando == "a":
        for i in range(n):
            proc = Processo(i,random.randint(1, 100),random.randint(0, 15))
            lista.append(proc)
    else:
        for i in range(n):
            b = int(input("P" + str(i) +" Burst:"))
            t = int(input("P" + str(i) +" Tempo de Chegada:"))
            proc = Processo(i,b,t)
            lista.append(proc)

    print ("\nTODOS OS PROCESSOS\n")
    print ("proc","burst","tcheg")
    for i in lista:
        print(i.nome," ", i.burst," ",i.tcheg)
        
    if (opcao == 1):
        ftchegada(lista, n)
    elif (opcao == 2):
        fburst(lista, n)
    elif (opcao == 3):
        fprioridade(lista, n)
    elif (opcao == 4):
        fquantum(comando, lista, n)
    elif (opcao == 5):
        fmult(lista, n)
    else:
        print("Opção invalida, tente novamente.")
