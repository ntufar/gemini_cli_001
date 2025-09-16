import React from 'react';

interface ResultsDisplayProps {
  propagandaScore: number | null;
  identifiedTechniques: string[];
  explanation: string;
}

const ResultsDisplay: React.FC<ResultsDisplayProps> = ({ propagandaScore, identifiedTechniques, explanation }) => {
  if (propagandaScore === null) {
    return null;
  }

  const scoreVariant = propagandaScore > 0.7 ? 'danger' : propagandaScore > 0.4 ? 'warning' : 'success';
  const scoreWidth = propagandaScore * 100;

  return (
    <div className="card mt-4">
      <div className="card-header bg-primary text-white">
        Analysis Results
      </div>
      <div className="card-body">
        <h5 className="card-title">Propaganda Score: {propagandaScore.toFixed(2)}</h5>
        <div className="progress mb-3">
          <div
            className={`progress-bar bg-${scoreVariant}`}
            role="progressbar"
            style={{ width: `${scoreWidth}%` }}
            aria-valuenow={scoreWidth}
            aria-valuemin={0}
            aria-valuemax={100}
          >
            {scoreWidth.toFixed(0)}%
          </div>
        </div>
        <h6 className="card-subtitle mb-2 text-muted">Identified Techniques:</h6>
        {
          identifiedTechniques.length > 0 ? (
            <ul className="list-group mb-3">
              {identifiedTechniques.map((tech, index) => (
                <li key={index} className="list-group-item">{tech}</li>
              ))}
            </ul>
          ) : (
            <p>No specific techniques identified.</p>
          )
        }
        <h6 className="card-subtitle mb-2 text-muted">Explanation:</h6>
        <p className="card-text">{explanation}</p>
      </div>
    </div>
  );
};

export default ResultsDisplay;
