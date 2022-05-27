def achievements(number_of_medals, type_of_medal):
    dict1 = {}
    for i in range(len(number_of_medals)):
        dict1[type_of_medal[i]] = number_of_medals[i]
    for key,value in dict1.items():
        print(key, value)

with open("score.txt", "r") as scores:          #opened alias scores
    each_line = scores.readlines()              # reads each line of the text file score
    score_list = []                             # initialising the score_list as empty list
    for i in each_line: 
        score = i.strip("\n") 
        
                                                # striping the string \n from the list made directly from file
        score_list.append(int(score))           # appending the score_list with elements as integers to compare

l = len(score_list)                             # using l to get the last score of the game
if score_list[l-1] >= 2500:                     # dividing the scores into various categories
    print("Platinum Player")
elif 2000 <= score_list[l-1] <= 2450:
    print(str(score_list[l-1]) + " Terminator")
elif 1500 <= score_list[l-1] <= 1950:
    print(str(score_list[l-1]) + " Annihilator")
elif 1000 <= score_list[l-1] <= 1450:
    print(str(score_list[l-1]) + " Assasinator")
elif 500 <= score_list[l-1] <= 950:
    print(str(score_list[l-1]) + " Mehnat kar bhai")
print("Current Score:", score_list[l-1])
gold_medal = []   #for gold medal
silver_medal = [] #for silver medal
bronze_medal = [] # for bronze medal

for i in score_list:                           # dividing the score on the basis of medal distribution            
    if i >= 2500:
        gold_medal.append(i)                   # appending the gold_medal list so as to carry the score in it
    elif 2250 <= i <= 2450:
        silver_medal.append(i)                 # appending the silver_medal list so as to carry the score in it
    elif 2000 <= i <= 2200:
        bronze_medal.append(i)                 # appending the bronze_medal list so as to carry the score in it
number_of_gold = len(gold_medal)               # getting total numbers of gold_medal
number_of_silver = len(silver_medal)           # getting total numbers of silver_medal
number_of_bronze = len(bronze_medal)           # getting total numbers of bronze_medal

number_of_medals = [number_of_gold, number_of_silver, number_of_bronze]
type_of_medal = ["Gold Medal:   ", "Silver Medal: ", "Bronze Medal: "]
achievements(number_of_medals, type_of_medal)

print("Highest Score:", max(score_list))       # printing the highest score



        
    


    
    

    
        
    
