import React, { useState } from 'react';

interface PropagandaFormProps {
  onSubmit: (text: string, url: string) => void;
  loading: boolean;
}

const PropagandaForm: React.FC<PropagandaFormProps> = ({ onSubmit, loading }) => {
  const [text, setText] = useState('');
  const [url, setUrl] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(text, url);
  };

  return (
    <form onSubmit={handleSubmit} className="mb-4">
      <div className="mb-3">
        <label htmlFor="textInput" className="form-label">Enter Text:</label>
        <textarea
          className="form-control"
          id="textInput"
          rows={5}
          value={text}
          onChange={(e) => setText(e.target.value)}
          disabled={loading}
        ></textarea>
      </div>
      <div className="mb-3">
        <label htmlFor="urlInput" className="form-label">Or Enter URL:</label>
        <input
          type="url"
          className="form-control"
          id="urlInput"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          disabled={loading}
        />
      </div>
      <button type="submit" className="btn btn-primary" disabled={loading}>
        {loading ? 'Analyzing...' : 'Analyze'}
      </button>
    </form>
  );
};

export default PropagandaForm;
