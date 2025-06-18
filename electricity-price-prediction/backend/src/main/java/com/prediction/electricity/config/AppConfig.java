package com.prediction.electricity.config;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Configuration;

@Configuration
public class AppConfig {
    
    @Value("${ml.service.url}")
    private String mlServiceUrl;
    
    public String getMlServiceUrl() {
        return mlServiceUrl;
    }
} 