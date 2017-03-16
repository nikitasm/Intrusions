USE [intrusions]
BULK
INSERT [intrusion_corrupted_data]
FROM 'C:\Users\Morpheus\Desktop\kddcup.data_10_percent_corrupted.txt'
WITH (
	FIELDTERMINATOR = ';',
	ROWTERMINATOR = '0x0a',
	FIRSTROW = 1
)
GO