# 📚 Library Collection - Sistema de Acervo Bibliográfico
### Projeto Completo: Versão Terminal + Versão Web (Django)

## 👨‍💻 Informações do Projeto
- Desenvolvedor: João Victor Silva dos Santos
- Curso: Back-end em Python
- Instituição: IFBA / CEPEDI
- Professor(a): Karina Leite
- Data de Entrega: 19/03/2026

## 📖 Sobre o Projeto
O Library Collection é um sistema de gerenciamento de acervos bibliográficos desenvolvido em duas versões:
1. Versão Terminal - Python puro com menu interativo
2. Versão Web (Django) - Interface web com autentição

Este projeto demonstra a evolução de uma aplicação Python básica para um sistema web, aplicando os conceitos aprendidos durante o curso.

## 🎯 Problemas que Resolve
Pessoas que colecionam livros e querem organizar seu acervo pessoal de forma moderna e eficiente. Este sistema oferece:

- 📖 Catalogação de livros, revistas, manuscritos e outros materiais
- 🗂️ Organização por categorias
- ⭐ Favoritos pessoais com notas e anotações
- 🔍 Busca e consulta de itens
- 👤 Perfil personalizado
- 📱 Interface web
- 💾 Seus dados salvos e privados

## 🚀 Duas Versões do Projeto
📟 Versão 1: Terminal (Python Puro)  
Interface de linha de comando com menu interativo  

**Tecnologias:**  
- Python 3
- SQLite3
- Classes Python puras

**Pasta:** `terminal/`  

<sub>────────────────────────────────────────────</sub>

🌐 Versão 2: Web (Django)  
Interface web com autenticação de usuários.

**Tecnologias:**
- Django 5
- Bootstrap 5
- SQLite3
- Sistema de autenticação
- Upload de imagens

**Pasta:** `django/` 

## 🚀 Como Executar
📟 Versão Terminal  
**Pré-requisitos**
- Python 3 instalado

**Passo a Passo**  
1. Abra o terminal
2. Navegue até a pasta usando: `cd`
3. Execute o programa usando: `python main.py`

<sub>────────────────────────────────────────────</sub>

🌐 Versão Django
**Pré-requisitos**
- Python 3 instalado
- pip (gerenciador de pacotes)

**Passo a Passo**  
1. Abra o terminal
2. Navegue até a pasta usando: `cd`
3. Instale as dependências: `pip install django pillow`
4. Execute as migrações: `python manage.py makemigrations` e `python manage.py migrate`
5. Se quiser admin, crie um superusuário: `python manage.py createsuperuser`
6. Rode o servidor: `python manage.py runserver`
7. Acesse no navegador: http://127.0.0.1:8000

## ⚙️ Funcionalidades
📟 Versão Terminal  
**CRUD de Itens**
- Cadastrar com título, autor, ano, tipo e categoria
- Listar todos os itens
- Atualizar informações
- Deletar com confirmação

**CRUD de Categorias**
- Adicionar novas categorias
- Listar categorias disponíveis
- Deletar (com validação de uso)

**Validações**
- Título obrigatório
- Autor padrão "Anônimo"
- Ano: -3000 até atual+1 (suporta a.C.)
- Ano 0 não permitido
- Tipo obrigatório
- Categoria deve existir

**Recursos Especiais**
- Menu interativo
- Tratamento de erros
- Confirmações de exclusão
- Categorias padrão automáticas
- Validação de categoria em uso

<sub>────────────────────────────────────────────</sub>

**✅ Versão Django (Web)**  

**Tudo da versão Terminal mais:

**🔐 Autenticação**
- ✅ Registro de usuários
- ✅ Login/Logout
- ✅ Perfil personalizado com foto
- ✅ Criação automática de perfil

**📸 Upload de Imagens**
- ✅ Imagem para itens
- ✅ Imagem para categorias
- ✅ Foto de perfil
- ✅ Placeholder automático

**⭐ Sistema de Favoritos**
- ✅ Adicionar/remover favoritos
- ✅ Notas pessoais em favoritos
- ✅ Visualizar no perfil
- ✅ Proteção contra duplicatas

**🔍 Busca e Filtros**
- ✅ Busca por título/autor
- ✅ Filtro por categoria
- ✅ Múltiplas categorias por item

**🎨 Interface**
- ✅ Design responsivo (Bootstrap 5)
- ✅ Formulários validados

##🎓 Aprendizados

**Na versão Terminal:**
- Aprendi POO com classes Python
- Banco de dados com SQL direto
- Validações básicas
- Menu interativo

**Na versão Web (Django):**  
- Django Framework
- Django ORM
- Templates e herança
- Sistema de autenticação
- Upload de arquivos
- Relacionamentos N:N
- Signals automáticos
- Bootstrap e design

**Principais desafios**
1. Configurar upload de imagens
2. Relacionamento ManyToMany
3. Sistema de autenticação
4. Signals para auto-criação
5. Templates com Bootstrap
6. Admin com CSS e Bootstrap

## 📸 Capturas de Tela

<img width="1339" height="718" alt="Screenshot_352" src="https://github.com/user-attachments/assets/c9c39a48-3ce5-4df0-a0b1-b71f556e180d" />

<img width="1338" height="719" alt="Screenshot_353" src="https://github.com/user-attachments/assets/0e4c7dea-c764-4996-b3db-bfa3d4c9e627" />

<img width="1338" height="721" alt="Screenshot_354" src="https://github.com/user-attachments/assets/e4d1b670-e9fd-4bae-a88b-ea35952c9f25" />

<img width="1335" height="714" alt="Screenshot_355" src="https://github.com/user-attachments/assets/de6ec271-07e8-42fb-9347-03972c530c28" />

<img width="1336" height="720" alt="Screenshot_356" src="https://github.com/user-attachments/assets/6877c0d5-e86e-465f-8006-7f26f52d8074" />

<img width="1331" height="715" alt="Screenshot_357" src="https://github.com/user-attachments/assets/ef83accd-476b-4b89-b375-4a9fb28f58a8" />

<img width="1337" height="716" alt="Screenshot_358" src="https://github.com/user-attachments/assets/c1dbde32-b0bb-43d2-b8e6-38a63c3019f0" />
