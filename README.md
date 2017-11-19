# Python1

Laboratory Project 1
Project on Random Numbers and Stochastic Experiments


1.	Number of rolls needed to get a “7” with two dice
Introduction: The experiment is roll a pair of fair dice and calculate the sum of the faces. The first time get a “7” the experiment is considered a “success”. Record the number of rolls and stop the experiment. Repeat the experiment 100000 times. Each time keep track of the number of roll it takes to have “success” and generate a Probability Mass Function for the number of rolls it takes for “success”.
Methodology: The methodology I used in this problem is using while loop to keep tracking each experiment roll numbers. If get the first “7” then store the roll number to the roll history list. For the probability, use the roll history list divide the N turns which is 100000 total turns.

Result: 






















2.	Getting 50 heads when tossing 100 coins

Introduction: This experiment is toss 100 fair coins and record the number of “heads” and if get exactly 50 heads in each experiment we call it “success”. Repeat the experiment 100000 times and get the total successes and calculate the probability of success.
Methodology: The methodology I used in this experiment is generates the random integers 0 or 1 to represents head of coin or tail of coin. Keep tracking the number of counts for head and tail in each experiments and if exactly has 50 heads then make it as “success” and increase the number of success.   
Conclusion: get the probability of success using number of successes divide 100000 experiment times.
Result:	
Probability of 50 heads in tossing 100 fair coins	
Ans.	P = 0.08016





3.	Getting 4 of a kind

Introduction: This experiment is draw 5 cards from a deck of 52 cards that has 13 ranks and 4 suits. In each experiment if draw 4 of a kind then call the experiment “success”. Repeat the experiment 100000 times and keep track of the successes. After 100000 experiments, count the total successes and calculate probability of 4 of a kind.
Methodology: The methodology I used for this experiment is creating a class called Card that has 4 different suits and 13 different ranks and a custom function getrank() to return rank value of each card. I create another class called Deck that stores the 52 cards and custom function pop_card() for removing a card from deck. Each time drawing 5 cards from the deck, check the rank of the card and store in the integer list. Sort the integer list and check first 4 cards to see if the ranks are the same. 
Conclusion:  when have 4 of a kind in each turn we call it success, after 100000 times of experiment, use success times divide 100000 times of experiment to get probability.
Result: 
Probability of 4 of a kind	
Ans.	p = 0.00017 







4.	The Password Hacking Problem

Introduction: This experiment is for use different size of string list to match if there is user inputted 4 letter password for login. The total number of passwords which can be produced is n=26^4. 
i.	Use 10^5 size string list to see if we can find the password.
ii.	Use 10^6 size string list to see if we can find the password.
iii.	Through test to figure out what size of string list we can have probability that approximately equals to 0.5
Methodology: The methodology I used for this experiment is first, make a 26 English characters list and create a 10^5 size of 4 letter words randomly pick up from character list. Go through the list if found the exactly same 4 letter words as password we called it success. To get the probability with success times divide total 1000 experiment times. Second, create 10^6 size of 4 letter words randomly pick up from character list to test this experiment. Last, try different size of 4 letter words list to see if we can find probability approximately equals to 0.5.
		Result: 
m=10^5
Prob. That at least one of the words matches the password	
p=0.188
m=10^6
Prob. That at least one of the words matches the password	
p=0.868
p=0.5
Approximate number of words in the list	
m=315000
