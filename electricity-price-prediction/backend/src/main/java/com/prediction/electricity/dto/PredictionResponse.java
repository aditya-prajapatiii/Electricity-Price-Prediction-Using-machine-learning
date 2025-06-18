package com.prediction.electricity.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.time.LocalDateTime;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PredictionResponse {

    private Long id;
    private Integer hour;
    private Double load;
    private Double temperature;
    private Boolean weekend;
    private Boolean holiday;
    private Double predictedPrice;
    private LocalDateTime createdAt;
}