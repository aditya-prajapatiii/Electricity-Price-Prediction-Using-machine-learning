import axios from 'axios';

const API_URL = 'http://localhost:8080/api';

// Create axios instance with base URL
const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Prediction API calls
export const getPrediction = async (predictionData) => {
  try {
    const response = await apiClient.post('/predictions', predictionData);
    return response.data;
  } catch (error) {
    throw error;
  }
};

export const getRecentPredictions = async () => {
  try {
    const response = await apiClient.get('/predictions/recent');
    return response.data;
  } catch (error) {
    throw error;
  }
};

export default {
  getPrediction,
  getRecentPredictions,
}; 