# Anotações de Web Mobile

---

## Instruções para Gerenciamento do Projeto
1. Abrir Ubuntu WSL
2. git pull origin main
   git fetch
   git merge

### Atualizar os Dados no Repositório
1. git add .
2. git commit -m "Atualizando arquivos do projeto"
3. git push origin main

### Subindo ambiente virtual
1. virtualenv --version
Se não tiver instala
2. virtualenv -p python3 virtual
3. Para iniciar: source ./virtual/bin/activate

4. Para desativar: desactivate

### Pasta para acessar no windows
- \\wsl$\Ubuntu\home\enzolucas\web-mobile

### Procedimentos ao Final de Cada Aula
1. rm -rf C:\Users\Aluno\Documents\web-mobile

2. git config --global --unset user.name
   git config --global --unset user.email

3. - Pressione Ctrl+Shift+Delete.
   - Selecione a opção "Tudo" para limpar histórico, cookies e cache.

---

## Aula 1 - 12/03/2025


### Aplicação Web
- **Definição:** Sistemas que rodam no navegador, desenvolvidos com **HTML**, **JavaScript** e **CSS**. Eles podem ser executados localmente ou a partir de um servidor web (HTTP), conhecido como *Web Host*.  
- **Função do Servidor Web:** O servidor recebe uma requisição e devolve uma resposta ao cliente. Geralmente, os servidores enviam instruções em **HTML**, que o navegador utiliza para renderizar o conteúdo de forma estruturada ao usuário.

### Sobre HTML
- **World Wide Web (WWW):** Sistema global de servidores na internet que suporta documentos formatados, incluindo links para gráficos, áudios e vídeos.  
- **HTML:** Não é uma linguagem de programação, mas sim de marcação, utilizada para estruturar blocos e organizar o conteúdo.  
  - O dinamismo e a lógica interativa são implementados através do **JavaScript**, que é de fato uma linguagem de programação.
  - Os elementos HTML formam a base da construção das páginas e podem ser estilizados com **CSS**.

### Sobre JavaScript
- **Definição:** Uma linguagem de alto nível, leve e interpretada, usada para manipular o comportamento das páginas web.  
- **Importância:** Essencial para o desenvolvimento *front-end*, sendo amplamente utilizada também em aplicações **mobile**, **desktop** e até no **back-end** com tecnologias como Node.js.

### Sobre CSS
- **Definição:** Não é uma linguagem de programação, mas sim um conjunto de regras para definir a aparência visual de documentos HTML ou XML.  
- **Função:** Estilizar e layoutar elementos, conferindo identidade visual ao projeto.

### Sobre Git e Versionamento
- Git: Sistema de controle de versão distribuído que rastreia mudanças no código e permite colaboração entre desenvolvedores.

- Versionamento: Prática de manter um histórico organizado das alterações, possibilitando reverter mudanças indesejadas.

**Principais Comandos:**
- git init: Inicializa um repositório.
- git add: Adiciona arquivos para o stage.
- git commit: Registra mudanças com uma mensagem.
- git push: Envia alterações para o repositório remoto.
- git pull: Atualiza o código local com mudanças remotas.
- Vantagens: Organização, rastreabilidade, colaboração e segurança no desenvolvimento de projetos.

---

## Aula 2 - 19/03/2025
Falta

---

## Aula 3 - 02/04/2025 Capítulo 2 - Padrões Arquiteturais
# Padrões Arquiteturais

---

## Definição
Os padrões arquiteturais definem a estrutura, integrações e organização dos componentes de software, facilitando a comunicação entre desenvolvedores e garantindo escalabilidade, manutenção e reutilização de código.

## Padrões Existentes
- Monolítico
- Microserviços
- Modelo-Visão-Controlador (MVC)

### Padrão Monolítico
- **Descrição:** A solução é formada por módulos que agem separadamente, mas ainda estão ligados, criando um único sistema.  
- **Facilidade:** Inicialmente, é fácil criar uma solução única interligando todas as funcionalidades do sistema.
- **Problemas:**  
  - Escalabilidade limitada.  
  - Dificuldade na integração de novas tecnologias.  
  - Maior complexidade à medida que o sistema cresce.  
  - Dependência elevada entre os componentes.  
  - Dificuldade em atualizar ou implementar mudanças.  
- **Uso Ideal:** Projetos de pequena complexidade (não se deve usar uma "bazuca" para matar uma formiga).

### Padrão Microserviços
- **Descrição:** Funcionalidades separadas em serviços autônomos e independentes, que se comunicam via APIs.
- **Vantagens:**  
  - Cada funcionalidade é implementada como um serviço bem definido.  
  - Independência para cada serviço, facilitando a manutenção e escalabilidade.
- **Desafios:**  
  - Necessidade de desenvolvedores qualificados.
  - Complexidade na comunicação entre os serviços.  

![Microserviços vs Monolítico](https://k21academy.com/wp-content/uploads/2023/07/rancher_blog_microservices-and-monolithic-architectures.webp)

### Padrão MVC (Model-View-Controller)
- **Descrição:** O padrão MVC separa a representação de dados da interação com o usuário, facilitando a manutenção do sistema.
  - **Modelo (Model):** Responsável pelos dados da aplicação, regras de negócio e funções.  
  - **Visão (View):** Apresenta os dados ao usuário, podendo ser gráficos, tabelas, etc.  
  - **Controlador (Controller):** Media a entrada do usuário, convertendo-a em comandos para o modelo ou a visão.
- **Vantagens:**  
  - Separação de responsabilidades, o que facilita a manutenção e reutilização de código.

![Camadas do MVC](https://vaidegrails.wordpress.com/wp-content/uploads/2015/06/atuacao_das_camadas_mvc.png)

### Variações do Padrão MVC
#### Model-View-Template (MVT)
- **Modelo (Model):** Camada de acesso aos dados, responsável pelo banco de dados.
- **Template:** A camada que lida com a apresentação da informação ao usuário.
- **Visão (View):** Implementa a lógica de negócios e interage com o modelo para transportar dados e renderizar um template.

### Mapeamento de Objeto Relacionado - ORM
- **Definição:** Técnica de desenvolvimento que facilita a integração entre programação orientada a objetos e bancos de dados relacionais, mapeando tabelas de bancos de dados como classes e registros como instâncias dessas classes.
- **Vantagens:**  
  - O programador não precisa se preocupar com comandos SQL diretamente, utilizando uma interface simples de programação.
  - A relação entre os dados no banco e os objetos no programa é configurada pelo programador, permitindo flexibilidade na organização dos dados.
- **Exemplo de Ferramentas:**  
  - **Hibernate (Java):** Utiliza arquivos XML ou anotações para mapear o modelo.  
  - **Django ORM (Python):** Utiliza herança de classes para o mapeamento.  
  - **SQLAlchemy (Python):** Framework que facilita a comunicação entre classes e banco de dados.
  - **Pony ORM (Python):** Ferramenta gráfica para gerar o código que representa o modelo do banco.

![Exemplo ORM](https://dkrn4sk0rn31v.cloudfront.net/2019/11/03082048/ORM-IMG.png)

---

### Resumo sobre Python
Python é uma linguagem de programação de alto nível, amplamente utilizada por sua sintaxe simples e versatilidade. É muito popular em áreas como desenvolvimento web, automação, análise de dados, inteligência artificial e muito mais.

