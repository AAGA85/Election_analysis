# Election_analysis

## Project Overview
A Colorado Board of Elections employee has requested our assistance to audit the election results of a recent local congressional election. This project requires to develop specific tasks in Python to be able to deliver the following information:

1. Calculate the total number of votes cast.
2. Get the voter turnout for each county including the percentage of votes from each county out the total count.
3. Determine the county with the highest turnout.
4. Get a complete list of candidates who received votes.
5. Calculate the total number of votes each candidate received.
6. Calculate the percentage of votes each candidate won.
7. Determine the winner of the election based on popular vote.

## Resources
- Data Source: election_results.cvs
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Results 
The analysis of the election show that:
- There were 369,711 votes cast in the election.
- The voter turnout for each county and their percentage of the total votes were:
    - Jefferson had 38,855 of voters who participated in the election: this represents 10.5% of the total votes.
    - Denver had 306,055 of voters who participated in the election: this represents 82.8% of the total votes. 
    - Arapahoe had 24,801 of voters who participated in the election: this represents 6.7% of the total votes.
- The county with the largest number of voters was Denver
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were:
    - Charles Casper Stockham received 23.0%  of the vote and 85,213 number of votes
    - Diana DeGette received 73.8% of the vote and 272,892 number of votes
    - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
- The winner of the election was:
    - Diana DeGette, who received 73.8% of the vote and 272,892 number of votes
    
 Please find all this data summarized in the attached file called [***election analysis***](https://github.com/AAGA85/Election_analysis/blob/7769c16d94b39fac422425c1e0c8ba11dabd59bd/analysis/election_analysis.txt)
 
 The full script of this analysis can be found here [***Election Analysis code***](https://github.com/AAGA85/Election_analysis/blob/7769c16d94b39fac422425c1e0c8ba11dabd59bd/PyPoll_Challenge.py)
 

## Challenge Summary

Excel and VBA as we have studied previously, are common tools for data analysis. They could be used to develop this project but as we have discovered in previous modules their use can be complex when we need to work with several operations and large data sets, the time of execution can be impacted significantly because the amount of data and operations. In this module we have been able to discover that Python is more efficient with large amount of data, besides that Python code can be stored as scripts then the code can be reused and manipulated by many other users and all this for free. 

One of the challenge of this project,  besides the presentation of audit results as requested, was to develop a code easy to use and modify to audit other types of elections. Then based on the conclusion previously described, Python help us to meet with this challenge. Other users will be able to understant the scrip becuase it includes a full and clear description of each task. The user can identify the comment of each taks with a # or number sign before each comment.

This code is so easy to use, the new user just need to allocate the file to be load (the file where the program will read the data) to the current working directory, save the code and run it.

![Retrive the data](https://user-images.githubusercontent.com/106939511/176815532-c33256bd-de73-45f3-b06f-9c0aaef6f8af.png)


