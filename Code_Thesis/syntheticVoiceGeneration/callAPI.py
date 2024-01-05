import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="key/masterthesis-390612-b3d223acf14f.json"
key = "AIzaSyA50vQuWQbZgYLTpYWzWi0m26cDhFXLtz8"

def synthesize_text(_id, text, pitch, gender):
    """Synthesizes speech from the input string of text."""
    from google.cloud import texttospeech

    client = texttospeech.TextToSpeechClient()

    input_text = texttospeech.SynthesisInput(text=text)

    # Note: the voice can also be specified by name.
    # Names of voices can be retrieved with client.list_voices().
    if gender == "f":       
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-F",     #en-US-Neural2-F, en-US-Wavenet-E, en-US-Studio-O
            ssml_gender= texttospeech.SsmlVoiceGender.FEMALE,
        )
    if gender == "m":
        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-J",     #en-US-Neural2-J", en-US-Wavenet-J, en-US-Studio-M
            ssml_gender= texttospeech.SsmlVoiceGender.MALE,
        )
    
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.LINEAR16,
        pitch= pitch
    )

    response = client.synthesize_speech(
        request={"input": input_text, "voice": voice, "audio_config": audio_config}
    )

    # The response's audio_content is binary.
    with open("C:/Users/anton/OneDrive/Antons-Dokumente/TU_Berlin/Masterarbeit/HateSpeech/Code_Thesis/data/outputVoices/sample_{}_p{}_{}.wav".format(_id,pitch,gender), "wb") as out:
        out.write(response.audio_content)
        print('Audio content written to file /output')