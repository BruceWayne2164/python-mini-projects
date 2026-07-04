questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "Which language is used for AI and Data Science?",
        "options": ["A. C", "B. Java", "C. Python", "D. HTML"],
        "answer": "C"
    },
    {
        "question": "How many continents are there?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "C"
    },
    {
        "question": "Which planet is called the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "What does CPU stand for?",
        "options": [
            "A. Central Processing Unit",
            "B. Computer Processing Unit",
            "C. Central Program Unit",
            "D. Control Processing Unit"
        ],
        "answer": "A"
    }
]

score = 0

print("=" * 40)
print("        PYTHON QUIZ APPLICATION")
print("=" * 40)

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print("❌ Wrong!")
        print("Correct Answer:", q["answer"])

print("\n" + "=" * 40)
print("Quiz Finished!")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("🏆 Excellent!")
elif percentage >= 60:
    print("👍 Good Job!")
else:
    print("📚 Keep Practicing!")
