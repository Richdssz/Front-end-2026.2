# -*- coding: utf-8 -*-
import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#718096"))
        
        # Header (pages > 1)
        if self._pageNumber > 1:
            self.drawString(54, 750, "CineVault - Guia Técnico & Conceitual: Java vs TypeScript/Next.js")
            self.setStrokeColor(colors.HexColor("#E2E8F0"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
        
        # Footer
        text = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(558, 36, text)
        self.drawString(54, 36, "Locadora CineVault | UNICAP - POO, Camadas, Async e Persistência")
        self.setStrokeColor(colors.HexColor("#E2E8F0"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()

def build_pdf(filename="GUIA_COMPLETO_CRUD_ASYNC_JAVA_JS.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=letter,
        leftMargin=54,
        rightMargin=54,
        topMargin=54,
        bottomMargin=54
    )
    
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=22,
        leading=26,
        textColor=colors.HexColor("#1A202C"),
        spaceAfter=6
    )
    
    subtitle_style = ParagraphStyle(
        'DocSubtitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#4A5568"),
        spaceAfter=15
    )
    
    h1_style = ParagraphStyle(
        'H1',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=15,
        leading=19,
        textColor=colors.HexColor("#2B6CB0"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True
    )
    
    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=16,
        textColor=colors.HexColor("#2D3748"),
        spaceBefore=10,
        spaceAfter=4,
        keepWithNext=True
    )
    
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=14,
        textColor=colors.HexColor("#2D3748"),
        spaceAfter=6
    )
    
    body_bold = ParagraphStyle(
        'BodyBold',
        parent=body_style,
        fontName='Helvetica-Bold'
    )
    
    callout_style = ParagraphStyle(
        'Callout',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=13.5,
        textColor=colors.HexColor("#2C5282")
    )
    
    code_style = ParagraphStyle(
        'CodeText',
        parent=styles['Normal'],
        fontName='Courier',
        fontSize=8,
        leading=10.5,
        textColor=colors.HexColor("#1A202C")
    )
    
    code_header = ParagraphStyle(
        'CodeHeader',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor("#FFFFFF")
    )

    story = []

    def make_code_box(code_text, lang_title, bg_header="#2B6CB0"):
        escaped = code_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br/>').replace(' ', '&nbsp;')
        t = Table([
            [Paragraph(lang_title, code_header)],
            [Paragraph(escaped, code_style)]
        ], colWidths=[504])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (0, 0), colors.HexColor(bg_header)),
            ('PADDING', (0, 0), (0, 0), 4),
            ('BACKGROUND', (0, 1), (0, 1), colors.HexColor("#F7FAFC")),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor("#CBD5E0")),
            ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
            ('TOPPADDING', (0, 1), (0, 1), 6),
            ('BOTTOMPADDING', (0, 1), (0, 1), 6),
            ('LEFTPADDING', (0, 1), (0, 1), 8),
            ('RIGHTPADDING', (0, 1), (0, 1), 8),
        ]))
        return t

    def make_callout(text, bg="#EBF8FF", border="#3182CE"):
        t = Table([[Paragraph(text, callout_style)]], colWidths=[504])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.HexColor(bg)),
            ('BOX', (0, 0), (-1, -1), 1, colors.HexColor(border)),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('RIGHTPADDING', (0, 0), (-1, -1), 10),
        ]))
        return t

    # CAPA / CABEÇALHO
    story.append(Paragraph("🎬 CineVault: Guia Rápido & Prático", title_style))
    story.append(Paragraph("Do Java (POO / Camadas) ao TypeScript / Next.js: Async, API Externa e Banco Back4App", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#3182CE"), spaceBefore=0, spaceAfter=12))

    story.append(Paragraph("1. O Mapa Geral do Fluxo (Ciclo de Vida dos Dados)", h1_style))
    story.append(Paragraph(
        "Em um sistema de locadora moderno, o usuário não precisa digitar manualmente nome, diretor, gênero e ano de cada filme. O ciclo de dados divide-se em 3 etapas claras:",
        body_style
    ))

    # Tabela com as 3 etapas
    tabela_etapas = Table([
        [Paragraph("Etapa", body_bold), Paragraph("O que acontece", body_bold), Paragraph("Tecnologia Envolvida", body_bold)],
        [
            Paragraph("<b>1. Busca na API</b>", body_style),
            Paragraph("Usuário digita 'Matrix'. O app consulta a base global de filmes (OMDb) e traz todos os metadados prontos em JSON.", body_style),
            Paragraph("HTTP GET / fetch assíncrono (OMDb API)", code_style)
        ],
        [
            Paragraph("<b>2. Cadastro no Banco</b>", body_style),
            Paragraph("Com os dados preenchidos da API, o usuário confirma o cadastro. O filme é salvo no banco de dados da locadora com status 'DISPONÍVEL'.", body_style),
            Paragraph("SDK Back4App / Parse Server (POST/save)", code_style)
        ],
        [
            Paragraph("<b>3. Consulta / Listagem</b>", body_style),
            Paragraph("A locadora recupera os filmes cadastrados para montar a vitrine e gerenciar locações / devoluções.", body_style),
            Paragraph("Parse Query / find() -> Tabela/Grid na tela", code_style)
        ]
    ], colWidths=[110, 240, 154])
    tabela_etapas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#EDF2F7")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tabela_etapas)
    story.append(Spacer(1, 14))

    # PARTE 2: ASYNC NO JAVA vs JAVASCRIPT
    story.append(Paragraph("2. O que é 'Async'? O Choque Java vs JavaScript", h1_style))
    story.append(Paragraph(
        "<b>Por que precisamos de assincronismo?</b> Quando seu código pede algo pela rede (internet) ou para um banco de dados remoto, a resposta demora centenas de milissegundos. Se o código travasse esperando (síncrono bloqueante), o programa ou a aba do navegador congelaria por completo.",
        body_style
    ))
    story.append(make_callout(
        "<b>Analogia do Restaurante:</b><br/>"
        "• <b>Síncrono (Ruim):</b> O garçom anota seu pedido e fica parado olhando a cozinha cozinhar até o prato sair. Ele não atende nenhuma outra mesa.<br/>"
        "• <b>Assíncrono (Ideal):</b> O garçom passa o pedido à cozinha, te dá uma comanda (<b>Promise</b> / <b>CompletableFuture</b>) e continua atendendo outras mesas. Quando a cozinha avisa que o prato está pronto, ele te entrega."
    ))
    story.append(Spacer(1, 10))

    story.append(Paragraph("A Comparação de Código: Como pedir dados sem travar", h2_style))

    codigo_java_async = """// Em Java (HttpClient nativo assíncrono com CompletableFuture):
public CompletableFuture<String> buscarFilmeAsync(String titulo) {
    HttpClient client = HttpClient.newHttpClient();
    HttpRequest request = HttpRequest.newBuilder()
        .uri(URI.create("https://www.omdbapi.com/?t=" + titulo + "&apikey=CHAVE"))
        .GET()
        .build();

    // sendAsync envia em thread secundária, NÃO trava a thread principal!
    return client.sendAsync(request, HttpResponse.BodyHandlers.ofString())
        .thenApply(HttpResponse::body); // Extrai o corpo quando chegar
}

// O que cada função faz:
// 1. HttpClient.newHttpClient(): Instancia o cliente HTTP do Java.
// 2. client.sendAsync(...): Dispara a requisição em background e retorna uma promessa futura (CompletableFuture).
// 3. thenApply(...): Callback acionado assim que a resposta da rede chega."""

    story.append(make_code_box(codigo_java_async, "Java: Requisição Assíncrona (CompletableFuture)", "#805AD5"))
    story.append(Spacer(1, 8))

    codigo_js_async = """// Em TypeScript / JavaScript (async / await nativo):
async function buscarFilmeAsync(titulo: string): Promise<any> {
    // 1. O 'await' pausa ESTA FUNÇÃO até a rede responder, mas NÃO trava o navegador
    const resposta = await fetch(`https://www.omdbapi.com/?t=${titulo}&apikey=CHAVE`);
    
    // 2. Extrai e converte o JSON que veio no corpo da resposta
    const dados = await resposta.json();
    
    return dados;
}

// O que cada função/palavra faz:
// 1. async: Declara que a função retorna uma Promise (equivalente ao CompletableFuture do Java).
// 2. fetch(): Faz o GET HTTP nativo do navegador/Node.
// 3. await: Suspende a execução da linha até a Promise resolver, entregando o resultado limpo."""

    story.append(make_code_box(codigo_js_async, "JavaScript / TypeScript: async / await", "#2B6CB0"))
    
    story.append(PageBreak())

    # PARTE 3: ARQUITETURA EM CAMADAS (JAVA vs CINEVAULT)
    story.append(Paragraph("3. Arquitetura em Camadas: Você já conhece isso do Java!", h1_style))
    story.append(Paragraph(
        "Se você está aprendendo Camadas em Java, observe como o projeto da locadora CineVault em Next.js usa <b>exatamente os mesmos conceitos</b> com nomes ligeiramente diferentes:",
        body_style
    ))

    tabela_camadas = Table([
        [Paragraph("Camada", body_bold), Paragraph("No Java", body_bold), Paragraph("No CineVault (Next.js)", body_bold), Paragraph("Responsabilidade", body_bold)],
        [
            Paragraph("<b>Modelo (Entidade)</b>", body_style),
            Paragraph("<code>Filme.java</code> (Classe com atributos e getters/setters)", code_style),
            Paragraph("<code>types/movie.ts</code> (Interface TypeScript)", code_style),
            Paragraph("Define a estrutura de dados: titulo, diretor, ano, status.", body_style)
        ],
        [
            Paragraph("<b>Persistência (DAO/Repo)</b>", body_style),
            Paragraph("<code>FilmeDAO.java</code> ou <code>FilmeRepository.java</code>", code_style),
            Paragraph("<code>services/parseMovieService.ts</code>", code_style),
            Paragraph("Quem fala com o banco: faz save(), find(), delete().", body_style)
        ],
        [
            Paragraph("<b>Integração Externa</b>", body_style),
            Paragraph("<code>OmdbClientService.java</code>", code_style),
            Paragraph("<code>services/omdbService.ts</code>", code_style),
            Paragraph("Quem busca filmes na internet com fetch().", body_style)
        ],
        [
            Paragraph("<b>Apresentação (UI)</b>", body_style),
            Paragraph("JSP / Swing / Thymeleaf", code_style),
            Paragraph("Componente React (<code>page.tsx</code>)", code_style),
            Paragraph("O formulário com botão e a tabela na tela.", body_style)
        ]
    ], colWidths=[95, 125, 135, 149])
    tabela_camadas.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor("#EDF2F7")),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor("#CBD5E0")),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 5),
        ('RIGHTPADDING', (0, 0), (-1, -1), 5),
    ]))
    story.append(tabela_camadas)
    story.append(Spacer(1, 14))

    # PARTE 4: CÓDIGOS COMPLETOS DAS OPERAÇÕES DO CRUD
    story.append(Paragraph("4. Código Detalhado: As 3 Operações Principais", h1_style))
    story.append(Paragraph(
        "Abaixo estão os blocos essenciais de código que você precisa entender para a entrega do seu projeto.",
        body_style
    ))

    # OPERAÇÃO 1: BUSCA NA API DO OMDB
    story.append(Paragraph("Operação 1: Buscar Filme na API Externa (OMDb)", h2_style))
    code_op1 = """// src/services/omdbService.ts
export async function buscarFilmeNoOMDb(titulo: string) {
    const chave = process.env.NEXT_PUBLIC_OMDB_API_KEY;
    const url = `https://www.omdbapi.com/?apikey=${chave}&t=${encodeURIComponent(titulo)}`;

    const res = await fetch(url);
    const dados = await res.json();

    if (dados.Response === "False") {
        throw new Error(dados.Error || "Filme não encontrado no OMDb.");
    }

    // Retorna um objeto limpo e adaptado para a nossa locadora:
    return {
        title: dados.Title,
        director: dados.Director,
        year: parseInt(dados.Year),
        genre: dados.Genre,
        posterUrl: dados.Poster !== "N/A" ? dados.Poster : "",
        synopsis: dados.Plot
    };
}

// O QUE FAZ:
// - encodeURIComponent: Limpa espaços e acentos no nome para a URL não quebrar.
// - fetch(): Dispara a requisição GET assíncrona.
// - dados.Response === 'False': A OMDb responde 200 OK mesmo quando não acha o filme,
//   avisando com esse campo se encontrou ou não."""
    story.append(make_code_box(code_op1, "TypeScript: omdbService.ts", "#2B6CB0"))
    story.append(Spacer(1, 10))

    # OPERAÇÃO 2: SALVAR NO BANCO BACK4APP
    story.append(Paragraph("Operação 2: Cadastrar Filme no Banco de Dados (Back4App)", h2_style))
    code_op2 = """// src/services/parseMovieService.ts
import Parse from "@/lib/parseClient";

export async function cadastrarFilme(dadosFilme: any) {
    // 1. Cria uma nova instância da classe 'Movie' no Back4App (como dar 'new Movie()' em Java)
    const Movie = Parse.Object.extend("Movie");
    const novoFilme = new Movie();

    // 2. Preenche os campos (equivalente aos setters: filme.setTitulo(...))
    novoFilme.set("title", dadosFilme.title);
    novoFilme.set("director", dadosFilme.director);
    novoFilme.set("year", dadosFilme.year);
    novoFilme.set("genre", dadosFilme.genre);
    novoFilme.set("posterUrl", dadosFilme.posterUrl);
    novoFilme.set("status", "DISPONIVEL"); // Regra de negócio: todo filme nasce disponível

    // 3. Salva no banco de dados remoto de forma assíncrona
    const resultado = await novoFilme.save();
    return resultado.id; // Retorna o ID único gerado pelo banco
}

// O QUE FAZ:
// - Parse.Object.extend('Movie'): Mapeia a tabela 'Movie' no banco NoSQL do Parse.
// - novoFilme.set(campo, valor): Atribui as propriedades ao objeto.
// - novoFilme.save(): Envia um POST para o Back4App persistir o registro."""
    story.append(make_code_box(code_op2, "TypeScript: parseMovieService.ts - cadastrarFilme()", "#2B6CB0"))

    story.append(PageBreak())

    # OPERAÇÃO 3: LISTAR DO BANCO
    story.append(Paragraph("Operação 3: Buscar / Listar Filmes do Banco (Back4App)", h2_style))
    code_op3 = """// src/services/parseMovieService.ts
export async function listarFilmes() {
    // 1. Cria uma consulta para a classe 'Movie' (equivalente ao SELECT * FROM Movie no SQL)
    const Movie = Parse.Object.extend("Movie");
    const query = new Parse.Query(Movie);

    // 2. Ordena os mais recentes primeiro
    query.descending("createdAt");

    // 3. Executa a busca assíncrona no banco de dados
    const resultados = await query.find();

    // 4. Converte os objetos Parse em um array JSON limpo para a tela
    return resultados.map(filme => ({
        id: filme.id,
        title: filme.get("title"),
        director: filme.get("director"),
        year: filme.get("year"),
        genre: filme.get("genre"),
        posterUrl: filme.get("posterUrl"),
        status: filme.get("status")
    }));
}

// O QUE FAZ:
// - new Parse.Query(Movie): Cria o construtor de consulta (Query Builder).
// - query.descending('createdAt'): Adiciona ordenação (ORDER BY criado_em DESC).
// - query.find(): Executa a query remota no Back4App.
// - filme.get('campo'): Equivalente ao getter do Java (filme.getTitulo())."""
    story.append(make_code_box(code_op3, "TypeScript: parseMovieService.ts - listarFilmes()", "#2B6CB0"))
    story.append(Spacer(1, 12))

    # OPERAÇÃO 4: CONECTANDO TUDO NA VIEW (REACT)
    story.append(Paragraph("5. Como a Tela (React View) Conecta Tudo", h1_style))
    story.append(Paragraph(
        "Na interface do usuário, nós juntamos a busca da API com o cadastro no banco usando funções de clique (event handlers):",
        body_style
    ))

    code_react_view = """// Trecho dentro do componente React (src/app/page.tsx):
export default function CatalogoFilmes() {
    const [filmeBuscado, setFilmeBuscado] = useState(null);

    // PASSO A: Usuário clica em 'Buscar na API'
    async function handleBuscar(nomeDigitado: string) {
        const dados = await buscarFilmeNoOMDb(nomeDigitado);
        setFilmeBuscado(dados); // Mostra na tela para confirmação
    }

    // PASSO B: Usuário gostou e clica em 'Confirmar e Cadastrar na Locadora'
    async function handleCadastrar() {
        if (!filmeBuscado) return;
        await cadastrarFilme(filmeBuscado); // Salva no Back4App
        alert('Filme cadastrado com sucesso no banco!');
        carregarFilmesDoBanco(); // Atualiza a lista na tela
    }

    return (
        <div>
           {/* Inputs, botões e cards de filmes renderizados aqui */}
        </div>
    );
}"""
    story.append(make_code_box(code_react_view, "React / Next.js: Conexão dos Eventos na View", "#1A202C"))
    story.append(Spacer(1, 14))

    # RECAPITULAÇÃO EXPRESSA PARA APRENDER EM 1 DIA
    story.append(Paragraph("6. Resumo de Bolso para Defender seu Projeto", h1_style))
    story.append(make_callout(
        "<b>Se o professor ou colega perguntar:</b><br/>"
        "• <b>Por que usou async/await?</b> Porque chamadas de rede para a OMDb API e para o Back4App levam tempo. Com async/await, o código aguarda a resposta sem congelar a interface do usuário.<br/>"
        "• <b>Como organizou o código?</b> Em arquitetura de camadas: uma camada de Tipos (Model), uma camada de Serviços para o OMDb e Back4App (Repository/DAO) e a Camada de Interface em React (View).<br/>"
        "• <b>O que é o Back4App?</b> É um Backend as a Service (BaaS) baseado em Parse Server que substitui a necessidade de criar controllers manuais e SQL para CRUD simples, persistindo objetos diretamente.",
        bg="#FEFCBF",
        border="#D69E2E"
    ))

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF gerado com sucesso: {filename}")

if __name__ == "__main__":
    build_pdf()
