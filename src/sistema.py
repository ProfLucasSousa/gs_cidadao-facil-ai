import json
import os
import re
import time
import unicodedata
 
BASE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "data", "base.json"
))
 
STOPWORDS = {
    "como", "para", "quero", "preciso", "onde", "qual",
    "quais", "uma", "meu", "minha", "com", "dos",
    "das", "que", "fazer", "posso", "sobre"
}
 
TESTES = [
    ("como tirar identidade", "DOC001"),
    ("consultar cpf", "DOC002"),
    ("tirar titulo eleitor", "DOC003"),
    ("carteira trabalho digital", "DOC004"),
    ("segunda via certidao", "DOC005"),
    ("encontrar ubs", "SAU001"),
    ("consultar vacinas", "SAU003"),
    ("cadastro unico", "BEN001"),
    ("encontrar cras", "BEN002"),
    ("", "VAZIO"),
    ("cadastro", "AMBIGUO"),
    ("renovar passaporte estrangeiro", "SEM_RESPOSTA")
]
 
 
def normalizar(texto):
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )
    return re.sub(r"[^a-z0-9 ]", " ", texto).strip()
 
 
def palavras(texto):
    return set(
        p for p in normalizar(texto).split()
        if len(p) > 2 and p not in STOPWORDS
    )
 
 
