# Speech Synthesis Project

## Overview

This Python script allows you to narrate a .txt file into a .wav file with a different voice for each character by assigning them a name and a voice based on your system's available ones.

## Story Requirements

The story must be formatted in the following manner:

Char1:: Bla bla bla.

Char2:: Bla bla Char3.

Char1:: Bla bla bla.

Char3:: Char1, bla bla.

## Instructions

- Make sure all project files are in the same directory, including your story. This is also where the output will be generated.
- Install the packages in requirements.txt using pip or conda.
- Spacy requires additional data based on your prefered language to recognize the names of voice banks and use them as character names. For English, use "python -m spacy download en_core_web_sm". Check [the install page](https://spacy.io/usage) for more info. 
- Run main.py
- Input the options based on the prompts. Make sure the number of characters does not exceed the number of voice banks on your system.

## Implementation Details

Pyttsx3 is used for voice synthesis. Though limited in options, it's easy to setup, lightweight, and can be run offline since it relies on your system, which also determines the voice fidelity.

Spacy is used for named entity recognition.

The default Wave library is used to concatenate the individual lines of the story into the final output.

## References

- [Pyttsx3](https://github.com/nateshmbhat/pyttsx3)
- [Spacy](https://spacy.io)
- [Wave concatenation code](https://stackoverflow.com/a/2900266)
