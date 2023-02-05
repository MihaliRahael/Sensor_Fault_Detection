# Sensor-Fault-Detection

### Problem Statement
The Air Pressure System (APS) is a critical component of a heavy-duty vehicle that uses compressed air to force a piston to provide pressure to the brake pads, slowing the vehicle down. The benefits of using an APS instead of a hydraulic system are the easy availability and long-term sustainability of natural air.

This is a Binary Classification problem, in which the affirmative class indicates that the failure was caused by a certain component of the APS, while the negative class
indicates that the failure was caused by something else.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions. ie we have to reduce false positives and false negatives. More importantly we have to reduce false negatives, since cost incurred due to false negative is 50 times higher than the false positives.

### Objectives
* Need to Handle many Null values in almost all columns
* No low-latency requirement.
* Interpretability is not important.
* Misclassification leads the unecessary repair costs.

### Solution Proposed 
In this project, the system in focus is the Air Pressure system (APS) which generates pressurized air that are utilized in various functions in a truck, such as braking and gear changes. The datasets positive class corresponds to component failures for a specific component of the APS system. The negative class corresponds to trucks with failures for components not related to the APS system.

The problem is to reduce the cost due to unnecessary repairs. So it is required to minimize the false predictions.
### Tech Stack Used
1. Python 
2. FastAPI 
3. Machine learning algorithms
4. Docker
5. MongoDB

### Infrastructure Required.

1. AWS S3
2. AWS EC2
3. AWS ECR
4. Git Actions

### Dataset
https://archive.ics.uci.edu/ml/datasets/APS+Failure+at+Scania+Trucks 

### Project Archietecture
![0_Sensor Training Pipeline](https://user-images.githubusercontent.com/106816732/216809181-b64110a6-2031-495d-ac81-b7c8bce13ddc.png)

