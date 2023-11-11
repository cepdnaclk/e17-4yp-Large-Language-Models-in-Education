import pandas as pd
import os
import time
from flask import Blueprint, request, jsonify
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util
from utilities.cache_lfu import CacheLFU

model = SentenceTransformer('all-MiniLM-L6-v2')
qa_model = pipeline(model="twmkn9/bert-base-uncased-squad2")

# Get the current directory of the file
current_directory = os.path.dirname(os.path.realpath(__file__))
# Construct the absolute path to the Excel file
excel_file_path = os.path.join(current_directory, '..', 'text_files', 'Multiprocessors.xlsx')

# Load data
df = pd.read_excel(excel_file_path)
dataset = df.values

embeddingsOfTheSubTopics = model.encode(dataset[:, 2])

# Create a cache for Multiprocessors
cacheMP = CacheLFU("MP")

# Request count for external API
request_count = 0

def call_API(request, cache):
  print("* * * * * * * From API * * * * * * * ")
  
  # Add delay to simulate API call
  time.sleep(0.5)
  
  global request_count 
  request_count += 1
  api_response = "API response - " + str(request_count)
  response = {"answer": api_response}
  print(response)
  
  # Add the new record to the cache
  new_record = {'Question': request, 'Response': api_response, 'Access Count': 0}
  cache.add_record(new_record)
  return api_response

def cache_handler(request, encoded_request, category):
  print("Cache handler called")
  print(cacheMP.cache_df)
  if category == "MP":
    cos_sim = util.cos_sim(cacheMP.embeddings_cache, encoded_request)
    if (max(cos_sim) > 0.75):
      print("* * * * * * * From Cache * * * * * * * ")
      print(cos_sim.argmax().item())
      # Update the access count
      cacheMP.update_count(cos_sim.argmax().item())
      return cacheMP.get_response(cos_sim.argmax().item())
    else:
      return call_API(request, cacheMP)
  # add other categories

def getTheRelevantRow(question, cos_similarities):
  max = cos_similarities[0]
  maxIndex = 0
  for idx, score in enumerate(cos_similarities):
    if (score > max):
      max = score
      maxIndex = idx
      
  return max, maxIndex

def getRelevantPassage(filename):
    text_file_path = os.path.join(current_directory, '..', 'text_files', 'Files', f'{filename}.txt')
    with open(text_file_path, encoding="utf8") as r:
        lines = r.readlines()
        return lines
    
def answerForTheQuestion(question, selectedPassage):
  resp = qa_model(question=question, context=selectedPassage)
  return resp['answer']

bp = Blueprint('api', __name__)

@bp.route('/api', methods=['POST'])
def api():
    try:
        request_data = request.get_json()
        question = request_data.get('question')
        category = request_data.get('category')
        
        # Currently only Multi Processor context is available
        if category != "MP":
          return jsonify({"error": "Invalid category"}), 400
        
        encoded_question = model.encode(question)
        
        # Check similarity
        cos_similarities = util.cos_sim(embeddingsOfTheSubTopics, encoded_question)
        
        # Call cache handler if the max similarity value is less than 0.5
        maxSimilarity = max(cos_similarities)
        print(maxSimilarity)
        if maxSimilarity < 0.5:
          print("Calling cache handler")
          response_from_cache_handler = cache_handler(question, encoded_question, category)
          print(response_from_cache_handler)
          return jsonify({"answer": response_from_cache_handler}), 200
        else:
          print("Check answer from context")
                
        selectedSubTopicRow = getTheRelevantRow(question, cos_similarities)[1]
        
        selectedFileName = dataset[selectedSubTopicRow][3]
        
        selectedPassage = getRelevantPassage(selectedFileName)[0]
        
        answer = answerForTheQuestion(question, selectedPassage)
                
        response_data = {"answer": f"{answer}"}
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
