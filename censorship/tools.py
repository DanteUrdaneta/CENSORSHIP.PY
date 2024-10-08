from pydub import AudioSegment
from pydub.generators import Sine
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

def get_similarity(word, target):
  try:
    word_embedding = model.encode(word, convert_to_tensor=True)
    target_embedding = model.encode(target, convert_to_tensor=True)

    cos_scores = util.pytorch_cos_sim(word_embedding, target_embedding)
    result = cos_scores.item()
    return result
  except Exception as e:
    print('Error gettin similarity:', e)
    return 0


def convertor(seconds):
   return int(float(seconds) * 1000)
 
def beep(end, start):
  try:
     duration = (start - end)
     residual = (duration * 0.3)
     print(duration)
     censure = Sine(1000).to_audio_segment(duration=duration + residual)
     return censure, residual
  except Exception as e:
    print('Error in beep:', e)
 
def replace_with_censure(audio_file, time_list):
  audio = AudioSegment.from_file(audio_file, format="mp3")

  if time_list:
    try:
      for time in time_list:
          starting = convertor(time['start'])
          ending = convertor(time['end'])
          censure, residual = beep(starting, ending)
          print(f'starting: {starting}, ending: {ending}, the type is: {type(starting)}, the type is: {type(ending)}')
          after = audio[:starting]
          before = audio[ending+residual:]
          audio = after + censure + before
    except Exception as e:
      print('Error in replace_with_censure:', e)
  return audio
 