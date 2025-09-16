import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_BASE_URL || 'http://localhost:8000';

interface AnalyzeRequest {
  text?: string;
  url?: string;
}

interface AnalyzeResponse {
  propaganda_score: number;
  identified_techniques: string[];
  explanation: string;
}

export const analyzeContent = async (data: AnalyzeRequest): Promise<AnalyzeResponse> => {
  try {
    const response = await axios.post<AnalyzeResponse>(`${API_BASE_URL}/analyze`, data);
    return response.data;
  } catch (error) {
    if (axios.isAxiosError(error) && error.response) {
      throw new Error(error.response.data.detail || 'An error occurred during analysis.');
    } else {
      throw new Error('An unexpected error occurred.');
    }
  }
};
