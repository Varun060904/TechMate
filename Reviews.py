import ollama

text=""

cat=input("What category device? eg : Phone , Laptops , Tv : ")

brand=input("what brand is your product from? eg: Apple , Samsung : ")

mod=input("What is the model of the product? eg: iphone 13 , X75 : ")

price=input("Enter the MRP of the product in Rs : ")

print("Answer the following questions based on numbers ranging from 1-10\n")

overall=int(input("Overall how much would you rate the product considerin all the aspects: "))

review1=int(input("How has the performance of the gadget met or exceeded your expectations: "))

review2=int(input("If your product is a battery oriented product - In terms of battery life, how satisfied are you with the device's ability to hold a charge and meet your daily usage needs?: "))

review3=int(input("How would you rate the build quality and durability of the gadget based on your usage and any potential wear and tear?: "))

review4=int(input("In terms of design and aesthetics, how visually appealing and ergonomic do you find the gadget?: "))

review5=int(input("How satisfied are you with the range and quality of connectivity options, such as Wi-Fi, Bluetooth, and any other relevant features?: "))

avg_rev_pts=round((review1+review2+review3+review4+review5)/5,2)
 
score=round((avg_rev_pts/10)*5,2)



print("\nAnswer the following questions with a text based answer \n")

review6=input("Can you share your experience with the user interface and overall ease of use of the gadget?")

review7=input("What standout features of the gadget have had the most positive impact on your daily life or activities?")

review8=input("Have you encountered any issues or challenges with the gadget, and if so, how responsive and effective was the customer support in resolving them?")

review9=input("Can you provide insights into the software and firmware updates you've received and how they have impacted the overall performance and functionality of the gadget?")

review10=input("Can you share a specific scenario or experience where the gadget proved to be exceptionally useful or, conversely, fell short of expectations?")

print("\nFinally provide us with the overall user expirience review")

overall_rev=input("Finally, kindly provide your overall assessment of the product, highlighting its strengths and weaknesses. Share your overall experience, and if given the opportunity to communicate with the brand, offer specific suggestions for product enhancement. Additionally, identify the standout features that would make you recommend this product to others : ")

print("\n\n*************************************************** PROCESSING THE DATA PLEASE WAIT ***************************************************\n\n")

stream = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': f"Explore and analyze user feedback on a gadget:1. **User Interface and Ease of Use:**- User Experience: {review6}2.**Standout Features:**- Impactful Features: {review7}3. **Issues and Customer Support:**- Challenges Faced: {review8}4. **Software and Firmware Updates:**- Impact on Performance: {review9}5. **Specific Scenarios:**- Noteworthy Experiences: {review10}.Analyze and summarize the key points from each response, providing insights into the overall satisfaction and areas for improvement with the gadget. Consider the user's perspective on user interface, standout features, customer support effectiveness, impact of updates, and specific scenarios. Keep the analysis concise and informative."}],
    stream=True,
)

with open('output.txt', 'a') as file:
    file.write(f"\n\n\nCategory:{cat} brand:{brand} model:{mod} price:{price}\n")
    file.write(f"Over Product Score (out of 5 pts) : {score}\n")
    
    for chunk in stream:
        file.write(chunk['message']['content'])

stream = ollama.chat(
    model='llama2',
    messages=[{'role': 'user', 'content': f"Given a user response to the following question about Category:{cat} brand:{brand} model:{mod}: kindly provide your overall assessment of the product, highlighting its strengths and weaknesses. Share your overall experience, and if given the opportunity to communicate with the brand, offer specific suggestions for product enhancement. Additionally, identify the standout features that would make you recommend this product to others.Use Illama2 to analyze the user's feedback, focusing on key aspects such as strengths, weaknesses, overall experience, suggestions for improvement, and standout features mentioned for potential recommendations. Provide insights and summaries based on the user's input only: {overall_rev}."}],
    stream=True,
)
with open('output.txt','a') as file:
    file.write("\nOverall review of the product : \n")
    for chunk in stream:
        file.write(chunk['message']['content'])

print("Output successfully written in output.txt")


