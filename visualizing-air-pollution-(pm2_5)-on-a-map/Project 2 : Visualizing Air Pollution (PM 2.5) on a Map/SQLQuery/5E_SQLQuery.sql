USE Project_PM25
SELECT city, longitude, latitude
FROM AirPollutionPM25
WHERE country IN (
SELECT TOP 1 country
FROM AirPollutionPM25
WHERE Year = '2011'
GROUP BY country
ORDER BY COUNT(city) DESC)						
AND Year = '2011'
