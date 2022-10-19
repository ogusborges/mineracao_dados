from os import close
from random import randrange
from sys import argv

if __name__ == '__main__':
    # Restore the database file name from
    # command line arguments, handle some
    # errors.
    try:
        nome_arquivo = argv[1]
        num_amostras = int(argv[2])

        arq = open(nome_arquivo, 'r', encoding = 'UTF-8')
    except IndexError:
        print('Você precisa especificar um nome de arquivo e quantidade de amostras.')
        exit(1)
    except OSError:
        print('Não foi possível abrir o arquivo.')
        exit(1)
    except:
        print('Um erro desconhecido aconteceu.')
        exit(1)

    contagem = sum(1 for _ in arq)

    indices = []

    # If the sample number is greater or equal than 
    # the csv file row count, put all indexes on list.
    if num_amostras >= contagem:
        indices = [i for i in range(0, contagem)]
    else:
        i = 0
        
        while i < num_amostras:
            num = randrange(start = 0, stop = contagem)

            if num not in indices:
                indices.append(num)
                i = i + 1

    arq.seek(0)

    res = open('resultado.csv', 'w', encoding = 'UTF-8')

    for i in range(0, contagem):
        linha = arq.readline()

        if i in indices:
            res.write(linha)

    res.close()
    arq.close()