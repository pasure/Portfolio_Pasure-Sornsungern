USE Project_PM25 
SELECT country, city, Year, longitude, latitude
FROM AirPollutionPM25
WHERE country IN ('Myanmar', 'Malaysia')
