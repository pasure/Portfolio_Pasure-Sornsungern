USE Project_PM25
SELECT Year, country , city , pm25
FROM AirPollutionPM25
WHERE pm25 > 50 AND Year = '2015'