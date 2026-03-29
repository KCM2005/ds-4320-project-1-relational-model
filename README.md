# DS 4320 Project 1: Predicting Hospital Readmission Risks
This is my repository for DS 4320 Project 1

# Executive Summary

# Name
Kalenga Mumba

# NetID
kew6jk

# DOI
[Project 1 - DOI](https://doi.org/10.5281/zenodo.19323230)

# Press release
insert press release link

# Data
insert data folder link

## Pipeline
insert pipeline files link

## License
insert license

## Problem Definition
Initial General Problem: Analyze the performance of soccer players to make informed decisions about player health and performance improvement.

Refined Specific Problem: Analyze the correlation between soccer players’ speed and instantaneous acceleration with their heart rate during a soccer match. Using the SoccerMon dataset, 2020-06-01-TeamA-5a3be598-2f51-426f-95a5-b63d1d7c1b43 (https://zenodo.org/records/10033832), which contains kinematic data (types of movements) and physiological data (heart rate), this specific problem will involve identifying whether speed or acceleration are associated with elevated heart rates.

## Rationale for refinement
The rationale for refining the problem statement is to shift from a broad analysis of soccer player performance to a focused investigation of the correlation between speed, instantaneous acceleration, and heart rate during a soccer match. Further, this refinement shows that high intensity running activities (speed and instantaneous acceleration) are critical components of soccer performance. By analyzing specific movement data, a data scientist can better understand how explosive movements and sprints affect heart rates. The focus on instantaneous acceleration, in particular, acknowledges that soccer involves frequent, brief bursts of high-intensity effort, making it a crucial aspect of the game's physical demands. This targeted approach can provide actionable insights for coaches and trainers to design more effective training programs, optimize player performance, and reduce excessive fatigue and injury risk.

## Motivation
My motivation for this project is two-fold. Firstly, as a keen observer of soccer, I have noticed the sport's explosive nature, with constant bursts of speed and rapid changes of direction - movements that are critical to the game. It is this explosive nature in its movements that nudged me to explore how speed and instantaneous acceleration impacts players physiologically, particularly their heart rates. By analyzing heart rate responses to these high-intensity movements, coaches can tailor training to match the sport's demands, ensuring players are prepared for explosive sprints, rapid cuts, and quick changes of direction. This insight enables targeted interventions to enhance endurance, speed, and agility while minimizing the risk of fatigue-related injuries, ultimately improving player performance and career longevity. Secondly, scientific evidence confirms that these high-intensity activities significantly elevate heart rate. As such, I am motivated to explore and analyze which movement type (speed, instantaneous acceleration) is closely correlated to players’ heart rates. Understanding the relationship between physical exertion (speed and acceleration) and physiological response (heart rate) can lead to more personalized and effective player management.

## Headline of Press Release and link to press release
add link here

## Terminology of KPIs
| Term / KPI       | Description                        | Relevance to Analysis                                                 |
| ---------------- | ---------------------------------- | --------------------------------------------------------------------- |
| player_name      | Name of the player                 | Identifies which player the movement and sensor data belongs to       |
| time             | Timestamp of the measurement       | Tracks changes in position, speed, and acceleration over time         |
| lat              | Latitude (GPS coordinate)          | Part of player position on the pitch for movement mapping             |
| lon              | Longitude (GPS coordinate)         | Part of player position on the pitch for movement mapping             |
| speed            | Player speed (m/s)                 | Measures intensity and bursts during attacking or defensive sequences |
| heart_rate       | Player’s heart rate (bpm)          | Monitors physical load and effort during match or training            |
| hacc             | Horizontal accuracy of GPS         | Indicates reliability of positional data                              |
| hdop             | Horizontal dilution of precision   | Indicates GPS signal quality and accuracy                             |
| signal_quality   | GPS signal strength                | Helps filter out unreliable measurements                              |
| num_satellites   | Number of satellites connected     | Higher = more accurate positioning                                    |
| inst_acc_impulse | Instantaneous acceleration impulse | Measures sudden movements and bursts                                  |
| accl_x           | Acceleration in X-axis             | Detects movement left to right                                        |
| accl_y           | Acceleration in Y-axis             | Detects movement forward or backward                                  |
| accl_z           | Acceleration in Z-axis             | Detects movement up and down                                          |
| gyro_x           | Gyroscope in X-axis                | Measures rotation and orientation of the player                       |
| gyro_y           | Gyroscope in Y-axis                | Measures rotation and orientation of the player                       |
| gyro_z           | Gyroscope in Z-axis                | Measures rotation and orientation of the player                       |

## Paragraph explaining the domain
This project operates within the domain of sports science, with a strong emphasis on performance analytics and physiological monitoring in soccer. It integrates principles of exercise physiology and biomechanics to understand the physiological demands of the sport, particularly how explosive movements (in this case speed, instantaneous acceleration) influence heart rate. Crucially, it leverages data analytics to analyze these physiological responses, aiming to optimize player training, personalize management strategies, and ultimately enhance performance and career longevity.

## Background readings
Folder is in the repo

## Table showing summary of readings
| Title                                                                                                                                                            | Brief description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Link                                                                                                                          |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Physical Demands of Top-Class Soccer Friendly Matches in Relation to a Playing Position Using Global Positioning System Technology                               | Mallo et al (2015) used GPS technology to analyze physical demands on professional soccer players during friendly matches.<br>Revealed position-specific differences in distance covered and intensity.<br>Wide midfielders covered the greatest distances at high intensity (>19.8 km/h).<br>Central midfielders covered the most distance overall.<br>The study stresses emphasis on distance moved relative to playing position when comparing physical demands data.                                                                                                                                                 | [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC4633253/#:~:text=Total%20distance%20covered%2C%20distance%20in,km%C2%B7h%2D1) |
| Changes in Acceleration and Deceleration Capacity Throughout Professional Soccer Match-Play                                                                      | Russell et al (2016) tracked acceleration and deceleration patterns in professional soccer players during matches.<br>High-intensity actions like sprints, accelerations, and decelerations reduce in the last 15 minutes.<br>Likely corresponds to increased heart rate and fatigue.                                                                                                                                                                                                                                                                                                                                    | [Link](https://journals.lww.com/nsca-jscr/FullText/2016/10000/Changes_in_Acceleration_and_Deceleration_Capacity)              |
| High-Intensity Acceleration and Deceleration Demands in Elite Team Sports Competitive Match Play: A Systematic Review and Meta-Analysis of Observational Studies | Harper et al (2019) conducted a systematic review and meta-analysis of major team sports (American Football, Australian Football, hockey, rugby, and soccer).<br>Examined high-intensity acceleration and deceleration demands in elite team sports match play.<br>All sports had more high and very high intensity decelerations than accelerations.<br>Soccer had significantly more high-intensity and very high-intensity decelerations than accelerations.<br>Indicates players frequently slow down quickly (decelerate) during matches.<br>This is likely due to rapid changes in direction or stopping suddenly. | [Link](https://pmc.ncbi.nlm.nih.gov/articles/PMC6851047/pdf/40279_2019_Article_1170.pdf)                                      |
| Locomotor performance parameters as predictors of high-performing male soccer teams. A multiple-season study on professional soccer.                             | Makar et al (2024) analyzed locomotor (speed and acceleration) demands in the Turkish Super League.<br>Running speed (4.01-5.5 m/s) and accelerations (5.5-7.0 m/s²) significantly predict team success.                                                                                                                                                                                                                                                                                                                                                                                                                 | [Link](https://www.nature.com/articles/s41598-024-80181-z)                                                                    |
| Player Load, Acceleration, and Deceleration During Forty-Five Competitive Matches of Elite Soccer                                                                | Dalen et al (2016) analyzed match data from elite soccer players.<br>Accelerations contribute 7-10% of total player load.<br>Decelerations contribute 5-7% of total player load.<br>Other high-intensity movements also significantly contribute to workload.<br>Motion analysis alone may underestimate total player load.                                                                                                                                                                                                                                                                                              | [Link](https://pubmed.ncbi.nlm.nih.gov/26057190/)                                                                             |
| Validity of heart rate as an indicator of aerobic demand during soccer activities in amateur soccer players.                                                     | Esposito et al (2004) validated using heart rate (HR) to monitor physiological demands in soccer.<br>Compared HR-oxygen uptake relationships in lab and field tests.<br>HR increased linearly with oxygen uptake in both settings.<br>HR effectively reflects metabolic expenditure in soccer.<br>Allows accurate estimation of physiological demands from field-measured HR.                                                                                                                                                                                                                                            | [Link](https://link.springer.com/article/10.1007/s00421-004-1192-4#citeas)                                                    |
| Characteristics of Heart Rate Changes of Elite Sprinters during Speed Training                                                                                   | Xing et al (2021) found that elite sprinters' heart rate responses during max-intensity training showed direct relationships with exercise load.<br>Heart rate peaks approximately 12 seconds post-exercise.<br>Peak heart rate reaches about 110% of end-point heart rate.                                                                                                                                                                                                                                                                                                                                              | [Link](https://www.davidpublisher.com/Public/uploads/Contribute/61dffa861945b.pdf)                                            |
