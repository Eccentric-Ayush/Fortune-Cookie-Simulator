# Fortune-Cookie-Simulator
This Python program simulates cracking open a fortune cookie.
# Fortune Cookie Simulator with Text-to-Speech

## Description

This Python program simulates cracking open a fortune cookie. Each time you press Enter, it displays a random fortune and lucky number, then reads them aloud using the pyttsx3 text-to-speech engine.

## Features

- Randomly selects a fortune message from a predefined list  
- Generates a five-digit lucky number  
- Reads the fortune and number aloud with adjustable speech rate and volume  
- Simple console interface for repeated use  

## Requirements

- Python 3.x  
- pyttsx3  

## Installation

1. Clone or download this repository.  
2. Install pyttsx3:  
   ```bash
   pip install pyttsx3
   ```

## Usage

1. Run the script:  
   ```bash
   python fortune_cookie.py
   ```  
2. Press **Enter** to crack a cookie.  
3. Listen as the program speaks your fortune and lucky number.  
4. Type `y` to open another cookie or any other key to exit.

## Customization

- Edit the `fortunes` list in the script to add or change messages.  
- Adjust voice properties like rate and volume via `engine.setProperty`.  
- Integrate other pyttsx3 voices by querying available voices and switching the `voice` property.