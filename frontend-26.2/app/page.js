import styles from "./page.module.css";

export default function Home() {
  console.log("Teste teste");
  return (
    <div className={styles.page}>
      <main className={styles.main}> Olá, turma!</main>
    </div>
  );
}
