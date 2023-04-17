!pip -qqq install git+https://github.com/openai/whisper.git 
  
import whisper
import torch 
import os

device = "cuda" if torch.cuda.is_available() else "cpu"
whisper_model = whisper.load_model("large", device=device)

!pip -qqq install pytube
from pytube import YouTube

def video_to_audio(video_URL, destination, final_filename):

  # Get the video
  video = YouTube(video_URL)

  # Convert video to Audio
  audio = video.streams.filter(only_audio=True).first()

  # Save to destination
  output = audio.download(output_path = destination)

  _, ext = os.path.splitext(output)
  new_file = final_filename + '.mp3'

  # Change the name of the file
  os.rename(output, new_file)

# Video to audio
video_URL = 'https://www.youtube.com/watch?v=oL1uem6-3m4'
destination = "."
final_filename = "ServiceNowTraining"
video_to_audio(video_URL, destination, final_filename)

audio_file = "ServiceNowTraining.mp3"
result = whisper_model.transcribe(audio_file)
print(result["text"])


