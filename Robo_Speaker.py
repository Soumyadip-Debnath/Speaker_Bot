import os

if __name__ == '__main__':
    print("Welcome to Robo Speaker 1.0")
    while True:
        x = input("Enter what you want me to Speak for You:")
        command = f"PowerShell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{x}')"
        os.system(command)
 