import openai
API_KEY='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'
model_id='whisper-1'
media_file_path=url('https://www.youtube.com/watch?v=QxU-JrfA824')
media_file=open(media_file_path,'rb')

response=openai.Audio.translate(
    api_key=API_KEY,
    model=model_id,
    file=media_file
)
print(response.data['text'])
