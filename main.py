import csv
from datetime import datetime


def extrair_dados(caminho_arquivo):
    """
    Extrai os dados do arquivo CSV.
    Retorna uma lista de dicionários.
    """
    clientes = []

    try:
        with open(caminho_arquivo, mode="r", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for linha in leitor:
                clientes.append({
                    "id": linha["id"],
                    "nome": linha["nome"],
                    "conta": linha["conta"],
                    "cartao": linha["cartao"],
                    "limite": float(linha["limite"])
                })

        print(f"Extração concluída: {len(clientes)} clientes carregados.")
        return clientes

    except FileNotFoundError:
        print(f"Erro: o arquivo '{caminho_arquivo}' não foi encontrado.")
        return []
    except Exception as erro:
        print(f"Erro ao extrair os dados: {erro}")
        return []


def gerar_mensagem(cliente):
    """
    Transforma os dados do cliente em uma mensagem personalizada.
    """
    nome = cliente["nome"]
    limite = cliente["limite"]

    if limite >= 3000:
        perfil = "premium"
        oferta = "Você tem acesso a condições especiais de investimento e crédito."
    elif limite >= 2000:
        perfil = "intermediário"
        oferta = "Você pode aproveitar novas opções de parcelamento e benefícios exclusivos."
    else:
        perfil = "básico"
        oferta = "Temos sugestões para ajudar você a organizar melhor sua vida financeira."

    mensagem = (
        f"Olá, {nome}! Identificamos que seu perfil atual é {perfil}. "
        f"Seu limite disponível é de R$ {limite:.2f}. {oferta}"
    )

    return mensagem


def transformar_dados(clientes):
    """
    Gera mensagens personalizadas para cada cliente.
    """
    dados_transformados = []

    for cliente in clientes:
        mensagem = gerar_mensagem(cliente)

        dados_transformados.append({
            "id": cliente["id"],
            "nome": cliente["nome"],
            "conta": cliente["conta"],
            "cartao": cliente["cartao"],
            "limite": f'{cliente["limite"]:.2f}',
            "mensagem": mensagem
        })

    print("Transformação concluída: mensagens geradas com sucesso.")
    return dados_transformados


def carregar_dados(caminho_saida, dados):
    """
    Salva os dados transformados em um novo arquivo CSV.
    """
    if not dados:
        print("Nenhum dado para salvar.")
        return

    campos = ["id", "nome", "conta", "cartao", "limite", "mensagem"]

    try:
        with open(caminho_saida, mode="w", newline="", encoding="utf-8") as arquivo:
            escritor = csv.DictWriter(arquivo, fieldnames=campos)
            escritor.writeheader()
            escritor.writerows(dados)

        print(f"Carregamento concluído: arquivo '{caminho_saida}' salvo com sucesso.")

    except Exception as erro:
        print(f"Erro ao salvar os dados: {erro}")


def exibir_resumo(dados):
    """
    Exibe um pequeno resumo final do processamento.
    """
    print("\n===== RESUMO DO PROCESSO ETL =====")
    print(f"Total de registros processados: {len(dados)}")
    print(f"Data e hora da execução: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print("Arquivo final gerado com sucesso.")


def main():
    arquivo_entrada = "dados_clientes.csv"
    arquivo_saida = "mensagens_geradas.csv"

    # ETAPA 1 - EXTRAÇÃO
    clientes = extrair_dados(arquivo_entrada)

    if not clientes:
        print("Processo encerrado.")
        return

    # ETAPA 2 - TRANSFORMAÇÃO
    dados_transformados = transformar_dados(clientes)

    # ETAPA 3 - CARREGAMENTO
    carregar_dados(arquivo_saida, dados_transformados)

    # RESUMO
    exibir_resumo(dados_transformados)


if __name__ == "__main__":
    main()