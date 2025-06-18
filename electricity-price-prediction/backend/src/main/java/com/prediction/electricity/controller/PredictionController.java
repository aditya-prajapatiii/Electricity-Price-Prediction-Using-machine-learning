package com.prediction.electricity.controller;

import com.prediction.electricity.dto.PredictionRequest;
import com.prediction.electricity.dto.PredictionResponse;
import com.prediction.electricity.service.PredictionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import javax.validation.Valid;
import java.util.List;

@RestController
@RequestMapping("/api/predictions")
public class PredictionController {

    private final PredictionService predictionService;

    @Autowired
    public PredictionController(PredictionService predictionService) {
        this.predictionService = predictionService;
    }

    @PostMapping
    public ResponseEntity<PredictionResponse> predictPrice(@Valid @RequestBody PredictionRequest request) {
        PredictionResponse response = predictionService.predictPrice(request);
        return ResponseEntity.ok(response);
    }

    @GetMapping("/recent")
    public ResponseEntity<List<PredictionResponse>> getRecentPredictions() {
        List<PredictionResponse> predictions = predictionService.getRecentPredictions();
        return ResponseEntity.ok(predictions);
    }
}