USE Project_PM25
SELECT country , AVG(pm25) As AveragePM25
FROM AirPollutionPM25
GROUP BY country
ORDER BY AVG(pm25) DESC