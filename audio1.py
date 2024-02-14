# import speech_recognition as sr
# # Initialize the recognizer
# recognizer = sr.Recognizer ( )
# # Use the default microphone as the source

# from gtts import gTTS
# from io import BytesIO
# from pydub import AudioSegment
# from pydub.playback import play

# def text_audio(text) :
#     # Text to be converted to audio
#     # text = "Hello! This is a test of text—to—speech conversion."
#     # Language (optional, default is English - 'en')
#     language = 'en'
#     # Create an instance of gTTS
#     tts = gTTS(text=text, lang=language)
#     # Save speech to BytesIO object (in—memory file)
#     mp3_fp = BytesIO()
#     tts.write_to_fp(mp3_fp)
#     mp3_fp.seek(0) # Move to the beginning of the file
    
#     # Load the audio from BytesIO using pydub
#     audio = AudioSegment.from_file(mp3_fp, format="mp3")
    
#     # Play the speech
#     play(audio)
    
# if __name__ == "__main__":
#     text_audio("Hello! This is a test of text—to—speech conversion.")