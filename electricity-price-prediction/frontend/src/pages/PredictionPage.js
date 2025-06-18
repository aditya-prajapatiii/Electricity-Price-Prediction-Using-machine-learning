import React from 'react';
import { Container, Row, Col } from 'react-bootstrap';
import PredictionForm from '../components/PredictionForm';

const PredictionPage = () => {
  return (
    <Container>
      <Row className="py-3">
        <Col>
          <h2>Make a Prediction</h2>
          <p>
            Enter the parameters below to predict electricity prices based on
            your inputs. Our machine learning model will analyze the data and
            provide an estimated price.
          </p>
        </Col>
      </Row>
      <Row>
        <Col md={12}>
          <PredictionForm />
        </Col>
      </Row>
    </Container>
  );
};

export default PredictionPage; 