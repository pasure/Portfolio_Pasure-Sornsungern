USE [Project_PM25]
GO

UPDATE [dbo].[AirPollutionPM25]    
   SET Geom = geometry:: STGeomFromText('POINT('+convert(varchar(20),longitude)+' '+convert(varchar(20),latitude)+')',4326);
GO


