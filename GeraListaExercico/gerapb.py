arquivo1 = open( 'lista.txt', 'r')
i = 0
for linha in arquivo1:
    i = i+1
    linha = linha.rstrip()
    if i < 10:
        arquivo = open(f'pb0{i}.py','w')
        arquivo.write(f'#{linha}')   
        arquivo.close
    else:
        arquivo = open(f'pb{i}.py','w')
        arquivo.write(f'#{linha}')
        arquivo.close