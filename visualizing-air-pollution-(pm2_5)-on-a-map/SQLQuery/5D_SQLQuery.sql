USE Project_PM25
DECLARE @TH geometry ='POINT EMPTY';
SELECT @TH = geometry::EnvelopeAggregate(Geom)
FROM AirPollutionPM25
WHERE country='Thailand' 
SELECT @TH.STEnvelope().ToString()
