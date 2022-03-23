# CRUD DJANGO

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

- superusercredentials para acessar o painel de administrador do Django caso desejar:
1. username: admin
2. email: admin@admin.com
3. senha: admin
