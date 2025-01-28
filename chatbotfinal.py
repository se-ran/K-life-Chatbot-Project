import altair as alt
import streamlit as st
from streamlit_chat import message
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import json
import openai
from sentence_transformers import SentenceTransformer, util
from rank_bm25 import BM25Okapi
import torch

openai.api_key = ###
excel_file_path = r"C:\Users\Administrator\Desktop\chatbot\chatbot_embedding.csv"

df = pd.read_csv(excel_file_path)
df['embedding'] = df['embedding'].apply(json.loads)

corpus = df['질문'].apply(str)
tokenized_corpus = [doc.split() for doc in corpus]
bm25 = BM25Okapi(tokenized_corpus) # BM25 Model Initialization

model = SentenceTransformer('klue/roberta-base') # Load KLUE RoBERTa Model

# Conversation Script Initialization Function
def initialize_conversation():
    return [{"role": "system", "content": "You are an assistant who provides information about Korean life in Korea to foreigners living in Korea."}]

# Main Application
def main():
    st.header('Foreign Resident Consultation Chatbot')
    st.markdown("Providing information on health insurance, related laws, and life in Seoul")
    conversation = initialize_conversation()
    
    if 'generated' not in st.session_state:
        st.session_state.generated = []

    if 'past' not in st.session_state:
        st.session_state.past = []


    user_input = st.text_input("You:", key="user_input")
    
    if st.button("Send"):
        if user_input:
            st.session_state.past.append(user_input)
            conversation.append({"role": "user", "content": user_input})
            
            user_embedding = model.encode(user_input, convert_to_tensor=True)
            
            answer_embeddings = [model.encode(answer, convert_to_tensor=True) for answer in df['질문']]
            question_embeddings = torch.stack(answer_embeddings)
            similarities = util.pytorch_cos_sim(user_embedding, question_embeddings)

            max_similarity_values, max_similarity_indices = similarities.max(dim=1)
            max_similarity_index = max_similarity_indices[torch.argmax(max_similarity_values)].item()
            max_similarity_value = max_similarity_values[torch.argmax(max_similarity_values)].item()

            if max_similarity_value > 0.85:
                answer = df.loc[max_similarity_index, '답']
                st.session_state.generated.append(answer)  # Save the generated answer

            else:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=conversation
                )
                gpt_response = response['choices'][0]['message']['content']
                st.session_state.generated.append(gpt_response) # Save the generated answer

    # Display past conversations and answers
    for i in range(len(st.session_state.past)):
        message(st.session_state.past[i], is_user=True, key=str(i) + '_user')
        if len(st.session_state.generated) > i:
            message(st.session_state.generated[i], key=str(i) + '_bot')

if __name__ == "__main__":
    main()
