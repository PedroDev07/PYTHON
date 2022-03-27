class ArquivoTexto(object):

    def __init__(self, arquivo: str):
        self.arquivo = arquivo
        self.conteudo = self._extrair_conteudo()

    def _extrair_conteudo(self):
        conteudo = None
        with open(file=self.arquivo, mode='r', encoding='utf8') as arquivo:
            conteudo = arquivo.readlines()
        return conteudo


    def extrair_linha(self, numero_linha: int):
        palavras_linha = []    
        with open(file='./musica.txt', mode='r', encoding='utf8') as leitura: #abrindo arquivo txt em modo somente leitura
            linha = leitura.readline()#lendo a primeira linha
            for linha in self.conteudo:#enquanto linha não tiver valor nulo faça:
                palavras_linha.append(linha)# salva o valor na lista de palavas linha
                linha = leitura.readline()# lê uma nova linha, se a linha não existir, salva o valor None
                numero_linhax = numero_linha - 1 # Estou subtraindo 2 do indice para ficar compatível com a solicitação da atividade
                palavras_linha = palavras_linha[numero_linhax]# printando a linha que será utilizada na chamada da função
        return palavras_linha# retornando o valor final
