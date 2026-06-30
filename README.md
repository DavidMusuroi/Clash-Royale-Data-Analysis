# Project Overview

This project generates synthetic data related to player performance and win probability, performs data cleaning, visualization, and applies a machine learning model (Random Forest) to predict match outcomes.

---

## Setup

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

In order to exit it, just type deactivate in the terminal

---

## Project Workflow

In the determine_win.py function, I defined the data generation logic. I randomly
selected several features that I considered relevant for estimating a player’s
win probability — such as trophy count, current win streak, and others — and
developed a random formula to compute this probability. The maximum possible value
was intentionally set to 130%, exceeding 100%, to introduce inconsistent
data points that could later be removed. A player is considered to have won if a
randomly generated number is lower than their win probability, and to have lost
otherwise. The function returns a dictionary containing all ten columns of data.

In the main function, I generated random values for the ten columns across 1,000
instances, splitting them into 700 training samples and 300 testing samples, both
randomly selected. These subsets were saved into separate CSV files. Next, I
removed missing or invalid values — specifically cases where the win probability
exceeded 100%, or where the Favourite_Win_Condition column was "N.A.", an error
intentionally introduced to simulate missing data — and exported the cleaned 
subsets to new CSV files.

Afterward, I computed descriptive statistics using the describe() function and
created histograms, count plots, box plots, and violin plots within the plots.py
module for the relevant variables. Since they could not be displayed directly,
I saved them as .jpg images.

Finally, in the main function, I used a Random Forest classifier to train on the
training subset and evaluate the testing subset, as this was a classification problem.
Categorical variables were encoded using One-Hot Encoding, allowing me to determine the
model’s accuracy. I then generated a confusion matrix, which I also saved as a .jpg image.
