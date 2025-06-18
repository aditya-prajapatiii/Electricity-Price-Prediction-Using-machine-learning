package com.prediction.electricity.repository;

import com.prediction.electricity.model.PredictionRecord;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface PredictionRecordRepository extends JpaRepository<PredictionRecord, Long> {

    List<PredictionRecord> findTop10ByOrderByCreatedAtDesc();
}