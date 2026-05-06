import { useState } from "react";
import axios from "axios";

function App() {
  const [formData, setFormData] = useState({
    salario_bruto: 9000,
    outras_rendas: 0,
    despesas_fixas: 3000,
    despesas_variaveis: 1500,
    reserva_emergencia: 30000,
    dividas_atuais: 2000,
    property_value: 500000,
    monthly_rent: 2500
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: Number(e.target.value)
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      const response = await axios.post(
        "http://127.0.0.1:8000/analysis",
        {
          financial_data: {
            salario_bruto: formData.salario_bruto,
            outras_rendas: formData.outras_rendas,
            despesas_fixas: formData.despesas_fixas,
            despesas_variaveis: formData.despesas_variaveis,
            reserva_emergencia: formData.reserva_emergencia,
            dividas_atuais: formData.dividas_atuais
          },
          property_value: formData.property_value,
          monthly_rent: formData.monthly_rent
        }
      );

      setResult(response.data.data);
    } catch (error) {
      console.error("Erro na requisição:", error);
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Financial Property Analysis</h1>

      <form onSubmit={handleSubmit}>
        {Object.keys(formData).map((key) => (
          <div key={key} style={{ marginBottom: "10px" }}>
            <label>{key}</label>
            <input
              type="number"
              name={key}
              value={formData[key]}
              onChange={handleChange}
              style={{ marginLeft: "10px" }}
            />
          </div>
        ))}

        <button type="submit">
          {loading ? "Analyzing..." : "Analyze"}
        </button>
      </form>

      {result && (
        <div style={{ marginTop: "2rem" }}>
          <h2>Result:</h2>
          <pre>{JSON.stringify(result, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;