"""Assistente cidadão e avaliações reproduzíveis, usando a biblioteca padrão.

Execução interativa: python src/sistema.py
Avaliação: python src/sistema.py --testes --comparar-modelos --usabilidade --regressoes
"""
import json
import os
import re
import time
import unicodedata
import argparse
from datetime import date, datetime
from urllib.parse import urlparse

BASE = os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..", "data", "base.json"
))
SINONIMOS = {"cadastral": "cadastro"}

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
TESTES += [
    ("DOC001", "DOC001"),
    ("Como emitir a Carteira de Identidade Nacional?", "DOC001"),
    ("Onde vejo as vacinas que tomei?", "SAU003"),
    ("Como acessar meu cartao SUS?", "SAU002"),
    ("Onde buscar atendimento de urgencia?", "SAU005"),
    ("Quero informacoes do Bolsa Familia", "BEN003"),
    ("Onde consultar o BPC?", "BEN004"),
    ("Como obter desconto energia?", "BEN005"),
    ("Receita de bolo de cenoura", "SEM_RESPOSTA"),
    ("   ", "VAZIO"),
]


def normalizar(texto):
    """Remove diferenças de caixa, acentuação e pontuação."""
    texto = unicodedata.normalize("NFD", texto.lower())
    texto = "".join(
        c for c in texto
        if unicodedata.category(c) != "Mn"
    )
    return re.sub(r"[^a-z0-9 ]", " ", texto).strip()


def palavras(texto):
    """Seleciona termos relevantes e aplica o pequeno mapa de sinônimos."""
    return set(
        SINONIMOS.get(p, p) for p in normalizar(texto).split()
        if len(p) > 2 and p not in STOPWORDS
    )


def carregar_base(caminho=None):
    """Valida o JSON e suas referências antes de disponibilizar orientações."""
    try:
        with open(caminho or BASE, encoding="utf-8") as arquivo:
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
            if any(not isinstance(r, str) or not r.strip()
                   for r in item["relacionados"]):
                raise ValueError("Identificador de relacionamento inválido.")
            endereco = urlparse(item["fonte"])
            if endereco.scheme != "https" or not endereco.netloc:
                raise ValueError("Fonte deve ser uma URL HTTPS válida.")
            verificacao = date.fromisoformat(item["data_verificacao"])
            if verificacao > date.today():
                raise ValueError("Data de verificação futura.")

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
    """Soma pesos por termos do título e palavras-chave; não interpreta intenção."""
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
    """Prioriza o ID exato e ordena correspondências lexicais dentro do tema."""
    resultados = []

    for item in base:
        if tema and item["tema"] != tema:
            continue
        if consulta.strip().upper() == item["id"].upper():
            return [(1000, item)]

        nota = pontuar(consulta, item)
        if nota >= 2:
            resultados.append((nota, item))

    resultados.sort(key=lambda x: (-x[0], x[1]["id"]))
    return resultados


def diagnosticar(consulta, base, tema=None):
    """Distingue entrada vazia, ausência, empate e orientação encontrada."""
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


def formatar_resposta(item, modelo="B"):
    """Aplica os modelos de instrução sem acrescentar conteúdo à base."""
    if modelo == "A":
        return f"Orientação:\n{item['orientacao']}\nFonte: {item['fonte']}"
    return (
        f"CIDADÃO FÁCIL AI - ORIENTAÇÃO\nTema: {item['tema']}\n"
        f"Pergunta: {item['pergunta']}\n\nOrientação:\n{item['orientacao']}\n"
        f"\nFonte: {item['fonte']}\nData de verificação: {item['data_verificacao']}\n"
        "\nAVISO:\nEste assistente não representa um órgão público.\n"
        "Confirme informações e requisitos na fonte oficial."
    )


def responder(item, modelo="B"):
    print("\n" + "=" * 55)
    print(formatar_resposta(item, modelo))
    print("=" * 55)


def mostrar_relacionados(item, indice):
    """Percorre o grafo até o usuário retornar; opções inválidas permitem nova tentativa."""
    while True:
        relacionados = [indice[c] for c in item["relacionados"] if c in indice]
        if not relacionados:
            return
        print("\nAssuntos relacionados:")
        for numero, registro in enumerate(relacionados, 1):
            print(numero, "-", registro["pergunta"])
        escolha = input("Número para continuar ou Enter para voltar: ").strip()
        if not escolha:
            return
        if escolha.isascii() and escolha.isdigit() and 1 <= int(escolha) <= len(relacionados):
            item = relacionados[int(escolha) - 1]
            responder(item)
        else:
            print("Opção inválida. Escolha um número da lista ou pressione Enter.")


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
        print("Temas disponíveis:", ", ".join(sorted({r["tema"] for r in base})))

    elif estado == "AMBIGUO":
        print("Encontrei mais de uma orientação possível:")

        for numero, item in enumerate(resultado, 1):
            print(numero, "-", item["pergunta"])

        escolha = input("Escolha um número: ").strip()

        if escolha.isascii() and escolha.isdigit():
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
    """Mede a seleção do registro/estado e apresenta esperado, obtido e duração."""
    print("\n=== TESTES AUTOMÁTICOS ===")

    acertos = 0
    tempos = []
    registros = []

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
        esperado_item = next((i for i in base if i["id"] == esperado), None)
        registros.append({
            "pergunta": pergunta, "esperado": esperado, "obtido": obtido,
            "orientacao_esperada": esperado_item["orientacao"] if esperado_item else esperado,
            "resposta_obtida": formatar_resposta(resultado) if estado == "ENCONTRADO" else estado,
            "acerto": correto, "tempo_segundos": duracao,
        })

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
    relatorio = {"data_execucao": datetime.now().astimezone().isoformat(),
                 "total": total, "acertos": acertos, "taxa_acerto": taxa,
                 "tempo_medio_segundos": media, "testes": registros}
    return relatorio


