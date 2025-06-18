package com.prediction.electricity.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotNull;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class PredictionRequest {

    @NotNull(message = "Hour is required")
    @Min(value = 0, message = "Hour must be between 0 and 23")
    @Max(value = 23, message = "Hour must be between 0 and 23")
    private Integer hour;

    @NotNull(message = "Load is required")
    private Double load;

    @NotNull(message = "Temperature is required")
    private Double temperature;

    private Boolean weekend = false;
    private Boolean holiday = false;
}