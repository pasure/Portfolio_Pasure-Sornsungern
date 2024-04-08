CREATE TABLE [dbo].[AirPollutionPM25] (
    [country]      NVARCHAR (50)    NOT NULL,
    [city]         NVARCHAR (50)    NOT NULL,
    [Year]         INT              NOT NULL,
    [pm25]         FLOAT (53)       NOT NULL,
    [latitude]     FLOAT (53)       NULL,
    [longitude]    FLOAT (53)       NULL,
    [population]   FLOAT (53)       NULL,
    [wbinc16_text] NVARCHAR (50)    NULL,
    [Region]       NVARCHAR (50)    NULL,
    [conc_pm25]    NVARCHAR (50)    NULL,
    [color_pm25]   NVARCHAR (50)    NULL,
    [Geom]         [sys].[geometry] NULL,
    CONSTRAINT [PK_AirPollutionPM25] PRIMARY KEY CLUSTERED ([country] ASC, [city] ASC, [Year] ASC, [pm25] ASC)
);