def comparar_modelos(base):
    """Compara conteúdo, fonte e transparência nos cenários de teste."""
    print("\n=== COMPARAÇÃO DOS MODELOS ===")
    registros = []
    for pergunta, esperado in TESTES:
        estado, item = diagnosticar(pergunta, base)
        if estado != "ENCONTRADO":
            registros.append({"pergunta": pergunta, "estado": estado,
                              "A": estado, "B": estado})
            continue
        a, b = formatar_resposta(item, "A"), formatar_resposta(item, "B")
        registros.append({"pergunta": pergunta, "esperado": esperado,
                          "obtido": item["id"], "A": a, "B": b,
                          "criterios": {"mesma_orientacao": item["orientacao"] in a and item["orientacao"] in b,
                                        "fonte_em_ambos": item["fonte"] in a and item["fonte"] in b,
                                        "data_em_B": item["data_verificacao"] in b,
                                        "aviso_em_B": "não representa um órgão público" in b},
                          "caracteres_A": len(a), "caracteres_B": len(b)})
        print("\nPergunta:", pergunta)
        print("MODELO A:\n" + a)
        print("MODELO B:\n" + b)
    print("\nB é o padrão por explicitar tema, data e limites. A é mais curto.")
    print("Os critérios verificam estrutura e consistência; compreensão humana exige avaliação própria.")
    return registros


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

            if escolha.isascii() and escolha.isdigit() and 1 <= int(escolha) <= len(temas):
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


TAREFAS = [
    ("Encontrar orientação sobre CIN", ["1", "Como tirar minha identidade?", "", "0"],
     ["Carteira de Identidade Nacional", "Fonte:", "Data de verificação:"]),
    ("Consultar saúde pelo menu de temas", ["2", "3", "encontrar UBS", "", "0"],
     ["Tema: Saúde", "Unidade Básica de Saúde"]),
    ("Navegar por CIN, CPF e CTPS", ["1", "DOC001", "1", "2", "", "0"],
     ["Pergunta: Como consultar a situação cadastral do CPF?",
      "Pergunta: Como acessar a Carteira de Trabalho Digital?"]),
    ("Tratar pergunta fora da base", ["1", "renovar passaporte estrangeiro", "0"],
     ["Não encontrei informação suficiente", "Temas disponíveis:"]),
    ("Inspecionar estrutura e limites da resposta", ["1", "consultar vacinas", "", "0"],
     ["Tema:", "Pergunta:", "Orientação:", "Fonte:", "Data de verificação:",
      "não representa um órgão público", "Confirme informações"]),
    ("Recuperar-se de opção inválida nos relacionados", ["1", "DOC001", "99", "1", "", "0"],
     ["Opção inválida. Escolha um número da lista", "Pergunta: Como consultar a situação cadastral do CPF?"]),
]


