# Translation-App 
#### LingoBridge Translation Software

## Description

This project was created for the software LingoBridge, which is a Translation Platform focused on real-time connection between speakers of different languages. 

## Overview

The purpose of this application is to bridge language barriers through instant text translation. Users can select input and output languages, enter text, and receive immediate translations displayed side by side.

## Key features include
- Side-by-side text translation
- Multiple language selection
- Simple Streamlit-based user interface
- Real-time translation using GoogleTranslator
- Real-time translation history panel
- Character Count
- Friendly Translation Reactions
- Typing Mood Indicator

## Prerequisites

#### Before running this project, ensure you have the following installed:

- Python 3.8 or higher
- pip (Python package manager)
- Basic understanding of Python and command-line usage
- deep-translator
## Installation Instructions

 1. Clone or download the project files to your local machine.
   ```
   git clone https://github.com/emanual3murry-coder/LingoBridge.git
   cd Language-Translator
   ```
 3. Create a virtual environment
  ```
     python -m venv venv
     source venv/bin/activate   # macOS/Linux
     venv\Scripts\activate      # Windows
   ```
 3. Install the required dependencies using pip:

    ```
    pip install streamlit
    pip install deep-translator

## How to Run the Program

1. From the root directory, run the Streamlit application:

   ```   
   streamlit run Translator2.py
   
2. The application will automatically open in your web browser.
   If it does not, navigate to:
   ```
   http://localhost:8501
   ```
## Usage Instructions

1. Upon launching the application, select the **source language** (input language).
2. Select the **target language** (output language).
3. Enter the word or phrase you wish to translate into the text box on the left.
4. Click the **Translate** button.
5. The translated text will appear on the right side of the screen.
6. Previous translations appear in the sidebar history panel.

***To improve user experience and personality, the app includes dynamic feedback messages, friendly success responses, and thoughtful empty states that guide users naturally through the translation process.*** 

## License**

This project is not licensed and is intended for educational purposes only.

Acknowledgements
Streamlit for the web application framework
deep-translator for translation functionality
GoogleTranslator API via deep-translator

