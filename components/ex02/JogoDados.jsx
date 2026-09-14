"use client";

import { useState } from "react";
import Jogador from "./Jogador";

export default function JogoDados() {
    // 1. Estados dos Dados (começam valendo 1, por exemplo)
    const [dado1J1, setDado1J1] = useState(6);
    const [dado2J1, setDado2J1] = useState(6);
    const [dado1J2, setDado1J2] = useState(6);
    const [dado2J2, setDado2J2] = useState(6);

    // 2. Estados do Fluxo da Partida
    const [rodada, setRodada] = useState(1);
    const [vezDoJogador1, setVezDoJogador1] = useState(true);
    const [mensagem, setMensagem] = useState("Vez do Jogador 1");

    // 3. Placar Acumulado de Vitórias
    const [vitoriasJ1, setVitoriasJ1] = useState(0);
    const [vitoriasJ2, setVitoriasJ2] = useState(0);
    const [fimDeJogo, setFimDeJogo] = useState(false);

    // Função utilitária para sortear de 1 a 6
    function sortearDado() {
        return Math.floor(Math.random() * 6) + 1;
    }

    // Ação do Jogador 1
    function jogarJogador1() {
        const d1 = sortearDado();
        const d2 = sortearDado();

        setDado1J1(d1);
        setDado2J1(d2);

        // Passa a vez para o Jogador 2
        setVezDoJogador1(false);
        setMensagem("Vez do Jogador 2");
    }

    // Ação do Jogador 2 (Aqui fecha a rodada!)
    function jogarJogador2() {
        const d1 = sortearDado();
        const d2 = sortearDado();

        setDado1J2(d1);
        setDado2J2(d2);

        // Calcula a soma de cada um nesta rodada
        const somaJ1 = dado1J1 + dado2J1;
        const somaJ2 = d1 + d2;

        let novasVitoriasJ1 = vitoriasJ1;
        let novasVitoriasJ2 = vitoriasJ2;

        // Compara quem ganhou a rodada
        if (somaJ1 > somaJ2) {
            novasVitoriasJ1++;
            setVitoriasJ1(novasVitoriasJ1);
            setMensagem("Jogador 1 venceu a rodada");
        } else if (somaJ2 > somaJ1) {
            novasVitoriasJ2++;
            setVitoriasJ2(novasVitoriasJ2);
            setMensagem("Jogador 2 venceu a rodada");
        } else {
            setMensagem("Empate nesta rodada");
        }

        // Regra de Vitória Instantânea: se alguém atingir 3 vitórias, ganha na hora!
        if (novasVitoriasJ1 === 3) {
            setFimDeJogo(true);
            setMensagem("Jogador 1 venceu o jogo (3 vitórias)!");
        } else if (novasVitoriasJ2 === 3) {
            setFimDeJogo(true);
            setMensagem("Jogador 2 venceu o jogo (3 vitórias)!");
        } else if (rodada === 5) {
            // Se chegou na 5ª rodada sem ninguém bater 3
            setFimDeJogo(true);

            if (novasVitoriasJ1 > novasVitoriasJ2) {
                setMensagem("Jogador 1 venceu o jogo!");
            } else if (novasVitoriasJ2 > novasVitoriasJ1) {
                setMensagem("Jogador 2 venceu o jogo!");
            } else {
                setMensagem("Empate geral!");
            }
        } else {
            // Continua para a próxima rodada
            setRodada(rodada + 1);
            setVezDoJogador1(true);
        }
    }

    // Função de Reiniciar (botão "Jogar Novamente")
    function reiniciarJogo() {
        setDado1J1(1);
        setDado2J1(1);
        setDado1J2(1);
        setDado2J2(1);
        setRodada(1);
        setVitoriasJ1(0);
        setVitoriasJ2(0);
        setVezDoJogador1(true);
        setFimDeJogo(false);
        setMensagem("Vez do Jogador 1");
    }

    return (
        <div className="jogo-container">
            <h1 className="jogo-titulo">Jogo de Dados</h1>
            <span className="jogo-rodada">Rodada {rodada}/5</span>

            {/* As duas colunas com o componente Jogador */}
            <div className="jogadores-grid">
                <Jogador
                    nome="Jogador 1"
                    vitorias={vitoriasJ1}
                    dado1={dado1J1}
                    dado2={dado2J1}
                    onJogar={jogarJogador1}
                    desabilitado={!vezDoJogador1 || fimDeJogo}
                />

                <Jogador
                    nome="Jogador 2"
                    vitorias={vitoriasJ2}
                    dado1={dado1J2}
                    dado2={dado2J2}
                    onJogar={jogarJogador2}
                    desabilitado={vezDoJogador1 || fimDeJogo}
                />
            </div>

            {/* Mensagem central */}
            <div className="mensagem-box">
                <p className="mensagem-texto">{mensagem}</p>
            </div>

            {/* Botão só aparece quando o jogo terminar (rodada 5 concluída) */}
            {fimDeJogo && (
                <button className="btn-reiniciar" onClick={reiniciarJogo}>
                    Jogar Novamente
                </button>
            )}
        </div>
    );
}