def executar_regressoes():
    """Valida arquivos, busca e fluxos sem depender de arquivos auxiliares."""
    import contextlib
    import copy
    import io
    import sys
    import tempfile
    import unittest
    from pathlib import Path
    from unittest.mock import patch
    sistema = sys.modules[__name__]

    class SistemaTests(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.base = sistema.carregar_base()
            cls.indice = {item["id"]: item for item in cls.base}

        def carregar_conteudo(self, conteudo):
            with tempfile.TemporaryDirectory() as pasta:
                arquivo = Path(pasta) / "base.json"
                arquivo.write_text(conteudo, encoding="utf-8")
                with contextlib.redirect_stdout(io.StringIO()):
                    return sistema.carregar_base(arquivo)

        def test_consultas_e_limitacoes(self):
            for pergunta, esperado in sistema.TESTES:
                with self.subTest(pergunta=pergunta):
                    estado, resultado = sistema.diagnosticar(pergunta, self.base)
                    obtido = resultado["id"] if estado == "ENCONTRADO" else estado
                    self.assertEqual(esperado, obtido)

        def test_arquivo_ausente(self):
            with tempfile.TemporaryDirectory() as pasta:
                with contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual([], sistema.carregar_base(Path(pasta) / "ausente.json"))

        def test_arquivos_invalidos(self):
            for texto in ("", "[]", "{}", "{", "[null]", "[{}]"):
                with self.subTest(texto=texto):
                    self.assertEqual([], self.carregar_conteudo(texto))

        def test_dados_inconsistentes(self):
            variantes = [
                ("relacionados", [{}]), ("relacionados", [[]]),
                ("relacionados", ["INEXISTENTE"]), ("palavras_chave", []),
                ("palavras_chave", [None]), ("fonte", "texto"),
                ("data_verificacao", "PENDENTE"), ("data_verificacao", "2999-01-01"),
            ]
            for campo, valor in variantes:
                with self.subTest(campo=campo, valor=valor):
                    dados = copy.deepcopy(self.base)
                    dados[0][campo] = valor
                    self.assertEqual([], self.carregar_conteudo(json.dumps(dados)))
            dados = copy.deepcopy(self.base)
            dados[1]["id"] = dados[0]["id"]
            self.assertEqual([], self.carregar_conteudo(json.dumps(dados)))

        def test_filtro_de_tema(self):
            self.assertEqual("SEM_RESPOSTA", sistema.diagnosticar("CPF", self.base, "Saúde")[0])

        def test_navegar_por_tres_assuntos_e_rejeitar_opcoes(self):
            saida = io.StringIO()
            with patch("builtins.input", side_effect=["x", "99", "²", "1", "2", ""]):
                with contextlib.redirect_stdout(saida):
                    sistema.mostrar_relacionados(self.indice["DOC001"], self.indice)
            self.assertEqual(3, saida.getvalue().count("Opção inválida"))
            self.assertIn(self.indice["DOC002"]["pergunta"], saida.getvalue())
            self.assertIn(self.indice["DOC004"]["pergunta"], saida.getvalue())

        def test_menu_tema_ambiguidades_e_fallback(self):
            entradas = ["x", "2", "99", "2", "²", "1", "cadastro", "99",
                        "1", "cadastro", "1", "", "1", "", "1", "bolo cenoura", "0"]
            saida = io.StringIO()
            with patch("builtins.input", side_effect=entradas):
                with contextlib.redirect_stdout(saida):
                    sistema.main()
            for mensagem in ("Opção inexistente", "Tema inválido", "Opção inválida",
                             "Digite uma pergunta válida", "Temas disponíveis", "Obrigado"):
                self.assertIn(mensagem, saida.getvalue())

        def test_comparacao_modelos(self):
            with contextlib.redirect_stdout(io.StringIO()):
                resultados = sistema.comparar_modelos(self.base)
            self.assertEqual(len(sistema.TESTES), len(resultados))
            for resultado in resultados:
                if "criterios" in resultado:
                    self.assertTrue(all(resultado["criterios"].values()))

    resultado = unittest.TextTestRunner(verbosity=2).run(
        unittest.defaultTestLoader.loadTestsFromTestCase(SistemaTests)
    )
    return resultado.wasSuccessful()


def avaliar_usabilidade():
    """Executa roteiro de tarefas; não mede compreensão ou satisfação humana."""
    import contextlib
    import io
    from unittest.mock import patch
    tarefas = TAREFAS
    registros = []
    for nome, entradas, mensagens in tarefas:
        saida = io.StringIO()
        inicio = time.perf_counter()
        with patch("builtins.input", side_effect=entradas):
            with contextlib.redirect_stdout(saida):
                main()
        texto = saida.getvalue()
        faltantes = [mensagem for mensagem in mensagens if mensagem not in texto]
        registros.append({"tarefa": nome, "entradas": entradas,
                          "concluida": not faltantes, "mensagens_ausentes": faltantes,
                          "tempo_automatizado_segundos": time.perf_counter() - inicio,
                          "saida": texto})
        print(nome, "-", "CONCLUÍDA" if not faltantes else "FALHOU")
    print(f"Roteiro: {sum(r['concluida'] for r in registros)}/{len(registros)} tarefas concluídas.")
    print("Execução automatizada, sem participante humano. Não mede tempo de uso humano.")
    return registros


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Assistente acadêmico de orientação cidadã")
    parser.add_argument("--testes", action="store_true", help="Executa as perguntas de teste")
    parser.add_argument("--comparar-modelos", action="store_true", help="Compara os modelos A e B")
    parser.add_argument("--usabilidade", action="store_true", help="Executa roteiro automatizado de tarefas")
    parser.add_argument("--regressoes", action="store_true", help="Valida arquivos e fluxos")
    argumentos = parser.parse_args()
    avaliacao = any(vars(argumentos).values())
    sucesso = True
    if avaliacao:
        dados = carregar_base()
        if not dados:
            raise SystemExit(1)
        if argumentos.testes:
            resultado = executar_testes(dados)
            sucesso &= resultado["acertos"] == resultado["total"]
        if argumentos.comparar_modelos:
            comparar_modelos(dados)
        if argumentos.usabilidade:
            sucesso &= all(r["concluida"] for r in avaliar_usabilidade())
        if argumentos.regressoes:
            sucesso &= executar_regressoes()
        raise SystemExit(0 if sucesso else 1)
    main()
