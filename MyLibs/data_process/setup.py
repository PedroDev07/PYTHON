from gettext import install
from setuptools import setup, find_packages

with open ("README.md", "r") as f:
    page_description = f.read()
    
with open("requirements.txt") as f:
    requirements = f.read().splitlines()
    
setup(
    name="Data_processing",#nome do pacote
    version="0.0.1",#versao do pacote
    author="Pedro Lucas",#autor do pacote
    author_email="pedrodeveloper7@gmail.com",#email do autor
    description="Pacote pessoal para análise de dados",#descricao curta
    long_description=page_description,#vai ter uma pagina de descricao
    long_description_content_type="text/markdown",
    url="",#url do projeto no git
    packages=find_packages(),#encontra os pacotes dependentes
    #vai encontrar no txt os pacotes que precisam ser instalados juntos
    python_requires='>=3.8',#versao do python necessaria para rodar o pacote
)