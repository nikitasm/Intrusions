USE [intrusions]
BULK
INSERT [intrusion-data]
FROM 'C:\Users\Morpheus\Downloads\Apothikes\kddcup.data_10_percent_aggregated_without_dots_final.txt'
WITH (
	FIELDTERMINATOR = ';',
	ROWTERMINATOR = '0x0a',
	FIRSTROW = 1
)
GO
