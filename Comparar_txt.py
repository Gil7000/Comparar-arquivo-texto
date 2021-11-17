# Ler e comparar dois arquivos TXT
# Procura pelo arquivo newfile.txt e oldfile.txt no subdiretório Files
# Cria um novo arquivo, resultfile.txt
# from IPython.display import display
import os
import time

def file_exist(arq):
    if not os.path.isfile(arq):
        print("Arquivo "+arq+" não localizado")
        print("Finalizando o programa.")
        exit()

def open_file(arq):
    print('Abrindo arquivo ['+arq+'].......................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    filearq = open(arq, 'r', encoding='ANSI')  # abre o arquivo no modo de leitura
    conteudo_arq = filearq.readlines()

    # insere o conteúdo do arquivo oldfile.txt na lista oldfile
    listarq = []
    for i in range(len(conteudo_arq)):
        listarq.append(conteudo_arq[i])
    filearq.close()  # fecha o arquivo

    print('Quantidade de registros no arquivo '+arq+' .....: ' + str(len(listarq)))
    return listarq

os.chdir('.\Files')  # altera para esse diretório - Windows
# os.chdir('Files/')    # altera para esse diretório - Mac Os
print('Diretório de trabalho...............................: ' + os.getcwd())
print('Inicio..............................................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


# verificar se os arquivos existem no diretório

file_exist('oldfile.txt')
file_exist('newfile.txt')

while True:
    cab = input("O arquivo possuí cabeçalho? (S)im (N)ão ")
    if cab.upper() in ("S", "N"):
        break

#Salva o conteúdo dos arquivos numa LIST
oldfile = open_file('oldfile.txt')
newfile = open_file('newfile.txt')

print('Separando as linhas diferentes entre os arquivos....: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# insere na lista result apenas as linhas que existem em newfile e não existem em oldfile
result = sorted(list(set(newfile) - set(oldfile)))  #o arquivo resultado esta sendo ordenado, caso não queira, substitua o comando para [result = list(set(newfile) - set(oldfile))]
cab == ""
if cab.upper() == "S":
    result.insert(0, newfile[0])  # insere o cabeçalho na 1a linha

print('Quantidade de registros diferentes..................: ' + str(len(result)))
resultFile = open('resultfile.txt', 'w')

for i in range(len(result)):
    resultFile.write(result[i])

resultFile.close()
print('Termino: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# GAS 14/11/2021
