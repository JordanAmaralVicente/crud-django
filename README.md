# CRUD DJANGO
Projeto básico de CRUD com a biblioteca Django que realizar salvar as informações em um Banco SQLite. E com bootstrap para estilizar os componentes. O bootstrap foi escolhido pois meu foco não foi no HTML/CSS e sim no Django, então, uma vez que o bootstrap facilita a estilização, o mesmo foi usado

O projeto dá a opção e criar, listar, atualizar e deletar produtos (CRUD).

# Como rodar ?
1. primeiro, você precisa ter o [python3.10](https://www.python.org/downloads/release/python-3103/) instalado em sua máquina.
2. Caso já tenha, você deve ativar o ambiente de desenvolvimento virtual (venv) do projeto. Para isse, rode o seguinte comando na raíz do projeto:

- No MacOS ou no Linux

```bash
source venv/bin/activate  
```
- No Windows:

```PowerShell
venv\Scripts\Activate.ps1
```

3. Após ter ativado o venv, instalar o framework Django:

```bash
pip install django
```
4. Instalado o django, será necessário, ou talvez não, rodar as migrations:

```bash
python3.10 manage.py migrate
```

5. Por fim, uma vez tendo feito todo o setup do projeto, basta rodar o comando de inicar o servidor e acessar a página no endereço: http://127.0.0.1:8000/ em seu naveagor:
```bash
python3.10 manage.py runserver
```

# Já feito
1. Dar a opção do usuário realizar buscas


# Próximos Passos
2. Dar a opção do usuário executar filtros e ordenação de buca
3. Fazer integração com um banco diferente do SQlite
4. Criar mais funcionalides - Como cadastro / Login
5. Usar uma biblioteca de teste para os componentes


## superusercredentials para acessar o painel de administrador do Django caso desejar:
1. username: admin
2. email: admin@admin.com
3. senha: admin