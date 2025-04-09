<p align="center">
  <img src="imagens/imgcabeçalho2.png" width="100%">
</p>

<h1 align="center">🍫 Brigaderia Encanto</h1>

<p align="center">
  Aplicativo web simples e prático feito com Python + Streamlit para registrar pedidos de brigadeiros artesanais. Ideal para pequenas empresas que desejam organizar seus pedidos digitalmente, com interface amigável e banco de dados local, pronto para crescer junto com o negócio!
</p>

---

## 🟫 Descrição do Projeto

O **Brigaderia Encanto** permite o cadastro do cliente e a visualização de pedidos contendo:
- Nome do cliente
- Sabor do brigadeiro:

|**Brigadeiro**                                                  |   **Sabor**                  |
| -------------------------------------------------------------- | ----------------------------|
| <img src="imagens/tradicional.png" width="140" height="140">      | **Tradicional**             |
| <img src="imagens/nutella.png" width="140" height="140">          | **Nutella**                 |
| <img src="imagens/brigadeiro_com_morango.png" width="140" height="140"> | **Brigadeiro com Morango**  |
| <img src="imagens/brigadeiro_com_castanha.png" width="140" height="140"> | **Brigadeiro com Castanha** |
| <img src="imagens/brigadeiro_com_amendoim.png" width="140" height="140"> | **Brigadeiro com Amendoim** |


- Quantidade de unidades
- Carrinho
- Finalizar pedido

Os dados são armazenados localmente em um banco **SQLite**, com estrutura preparada para futura migração para o **Azure SQL Database**.

---

## 🟫 Funcionalidades

- Registro de pedidos com nome, sabor e quantidade
- Validação de campos obrigatórios
- Lista dos pedidos já cadastrados
- Interface leve e responsiva com Streamlit
- Armazenamento local automático (`brigaderia.db`)
- Pronto para ser migrado para banco de dados em nuvem (Azure SQL)

--- 

## 🟫 Teste

<p align="center">
  <img src="./imagens/teste1.png" width="750" />
</p>

<p align="center">
  <img src="./imagens/teste2.png" width="750" />
</p>

---

## 🟫 Tecnologias Utilizadas

- **Linguagem**: ![Python Badge](https://img.shields.io/badge/python-3.9-703B26?style=flat&logo=python&logoColor=703B26)
- **Framework Web**: ![Streamlit Badge](https://img.shields.io/badge/streamlit-v1.2.0-703B26?style=flat&logo=streamlit&logoColor=703B26)
- **Banco de Dados Local**: ![SQLite Badge](https://img.shields.io/badge/sqlite-3.34.1-703B26?style=flat&logo=sqlite&logoColor=703B26)
- **Bibliotecas**:
  - ![Pandas Badge](https://img.shields.io/badge/pandas-1.2.3-703B26?style=flat&logo=pandas&logoColor=703B26)
  - ![Datetime Badge](https://img.shields.io/badge/datetime-4.3-703B26?style=flat&logoColor=703B26)
  - ![SQLite3 Badge](https://img.shields.io/badge/sqlite3-3.35.0-703B26?style=flat&logoColor=703B26)
- **Ambiente Virtual**: ![Venv Badge](https://img.shields.io/badge/venv-virtualenv-703B26?style=flat&logoColor=703B26)
- **Editor**: ![VSCode Badge](https://img.shields.io/badge/vscode-1.56-703B26?style=flat&logo=visualstudiocode&logoColor=703B26)
- **Controle de Versão**: ![Git Badge](https://img.shields.io/badge/git-2.30-703B26?style=flat&logo=git&logoColor=703B26)


---

## 🟫 Como rodar o projeto localmente

1. **Clone o repositorio**:

bash

`git clone https://github.com/AraujoTech1/brigaderia-encanto.git` 


2. **Ative o ambiente virtual**:

- No Windows:

 bash
 
 `python -m venv venv` 

 Depois

`venv\Scripts\activate` 

3. **Instale as dependências**:

bash

`pip install -r requirements.txt` 

4. **Rodando o projeto**:

bash

`streamlit run app.py` 


**Após rodar o comando acima, o aplicativo estará disponível no seu navegador localmente.**

---
## ⚖️ Licença ⚖️

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](./LICENSE) para mais detalhes.



---

<p align="center">Desenvolvido com 🤎 e ☕!</p>
