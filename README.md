<div align="center">

  <!-- Banner Oficial UNICAP com link para o Portal -->
  <a href="https://portal.unicap.br" target="_blank" rel="noopener noreferrer">
    <img src="assets/docs/unicap-banner.png" alt="UNICAP - Universidade Católica de Pernambuco" width="360" style="border-radius: 8px;" />
  </a>

  <br/><br/>

  <h1>Desenvolvimento Front-End • 2026.2</h1>
  <p><strong>Universidade Católica de Pernambuco (UNICAP)</strong></p>

  <!-- Badges de Tecnologias, Docência e Instituição -->
  <a href="https://portal.unicap.br" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/UNICAP-Universidade%20Católica%20de%20Pernambuco-990000?style=for-the-badge&logo=academic-tree&logoColor=white" alt="UNICAP" />
  </a>
  <a href="https://marciobueno.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Docente-Prof.%20Márcio%20Bueno-D4AF37?style=for-the-badge&logo=googlechrome&logoColor=black" alt="Prof. Márcio Bueno" />
  </a>
  <a href="https://nextjs.org/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Next.js-16.3-black?style=for-the-badge&logo=nextdotjs&logoColor=white" alt="Next.js" />
  </a>
  <a href="https://react.dev/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/React-19.0-61DAFB?style=for-the-badge&logo=react&logoColor=black" alt="React" />
  </a>
  <a href="https://vercel.com/" target="_blank" rel="noopener noreferrer">
    <img src="https://img.shields.io/badge/Vercel-Deploy-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Deploy Vercel" />
  </a>

  <br/><br/>

</div>

---

## 📖 Sobre o Projeto

