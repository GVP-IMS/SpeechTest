### Import Space ###

import os
import pyttsx3
import wave
import spacy

# Get working directories
current_dir = os.getcwd()
line_dir = os.path.join(current_dir, 'lines')

# Record each speaker's lines
def get_lines(char_count, story_file_name, special="No"):

    # Start voice engine and get different voices
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    # Load NLP tool for named entity recognition
    nlp = spacy.load("en_core_web_sm")

    # Get characters from speaker voices
    chars = []
    for voice in voices:
        for entity in nlp(voice.name).ents:
            if entity.label_ == 'PERSON':
                chars.append(str(entity).split()[0])
                break

    # Replace names in story with characters
    text = ""
    with open(story_file_name+'.txt') as file:
        text = file.read()
    for i in range(char_count):
        text = text.replace(f"Char{i+1}", str(chars[i]))
    with open(story_file_name+'_edited.txt', "w") as file:
        file.write(text)
    
    # Get lines of story
    with open(story_file_name+'_edited.txt') as f:
        lines = [line.rstrip() for line in f]

    # Set character & speaker voice and get audio for each line
    normal_rate = engine.getProperty('rate')-20

    for id, line in enumerate(lines):
        engine.setProperty('rate', normal_rate)
        speaker, dialogue = line.split('::')

        # Special = specific settings for the crazy beam default story, ignore otherwise
        if special == "Yes":
            if chars.index(speaker) == 1 and id == 7:
                engine.setProperty('voice', voices[chars.index(speaker)].id)
            elif chars.index(speaker) == 1:
                engine.setProperty('rate', 320)
                engine.setProperty('voice', voices[chars.index(speaker)].id)
            else:
                engine.setProperty('voice', voices[chars.index(speaker)].id)
        else:
            engine.setProperty('voice', voices[chars.index(speaker)].id)
        
        # Save audio
        file = os.path.join(line_dir,f'{id}{speaker}.wav')
        engine.save_to_file(dialogue, file)
        engine.runAndWait()

# Merge individual recordings into the final story
def merge_lines(line_dir, story_file_name):

    # Get audio data
    lines = []
    for filename in os.listdir(line_dir):
        fullname = os.path.join(line_dir, filename)
        w = wave.open(fullname, 'rb')
        lines.append([w.getparams(), w.readframes(w.getnframes())])
        w.close()

    # Merge and save audio
    # Copied from: https://stackoverflow.com/a/2900266
    output = wave.open(story_file_name + '_final.wav', 'wb')
    output.setparams(lines[0][0])
    for i in range(len(lines)):
        output.writeframes(lines[i][1])
    output.close()

# Main
def main():

    # Create lines folder because GitHub is [SILLY] and doesn't let me upload empty folders normally
    if not os.path.exists(line_dir):
        os.makedirs(line_dir)

    print("Input the number of characters in the story. Make sure you have enough voices, Pytssx3 uses your system's voice banks!")
    char_count = int(input())
    print("Input the file name of the story. It must be in .txt format, but don't write the extension.")
    story_file_name = input()
    print("Input 'No' if you're NOT generating the provided beam story. Otherwise, input 'Yes' to speed up certain parts as intended.")
    special = input()
    if special != "Yes":
        special == "No"

    get_lines(char_count, story_file_name, special)
    merge_lines(line_dir, story_file_name)

if __name__ == "__main__":
    main()
