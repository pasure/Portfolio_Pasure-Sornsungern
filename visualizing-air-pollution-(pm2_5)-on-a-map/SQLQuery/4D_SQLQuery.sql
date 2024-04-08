USE Project_PM25
SELECT SUM(population) As  SummaryofPopulation
FROM AirPollutionPM25
WHERE Year = '2017' AND color_pm25 = 'yellow'
