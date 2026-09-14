import Dado from "./Dado";

export default function Jogador({ nome, vitorias, dado1, dado2, onJogar, desabilitado }) {
    return (
        <div className="jogador-card">
            <h2 className="jogador-nome">{nome}</h2>
            <span className="jogador-vitorias">Vitórias: {vitorias}</span>

            <div className="dados-dupla">
                <Dado valor={dado1} />
                <Dado valor={dado2} />
            </div>

            <button 
                className="btn-jogar" 
                onClick={onJogar} 
                disabled={desabilitado}
            >
                Jogar
            </button>
        </div>
    );
}
