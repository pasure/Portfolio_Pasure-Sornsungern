USE Project_PM25
SELECT country ,city, pm25 ,Year 
FROM AirPollutionPM25
WHERE country = 'Thailand'
ORDER BY Year DESC