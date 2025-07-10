# Códigos ANSI para cores e estilos
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"  # Reseta para o estilo padrão

print(f"{RED}Este texto está em vermelho!{RESET}")
print(f"{GREEN}Este texto está em verde!{RESET}")
print(f"{YELLOW}Este texto está em amarelo!{RESET}")
print(f"{BLUE}Este texto está em azul!{RESET}")
print(f"{CYAN}Este texto está em ciano!{RESET}")
print('\033[4;30;45mOlá,mundo!')
print("\033[1;31mTexto em vermelho negrito\033[0m")
print("\033[3;34mTexto em azul itálico\033[0m")
print("\033[4;93mTexto sublinhado em amarelo brilhante\033[0m")
print("\033[7;92mTexto invertido em verde brilhante\033[0m")
print("\033[38;5;200mTexto em magenta (256 cores)\033[0m")
print("\033[48;5;202mFundo em laranja (256 cores)\033[0m")
