#question answer quiz
print("KBC Quiz!\U0001F600")
questions=[["A.How many days do we have in a week?","5","7","8","9",2],
["B.Which animal is known as the 'Ship of the Desert?'","camel","horse","elephant","goat",1],
["C.Can you name the country from where Parmesan cheese comes?","India","China","Italy"," France",3],
["D.What type of tree do dates grow on?","Coconut","Pine","Palm","Birch",2],
["E.Which one is not amongst the Seven Wonders of the World?"," Mecca Madina",
 " Statue of Liberty","Taj Mahal"," The Great Wall of China",1],
["F.What is the hottest continent on Earth?","Asia","Europe","Africa","South America",3]]
total=0
prize=[1000,3000,5000,10000,15000,20000,35000,40000,55000]

for i in range(0,len(questions)):
    question=questions[i] 
    print(f"Question for Rs.{prize[i]}")
    if i is [0] or [1] or [2] or [3] or [4] or [5] or [6] or [7]:
       print(questions[i][0])
   
    print(f"(1).{question[1]}           (2).{question[2]}" )
    print(f"(3).{question[3]}           (4).{question[4]}" )
    reply=int(input("Enter your option number : "))
    if reply==question[-1]:
        print(f"you won Rs.{prize[i]}\n")
    else:
        print("OOPS!Wrong answer\U0001f910\n")
        break
    
total=total+prize[i]
print(f"Total amount you win=Rs.{total}\n")


