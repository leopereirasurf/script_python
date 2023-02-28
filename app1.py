import streamlit as st

# Título do sidebar
st.sidebar.title('Menu1')

# Páginas disponíveis
paginas = ['Pagina 1', 'Pagina 2', 'Pagina 3']
# Seleção da página
paginaselecionada = st.sidebar.selectbox('Selecione a página', paginas)

# Conteúdo das páginas
if paginaselecionada == 'Pagina 1':
    st.title('Página 1 - Aula 8')
elif paginaselecionada == 'Pagina 2':
    st.title('Você selecionou a Página 2 - Aula 8')
    st.selectbox('Escolha uma opção', ('Opção 1', 'Opção 2'))
elif paginaselecionada == 'Pagina 3':
    st.title('Você selecionou a Página 3 - Aula 8')
    