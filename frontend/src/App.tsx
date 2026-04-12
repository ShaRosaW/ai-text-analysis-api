import { useState } from 'react';
import './index.css';

import { TextForm } from './components/TextForm';
import { ResultCard } from './components/ResultCard';

type AnalysisResponse = {
  summary: string;
  keywords: string[];
  action_items: string[];
};

function App() {
  const [result, setResult] = useState<AnalysisResponse | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleAnalyze = async (text: string) => {
    setLoading(true);
    setError('');
    setResult(null);

    try {
      const apiUrl = import.meta.env.VITE_API_URL;
      const response = await fetch(`${apiUrl}/analyze`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ text }),
      });

      if (!response.ok) {
        throw new Error('Failed to analyze text.');
      }

      const data: AnalysisResponse = await response.json();
      setResult(data);
    } catch (err) {
      setError('Something went wrong while analyzing the text.');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className='app'>
      <div className='container'>
        <header className='hero'>
          <p className='eyebrow'>FastAPI + React + TypeScript</p>
          <h1>AI Text Analysis</h1>
          <p className='subtitle'>
            Submit text and receive a structured analysis with a summary,
            keywords, and action items.
          </p>
        </header>

        <section className='panel'>
          <TextForm onSubmit={handleAnalyze} loading={loading} />
        </section>

        {error && <p className='error'>{error}</p>}

        {!result && !error && !loading && (
          <section className='empty-state'>
            <p>Enter text above and run an analysis to see the results here.</p>
          </section>
        )}

        {result && (
          <section className='results'>
            <ResultCard title='Summary'>
              <p>{result.summary}</p>
            </ResultCard>

            <ResultCard title='Keywords'>
              <ul>
                {result.keywords.map((keyword, index) => (
                  <li key={index}>{keyword}</li>
                ))}
              </ul>
            </ResultCard>

            <ResultCard title='Action Items'>
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
