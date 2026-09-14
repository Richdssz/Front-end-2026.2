export default function Dado({ valor }) {
    return (
        <img
            src={`/dados/dado${valor}.png`}
            alt={`Dado ${valor}`}
            width={80}
            height={80}
        />
    );
}