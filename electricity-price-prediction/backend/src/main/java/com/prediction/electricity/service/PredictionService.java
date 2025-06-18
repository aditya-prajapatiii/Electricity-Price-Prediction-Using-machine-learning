package com.prediction.electricity.service;

import com.prediction.electricity.config.AppConfig;
import com.prediction.electricity.dto.PredictionRequest;
import com.prediction.electricity.dto.PredictionResponse;
import com.prediction.electricity.model.PredictionRecord;
import com.prediction.electricity.repository.PredictionRecordRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class PredictionService {

    private final PredictionRecordRepository predictionRecordRepository;
    private final RestTemplate restTemplate;
    private final AppConfig appConfig;

    @Autowired
    public PredictionService(PredictionRecordRepository predictionRecordRepository,
            RestTemplate restTemplate,
            AppConfig appConfig) {
        this.predictionRecordRepository = predictionRecordRepository;
        this.restTemplate = restTemplate;
        this.appConfig = appConfig;
    }

    public PredictionResponse predictPrice(PredictionRequest request) {
        // Prepare data for ML service
        Map<String, Object> predictionData = new HashMap<>();
        predictionData.put("hour", request.getHour());
        predictionData.put("load", request.getLoad());
        predictionData.put("temperature", request.getTemperature());
        predictionData.put("is_weekend", request.getWeekend());
        predictionData.put("is_holiday", request.getHoliday());

        // Call ML service
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<Map<String, Object>> entity = new HttpEntity<>(predictionData, headers);

        ResponseEntity<Map> response = restTemplate.postForEntity(
                appConfig.getMlServiceUrl() + "/predict",
                entity,
                Map.class);

        // Extract prediction
        Map<String, Object> responseBody = response.getBody();
        Double predictedPrice = (Double) responseBody.get("predicted_price");

        // Save to database
        PredictionRecord record = new PredictionRecord();
        record.setHour(request.getHour());
        record.setLoad(request.getLoad());
        record.setTemperature(request.getTemperature());
        record.setWeekend(request.getWeekend());
        record.setHoliday(request.getHoliday());
        record.setPredictedPrice(predictedPrice);

        PredictionRecord savedRecord = predictionRecordRepository.save(record);

        // Create response
        return mapToResponse(savedRecord);
    }

    public List<PredictionResponse> getRecentPredictions() {
        return predictionRecordRepository.findTop10ByOrderByCreatedAtDesc()
                .stream()
                .map(this::mapToResponse)
                .collect(Collectors.toList());
    }

    private PredictionResponse mapToResponse(PredictionRecord record) {
        return new PredictionResponse(
                record.getId(),
                record.getHour(),
                record.getLoad(),
                record.getTemperature(),
                record.isWeekend(),
                record.isHoliday(),
                record.getPredictedPrice(),
                record.getCreatedAt());
    }
}