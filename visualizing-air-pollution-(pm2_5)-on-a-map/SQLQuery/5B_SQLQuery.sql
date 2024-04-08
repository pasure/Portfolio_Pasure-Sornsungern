USE Project_PM25 
DECLARE @h geometry ='POINT EMPTY';  
SET @h = geometry::STGeomFromText('POINT(100.554 13.7462)', 4326);
SELECT DISTINCT TOP 50  country, city, Geom.STDistance(@h) as Distance, Geom.STAsText() As Point, longitude , latitude
FROM AirPollutionPM25
WHERE city NOT LIKE 'Bangkok'
ORDER BY Geom.STDistance(@h) ASC

