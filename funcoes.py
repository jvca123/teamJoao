def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'vertical':
        for i_linha in range(linha, linha + tamanho):
            posicoes.append([i_linha, coluna])
    else:
        for i_coluna in range(coluna, coluna + tamanho):
            posicoes.append([linha, i_coluna])
            
    return posicoes

def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    if nome_navio in frota:
        frota[nome_navio].append(define_posicoes(linha, coluna, orientacao, tamanho))
    else:
        frota[nome_navio] = [define_posicoes(linha, coluna, orientacao, tamanho)]
    
    return frota
