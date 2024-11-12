import os

def renomear_imagens_webp(diretorio):
    # Obtendo a lista de arquivos na pasta
    arquivos = sorted([f for f in os.listdir(diretorio) if f.endswith('.webp')])

    # Iterando sobre os arquivos para renomeá-los
    for index, arquivo in enumerate(arquivos):
        # Criando o novo nome para o arquivo
        novo_nome = f"img-{index + 1}.webp"
        
        # Obtendo o caminho completo dos arquivos antigo e novo
        caminho_antigo = os.path.join(diretorio, arquivo)
        caminho_novo = os.path.join(diretorio, novo_nome)
        
        # Renomeando o arquivo
        os.rename(caminho_antigo, caminho_novo)
        print(f"Arquivo '{arquivo}' renomeado para '{novo_nome}'")

# Exemplo de uso
diretorio_imagens = "./"
renomear_imagens_webp(diretorio_imagens)
