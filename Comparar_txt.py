<<<<<<< HEAD
# Ler e comparar dois arquivos TXT
# Procura pelo arquivo newfile.txt e oldfile.txt no subdiretório Files
# Cria um novo arquivo, resultfile.txt
# from IPython.display import display
import os
import time

os.chdir('.\Files')  # altera para esse diretório - Windows
# os.chdir('Files/')    # altera para esse diretório - Mac Os
print('Diretório de trabalho...............................: ' + os.getcwd())
print('Inicio..............................................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# verificar se os arquivos existem no diretório

if not os.path.isfile('oldfile.txt'):
    print("Arquivo oldfile.txt não localizado")
    print("Finalizando o programa.")
    exit()
elif not os.path.isfile('newfile.txt'):
    print("Arquivo newfile.txt não localizado")
    print("Finalizando o programa.")
    exit()
else:
    while True:
        cab = input("O arquivo possuí cabeçalho? (S)im (N)ão ")
        if cab.upper() in ("S", "N"):
            break

#inicio do tratamento do arquivo oldfile.txt
print('Abrindo arquivo [oldfile.txt]........................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

fileoldfile = open('oldfile.txt', 'r', encoding='ANSI')  # abre o arquivo oldfile.txt no modo de leitura
conteudo_old = fileoldfile.readlines()

# insere o conteúdo do arquivo oldfile.txt na lista oldfile
oldfile = []
for i in range(len(conteudo_old)):
    oldfile.append(conteudo_old[i])
fileoldfile.close()  # fecha o arquivo

print('Quantidade de registros no arquivo oldfile...........: ' + str(len(oldfile)))
#Fim do tratamento do arquivo oldfile.txt

#inicio do tratamento do arquivo newfile.txt
print('Abrindo arquivo [newfile.txt]........................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

filenewfile = open('newfile.txt', 'r', encoding='ANSI')  # abre o arquivo newfile.txt no modo de leitura
conteudo_new = filenewfile.readlines()

# insere o conteúdo do arquivo newfile.txt na lista newfile
newfile = []
for i in range(len(conteudo_new)):
    newfile.append(conteudo_new[i])
filenewfile.close()  # fecha o arquivo

print('Quantidade de registros no arquivo newfile...........: ' + str(len(newfile)))
#fim do tratamento do arquivo newfile.txt

print('Separando as linhas diferentes entre os arquivos.....: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# insere na lista result apenas as linhas que existem em newfile e não existem em oldfile
result = sorted(list(set(newfile) - set(oldfile)))  #o arquivo resultado esta sendo ordenado, caso não queira, substitua o comando para [result = list(set(newfile) - set(oldfile))]
if cab.upper() == "S":
    result.insert(0, newfile[0])  # insere o cabeçalho na 1a linha

print('Quantidade de registros diferentes..................: ' + str(len(result)))
resultFile = open('resultfile.txt', 'w')

for i in range(len(result)):
    resultFile.write(result[i])

resultFile.close()
print('Termino: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# GAS 14/11/2021
=======
# Ler e comparar dois arquivos TXT
# Procura pelo arquivo newfile.txt e oldfile.txt no subdiretório Files
# Cria um novo arquivo, resultfile.txt
# from IPython.display import display
import os
import time

os.chdir('.\Files')  # altera para esse diretório - Windows
# os.chdir('Files/')    # altera para esse diretório - Mac Os
print('Diretório de trabalho...............................: ' + os.getcwd())
print('Inicio..............................................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

# verificar se os arquivos existem no diretório

if not os.path.isfile('oldfile.txt'):
    print("Arquivo oldfile.txt não localizado")
    print("Finalizando o programa.")
    exit()
elif not os.path.isfile('newfile.txt'):
    print("Arquivo newfile.txt não localizado")
    print("Finalizando o programa.")
    exit()
else:
    while True:
        cab = input("O arquivo possuí cabeçalho? (S)im (N)ão ")
        if cab.upper() in ("S", "N"):
            break

#inicio do tratamento do arquivo oldfile.txt
print('Abrindo arquivo [oldfile.txt]........................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

fileoldfile = open('oldfile.txt', 'r', encoding='ANSI')  # abre o arquivo oldfile.txt no modo de leitura
conteudo_old = fileoldfile.readlines()

# insere o conteúdo do arquivo oldfile.txt na lista oldfile
oldfile = []
for i in range(len(conteudo_old)):
    oldfile.append(conteudo_old[i])
fileoldfile.close()  # fecha o arquivo

print('Quantidade de registros no arquivo oldfile...........: ' + str(len(oldfile)))
#Fim do tratamento do arquivo oldfile.txt

#inicio do tratamento do arquivo newfile.txt
print('Abrindo arquivo [newfile.txt]........................: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

filenewfile = open('newfile.txt', 'r', encoding='ANSI')  # abre o arquivo newfile.txt no modo de leitura
conteudo_new = filenewfile.readlines()

# insere o conteúdo do arquivo newfile.txt na lista newfile
newfile = []
for i in range(len(conteudo_new)):
    newfile.append(conteudo_new[i])
filenewfile.close()  # fecha o arquivo

print('Quantidade de registros no arquivo newfile...........: ' + str(len(newfile)))
#fim do tratamento do arquivo newfile.txt

print('Separando as linhas diferentes entre os arquivos.....: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# insere na lista result apenas as linhas que existem em newfile e não existem em oldfile
result = sorted(list(set(newfile) - set(oldfile)))  #o arquivo resultado esta sendo ordenado, caso não queira, substitua o comando para [result = list(set(newfile) - set(oldfile))]
if cab.upper() == "S":
    result.insert(0, newfile[0])  # insere o cabeçalho na 1a linha

print('Quantidade de registros diferentes..................: ' + str(len(result)))
resultFile = open('resultfile.txt', 'w')

for i in range(len(result)):
    resultFile.write(result[i])

resultFile.close()
print('Termino: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# GAS 14/11/2021
>>>>>>> 637ab1b7f98ea7402d84e7259313c57344d1fc5a
