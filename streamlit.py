import streamlit as st
import googletrans
from googletrans import Translator
from gtts import gTTS
import os

# Function to translate text
def translate_text(text, target_lang):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang)
    return translated_text.text

# Function to convert text to speech
def text_to_speech(text, target_lang, voice_gender):
    lang = target_lang
    if target_lang == "hi":
        # Hindi does not support accents
        lang = "hi"

    tts = gTTS(text=text, lang=lang, slow=False, lang_check=False)
    tts.save("output.mp3")

# Main function to run the app
def main():
    st.title("Text-to-Speech Translation App")

    # Text input field
    input_text = st.text_area("Enter text to translate:", "")

    # Dropdown to select source and target languages
    source_lang = "en"  # Source language is English by default
    target_lang = st.selectbox("Select Target Language", googletrans.LANGUAGES.keys())

    # Radio button group to select voice gender
    voice_gender = st.radio("Select Voice Gender:", ("Male", "Female"))

    # Button to initiate translation and speech synthesis
    if st.button("Translate and Speak"):
        # Perform translation
        translated_text = translate_text(input_text, target_lang)

        # Display translated text
        st.subheader("Translated Text:")
        st.write(translated_text)

        # Convert translated text to speech
        text_to_speech(translated_text, target_lang, voice_gender)

        # Play the audio
        st.audio("output.mp3", format='audio/mp3')

if __name__ == "__main__":
    main()
