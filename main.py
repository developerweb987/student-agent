import openai

# 🔑 Set your OpenAI API key here directly
openai.api_key = ""



def run_agent():
    print("\n🎓 Welcome to the Smart Student Agent Assistant!")
    print("Type 'exit' to quit.")
    print("Ask academic questions, request study tips, or paste text to summarize.\n")

    while True:
        user_input = input("📚 You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break

        try:
            response = openai.chat.completions.create(
                model="gpt-4o",  # Use "gpt-3.5-turbo" if "gpt-4o" gives error
                messages=[
                    {"role": "system", "content": "You are a smart assistant for students. You answer academic questions, give study tips, and summarize small text passages."},
                    {"role": "user", "content": user_input}
                ],
                temperature=0.5
            )

            answer = response.choices[0].message.content
            print(f"🤖 Agent: {answer}\n")

        except Exception as e:
            print(f"❌ Error: {e}\n")

if __name__ == "__main__":
    run_agent()
