questionBank=[ {"Question":"What is the national animal of India?",
              "option":["A. Peacock",  "B. Lion", "C. Tiger", "D. Dog"],
              "Ans":"C",
              },
              {"Question":"Who is  known as the father of nation?",
              "option":["A. Rabindra Nath Tagore",  "B. Mahatma Gandhi",
                        "C. Sharukh Khan", "D. Salman Khan"],
              "Ans":"B",
              }
            ]

print('🥳Welcome to Kaun Banega Crorepati !')
total_winning=0
prizeMoney=[1000, 25000]
for i,q in enumerate(questionBank):
  print(f"\n The {i+1} question for money {prizeMoney[i]} is in front of you \n")
  print(q["Question"])
  for option in q["option"]:
    print(option)

  user_input=input("Choose any 1 option A , B, C, D: or Press Q for Quit ")
  user_input = user_input.upper()
  if(user_input=="Q"):
    print(f"Thank you for game and you won {total_winning}")
    break
  if(user_input == q["Ans"]):
    total_winning+=prizeMoney[i]
    print(f"\n Kya baat hai !! Aap jeet chuke hai {total_winning}")

  else:
    print("Uff answer galat hai , GAME OVER!!")
    total_winning=0
    break
