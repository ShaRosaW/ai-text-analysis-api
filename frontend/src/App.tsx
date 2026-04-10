import { useState } from "react";
import "./index.css";

type AnalysisResponse = {
  summary: string;
  keywords: string[];
  action_items: string[];
};

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState<AnalysisResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e: React.SyntheticEvent<HTMLFormElement, SubmitEvent>) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
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
        <p className="subtitle">
          A simple React frontend connected to a FastAPI backend.
        </p>

        <form onSubmit={handleSubmit} className="form">
          <label htmlFor="text">Input text</label>
          <textarea
            id="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            placeholder="Paste or type text here..."
            rows={10}
          />

          <button type="submit" disabled={loading || !text.trim()}>
            {loading ? "Analyzing..." : "Analyze"}
          </button>
        </form>

        {error && <p className="error">{error}</p>}

        {result && (
          <section className="results">
            <div className="card">
              <h2>Summary</h2>
              <p>{result.summary}</p>
            </div>

            <div className="card">
              <h2>Keywords</h2>
              <ul>
                {result.keywords.map((keyword, index) => (
                  <li key={index}>{keyword}</li>
                ))}
              </ul>
            </div>

            <div className="card">
              <h2>Action Items</h2>
              <ul>
                {result.action_items.map((item, index) => (
                  <li key={index}>{item}</li>
                ))}
              </ul>
            </div>
          </section>
        )}
      </div>
    </main>
  );
}

export default App;
