import React, { useState } from 'react';
import PropagandaForm from './components/PropagandaForm';
import ResultsDisplay from './components/ResultsDisplay';
import LoadingSpinner from './components/LoadingSpinner';
import { analyzeContent } from './services/api';

interface AnalysisResult {
  propaganda_score: number;
  identified_techniques: string[];
  explanation: string;
}

function App() {
  const [loading, setLoading] = useState<boolean>(false);
  const [results, setResults] = useState<AnalysisResult | null>(null);
  const [error, setError] = useState<string | null>(null);

  const handleAnalyze = async (text: string, url: string) => {
    setLoading(true);
    setResults(null);
    setError(null);

    try {
      const data = text ? { text } : { url };
      const response = await analyzeContent(data);
      setResults(response);
    } catch (err: any) {
      setError(err.message || 'Failed to analyze content.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="container mt-5">
      <h1 className="text-center mb-4">Propaganda Detector</h1>
      <PropagandaForm onSubmit={handleAnalyze} loading={loading} />
      {error && <div className="alert alert-danger">{error}</div>}
      <LoadingSpinner loading={loading} />
      {results && (
        <ResultsDisplay
          propagandaScore={results.propaganda_score}
          identifiedTechniques={results.identified_techniques}
          explanation={results.explanation}
        />
      )}
    </div>
  );
}

export default App;