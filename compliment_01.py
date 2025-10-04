# FILE NAME - compliment_01.py

# NAME: Norgie Caceres 
# DATE: 10/02/2025
# BRIEF DESCRIPTION: This script prompts the user for input and displays a compliment only if the respond matches the
# predefine positive answer.



# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience



########## ENTER YER CODE BELOW THIS LINE ##########
def main():
    compliment()

def compliment ():
    
    user_answer = input("Would you like a compliment? ")
    
    if user_answer == "yes".lower():
        print("You have wonderful eyes.\nThank you for playing.")        
    else:
        print("Thank you for playing.")
        


main()

########### END YER CODE ABOVE THIS LINE ###########

    



########################################
#          SAMPLE OUTPUT
########################################

'''
Would you like a compliment? yes
You have wonderful eyes.
Thank you for playing.
'''


'''
Would you like a compliment? y
Thank you for playing.
'''


'''
Would you like a compliment? Yes
Thank you for playing.
'''


'''
Would you like a compliment? no
Thank you for playing.
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. On a scale of 1 to 10 (where 10 is the hardest), how would you rate this lab?

I would give this a 4.


2. What was the hardest part of this lab?
The hardest part about this lab was finding the method using the lower() funtion properly.







'''