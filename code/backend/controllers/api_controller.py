import pandas as pd
import os
from flask import Blueprint, request, jsonify
from transformers import pipeline
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')
qa_model = pipeline('question-answering')

# Get the current directory of the file
current_directory = os.path.dirname(os.path.realpath(__file__))
# Construct the absolute path to the Excel file
excel_file_path = os.path.join(current_directory, '..', 'text_files', 'Multiprocessors.xlsx')

# Load data
df = pd.read_excel(excel_file_path)
dataset = df.values

embeddingsOfTheSubTopics = model.encode(dataset[:, 2])

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
  print(qa_model(question=question, context=selectedPassage))
  return qa_model(question=question, context=selectedPassage)

bp = Blueprint('api', __name__)

@bp.route('/api', methods=['POST'])
def api():
    try:
        request_data = request.get_json()
        question = request_data.get('question')
        ecodedQuestion = model.encode(question)
        # Check similarity
        cos_similarities = util.cos_sim(embeddingsOfTheSubTopics, ecodedQuestion)
        
        selectedSubTopicRow = getTheRelevantRow(question, cos_similarities)[1]
        selectedFileName = dataset[selectedSubTopicRow][3]
        print(selectedFileName)
        
        selectedPassage = getRelevantPassage(selectedFileName)[0]
        
        answer = answerForTheQuestion(question, selectedPassage)
                
        response_data = {"answer": f"{answer}"}
        return jsonify(response_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
