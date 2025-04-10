# 📺 AniMangaTracker - API & Banco de Dados

**AniMangaTracker** é a API backend de um aplicativo que permite aos usuários organizarem suas listas de animes e mangás de forma personalizada, além de acompanhar a programação de lançamentos de animes ao longo do ano.

Esta API é responsável por armazenar e gerenciar as listas de anime e mangá de cada usuário, garantindo persistência dos dados e integração com o frontend do app. O projeto foi desenvolvido utilizando **Flask 3.1.0** e **SQLAlchemy 2.0.39**, com suporte total a **Docker** para execução em ambiente isolado.

---

## 🚀 Tecnologias Utilizadas

Este projeto foi desenvolvido utilizando as seguintes tecnologias e versões:

- **Python** 3.11.0 – Linguagem principal do projeto.
- **Flask** 3.1.0 – Framework leve para construção de APIs .
- **SQLAlchemy** 2.0.39 – ORM para integração com banco de dados .
- **Docker** latest – Containerização do ambiente de execução.

---

## 🛠️ Pré-requisitos

Certifique-se de ter os seguintes softwares instalados:

- [Python 3.11.0](https://www.python.org/downloads/release/python-3110/)
- [Docker](https://www.docker.com/)

⚠️ O projeto **deve ser executado dentro de um container Docker** para garantir compatibilidade e isolamento de ambiente.

---

## 📦 Instalação

### 1. Clone o repositório

```bash
git clone <URL DO REPOSITÓRIO>
cd <URL DO REPOSITÓRIO>
```
Substitua `<URL_DO_REPOSITORIO>` pela URL do repositório.

---

## 🐳 Executando com Docker (recomendado)

### 2. Construa a imagem Docker

```bash
docker build -t animanga-tracker-api .
```

### 3. Execute o container

```bash
docker run -d -p 5000:5000 animanga-tracker-api
```

> A API estará disponível em: http://localhost:5000

---

## 🔧 Executando Localmente com Flask (sem Docker)

> Recomendado apenas para desenvolvimento e testes locais.

### 1. Crie um ambiente virtual

```bash
python -m venv venv
```
Ative o ambiente:

- No Windows:

```bash
.venv\Scripts\activate
```

- No macOS e Linux:

```bash
source venv/bin/activate
```

### 2. Instale as dependências

```bash
pip install -r requirements.txt
```

### 3. Execute o servidor Flask

```bash
flask run --host 0.0.0.0 --port 5000
```

> A API estará disponível em: http://localhost:5000

---

## 🔗 Principais Endpoints

| Método | Rota                            | Descrição                             |
|--------|----------------------------------|----------------------------------------|
| GET    | `/anime_list`                    | Retorna a lista de animes do usuário   |
| POST   | `/anime`                         | Adiciona novo anime à lista do usuário |
| DELETE | `/anime?id=<id>`                 | Remove um anime da lista do usuário    |
| GET    | `/anime?id=<id>`                 | Retorna um anime da lista do usuário   |
| PUT    | `/anime?id=<id>`                 | Atualiza um anime da lista do usuário  |

---

## 📃 Licença

Este projeto está licenciado sob os termos da **MIT License**.  
