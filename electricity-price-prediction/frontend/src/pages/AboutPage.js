import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Card, ListGroup, Alert } from 'react-bootstrap';
import axios from 'axios';

const AboutPage = () => {
  const [modelInfo, setModelInfo] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchModelInfo = async () => {
      try {
        const response = await axios.get('http://localhost:5000/model-info');
        setModelInfo(response.data);
        setLoading(false);
      } catch (err) {
        setError('Unable to fetch model information');
        setLoading(false);
        console.error('Error fetching model info:', err);
      }
    };

    fetchModelInfo();
  }, []);

  const renderFeatureImportance = () => {
    if (!modelInfo || !modelInfo.model_info.feature_importance || modelInfo.model_info.feature_importance === "Not available") {
      return <Alert variant="info">Feature importance information not available</Alert>;
    }

    const importances = modelInfo.model_info.feature_importance;
    const sortedFeatures = Object.keys(importances).sort(
      (a, b) => importances[b] - importances[a]
    );

    return (
      <ListGroup variant="flush">
        {sortedFeatures.map((feature) => (
          <ListGroup.Item key={feature}>
            <strong>{feature}</strong>: {(importances[feature] * 100).toFixed(2)}%
          </ListGroup.Item>
        ))}
      </ListGroup>
    );
  };

  return (
    <Container>
      <Row className="py-3">
        <Col>
          <h2>About the Electricity Price Prediction System</h2>
          <p>
            This application predicts electricity prices using machine learning
            techniques based on historical data and various influencing factors.
          </p>
        </Col>
      </Row>

      <Row className="mb-4">
        <Col>
          <Card>
            <Card.Body>
              <Card.Title>System Overview</Card.Title>
              <Card.Text>
                The Electricity Price Prediction System is a full-stack web
                application that uses machine learning to predict electricity
                prices based on various inputs such as hour of the day,
                electricity load, temperature, and special day indicators
                (weekends/holidays).
              </Card.Text>
              <Card.Text>
                The system is built using a modern tech stack with clean
                architecture principles, separating concerns between the
                backend, frontend, and machine learning components.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row className="mb-4">
        <Col md={6}>
          <Card className="h-100">
            <Card.Header>Technical Architecture</Card.Header>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <strong>Backend:</strong> Java, Spring Boot, REST APIs
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>Frontend:</strong> React, Bootstrap, Chart.js
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>ML Service:</strong> Python, Flask, scikit-learn
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>Database:</strong> MySQL
              </ListGroup.Item>
            </ListGroup>
          </Card>
        </Col>
        <Col md={6}>
          <Card className="h-100">
            <Card.Header>Machine Learning Model</Card.Header>
            <Card.Body>
              {loading ? (
                <p>Loading model information...</p>
              ) : error ? (
                <Alert variant="warning">{error}</Alert>
              ) : (
                <>
                  <Card.Title>
                    {modelInfo?.model_info?.regressor_type || "Random Forest Regressor"}
                  </Card.Title>
                  <Card.Text>
                    The price prediction is performed using a {modelInfo?.model_info?.regressor_type || "Random Forest"}
                    model, which is an ensemble learning method that combines multiple decision trees to make a more accurate prediction.
                  </Card.Text>
                  <Card.Text>
                    <strong>Training Data Source:</strong> {modelInfo?.training_data_source || "Historical and synthetic data"}
                  </Card.Text>
                  <Card.Text>
                    <strong>Estimators:</strong> {modelInfo?.model_info?.n_estimators || "100"}
                  </Card.Text>
                  <Card.Text>
                    <strong>Max Depth:</strong> {modelInfo?.model_info?.max_depth || "Optimal depth determined automatically"}
                  </Card.Text>
                </>
              )}
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row className="mb-4">
        <Col>
          <Card>
            <Card.Header>Feature Importance</Card.Header>
            <Card.Body>
              <Card.Text>
                The model analyzes the importance of different factors in predicting electricity prices:
              </Card.Text>
              {loading ? (
                <p>Loading feature importance...</p>
              ) : error ? (
                <Alert variant="warning">{error}</Alert>
              ) : (
                renderFeatureImportance()
              )}
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row>
        <Col>
          <Card>
            <Card.Header>Factors Affecting Electricity Prices</Card.Header>
            <ListGroup variant="flush">
              <ListGroup.Item>
                <strong>Time of Day:</strong> Electricity demand varies
                throughout the day, with peak hours typically seeing higher
                prices.
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>Load:</strong> Higher demand generally leads to higher
                prices due to the need to activate more expensive generation
                sources.
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>Temperature:</strong> Extreme temperatures (both hot and
                cold) can increase electricity demand for heating/cooling.
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>Weekends/Holidays:</strong> Lower industrial demand
                typically results in lower prices during these periods.
              </ListGroup.Item>
              <ListGroup.Item>
                <strong>Seasonal Patterns:</strong> Seasonal changes affect both
                demand and supply of electricity.
              </ListGroup.Item>
            </ListGroup>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default AboutPage; 