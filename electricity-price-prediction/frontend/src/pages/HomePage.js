import React from 'react';
import { Container, Row, Col, Card, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const HomePage = () => {
  return (
    <Container>
      <Row className="py-5">
        <Col>
          <div className="text-center mb-4">
            <h1>Electricity Price Prediction System</h1>
            <p className="lead">
              Predict electricity prices using machine learning based on
              historical consumption data.
            </p>
          </div>
        </Col>
      </Row>

      <Row>
        <Col md={4} className="mb-4">
          <Card className="h-100">
            <Card.Body>
              <Card.Title>Make a Prediction</Card.Title>
              <Card.Text>
                Input your parameters to get a real-time electricity price
                prediction using our machine learning model.
              </Card.Text>
              <Link to="/predict">
                <Button variant="primary">Make Prediction</Button>
              </Link>
            </Card.Body>
          </Card>
        </Col>

        <Col md={4} className="mb-4">
          <Card className="h-100">
            <Card.Body>
              <Card.Title>View History</Card.Title>
              <Card.Text>
                Check the history of previous predictions and analyze the
                patterns of electricity price variations.
              </Card.Text>
              <Link to="/history">
                <Button variant="info">View History</Button>
              </Link>
            </Card.Body>
          </Card>
        </Col>

        <Col md={4} className="mb-4">
          <Card className="h-100">
            <Card.Body>
              <Card.Title>About the System</Card.Title>
              <Card.Text>
                Learn about how our system works, the machine learning algorithms
                used, and the factors affecting electricity prices.
              </Card.Text>
              <Link to="/about">
                <Button variant="secondary">Learn More</Button>
              </Link>
            </Card.Body>
          </Card>
        </Col>
      </Row>

      <Row className="py-4">
        <Col>
          <Card>
            <Card.Body>
              <Card.Title>Why Predict Electricity Prices?</Card.Title>
              <Card.Text>
                Electricity price prediction helps stakeholders make informed
                decisions about energy consumption, production, and trading.
                Accurate predictions can lead to significant cost savings for
                businesses and improved grid management for utilities.
              </Card.Text>
              <Card.Text>
                Our system uses advanced machine learning algorithms trained on
                historical data to provide accurate and timely predictions based
                on factors like time of day, load, temperature, and special day
                indicators.
              </Card.Text>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default HomePage; 