# 🎬 Plano de Projeto: CineLog (CRUD de Filmes com React + OMDb API)

Guia prático para desenvolver na raça uma aplicação de catálogo e diário cinematográfico ("Letterboxd de Bolso"), integrando a API externa do **OMDb** e implementando um **CRUD completo** em **React**.

---

## 🎯 Objetivo do Projeto
Construir uma aplicação onde o usuário pode buscar filmes reais da API do OMDb, salvá-los em sua coleção pessoal categorizados por status (**"Já Vi"**, **"Quero Ver"**, **"Favoritos"**), atribuir notas, comentários pessoais, editar avaliações e excluir registros.

---

## 🛠️ Tecnologias e Ferramentas
* **Frontend**: React (Vite)
* **Linguagem**: JavaScript (JSX)
* **Estilização**: CSS puro moderno (Dark Theme cinematográfico)
* **API Externa**: [OMDb API](https://www.omdbapi.com/)
* **Persistência**: `localStorage` (ou backend opcional caso solicitado pelo professor)

---

## 🏗️ Estrutura do Projeto

```text
cinelog/
├── public/
├── src/
│   ├── assets/
│   ├── components/
│   │   ├── Navbar.jsx          # Barra superior com logo e botão de adicionar
│   │   ├── MovieSearch.jsx     # Campo de busca e sugestões via OMDb API
│   │   ├── MovieModal.jsx      # Modal de cadastro/edição (nota, status, review)
│   │   ├── MovieCard.jsx       # Card do filme na coleção
│   │   ├── MovieGrid.jsx       # Grid com lista de filmes
│   │   └── FilterTabs.jsx      # Abas de filtro: Todos, Já Vi, Quero Ver, Favoritos
│   ├── services/
│   │   └── omdbApi.js          # Funções de requisição HTTP (fetch/axios) para a OMDb
│   ├── App.jsx                 # Estado central da aplicação e controle do CRUD
│   ├── App.css                 # Estilos globais e componentes visuais
│   └── main.jsx                # Ponto de entrada do React
├── index.html
├── package.json
└── vite.config.js
```

---

## 📋 Entidade: Estrutura do Filme Salvo no CRUD

Cada filme adicionado terá o seguinte formato:

```json
{
  "id": "tt0848228",
  "imdbID": "tt0848228",
  "title": "The Avengers",
  "year": "2012",
  "poster": "https://m.media-amazon.com/images/M/....jpg",
  "genre": "Action, Sci-Fi",
  "director": "Joss Whedon",
  "plot": "Earth's mightiest heroes must come together...",
  "status": "watched",         // "watched" (Já Vi) | "watchlist" (Quero Ver) | "favorite" (Favorito)
  "userRating": 4.5,           // Nota dada pelo usuário (0.5 a 5.0 estrelas)
  "userReview": "Filme incrível! O clímax em Nova York é histórico.",
  "createdAt": "2026-10-02T00:30:00.000Z"
}
```

---

## 🚀 Fases de Execução Passo a Passo

### Passo 1: Inicialização do Ambiente
- [ ] Criar o projeto React com Vite:
  ```bash
  npm create vite@latest cinelog -- --template react
  cd cinelog
  npm install
  ```
- [ ] Limpar arquivos padrão desnecessários do template.
- [ ] Iniciar o servidor de desenvolvimento:
  ```bash
  npm run dev
  ```

---

### Passo 2: Integração com a OMDb API (`services/omdbApi.js`)
- [ ] Configurar a chave de API (`API_KEY`).
- [ ] Criar função `searchMovies(query)`:
  - Endpoint: `https://www.omdbapi.com/?apikey=SUA_CHAVE&s=${query}`
  - Retorna a lista de filmes resumidos.
- [ ] Criar função `getMovieDetails(imdbID)`:
  - Endpoint: `https://www.omdbapi.com/?apikey=SUA_CHAVE&i=${imdbID}&plot=full`
  - Retorna detalhes completos (sinopse, elenco, diretor, pôster).

---

### Passo 3: O "C" do CRUD (Create / Cadastrar)
- [ ] Criar o componente de busca (`MovieSearch.jsx`).
- [ ] Exibir autocomplete com os resultados retornados pela OMDb API ao digitar.
- [ ] Ao clicar em um filme da lista, abrir o modal de cadastro (`MovieModal.jsx`):
  - Exibir pôster, título e ano carregados da API.
  - Selecionar o status: **Já Vi**, **Quero Ver** ou **Favorito**.
  - Informar a nota pessoal (1 a 5 estrelas).
  - Escrever comentário/review pessoal opcional.
- [ ] Salvar o novo objeto no estado do React e persistir no `localStorage`.

---

### Passo 4: O "R" do CRUD (Read / Visualizar)
- [ ] Criar o componente `MovieCard.jsx`:
  - Pôster em destaque com efeito hover.
  - Título, ano e gênero.
  - Badge colorido de status (*Já Vi*, *Quero Ver*, *Favorito*).
  - Estrelas da nota pessoal.
  - Botões rápidos de Ação (Editar e Deletar).
- [ ] Criar o componente `MovieGrid.jsx` para renderizar os cards em grid responsivo.
- [ ] Carregar a lista inicial salva do `localStorage` no primeiro render (`useEffect`).

---

### Passo 5: O "U" do CRUD (Update / Atualizar)
- [ ] Ao clicar em "Editar" no card:
  - Reabrir o modal preenchido com os dados atuais do filme.
- [ ] Permitir alterar:
  - Status (ex: mover de "Quero Ver" para "Já Vi").
  - Atualizar a nota.
  - Modificar a review.
- [ ] Atualizar o estado no React e sincronizar com o `localStorage`.

---

### Passo 6: O "D" do CRUD (Delete / Remover)
- [ ] Adicionar botão de exclusão no card ou modal.
- [ ] Exibir diálogo de confirmação simples para prevenir exclusões acidentais.
- [ ] Filtrar e remover o filme pelo `id` do estado e atualizar o `localStorage`.

---

### Passo 7: Filtros e Abas de Navegação
- [ ] Criar abas no topo:
  - **Todos**
  - **Já Vi** (`status === 'watched'`)
  - **Quero Ver** (`status === 'watchlist'`)
  - **Favoritos** (`status === 'favorite'`)
- [ ] Adicionar barra de filtro/pesquisa local dentro da sua própria coleção.
- [ ] Exibir contador de filmes por categoria (ex: "Já Vi (12)").

---

### Passo 8: Design Visual e Acabamento
- [ ] Tipografia moderna (Inter ou Outfit via Google Fonts).
- [ ] Tema escuro cinematográfico (preto, cinza grafite, acentos dourados e roxos).
- [ ] Estado de lista vazia (Empty State) bonito quando o usuário ainda não tiver cadastrado filmes.
- [ ] Feedback visual de carregamento (Loading spinner) nas requisições da OMDb API.
