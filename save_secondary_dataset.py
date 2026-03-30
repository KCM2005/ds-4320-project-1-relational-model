#Create tables
patients = df[['patient_nbr', 'age', 'gender', 'race']].drop_duplicates()
encounters = df[['encounter_id', 'patient_nbr', 'admission_type_id', 'time_in_hospital']]
treatments = df[['encounter_id', 'insulin']]
outcomes = df[['encounter_id', 'readmitted']]

#Save tables to csv
patients.to_csv("patients.csv", index=False)
encounters.to_csv("encounters.csv", index=False)
treatments.to_csv("treatments.csv", index=False)
outcomes.to_csv("outcomes.csv", index=False)

#Create tables using DuckDB
import duckdb

con = duckdb.connect()

con.execute("CREATE TABLE patients AS SELECT * FROM 'patients.csv'")
con.execute("CREATE TABLE encounters AS SELECT * FROM 'encounters.csv'")
con.execute("CREATE TABLE treatments AS SELECT * FROM 'treatments.csv'")
con.execute("CREATE TABLE outcomes AS SELECT * FROM 'outcomes.csv'")

#SQL query to count how many patients fall into each combination of insulin usage level (e.g., up, down, steady, no) and readmission outcome
#(e.g., <30 days, >30 days, no readmission)
query = """
SELECT 
    t.insulin,
    o.readmitted,
    COUNT(*) AS count
FROM treatments t
JOIN outcomes o 
    ON t.encounter_id = o.encounter_id
GROUP BY t.insulin, o.readmitted
ORDER BY t.insulin, o.readmitted;
"""

con.close()
