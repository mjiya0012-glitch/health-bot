print("💚 Health & Wellness ChatBot")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()
    if user == "hi" or user == "hello":
        print("🤖 Hello! I am your Health & Wellness ChatBot.")
    elif "water" in user:
        print("🤖 Drinking 7-8 glasses of water daily helps keep your body hydrated.")
    elif "exercise" in user or "workout" in user:
        print("🤖 Regular exercise improves physical and mental health.")
    elif "sleep" in user:
        print("🤖 Adults should get around 7-8 hours of sleep daily.")
    elif "food" in user or "diet" in user:
        print("🤖 Eat fruits, vegetables, and balanced meals for good health.")
    elif "stress" in user:
        print("🤖 Meditation, exercise, and proper sleep can help reduce stress.")
    elif "mental health" in user:
        print("🤖 Talking to friends, family, or a counselor can support mental wellness.")
    elif "yoga" in user:
        print("🤖 Yoga helps improve flexibility, focus, and relaxation.")
    elif "bmi" in user:
        print("🤖 BMI means Body Mass Index. It helps measure body fitness level.")
    elif "motivation" in user:
        print("🤖 Small healthy habits every day lead to big changes over time!")
    elif user == "bye":
        print("🤖 Stay healthy and take care! Goodbye 👋")
        break
    else:
        print("🤖 Sorry, I can only answer health and wellness related questions.")