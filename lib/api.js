import axios from "axios";

// 1. Criamos uma instância do Axios já pré-configurada
export const api = axios.create({
  baseURL: "https://parseapi.back4app.com/classes",
  headers: {
    "X-Parse-Application-Id": process.env.NEXT_PUBLIC_PARSE_APPLICATION_ID || "",
    // Usamos a REST API Key (ou a JavaScript Key caso seu app esteja aceitando para REST)
    "X-Parse-REST-API-Key": process.env.NEXT_PUBLIC_PARSE_REST_API_KEY || process.env.NEXT_PUBLIC_PARSE_JAVASCRIPT_KEY || "",
    "Content-Type": "application/json",
  },
});
