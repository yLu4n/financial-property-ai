import { useState } from "react";
import FinancialForm from "./components/FinancialForm";
import ResultDisplay from "./components/ResultDisplay";
import { runAnalysis } from "./services/api";

function App() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalysis = async (payload) => {
    setLoading(true);
    try {
      const data = await runAnalysis(payload);
      setResult(data);
    } catch (error) {
      console.error(error);
    }
    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
      <h1>Financial Property Analysis</h1>

      <FinancialForm onSubmit={handleAnalysis} loading={loading} />
      <ResultDisplay result={result} />
    </div>
  );
}

export default App;