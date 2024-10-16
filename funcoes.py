def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i_linha in range(linha, linha + tamanho):
            posicoes.append([i_linha, coluna])
    else:
        for i_coluna in range(coluna, coluna + tamanho):
            posicoes.append([linha, i_coluna])
            
    return posicoes
