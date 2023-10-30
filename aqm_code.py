import random

# Function to generate random sensor data
def generate_sensor_data():
    pm25 = random.uniform(0, 100)
    co = random.uniform(0, 5)
    no2 = random.uniform(0, 1)
    o3 = random.uniform(0, 0.1)
    return pm25, co, no2, o3

# Function to calculate the Air Quality Index (AQI)
def calculate_aqi(pm25, co, no2, o3):
    # Replace with your AQI calculation logic
    # This is a simplified example; use an appropriate formula for AQI calculation
    aqi = (pm25 + co + no2 + o3) / 4
    return aqi

# Function to classify air quality based on AQI
def classify_air_quality(aqi):
    if aqi <= 50:
        return "Good"
    elif aqi <= 100:
        return "Moderate"
    elif aqi <= 150:
        return "Unhealthy for Sensitive Groups"
    elif aqi <= 200:
        return "Unhealthy"
    else:
        return "Very Unhealthy"

# Generate sensor data
pm25, co, no2, o3 = generate_sensor_data()

# Calculate AQI
aqi = calculate_aqi(pm25, co, no2, o3)

# Classify air quality
air_quality = classify_air_quality(aqi)

# Output the results
print(f"PM2.5: {pm25} µg/m³")
print(f"CO: {co} ppm")
print(f"NO2: {no2} ppm")
print(f"O3: {o3} ppm")
print(f"AQI: {aqi}")
print(f"Air Quality: {air_quality}")
