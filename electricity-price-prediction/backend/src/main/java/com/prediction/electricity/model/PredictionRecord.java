package com.prediction.electricity.model;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.persistence.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "prediction_records")
@Data
@NoArgsConstructor
@AllArgsConstructor
public class PredictionRecord {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private int hour;
    private double load;
    private double temperature;
    private boolean weekend;
    private boolean holiday;

    private double predictedPrice;

    private LocalDateTime createdAt;

    @PrePersist
    public void prePersist() {
        createdAt = LocalDateTime.now();
    }
}