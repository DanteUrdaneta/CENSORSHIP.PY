from faster_whisper import WhisperModel
from censorship.tools import *

class Censorship_Audio():
  def __init__(self, model = 'large-v3', device = 'cpu', compute_type = 'int8'):
    self.model = WhisperModel(model, device = device, compute_type = compute_type)
  
  def whisper(self, audio):
    segments, _ = self.model.transcribe(audio, beam_size = 5, word_timestamps = True)
    return segments
  
  def similarity_search(self, audio, word):
    segments = self.whisper(audio)
    localization_list = []
    
    try:
      for segment in segments:
        for w in segment.words:
          if get_similarity(w.word, word) >= 0.7:
            localization = {'start': w.start, 'end': w.end}
            localization_list.append(localization)
          elif w.word == word:
            localization = {'start': w.start, 'end': w.end}
            localization_list.append(localization)

      return localization_list
            
    except Exception as e:
      print('Error in similarity search:', e)
      return  localization_list
  
  
  def censure_audio(self, audio, output_file, word_list):
    try:
      if word_list:
        for word in word_list:
            localization_list = self.similarity_search(audio, word)
            print(f'the word is: {word} and the localization list is: {localization_list}')
            sound = replace_with_censure(audio, localization_list)
            sound.export(output_file, format = output_file.split('.')[-1])
            audio = output_file
      return print(f'Censure done! the file {output_file} is ready!')
    except Exception as e:
      print('Error in censure_audio:', e)
      
    
  def return_audio_text(self, audio):
    try:
      result = ''
      segments = self.whisper(audio)
      for segment in segments:
        result += segment.text
      return result
    except Exception as e:
      print('Error in return_audio_text:', e)