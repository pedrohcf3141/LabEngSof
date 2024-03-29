# LabEngSof

  Trabalho para a disciplina Laboratório de Engenharia de Software

	MATÉRIA: LABORATÓRIO DE ENGENHARIA DE SOFTWARE
	
	PROFESSOR: FABRICIO GALENDE MARQUES DE CARVALHO
	
	ALUNO: PEDRO HENRIQUE CERQUEIRA FERNANDES
	
	RA:1460481621067
	
	OPÇÃO: FLUXO 1  FLUXO NORMAL- QUESTIONARIO E ENTREGAS DE TRABALHOS PRÁTICOS
	
	ENTREGA: 01
	
	TEMA: Sistema para criação de receitas
	
	REQUISITOS E RESTRIÇÕES GERAIS, TECNOLOGIA PYTHON: 
		1. Utilizar linguagem de programação Python (versão 3.6 ou superior) no back end;
		2. Utilizar SQLAlchemy (1.2.19 ou superior) para persistência de dados;
		3. Utilizar Jinja 2 ou similar para geração de páginas dinâmicas (tipo template);
		4. Utilizar o microframework Flask para implantação do sistema web;
		5. Utilizar o Gunicorn como servidor de implantação, em conjunto com o Flask;
		6. Utilizar o Virtualenv para isolamento de ambiente de desenvolvimento e obtenção de pacotes;
		7. Estruturar o sistema seguindo a arquitetura MVC. 
	
	
	REQUISITOS ESPECÍFICOS SISTEMA:
		Desenvolver um sistema para criação de receitas.
		Uma receita deve ser criada a partir de uma lista de ingredientes pré-cadastrados.
		Um ingrediente é caracterizado pelo menos por um nome (ex: banana) e por um id único.
		Cada ingrediente, previamente cadastrado, deve possuir uma quantidade específica na receita que a ele fica atrelada na receita (ex: 200g).
		Além da quantidade de cada ingrediente na receita, essa deve possuir um nome (ex: bolo de cenoura)  e  um  conjunto  de  passos  (1  a  N  passos)  que  devem  ser  executados  na  sua preparação. O diagrama de caso de uso seguinte dá uma ideia geral das funcionalidades esperadas para o sistema: 
		
		Notar que Gerenciar Ingredientes refere-se a: inserir, alterar, buscar e remover ingredientes.O mesmo se aplica às receitas. Além disso, não deve ser possível criar uma receita com um ingrediente não cadastrado nem tampouco remover um ingrediente caso esse esteja presente em pelo menos uma receita. 
	
	
	GITHUB: https://github.com/pedrohcf3141/LabEngSof
	
	VIDEO ENTREGA: 00
	
	video: https://youtu.be/K_D7tFdjlkk
	
	ENTREGA: 01
	video: https://youtu.be/F6uWtlAw_qQ
	
	ENTREGA 02 DADOS USANDO PERSISTÊNCIA

	fiz deploy no heroku o senhor pode acessar o site abaixo
	https://receitaria1.herokuapp.com/ingredientes 
	
	video: https://youtu.be/TlqEt9UqEtw

	Caso queira fazer o build local 
	Requisitos:
	Python 3.8
	Mysql
	git

	Primeiros passos:
	Navegue até a pasta onde quer clonar o projeto pelo terminal
	execute: git clone git@github.com:pedrohcf3141/LabEngSof.git
	ou caso não tenha chave ssh configurada na maquina 
	execute: git clone https://github.com/pedrohcf3141/LabEngSof.git

	va até a pasta receitaria1_61 com o comando:
	cd receitaria1_61

	execute: pip install -r requirements.txt
	Segunda etapa:
	Na pasta receitaria1_61 abra o arquivo config.py onde encontrará:
	a constante ENV ='prod' mude para ENV ='dev'
	na linha 5 onde está  SQLALCHEMY_DATABASE_URI ='mysql+pymysql://<Altere para seu usuario>:<Altere para sua senha>@localhost/receitaria'
	altere o usuário e a senha para as credenciais do seu banco Mysql
	Crie um schema em seu banco no qual inseriu as credenciais, utilize o nome de receitaria.


	Terceira etapa(popular o schema com tables e column):
	Na pasta raiz execute o comando: python manage.py db stamp head
	e depois: python manage.py db migrate
	e por fim: python manage.py db upgrade

	Etapa final:
	Execute: python manage.py runserver
	Após isso navegue até o localhost pelo navegador na página index: http://localhost:5000/