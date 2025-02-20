import React, { useState } from "react";

function App() {
  const [dados, setDados] = useState(null);

  const respostaAPI = async () => {
    try {
      const response = await fetch(
        "https://sistema-atendimento-api-production.up.railway.app/api/webhook/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMDgwMDcwLCJpYXQiOjE3Mzk5OTM2NzAsImp0aSI6IjdjNjFlYTE4NTkxMzQ4MmRiNmU0MzgxMGNhOGJjN2RhIiwidXNlcl9pZCI6MX0.SlBV2W49II81a3o_rQa9JyU5t8PDpKUhOOwVTsEage0"
          },
          body: JSON.stringify({
            usuario: "carlos",
            mensagem: "Meus pedidos"
          })
        }
      );

      if (!response.ok) {
        throw new Error(`Erro na requisição: ${response.status}`);
      }

      const data = await response.json();
      setDados(data);
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
      setDados({ erro: error.message });
    }
  };

  const enviarWebhook = async () => {
    try {
      const response = await fetch(
        "https://sistema-atendimento-api-production.up.railway.app/api/enviar-webhook/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQwMDgwMDcwLCJpYXQiOjE3Mzk5OTM2NzAsImp0aSI6IjdjNjFlYTE4NTkxMzQ4MmRiNmU0MzgxMGNhOGJjN2RhIiwidXNlcl9pZCI6MX0.SlBV2W49II81a3o_rQa9JyU5t8PDpKUhOOwVTsEage0"
          },
        }
      );

      if (!response.ok) {
        throw new Error(`Erro na envio: ${response.status}`);
      }

      const data = await response.json();
      setDados(data);
    } catch (error) {
      console.error("Erro ao buscar dados:", error);
      setDados({ erro: error.message });
    }
  };

  return (
    <div>
      <h1>Minha API Django</h1>
      <button onClick={respostaAPI}>Solicitar resposta a API</button>
      <pre>{JSON.stringify(dados, null, 2)}</pre>
      <button onClick={enviarWebhook}>Enviar Webhook</button>
      <pre>{JSON.stringify(dados, null, 2)}</pre>
    </div>
  );
}

export default App;