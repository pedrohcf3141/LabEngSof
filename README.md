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
	
	VIDEO ENTREGA 01:https://youtu.be/K_D7tFdjlkk
	
	ENTREGA: 02
	Ser disponibilizado via link do GitHub OK
	Conter arquivo com todas as dependências necessárias para "levantar a aplicação" (atentar para os arquivos build.gradle ou requirements.txt conforme você use Java ou Python);OK
	requirements.txt contido no diretório receitaria1_61
	
	Utilizar templates (ex. JSPs ou templates do Jinja) para as interfaces; OK
	Ter as interfaces acessíveis a partir de rotas (não deve ser possível visualizar um arquivo tal como home.jsp na barra de navegação); OK
	Conter nas interfaces todos os dados que são esperados (ex. formulários de entrada); OK
	Conter nas interfaces exemplos de dados de saídas (ex. listagem de itens, nesse caso, valores estáticos que não retornam de banco de dados); OK
	Esse protótipo não tem ênfase no visual, mas sim na navegabilidade e na coerência dos dados. Além disso, na capacidade de uso da ferramenta de build para obtenção das dependências. OK
	No arquivo README.MD, documentar o procedimento de build e colocar um link para um vídeo explicativo, no YouTube, onde você "levanta a aplicação" e navega nas interfaces. Explicar adequadamente as rotas. Esse vídeo deve ter duração aproximada máxima de 5 minutos.
	
	build:
		cd receitaria1_61
		pythom manage.py runserver
	
	video: https://youtu.be/F6uWtlAw_qQ
	
	
