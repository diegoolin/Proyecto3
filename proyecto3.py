import pygraphviz as pgv
import sys
def agregarNodo(nombreA,nombreB):
	gr.add_edge((nombreA,nombreB))
	
def agregarNodoAzul(nombreA,nombreB):
	gr.add_edge(nombreA,nombreB,color='blue')

def contarcodones(codonestotal,p):
    contador=0
    for i in codonestotal:
        if i ==p:
            contador+=1
    return contador
codigog={"GCU":"A","GCC":"A","GCA":"A","GCG":"A","CGU":"R","CGC":"R","CGA":"R","CGG":"R","AGA":"R","AGG":"R",
         "AAU":"N","AAC":"N","GAU":"D","GAC":"D","UGU":"C","UGC":"C","CAA":"Q","CAG":"Q",
         "GAA":"E","GAG":"E","GGU":"G","GGC":"G","GGA":"G","GGG":"G","CAU":"H","CAC":"H",
         "AUU":"I","AUC":"I","AUA":"I","UUA":"L","UUG":"L","CUU":"L","CUC":"L","CUA":"L","CUG":"L",
         "AAA":"K","AAG":"K","AUG":"M","UUU":"F","UUC":"F","CCU":"P","CCC":"P","CCA":"P","CCG":"P",
         "UCU":"S","UCC":"S","UCA":"S","UCG":"S","AGU":"S","AGC":"S","ACU":"T","ACC":"T","ACA":"T","ACG":"T",
         "UGG":"W","UAU":"Y","UAC":"Y","GUU":"V","GUC":"V","GUA":"V","GUG":"V","UAG":"STOP","UGA":"STOP","UAA":"STOP"}   
genetica=open(input("Ingrese nombre de secuencia:"))
geneticalimpia=[]
nombre=genetica.readlines(1)
linea=genetica.read()
i=0
while i<len(linea):
    if linea[i]=="I":
        while linea[i]!="F":
            i+=1
    else:
        geneticalimpia+=linea[i]
    i+=1 

for j in range(len(geneticalimpia)):
    if geneticalimpia[j]=="T":
        geneticalimpia[j]="U"
geneticalimpia="".join(geneticalimpia)
print("Sin IF:",geneticalimpia)

start=["AUG"]
stop1=["UAG","UAA","UGA"]
largogeneticalimpia=len(geneticalimpia)
codones=[]
i=0
while i<largogeneticalimpia-2:
    if start[0]==geneticalimpia[i:i+3]:
        while (i+3)<=len(geneticalimpia):
            if stop1[0]==geneticalimpia[i:i+3] or stop1[1]==geneticalimpia[i:i+3] or stop1[2]==geneticalimpia[i:i+3]:
                i+=largogeneticalimpia
            else:

                codones.append(geneticalimpia[i:i+3])
                i+=3
    i+=1
print("Tripletes:",codones)
cambio=[]
largo=len(codones)
i=0
while i<largo:
    if codones[i] in codigog:
        encontrar=codigog.get(codones[i])
        i+=1
        cambio.append(encontrar)
print("".join(cambio))
with open("secuencia.fasta","w") as f:
    f.write(nombre[0])
    f.write("".join(cambio))

A=0
C=0
U=0
G=0
largo=len(geneticalimpia)
for i in geneticalimpia:
            if i=="A":
                A+=1

            if i=="C":
                C+=1

            if i=="U":
                U+=1

            if i=="G":
                G+=1

porcentajeA=(A*100)/largo
porcentajeC=(C*100)/largo
porcentajeU=(U*100)/largo
porcentajeG=(G*100)/largo
print("El n??mero de nucleotidos A es de ",A-2," y el porcentaje es:",porcentajeA)
print("El n??mero de nucleotidos C es de ",C-2," y el porcentaje es:",porcentajeC)
print("El n??mero de nucleotidos U es de ",U-2," y el porcentaje es:",porcentajeU)
print("El n??mero de nucleotidos G es de ",G-2," y el porcentaje es:",porcentajeG)

for i in codones:
    contadorcod=contarcodones(codones,i)
    print("El codon",i,"se encuentra",contadorcod,"en la secuencia y su porcentaje es:",(contadorcod*100)/len(codones),"%")

polarespositivos=0
polaresnegativos=0
polaressincarga=0
apolares=0
sincarga=["S","T","C","Y","N","Q"]
negativos=["D","E"]
positivos=["H","R","K"]
apolar=["G","A","V","L","I","F","W","M","P"]

for i in cambio:
    if i in positivos:
        polarespositivos+=1

    elif i in negativos:
        polaresnegativos+=1
    elif i in apolar:
        apolares+=1
    elif sincarga:
        polaressincarga+=1
print("Amino??cidos polares positivos:",polarespositivos)
print("Amino??cidos polares negativos:",polaresnegativos)
print("Amino??cidos polares sin carga:",polaressincarga)
print("Amino??cidos apolares:",apolares)


gr = pgv.AGraph(rotate='360',bgcolor='white',directed=True)
gr.graph_attr['label']='Codon y Aminoacido tres letras'
# se agregan nodos.
i = 1
while (i < len(codones)):
	temp = codones[i-1]
	agregarNodoAzul(temp,codigog[temp])
	#agregarNodoAzul(dic[temp],dic2[dic[temp]])
	agregarNodo(temp,codones[i])
	i = i + 1
# Generaci??n de grafo en formato PNG.
gr.layout(prog='dot')
gr.draw('codonyAA.png')