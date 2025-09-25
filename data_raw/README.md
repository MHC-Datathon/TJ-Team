# 📂 data_raw

This folder contains the raw datasets used in the project.  
All files here are direct downloads from the **MTA Open Data portal** and related NYC Open Data sources.  
They are unprocessed — cleaning and analysis are performed in the `data_work/` stage.

---

## Datasets

### Ridership
- **MTA_Bus_Ridership__2020_-_2024.csv**  
  Monthly route-level bus ridership (historic dataset, 2020–2024).  
  Source: [NYC Open Data – MTA Bus Ridership 2020–2024](https://data.cityofnewyork.us/Transportation/MTA-Bus-Ridership-2020-2024/)

- **MTA_Bus_Ridership__Beginning_2025.csv**  
  Monthly route-level bus ridership (2025–present).  
  Source: [NYC Open Data – MTA Bus Ridership Beginning 2025](https://data.cityofnewyork.us/Transportation/MTA-Bus-Ridership-Beginning-2025/)

---

### Speeds
- **MTA_Bus_Speeds__2015_-_2020.csv**  
  Segment-level bus speeds, 2015–2020.  
  Source: [NYC Open Data – MTA Bus Speeds (2015–2020)](https://data.cityofnewyork.us/Transportation/MTA-Bus-Speeds-2015-2020/)

- **MTA_Bus_Speeds__2020_-_2024.csv**  
  Segment-level bus speeds, 2020–2024.  
  Source: [NYC Open Data – MTA Bus Speeds (2020–2024)](https://data.cityofnewyork.us/Transportation/MTA-Bus-Speeds-2020-2024/)

- **MTA_Bus_Speeds__Beginning_2025.csv**  
  Segment-level bus speeds, 2025–present.  
  Source: [NYC Open Data – MTA Bus Speeds (Beginning 2025)](https://data.cityofnewyork.us/Transportation/MTA-Bus-Speeds-Beginning-2025/)

---

### Wait Assessment
- **MTA_Bus_Wait_Assessment__2015_-_2020.csv**  
  Wait assessment data, 2015–2020.  
  Source: [NYC Open Data – MTA Bus Wait Assessment (2015–2020)](https://data.cityofnewyork.us/Transportation/MTA-Bus-Wait-Assessment-2015-2020/)

- **MTA_Bus_Wait_Assessment__2020_-_2024.csv**  
  Wait assessment data, 2020–2024.  
  Source: [NYC Open Data – MTA Bus Wait Assessment (2020–2024)](https://data.cityofnewyork.us/Transportation/MTA-Bus-Wait-Assessment-2020-2024/)

- **MTA_Bus_Wait_Assessment__Beginning_2025.csv**  
  Wait assessment data, 2025–present.  
  Source: [NYC Open Data – MTA Bus Wait Assessment (Beginning 2025)](https://data.cityofnewyork.us/Transportation/MTA-Bus-Wait-Assessment-Beginning-2025/)

---

### Automated Passenger Counts (APC)
- **MTA_Bus_Automated_Counter_Data__2019.csv**  
  Automated passenger count data (2019 sample).  
  Source: [NYC Open Data – MTA Bus Automated Counter Data](https://data.cityofnewyork.us/Transportation/MTA-Bus-Automated-Counter-Data/)

---

### Routes and Segments
- **MTA_Bus_Route_Segments__2019.csv**  
  Geographic and operational definitions of bus route segments.  
  Source: [NYC Open Data – MTA Bus Route Segments](https://data.cityofnewyork.us/Transportation/MTA-Bus-Route-Segments/)

---

### Other Supporting Data
- **Police_Precincts.csv**  
  NYPD police precinct shapefile export, used for mapping and geospatial joins.  
  Source: [NYC Open Data – NYPD Precincts](https://data.cityofnewyork.us/Public-Safety/Police-Precincts/)

---

⚠️ **Note**:  
- These files are kept raw for reproducibility.  
- Do not edit directly — any cleaning or processing should be saved into `data_work/`.  
