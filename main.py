from model import chain
from utils import get_voice_input, speak, remove_think_tags

def handle_conversation():
    context = ""
    print("Welcome to the AI Voice Assistant. Say 'exit' to quit.\n")

    while True:
        try:
            user_input = None
            while not user_input:
                user_input = get_voice_input()
                if user_input and user_input.lower() == "exit":
                    print("Exiting. Goodbye.")
                    return

            result = chain.invoke({
                "context": context,
                "question": user_input
            })

            reply_raw = result.content if hasattr(result, 'content') else str(result)
            clean_reply = remove_think_tags(reply_raw)

            print(f"Bot: {clean_reply}")
            speak(clean_reply)

            context += f"\nUser: {user_input}\nAI: {clean_reply}"
        except KeyboardInterrupt:
            print("Exiting. Goodbye.")
            break

if __name__ == "__main__":
    handle_conversation()
