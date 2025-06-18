import React, { useState } from 'react';
import { Form, Button, Row, Col, Card } from 'react-bootstrap';
import axios from 'axios';

const PredictionForm = () => {
  const [formData, setFormData] = useState({
    hour: 12,
    load: 15000,
    temperature: 25,
    weekend: false,
    holiday: false,
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;
    setFormData({
      ...formData,
      [name]: type === 'checkbox' ? checked : parseFloat(value),
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const response = await axios.post(
        'http://localhost:8080/api/predictions',
        formData
      );
      setPrediction(response.data);
    } catch (err) {
      setError(
        err.response?.data?.message ||
          'An error occurred while making the prediction'
      );
      console.error('Prediction error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <Card className="mb-4">
        <Card.Body>
          <Card.Title>Electricity Price Prediction</Card.Title>
          <Form onSubmit={handleSubmit}>
            <Row className="mb-3">
              <Col md={6}>
                <Form.Group controlId="hour">
                  <Form.Label>Hour of Day (0-23)</Form.Label>
                  <Form.Control
                    type="number"
                    name="hour"
                    min="0"
                    max="23"
                    value={formData.hour}
                    onChange={handleChange}
                    required
                  />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group controlId="load">
                  <Form.Label>Electricity Load (MW)</Form.Label>
                  <Form.Control
                    type="number"
                    name="load"
                    min="0"
                    step="100"
                    value={formData.load}
                    onChange={handleChange}
                    required
                  />
                </Form.Group>
              </Col>
            </Row>

            <Row className="mb-3">
              <Col md={6}>
                <Form.Group controlId="temperature">
                  <Form.Label>Temperature (°C)</Form.Label>
                  <Form.Control
                    type="number"
                    name="temperature"
                    step="0.1"
                    value={formData.temperature}
                    onChange={handleChange}
                    required
                  />
                </Form.Group>
              </Col>
              <Col md={6}>
                <Form.Group controlId="weekend" className="mt-4">
                  <Form.Check
                    type="checkbox"
                    name="weekend"
                    label="Is Weekend"
                    checked={formData.weekend}
                    onChange={handleChange}
                  />
                </Form.Group>
                <Form.Group controlId="holiday">
                  <Form.Check
                    type="checkbox"
                    name="holiday"
                    label="Is Holiday"
                    checked={formData.holiday}
                    onChange={handleChange}
                  />
                </Form.Group>
              </Col>
            </Row>

            <Button
              variant="primary"
              type="submit"
              disabled={loading}
              className="w-100"
            >
              {loading ? 'Predicting...' : 'Predict Price'}
            </Button>
          </Form>
        </Card.Body>
      </Card>

      {error && <div className="alert alert-danger">{error}</div>}

      {prediction && (
        <div className="prediction-result">
          <h4>Prediction Result</h4>
          <p>
            <strong>Predicted Price:</strong> $
            {prediction.predictedPrice.toFixed(2)} per MWh
          </p>
          <div className="mt-3">
            <h5>Input Parameters:</h5>
            <ul>
              <li>Hour: {prediction.hour}</li>
              <li>Load: {prediction.load.toFixed(2)} MW</li>
              <li>Temperature: {prediction.temperature.toFixed(2)} °C</li>
              <li>Weekend: {prediction.weekend ? 'Yes' : 'No'}</li>
              <li>Holiday: {prediction.holiday ? 'Yes' : 'No'}</li>
            </ul>
          </div>
        </div>
      )}
    </div>
  );
};

export default PredictionForm; 