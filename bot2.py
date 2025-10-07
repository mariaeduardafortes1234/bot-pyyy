def exibir_menu():
  print("\n" "+" "="* 50)
  print("Assistente Virtual - Tec Info RDS")
  print("=" * 50)
  print("Digite sua dúvida ou escolha uma opção: ")
  print("📃 'Menu' - Ver tópicos disponíveis")
  print("❓ 'Ajuda' - Como usar o assistente")
  print("🚪 'Sair' - Encerrar o atendimento\n")

def listar_topicos():
    print("📃 Tópicos disponíveis")
    print("✔️ Variáveis e tipos de dados")
    print("✔️ Estruturas condicionais (if/else)")
    print("✔️ Laços e repetição (for/while)")
    print("✔️ Listas e manipulação")
    print("✔️ Funções")
    print("✔️ Importar bibliotecas\n")

def buscar_respostas(pergunta):
    Respostas ={
        "Variável": {
            "texto": "Variáveis armazenam informações em Python, basta atribuir um valor:",
             "exemplo": "nome= 'João' \nidade = 17\naltura = 1.75"
        },
        "if":{
            "texto": "o comando permite que o programa tome decisões. Ele avalia uma condição, e se ela for verdadeira, executa um bloco de código específico:",
            "exemplo": ("idade = 20 if\nidade >= 18\n print(você é maior de idade e pode ter CNH)
if idade >= 18:
    print("Você é maior de idade e pode ter CNH.")
else:
    print("Você é menor de idade e não pode ter CNH.")
        },
        "for":{
            "texto": "É um comando de repetição que executa um bloco de código um número determinado de vezes",
            "exemplo": "...",
        },
        "list":{
            "texto": "É uma estrutura de dados fundamental que armazena uma coleção ordenada de itens sob um único nome de variável",
            "exemplo": "...",
        },
        "def":{
            "texto": "A palavra-chave que indica o início da definição de uma função",
            "exemplo": "...",
        },
        "import":{
            "texto": "é um comando que permite utilizar módulos, bibliotecas, pacotes ou arquivos de código externos em seu programa",
            "exemplo": "...",
        },
    }