Repositório central das atividades práticas da disciplina de **Desenvolvimento Front-End** da **[Universidade Católica de Pernambuco (UNICAP)](https://portal.unicap.br)**, ministrada pelo **[Prof. Márcio Bueno](https://marciobueno.com/)** no período letivo **2026.2**.

O projeto reúne os exercícios e desafios desenvolvidos ao longo do semestre com **Next.js (App Router)** e **React 19**, enfatizando:
- Componentização declarativa, modular e reutilizável.
- Estilização moderna com CSS (Dark Mode, tipografia e layout responsivo).
- Integração contínua e deploy na nuvem com **[Vercel](https://vercel.com/)**.

---

## 🎓 Informações Acadêmicas

| Campo | Detalhes |
| :--- | :--- |
| **Instituição** | [UNICAP — Universidade Católica de Pernambuco](https://portal.unicap.br) |
| **Disciplina** | Desenvolvimento Front-End |
| **Docente** | [Prof. Márcio Bueno](https://marciobueno.com/) |
| **Período Letivo** | 2026.2 |
| **Discente** | Richard Silva ([@Richdssz](https://github.com/Richdssz)) |

---

## 📚 Tabela de Atividades do Semestre

| # | Atividade / Tema | Descrição | Componentes / Arquivos | Rota / Demonstração | Status |
| :-: | :--- | :--- | :--- | :--- | :-: |
| **01** | **MiniBio & Card de Perfil** | Criação e estilização de um card de perfil com foto, insígnia sobreposta e frase de apresentação utilizando arquitetura modular em React/Next.js. | `components/Profile.js`<br/>`components/MiniBio.js`<br/>`app/page.js` | [🌐 Acessar Atividade](https://front-end-2026-2.vercel.app/) | Concluído |
| **02** | **Jogo de Dados** | Jogo de dados interativo para 2 jogadores disputado em 5 rodadas com sorteio dinâmico, soma, verificação automática de vencedor e vitória instantânea com 3 vitórias. | `components/ex02/Dado.jsx`<br/>`components/ex02/Jogador.jsx`<br/>`components/ex02/JogoDados.jsx`<br/>`app/jogo-dados/page.jsx` | [🎲 Acessar Jogo de Dados](https://front-end-2026-2.vercel.app/jogo-dados) | Concluído |
| **03** | **Integração Back4App** | Criação de App no Back4App com entidade remota e aplicação Next.js integrada para criação e listagem de registros. | `lib/api.js`<br/>`app/page.js` | Em desenvolvimento | ⏳ Em andamento |

---

## 🧩 Atividade 01 — MiniBio & Card de Perfil

### 📋 Especificação da Aula (Quadro de Aula)

<div align="center">
  <img src="assets/aulas/01-minibio-quadro.jpg" alt="Quadro da Aula - Especificação MiniBio" width="460" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
</div>

```text
react-01
├── app/
│   └── page.js          # Importa e exibe a MiniBio
└── components/
    ├── Profile.js       # Card interno: Foto de perfil + Selo + Nome
    └── MiniBio.js       # Card externo: <Profile /> + Frase personalizada
```

### 📱 Preview do Componente em Execução

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <strong>Estrutura de Elementos</strong><br/><br/>
        <img src="public/profile.png" width="90" style="border-radius: 50%;" />&nbsp;&nbsp;
        <img src="public/santa_logo.png" width="40" /><br/><br/>
        <code>components/Profile.js</code>
      </td>
      <td align="center" width="50%">
        <strong>Resultado Final Renderizado</strong><br/><br/>
        <img src="assets/docs/minibio-preview.png" alt="Card MiniBio em Execução" width="220" style="border-radius: 12px; box-shadow: 0 6px 18px rgba(0,0,0,0.4);" /><br/><br/>
        <code>components/MiniBio.js</code>
      </td>
    </tr>
  </table>
</div>

---

## 🎲 Atividade 02 — Jogo de Dados

### 📋 Especificação da Aula (Quadro de Aula)

<div align="center">
  <img src="assets/aulas/02-jogo-de-dados-quadro.png" alt="Quadro da Aula - Jogo de Dados" width="460" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
</div>

```text
jogo-dados
├── app/
│   └── jogo-dados/
│       └── page.jsx     # Rota da página: /jogo-dados
├── components/
│   └── ex02/
│       ├── Dado.jsx     # Renderiza a imagem do dado conforme a prop `valor` (1 a 6)
│       ├── Jogador.jsx  # Coluna do jogador: Título + Vitórias + 2 Dados + Botão
│       └── JogoDados.jsx# Tabuleiro completo: Gerenciador de estados, rodadas e placar
└── public/
    └── dados/           # Imagens transparentes dos dados (dado1.png a dado6.png)
```

### 📱 Preview do Componente em Execução

<div align="center">
  <table>
    <tr>
      <td align="center" width="50%">
        <strong>Assets dos Dados</strong><br/><br/>
        <img src="public/dados/dado1.png" width="45" />&nbsp;
        <img src="public/dados/dado2.png" width="45" />&nbsp;
        <img src="public/dados/dado3.png" width="45" /><br/><br/>
        <img src="public/dados/dado4.png" width="45" />&nbsp;
        <img src="public/dados/dado5.png" width="45" />&nbsp;
        <img src="public/dados/dado6.png" width="45" /><br/><br/>
        <code>public/dados/dado[1-6].png</code>
      </td>
      <td align="center" width="50%">
        <strong>Resultado Final Renderizado</strong><br/><br/>
        <img src="assets/docs/jogo-dados-preview.png" alt="Jogo de Dados em Execução" width="300" style="border-radius: 14px; box-shadow: 0 6px 18px rgba(0,0,0,0.4);" /><br/><br/>
        <code>components/ex02/JogoDados.jsx</code>
      </td>
    </tr>
  </table>
</div>

- **Dinâmica do Jogo**:
  - Partida disputada entre **2 Jogadores** (`Jogador 1` e `Jogador 2`).
  - Cada rodada sorteia 2 dados para cada jogador, vencendo quem tiver a **maior soma**.
  - **Alternância de Turnos:** Apenas um botão fica habilitado por vez.
  - **Vitória Instantânea:** Se qualquer um dos jogadores atingir **3 vitórias**, a partida é finalizada na hora!
  - Ao final das 5 rodadas (ou após 3 vitórias), exibe o resultado geral e o botão **"Jogar Novamente"** para reiniciar a partida.

---


---

---

## 🎬 Atividade 03 - Integração com Back4App

### 📋 Especificação da Aula (Quadro de Aula)

<div align="center">
  <img src="assets/aulas/03-back4app-quadro.png" alt="Quadro da Aula - Especificação Back4App" width="460" style="border-radius: 12px; box-shadow: 0 4px 12px rgba(0,0,0,0.15);" />
</div>

```text
Exercício:
- Crie um App no Back4App
  - Crie uma entidade
- Crie um App Next que:
  - Crie e liste entidades do Back4App
```


---

## 🛠️ Tecnologias Utilizadas

- **[Next.js 16 (Turbopack)](https://nextjs.org/)** — Framework React com suporte a App Router e renderização de alta performance.
- **[React 19](https://react.dev/)** — Biblioteca para criação de interfaces baseadas em componentes.
- **[CSS Moderno](https://developer.mozilla.org/pt-BR/docs/Web/CSS)** — Estilização modular com Dark Theme e flexbox.
- **[Vercel](https://vercel.com/)** — Plataforma de deploy e hospedagem contínua (CI/CD).

---

## 🚀 Como Executar Localmente

### Pré-requisitos
- **Node.js** (versão 18+)
- **npm**, **yarn** ou **pnpm**

### Comandos:

```bash
# 1. Clone o repositório
git clone https://github.com/Richdssz/Front-end-2026.2.git

# 2. Acesse a pasta do projeto
cd Front-end-2026.2

# 3. Instale as dependências
npm install

# 4. Inicie o servidor de desenvolvimento
npm run dev
```

Abra [http://localhost:3000](http://localhost:3000) no seu navegador para visualizar.

---

## ☁️ Deploy na Vercel

O projeto está configurado para deploy imediato na **Vercel**:

1. Acesse [vercel.com](https://vercel.com/) e faça login com a conta GitHub.
2. Importe o repositório `Richdssz/Front-end-2026.2`.
3. Mantenha as configurações padrão (Framework: **Next.js**, Root Directory: `./`).
4. Clique em **Deploy**.

---

<div align="center">
  <!-- Logo Circular Oficial UNICAP com Link para o Portal -->
  <a href="https://portal.unicap.br" target="_blank" rel="noopener noreferrer">
    <img src="assets/docs/unicap-logo.png" alt="Logo Oficial UNICAP" width="55" style="border-radius: 50%; box-shadow: 0 2px 8px rgba(0,0,0,0.15);" />
  </a>
  <br/><br/>
  <p><a href="https://portal.unicap.br" target="_blank" rel="noopener noreferrer"><strong>Universidade Católica de Pernambuco (UNICAP)</strong></a> • 2026.2</p>
  <p>Desenvolvido por <a href="https://github.com/Richdssz" target="_blank" rel="noopener noreferrer"><strong>Richard Silva</strong></a> • Orientação: <a href="https://marciobueno.com/" target="_blank" rel="noopener noreferrer"><strong>Prof. Márcio Bueno</strong></a></p>
</div>
