import random
import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)         # Speech rate (words per minute)
engine.setProperty('volume', 0.8)       # Volume level (0.0 to 1.0)

fortunes = [
    "You will have a pleasant surprise soon.",
    "A thrilling time is in your immediate future.",
    "Now is the time to try something new.",
    "You will make a valuable discovery.",
    "Happiness begins with facing life with a smile.",
    "A new opportunity will present itself today.",
    "You are destined for greatness.",
    "Your kindness will lead you to success."
]

def speak(text):
    engine.say(text)
    engine.runAndWait()

def open_fortune_cookie():
    print("\n🥠 Cracking open your fortune cookie...")
    time.sleep(1.5)
    
    fortune = random.choice(fortunes)
    lucky_number = random.randint(10000, 99999)
    
    # Print to console
    print("\n✨ Your Fortune: " + fortune)
    print("🍀 Lucky Number: " + str(lucky_number) + "\n")
    
    # Speak aloud
    speak("Your fortune is: " + fortune)
    speak("Your lucky number is " + str(lucky_number))

def main():
    print("Welcome to the Fortune Cookie Simulator!\n")
    speak("Welcome to the Fortune Cookie Simulator!")
    
    while True:
        input("Press Enter to open a fortune cookie...")
        open_fortune_cookie()
        
        again = input("Want another one? (y/n): ").strip().lower()
        if again != 'y':
            print("\nGoodbye! May your fortune come true. 🌟")
            speak("Goodbye! May your fortune come true.")
            break

if __name__ == "__main__":
    main()