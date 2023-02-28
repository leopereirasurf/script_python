import streamlit as st

# Define o nome de usuário e a senha válidos
username = "usuario"
password = "senha"

# Cria o formulário de login
login = st.sidebar.beta_container()
with login:
    st.header("Faça login")
    user = st.text_input("Nome de usuário")
    passw = st.text_input("Senha", type="password")
    submit = st.button("Entrar")

# Cria o formulário de cadastro de novo usuário
register = st.sidebar.beta_container()
with register:
    st.header("Crie uma nova conta")
    new_user = st.text_input("Novo nome de usuário")
    new_passw = st.text_input("Nova senha", type="password")
    confirm_passw = st.text_input("Confirme a nova senha", type="password")
    register_submit = st.button("Criar conta")

    # Verifica se o formulário de cadastro foi enviado e cria um novo usuário
    if register_submit:
        if new_passw == confirm_passw:
            username = new_user
            password = new_passw
            st.success("Conta criada com sucesso!")
        else:
            st.error("As senhas não correspondem.")

# Verifica se o formulário de login foi enviado e autentica o usuário
if submit:
    if user == username and passw == password:
        st.success("Bem-vindo, " + username + "!")
    else:
        st.error("Nome de usuário ou senha inválido.")
