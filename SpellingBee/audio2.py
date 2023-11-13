import requests
import json

# Replace with your Text to Speech subscription key
subscription_key = "dfd20c4ccd214c73aeb5f9b23a9387f8"

# Replace with the voice you want to use
voice = "en-US-AriaNeural"

# Replace with the text you want to convert to speech
text = "Capital Z"

# Specify the language and format of the audio file
headers = {
    "Ocp-Apim-Subscription-Key": subscription_key,
    "Content-Type": "application/ssml+xml",
    "X-Microsoft-OutputFormat": "riff-24khz-16bit-mono-pcm",
    "User-Agent": "en-US-AriaNeural"
}

# Create the SSML request
body = f"<speak version='1.0' xml:lang='en-us'><voice xml:lang='en-us' xml:gender='Female' name='{voice}' rate='0.7'>{text}</voice></speak>"

# Define el nombre del archivo WAV que deseas
output_file_name = "Capital Z.wav"

# Make the request to the Text to Speech API
response = requests.post("https://eastus.tts.speech.microsoft.com/cognitiveservices/v1", headers=headers, data=body)

# Guarda el archivo de audio generado con el nombre personalizado
with open(output_file_name, "wb") as audio_file:
    audio_file.write(response.content)

print(f"The file has been saved to {output_file_name}.")
