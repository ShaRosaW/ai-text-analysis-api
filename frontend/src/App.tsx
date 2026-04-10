import { useState } from "react";
import "./index.css";

import { TextForm } from "./components/TextForm";
import { ResultCard } from "./components/ResultCard";

type AnalysisResponse = {
  summary: string;
  keywords: string[];
  action_items: string[];
};

function App() {
  const API_URL = import.meta.env.VITE_API_URL;
  const [result, setResult] = useState<AnalysisResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleAnalyze = async (text: string) => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(`${API_URL}/analyze`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error("Failed to analyze text.");
      }

      const data: AnalysisResponse = await response.json();
      setResult(data);
    } catch (err) {
      setError("Something went wrong while analyzing the text.");
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="app">
      <div className="container">
        <h1>AI Text Analysis</h1>
        <TextForm onSubmit={handleAnalyze} loading={loading} />

        {error && <p className="error">{error}</p>}

        {result && (
          <section className="results">
            <ResultCard title="Summary">
              <p>{result.summary}</p>
            </ResultCard>

            <ResultCard title="Keywords">
              <ul>
                {result.keywords.map((keyword, index) => (
                  <li key={index}>{keyword}</li>
                ))}
              </ul>
            </ResultCard>

            <ResultCard title="Action Items">
              <ul>
                {result.action_items.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </ResultCard>
          </section>
        )}
      </div>
    </main>
  );
}

export default App;
