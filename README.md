# Modeling-and-Simulation-Pre-Final-Project
Histogram and Family of Distribution

Title: Optimizing Campus Elevator Efficiency Through Elevator Waiting Time Distribution Simulation
Description
This project simulates elevator waiting time behavior in a university building using Python, Monte Carlo simulation, and probability distributions. The system models realistic elevator operations during peak and non-peak campus hours, including student arrival rates, elevator travel delays, overcrowding, and floor request patterns.
The simulation generates 10,000 elevator usage scenarios to estimate student waiting times, elevator congestion, passenger arrival frequency, and service efficiency. Using histograms and probability charts, the project visualizes how waiting time uncertainty behaves in real campus elevator systems, especially in multi-floor academic buildings.

Objectives
•	Simulate realistic campus elevator operations using stochastic models.
•	Analyze elevator waiting time uncertainty through Monte Carlo simulation.
•	Visualize waiting time distributions using histograms and charts.
•	Evaluate elevator efficiency during peak and non-peak hours.
•	Predict student waiting time probabilities.
•	Apply Discrete-Event Queue Simulation concepts to elevator systems.
•	Demonstrate practical applications of probability distributions in real-world campus operations.

Features
•	Monte Carlo simulation with 10,000 runs
•	Histogram visualization for multiple probability distributions
•	Elevator waiting time prediction
•	Peak-hour congestion analysis
•	Percentile-based waiting time estimates (P10, P25, P50, P75, P90)
•	Floor request probability analysis
•	Professional dark-themed dashboard
•	Automatic image export (elevator_waiting_time_histograms.png)
•	Error handling for safe figure saving
•	Realistic campus elevator modeling

Concepts Applied
Monte Carlo Simulation
Randomized simulation method used to model uncertain elevator waiting conditions thousands of times.

Discrete-Event Queue Simulation
Models the sequence of elevator system events such as:
•	student arrivals
•	elevator dispatching
•	floor requests
•	passenger boarding
•	elevator travel delays
•	overcrowding during peak hours

Probability Distributions:
Exponential Distribution
Used for student arrival intervals at elevator lobbies.

Normal Distribution
Used for overall elevator waiting time caused by combined operational delays.

Poisson Distribution
Used for the number of students arriving during a specific time interval.

Binomial Distribution
Used for elevator occupancy success based on whether students can board before capacity is reached.

Triangular Distribution
Used for elevator travel time estimation when exact traffic and movement data are unavailable.

Requirements
Software Requirements
•	Python 3.x
•	Visual Studio Code (VS Code)

Python Libraries
Install the following libraries before running the program:
•	pip install numpy matplotlib

How to Run
Step 1 — Open VS Code
Launch Visual Studio Code.

Step 2 — Create Python File
Create a new file named:
elevator_simulation.py

Step 3 — Copy the Code
Paste the entire simulation code into the file.

Step 4 — Save the File
Press:
•	Ctrl + S (Windows)
•	Cmd + S (Mac)

Step 5 — Run the Program
Open the VS Code terminal and run:
python elevator_simulation.py

Step 6 — View Results
The program will:
•	display histograms and charts
•	print elevator waiting summaries in the terminal
•	save the visualization image automatically as:
elevator_waiting_time_histograms.png

Example Usage
A university facility administrator wants to estimate the probability that students wait more than 2 minutes for the elevator during class change hours.
The simulation:
•	generates 10,000 possible elevator scenarios
•	analyzes student arrival congestion
•	models elevator capacity limitations
•	estimates waiting time probabilities

Example Output
Waiting Time Summary
•	P10 Fastest Likely Wait : 12 seconds
•	P50 Most Likely Wait : 1 minute 18 seconds
•	P90 Worst Case Wait : 4 minutes 35 seconds

Peak-Hour Probability Example
•	Morning Rush : 41.2%
•	Lunch Time : 24.8%
•	Afternoon Rush : 28.5%
•	Evening : 5.5%

Conclusion
This project demonstrates how probability distributions, Monte Carlo simulation, and Discrete-Event Queue Simulation can be used to analyze uncertainty in campus elevator systems. By combining statistical modeling with data visualization, the simulation provides realistic predictions for elevator waiting times and congestion behavior.
The project also highlights how universities and building administrators can use simulation techniques to:
•	improve elevator scheduling
•	reduce student waiting times
•	optimize elevator traffic flow
•	improve campus operational efficiency
•	enhance student convenience and accessibility
Overall, the system serves as a practical application of statistics, operations research, and computer simulation in modern campus infrastructure management.
