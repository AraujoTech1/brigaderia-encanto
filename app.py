import streamlit as st
from utils import get_image_path
from database import init_db, adicionar_pedido
from datetime import datetime

st.set_page_config(page_title="Brigaderia Encanto 🍫", page_icon="🍫")
init_db()

st.title("🍫 Brigaderia Encanto")
st.subheader("Escolha os brigadeiros e adicione ao seu carrinho!")

# Mapeamento dos sabores para as imagens
sabores = {
    "Tradicional": "tradicional.png",
    "Nutella": "nutella.png",
    "Brigadeiro com Morango": "brigadeiro_com_morango.png",
    "Brigadeiro com Castanha": "brigadeiro_com_castanha.png",
    "Brigadeiro com Amendoim": "brigadeiro_com_amendoim.png"
}

# Carrinho de compras
if 'carrinho' not in st.session_state:
    st.session_state.carrinho = []

nome = st.text_input("Seu nome:")

# Selecione o sabor
sabor_escolhido = st.selectbox("Escolha o sabor:", list(sabores.keys()))

# Mostrar a imagem após seleção do sabor
if sabor_escolhido:
    st.image(get_image_path(sabores[sabor_escolhido]), width=250)

# Quantidade de brigadeiros
quantidade = st.number_input("Quantos brigadeiros?", min_value=1, step=1)

# Adicionar ao carrinho
if st.button("Adicionar ao Carrinho"):
    if sabor_escolhido and quantidade:
        carrinho_item = {
            "sabor": sabor_escolhido,
            "quantidade": quantidade,
            "imagem": get_image_path(sabores[sabor_escolhido])
        }
        st.session_state.carrinho.append(carrinho_item)
        st.success(f"{quantidade} brigadeiro(s) de sabor {sabor_escolhido} adicionado(s) ao carrinho!")

# Exibir os itens no carrinho
if len(st.session_state.carrinho) > 0:
    st.subheader("Itens no Carrinho:")
    for item in st.session_state.carrinho:
        st.image(item['imagem'], width=50)
        st.write(f"{item['quantidade']}x {item['sabor']}")
    
    # Enviar pedido
    if st.button("Enviar Pedido"):
        if nome:
            for item in st.session_state.carrinho:
                data_atual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                id_pedido = None  # O id será gerado automaticamente pelo banco de dados
                adicionar_pedido(id_pedido, nome, item['sabor'], item['quantidade'], data_atual)
            st.success(f"Pedido enviado com sucesso, {nome}! 🍬")
            st.session_state.carrinho = []  # Limpar carrinho após o envio
        else:
            st.warning("Preencha o nome antes de enviar o pedido.")
else:
    st.write("Seu carrinho está vazio. Adicione brigadeiros ao carrinho!")
