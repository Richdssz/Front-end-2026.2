import Link from "next/link";
import MiniBio from "../components/MiniBio.js";

export default function Home() {
  return (
    <div className="container-pagina">
      <div style={{ marginBottom: "20px", display: "flex", gap: "15px" }}>
        <Link href="/" style={{ color: "#0070f3", textDecoration: "underline" }}>Atividade 01 (MiniBio)</Link>
        <Link href="/jogo-dados" style={{ color: "#0070f3", textDecoration: "underline" }}>Atividade 02 (Jogo de Dados)</Link>
      </div>
      <MiniBio />
    </div>
  );
}
