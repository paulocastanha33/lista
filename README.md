# lista
Sistema de Gerenciamento de Tarefas(To-Do List) - Python com manipulação de arquivos

Este é um simples gerenciador de tarefas que funciona no terminal, permitindo ao usuário listar, adicionar, marcar como concluídas e remover tarefas. As tarefas são salvas em um arquivo `tarefas.txt` para persistência.

## Funcionalidades

- **Listar Tarefas:** Exibe a lista de todas as tarefas com seu status (Concluída ou Pendente).
- **Adicionar Tarefa:** Permite ao usuário adicionar uma nova tarefa à lista.
- **Marcar como Concluída:** Marca uma tarefa específica como concluída.
- **Remover Tarefa:** Remove uma tarefa da lista.
- **Persistência de dados:** As tarefas são salvas em um arquivo `tarefas.txt` no formato `descricao|status`.

## Requisitos

Este projeto utiliza a biblioteca [Colorama](https://pypi.org/project/colorama/) para adicionar cores ao terminal. Para rodá-lo, é necessário ter o seguinte:

- **Python 3.x**
- **Colorama** (para adicionar cores ao terminal)

## Instalação

1. Clone o repositório:
   
   git clone https://github.com/paulocastanha33/lista.git

2. Navegue até o diretório do projeto:

cd lista

3. Crie um ambiente virtual (opcional, mas recomendado):

python3 -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`

4. Instale as dependências:

pip install -r requirements.txt

5.Como Usar
Execute o script principal:

python app.py
Navegue pelo menu utilizando as opções disponíveis:

1: Listar tarefas
2: Adicionar tarefa
3: Marcar tarefa como concluída
4: Remover tarefa
5: Sair e salvar

# Estrutura do Código
limpar_tela(): Limpa a tela do terminal (compatível com Windows e Linux/macOS).
carregar_tarefas(): Carrega as tarefas do arquivo tarefas.txt.
salvar_tarefas(): Salva as tarefas no arquivo tarefas.txt.
listar_tarefas(): Lista as tarefas com seus status.
adicionar_tarefa(): Adiciona uma nova tarefa à lista.
marcar_como_concluida(): Marca uma tarefa como concluída.
remover_tarefa(): Remove uma tarefa da lista.
mostrar_menu(): Exibe o menu interativo no terminal.
main(): Função principal que executa o loop do programa.

# Licença
Este projeto está sob a licença MIT. Consulte o arquivo LICENSE para mais informações.

