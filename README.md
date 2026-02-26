# Sistema de Cadastro
Aplicação web de cadastro de usuários desenvolvida com Python + Flask + MySQL, com validação de formulário e armazenamento em banco de dados. Projeto Full Stack simples visando apenas 

## Tecnologias usadas
* Python
* Flask
* MySQL
* HTML5 + CSS3

## Estrutura do Projeto
```
formulario-de-cadastro/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── config.py
│
├── templates/
│   └── cadastro.html
│
├── static/
│   └── assets/
│       ├── css/
│       └── img/
│
├── .env
├── requirements.txt
└── README.md
```

## Como executar o projeto
### 1- Clone este repositorio no seu computador. Escolha um ambiente onde consiga acessar a pasta com facilidade.
No seu terminal, execute:
```
git clone https://github.com/nanic1/formulario-de-cadastro
cd formulario-de-cadastro
```

### 2- Instalar dependências
```
pip install -r requirements.txt
```

### 3- Configurar variáveis de ambiente
Na raiz do projeto, crie um arquivo .env. Nele, você vai colocar as informações do seu banco de dados, é importante tambem que você crie uma SECRET_KEY qualquer para o funcionamento de algumas funções específicas do Flask.
```
SECRET_KEY=chave-secreta
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=sua-senha
DB_NAME=cadastro
DATABASE_URL=mysql+pymysql://root:sua-senha@localhost/cadastro
```

### 4- Execução do projeto
Após todas as etapas, podemos finalmente executar o projeto e visualiza-lo. É importante que você esteja com o MySQL Workbench aberto e configurado.
Dentro do projeto, execute este comando:
```
python run.py
```

Se não houver nenhum erro, abra seu navegador e cole este link para acessar a página:
```
http://127.0.0.1:5000
```

Depois disso, você estará livre pra testar todas as funcionalidades da página feita.

## Funcionalidades
* Cadastro de usuário
* Validação de campos obrigatórios
* Verificação de senha
* Mensagem de sucesso e erro
* Criação automática do banco de dados e das tabelas na inicialização do projeto

## Autor
Pedro Kurtz
