FROM maven:3.8.5-openjdk-11 AS build

WORKDIR /app

# Copy Maven configuration files
COPY pom.xml .

# Download dependencies (for better caching)
RUN mvn dependency:go-offline

# Copy application source
COPY src ./src

# Build the application
RUN mvn package -DskipTests

# Create runtime image
FROM openjdk:11-jre-slim

WORKDIR /app

# Copy JAR from build stage
COPY --from=build /app/target/*.jar app.jar

# Expose port
EXPOSE 8080

# Run the application
ENTRYPOINT ["java","-jar","app.jar"] 