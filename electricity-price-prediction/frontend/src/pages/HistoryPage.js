import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Table, Card, Alert } from 'react-bootstrap';
import { getRecentPredictions } from '../services/api';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

// Register Chart.js components
ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const HistoryPage = () => {
  const [predictions, setPredictions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchPredictions = async () => {
      try {
        const data = await getRecentPredictions();
        setPredictions(data);
        setLoading(false);
      } catch (err) {
        setError('Failed to load prediction history');
        console.error('Error fetching predictions:', err);
        setLoading(false);
      }
    };

    fetchPredictions();
  }, []);

  // Prepare chart data
  const chartData = {
    labels: predictions.map((p, index) => `Prediction ${index + 1}`),
    datasets: [
      {
        label: 'Predicted Price ($/MWh)',
        data: predictions.map((p) => p.predictedPrice),
        fill: false,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        tension: 0.1,
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: 'Recent Price Predictions',
      },
    },
    scales: {
      y: {
        beginAtZero: false,
        title: {
          display: true,
          text: 'Price ($/MWh)',
        },
      },
    },
  };

  return (
    <Container>
      <Row className="py-3">
        <Col>
          <h2>Prediction History</h2>
          <p>View your recent electricity price predictions and their parameters.</p>
        </Col>
      </Row>

      {loading ? (
        <div className="text-center py-4">Loading prediction history...</div>
      ) : error ? (
        <Alert variant="danger">{error}</Alert>
      ) : predictions.length === 0 ? (
        <Alert variant="info">No prediction history found. Make a prediction first!</Alert>
      ) : (
        <>
          <Row className="mb-4">
            <Col>
              <Card>
                <Card.Body>
                  <Line data={chartData} options={chartOptions} />
                </Card.Body>
              </Card>
            </Col>
          </Row>

          <Row>
            <Col>
              <Card>
                <Card.Body>
                  <h4>Recent Predictions</h4>
                  <div className="table-responsive">
                    <Table striped bordered hover>
                      <thead>
                        <tr>
                          <th>#</th>
                          <th>Hour</th>
                          <th>Load (MW)</th>
                          <th>Temp (°C)</th>
                          <th>Weekend</th>
                          <th>Holiday</th>
                          <th>Predicted Price ($/MWh)</th>
                          <th>Date</th>
                        </tr>
                      </thead>
                      <tbody>
                        {predictions.map((prediction, index) => (
                          <tr key={prediction.id}>
                            <td>{index + 1}</td>
                            <td>{prediction.hour}</td>
                            <td>{prediction.load.toFixed(2)}</td>
                            <td>{prediction.temperature.toFixed(2)}</td>
                            <td>{prediction.weekend ? 'Yes' : 'No'}</td>
                            <td>{prediction.holiday ? 'Yes' : 'No'}</td>
                            <td>${prediction.predictedPrice.toFixed(2)}</td>
                            <td>
                              {new Date(prediction.createdAt).toLocaleString()}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </Table>
                  </div>
                </Card.Body>
              </Card>
            </Col>
          </Row>
        </>
      )}
    </Container>
  );
};

export default HistoryPage; 