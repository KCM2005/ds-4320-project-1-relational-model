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

## Domain Exposition
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