def carregar_base():
    try:
        with open(BASE, encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
 
        if not isinstance(dados, list) or not dados:
            raise ValueError("Base vazia ou inválida.")
 
        campos = {
            "id", "tema", "pergunta", "palavras_chave",
            "orientacao", "fonte", "data_verificacao",
            "relacionados"
        }
        ids = set()
 
        for item in dados:
            if not isinstance(item, dict):
                raise ValueError("Registro não é um dicionário.")
 
            if not campos.issubset(item):
                raise ValueError("Campos obrigatórios ausentes.")
 
            if any(
                not isinstance(item[c], str) or not item[c].strip()
                for c in campos - {"palavras_chave", "relacionados"}
            ):
                raise ValueError("Campo textual inválido.")
 
            if not isinstance(item["palavras_chave"], list):
                raise ValueError("Palavras-chave inválidas.")
 
            if not item["palavras_chave"] or any(
                not isinstance(p, str) or not p.strip()
                for p in item["palavras_chave"]
            ):
                raise ValueError("Palavra-chave vazia ou inválida.")
 
            if not isinstance(item["relacionados"], list):
                raise ValueError("Relacionamentos inválidos.")
 
            if item["id"] in ids:
                raise ValueError("Identificador duplicado.")
 
            ids.add(item["id"])
 
        for item in dados:
            if any(r not in ids for r in item["relacionados"]):
                raise ValueError("Relacionamento inexistente.")
 
        return dados
 
    except (OSError, ValueError, json.JSONDecodeError) as erro:
        print("Erro na base:", erro)
        return []
 
 
def pontuar(consulta, item):
    termos = palavras(consulta)
    if not termos:
        return 0
 
    pontos = 0
    titulo = palavras(item["pergunta"])
 
    pontos += 2 * len(termos & titulo)
 
    for chave in item["palavras_chave"]:
        chave_termos = palavras(chave)
        if chave_termos and chave_termos.issubset(termos):
            pontos += 5
        else:
            pontos += len(chave_termos & termos)
 
    return pontos
 
 
def buscar(consulta, base, tema=None):
    resultados = []
 
    for item in base:
        if tema and item["tema"] != tema:
            continue
 
        nota = pontuar(consulta, item)
        if nota >= 2:
            resultados.append((nota, item))
 
    resultados.sort(key=lambda x: (-x[0], x[1]["id"]))
    return resultados
 
 
def diagnosticar(consulta, base, tema=None):
    if not consulta.strip():
        return "VAZIO", None
 
    resultados = buscar(consulta, base, tema)
 
    if not resultados:
        return "SEM_RESPOSTA", None
 
    maior = resultados[0][0]
    empatados = [
        item for nota, item in resultados if nota == maior
    ]
 
    if len(empatados) > 1:
        return "AMBIGUO", empatados
 
    return "ENCONTRADO", empatados[0]
 
 
def responder(item, modelo="B"):
    print("\n" + "=" * 55)
 
    if modelo == "A":
        print(item["orientacao"])
        print("Fonte:", item["fonte"])
    else:
        print("CIDADÃO FÁCIL AI - ORIENTAÇÃO")
        print("Tema:", item["tema"])
        print("Pergunta:", item["pergunta"])
        print("\nOrientação:")
        print(item["orientacao"])
        print("\nFonte:", item["fonte"])
        print("Data de verificação:", item["data_verificacao"])
        print("\nAVISO:")
        print("Este assistente não representa um órgão público.")
        print("Confirme informações e requisitos na fonte oficial.")
 
    print("=" * 55)
 
 
def mostrar_relacionados(item, indice):
    relacionados = [
        indice[codigo]
        for codigo in item["relacionados"]
        if codigo in indice
    ]
 
    if not relacionados:
        return
 
    print("\nAssuntos relacionados:")
    for numero, registro in enumerate(relacionados, 1):
        print(numero, "-", registro["pergunta"])
 
    escolha = input(
        "Número para continuar ou Enter para voltar: "
    ).strip()
 
    if escolha.isdigit():
        posicao = int(escolha) - 1
        if 0 <= posicao < len(relacionados):
            responder(relacionados[posicao])
 
 
def consultar(base, indice, historico, tema=None):
    pergunta = input("\nDigite sua pergunta: ").strip()
    inicio = time.perf_counter()
 
    estado, resultado = diagnosticar(pergunta, base, tema)
    tempo = time.perf_counter() - inicio
 
    historico.append({
        "pergunta": pergunta,
        "resultado": estado,
        "tempo": tempo
    })
 
    if estado == "VAZIO":
        print("Digite uma pergunta válida.")
 
    elif estado == "SEM_RESPOSTA":
        print("Não encontrei informação suficiente na base.")
        print("Tente outra pergunta ou escolha um tema.")
 
    elif estado == "AMBIGUO":
        print("Encontrei mais de uma orientação possível:")
 
        for numero, item in enumerate(resultado, 1):
            print(numero, "-", item["pergunta"])
 
        escolha = input("Escolha um número: ").strip()
 
        if escolha.isdigit():
            posicao = int(escolha) - 1
            if 0 <= posicao < len(resultado):
                responder(resultado[posicao])
                mostrar_relacionados(resultado[posicao], indice)
            else:
                print("Opção inválida.")
        else:
            print("Opção inválida.")
 
    else:
        responder(resultado)
        mostrar_relacionados(resultado, indice)
 
    print(f"\nTempo de busca: {tempo:.6f} segundos")
 
 
def executar_testes(base):
    print("\n=== TESTES AUTOMÁTICOS ===")
 
    acertos = 0
    tempos = []
 
    for numero, (pergunta, esperado) in enumerate(TESTES, 1):
        inicio = time.perf_counter()
        estado, resultado = diagnosticar(pergunta, base)
        duracao = time.perf_counter() - inicio
 
        if estado == "ENCONTRADO":
            obtido = resultado["id"]
        else:
            obtido = estado
 
        correto = obtido == esperado
        if correto:
            acertos += 1
 
        tempos.append(duracao)
 
        print(f"\nTeste {numero}: {pergunta!r}")
        print("Esperado:", esperado)
        print("Obtido:", obtido)
        print("Resultado:", "ACERTO" if correto else "ERRO")
        print(f"Tempo: {duracao:.6f}s")
 
    total = len(TESTES)
    taxa = acertos / total * 100
    media = sum(tempos) / total
 
    print("\n=== INDICADORES ===")
    print(f"Acertos: {acertos}/{total}")
    print(f"Taxa de acerto: {taxa:.2f}%")
    print(f"Tempo médio: {media:.6f} segundos")
 
 
def comparar_modelos(base):
    print("\n=== COMPARAÇÃO DOS MODELOS ===")
    item = base[0]
 
    print("\nMODELO A - RESPOSTA DIRETA")
    responder(item, "A")
 
    print("\nMODELO B - RESPOSTA ESTRUTURADA")
    responder(item, "B")
 
    print("\nO modelo B apresenta mais contexto e avisos.")
    print("A avaliação de clareza deve ser feita por usuários.")
 
 
def main():
    base = carregar_base()
    if not base:
        return
 
    indice = {item["id"]: item for item in base}
    temas = sorted(set(item["tema"] for item in base))
    historico = []
 
    while True:
        print("\n" + "=" * 45)
        print("CIDADÃO FÁCIL AI PLUS")
        print("Assistente de orientação cidadã")
        print("=" * 45)
        print("1 - Fazer pergunta")
        print("2 - Consultar por tema")
        print("3 - Listar orientações")
        print("4 - Histórico da sessão")
        print("5 - Executar testes automáticos")
        print("6 - Comparar modelos de resposta")
        print("0 - Sair")
 
        opcao = input("\nEscolha uma opção: ").strip()
 
        if opcao == "0":
            print("Obrigado por utilizar o Cidadão Fácil AI!")
            break
 
        elif opcao == "1":
            consultar(base, indice, historico)
 
        elif opcao == "2":
            for numero, tema in enumerate(temas, 1):
                print(numero, "-", tema)
 
            escolha = input("Escolha o tema: ").strip()
 
            if escolha.isdigit() and 1 <= int(escolha) <= len(temas):
                tema = temas[int(escolha) - 1]
                consultar(base, indice, historico, tema)
            else:
                print("Tema inválido.")
 
        elif opcao == "3":
            for item in base:
                print(f"{item['id']} - {item['pergunta']}")
 
        elif opcao == "4":
            if not historico:
                print("Nenhuma consulta realizada.")
            else:
                for registro in historico:
                    print(
                        registro["pergunta"],
                        "-",
                        registro["resultado"]
                    )
 
        elif opcao == "5":
            executar_testes(base)
 
        elif opcao == "6":
            comparar_modelos(base)
 
        else:
            print("Opção inexistente.")
 
 
if __name__ == "__main__":
    main()