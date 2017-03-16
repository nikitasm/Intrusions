create view [status_prediction] as
select * from [corrected_data]
where (status!='null');