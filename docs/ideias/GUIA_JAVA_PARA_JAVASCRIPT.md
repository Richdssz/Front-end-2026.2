# ☕ Do Java Puro (POO Clássica) para o JavaScript/React: O Guia Definitivo

> Se você aprendeu **Java puro (Classes, Objetos, Métodos, Construtores, Encapsulamento, Coleções e SOLID)**, este guia traduz exatamente como cada um desses fundamentos funciona no **JavaScript ES6+** e no **React**, sem mágicas de frameworks de backend como Spring.

---

## 1. Tabela Comparativa Direta: Java Puro vs JavaScript

| Conceito em Java Puro | Equivalente em JavaScript (ES6+) | Explicação Prática |
| :--- | :--- | :--- |
| **Classe e Atributos** (`class Filme { private String nome; }`) | **Objetos Literais** (`{ nome: "Matrix" }`) ou `class` | No JS moderno usamos quase sempre objetos literais diretamente, pois são mais leves e não precisam de cerimônia. |
| **Getters e Setters** (`filme.getNome()`) | **Acesso Direto à Propriedade** (`filme.nome`) | Em JS os atributos dos objetos são públicos por padrão. Não há necessidade de criar getters/setters manuais a menos que haja regra de validação. |
| **Instanciação** (`Filme f = new Filme("Matrix");`) | **Objetos Literais ou Fábricas** (`const f = { nome: "Matrix" };`) | Você pode criar um objeto completo instantaneamente com chaves `{}`. |
| **`ArrayList<Filme>`** | **Array Dinâmico `[]`** (`const filmes = [];`) | No JS os arrays não têm tamanho fixo e aceitam métodos de manipulação diretamente. |
| **Sobrecarga de Métodos** (`void buscar(int id)`, `void buscar(String nome)`) | **Parâmetros Opcionais / Valores Padrão** | JS não suporta sobrecarga com mesmo nome de método; usamos parâmetros padrão (`(param = padrao)`) ou verificamos se é `undefined`. |
| **`NullPointerException`** | **`Cannot read property of undefined`** | O erro clássico de tentar acessar `objeto.atributo` quando `objeto` é `null` ou `undefined`. No JS usamos o Optional Chaining: `objeto?.atributo`. |
| **`System.out.println()`** | **`console.log()`** | Imprime valores no terminal ou no console do navegador (F12). |

---

## 2. Java Streams vs Métodos Funcionais de Array em JS

No Java 8+, quando você quer filtrar ou transformar uma `List<Filme>`, você faz:
```java
// Java Puro:
List<String> titulos = filmes.stream()
                             .filter(f -> f.getNota() >= 4.0)
                             .map(f -> f.getTitulo())
                             .collect(Collectors.toList());
```

No JavaScript, **o array já tem tudo isso nativo, sem precisar abrir stream ou chamar collect**:
```javascript
// JavaScript Puro:
const titulos = filmes
  .filter(f => f.nota >= 4.0)
  .map(f => f.titulo);
```

### Os 4 Métodos que Você Mais Vai Usar:

#### 1. `.map()` (Transformação 1 para 1)
Recebe uma lista de coisas e devolve uma nova lista do mesmo tamanho com os itens transformados:
```javascript
const numeros = [1, 2, 3];
const dobrados = numeros.map(n => n * 2); // [2, 4, 6]

// No React: transforma lista de dados em lista de elementos visuais (HTML):
const elementos = filmes.map(filme => <h2 key={filme.id}>{filme.titulo}</h2>);
```

#### 2. `.filter()` (Filtro booleano)
Cria um novo array contendo apenas os itens onde a função retorna `true`:
```javascript
const disponiveis = filmes.filter(f => f.status === "disponivel");
```

#### 3. `.find()` (Busca de um único item)
Equivalente ao `for` com `break` quando encontra o primeiro elemento:
```javascript
// Java: percorre com for e retorna o primeiro que tem id == 10
const matrix = filmes.find(f => f.id === 10);
```

#### 4. `.reduce()` (Acumulador)
Reduz um array inteiro a um único resultado (ex: somar todas as diárias):
```javascript
const totalPreco = filmes.reduce((soma, f) => soma + f.preco, 0);
```

---

## 3. O Que Substitui a POO Clássica no React?

No Java, a unidade básica de organização é a **Classe**.  
No React moderno, a unidade básica é a **Função (Componente Funcional)**:

### Java Puro (Orientado a Objetos):
```java
public class CardFilme {
    private String titulo;
    public CardFilme(String titulo) { this.titulo = titulo; }
    public void desenhar() {
        System.out.println("<div>" + this.titulo + "</div>");
    }
}
```

### React (Orientado a Funções):
```javascript
// Um componente é apenas uma função que recebe propriedades (props) e retorna HTML (JSX)
export function CardFilme({ titulo, ano, cartazUrl }) {
  return (
    <div className="card">
      <img src={cartazUrl} alt={titulo} />
      <h3>{titulo} ({ano})</h3>
    </div>
  );
}
```

---

## 4. SOLID e GRASP no JavaScript Sem Classes Monolíticas

Mesmo sem criar dezenas de `class`, os princípios continuam valendo 100%:

### 1. Responsabilidade Única (SRP - SOLID):
* Uma função ou arquivo deve ter apenas **uma razão para mudar**.
* `movieService.js`: Sabe apenas como se comunicar com o Back4App e salvar/listar filmes.
* `MovieCard.jsx`: Sabe apenas como exibir o card na tela. Não faz requisição HTTP!

### 2. Inversão de Dependência (DIP - SOLID) & Baixo Acoplamento (GRASP):
* Suas telas no React não chamam a API do Back4App diretamente.
* As telas chamam as funções abstratas de `movieService.js`:
  ```javascript
  // Na tela (page.js):
  import { listarFilmes } from "@/services/movieService";

  const filmes = await listarFilmes();
  ```
  Se amanhã você trocar o banco do Back4App por um arquivo JSON local ou banco MySQL, a tela **continua intacta**!

### 3. Especialista na Informação (GRASP):
* Quem conhece as regras de negócio de como um filme é formatado para a locadora é o módulo `adapters/movieAdapter.js`.
