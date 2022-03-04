USE Project_PM25
SELECT city, longitude , latitude
FROM AirPollutionPM25
WHERE wbinc16_text = 'Low income' AND Year = '2015'
