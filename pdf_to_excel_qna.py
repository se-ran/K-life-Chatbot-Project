#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import pandas as pd
import nltk
import pdfplumber
import re

nltk.download('punkt')


# In[ ]:


# 서울외국인포털/서울생활안내.xlsx

excel_file_path = 'C:/Users/Administrator/Desktop/chatbot/서울외국인포털/서울생활안내.xlsx'


# In[ ]:


# 생활법령정보.pdf
def extract_qa_from_pdf(pdf_file_path):
    try:
        with pdfplumber.open(pdf_file_path) as pdf:
            raw_text = "".join([page.extract_text() for page in pdf.pages])
        sentences = nltk.sent_tokenize(raw_text)
        filtered_sentences = [
            sentence for sentence in sentences if not any(
                phrase in sentence for phrase in ["2 / 5", "3 / 5", "4 / 5", "5 / 5", "6 / 6", "7 / 7", "8 / 8", "찾기쉬운 생활법령"]
            )
        ]

        questions, answers = [], []
        current_question, current_answer = None, None

        for sentence in filtered_sentences:
            sentence = sentence.strip()
            if not sentence:
                continue

            if sentence.endswith('?'):  # question
                if current_answer:  # Save the previous answer
                    answers.append(current_answer)
                    current_answer = None
                current_question = sentence
                questions.append(sentence)
            else:  # Otherwise, treat it as an answer
                if current_question:
                    current_answer = f"{current_answer} {sentence}".strip() if current_answer else sentence

        # Save the last answer
        if current_answer:
            answers.append(current_answer)

        return questions, answers

    except Exception as e:
        print("An error occurred:", e)
        return [], []

def save_qa_to_excel(pdf_file_paths, output_dir):
    for pdf_file_path in pdf_file_paths:
        try:
            questions, answers = extract_qa_from_pdf(pdf_file_path)
            data_list = [{"question": question, "answer": answer} for question, answer in zip(questions, answers)]
            pdf_name = os.path.basename(pdf_file_path).replace(".pdf", "")
            output_excel_path = os.path.join(output_dir, f"{pdf_name}_Q&A.xlsx")

            df = pd.DataFrame(data_list)
            df.to_excel(output_excel_path, index=False)
            print(f"Excel file has been saved: {output_excel_path}")

        except Exception as e:
            print(f"Error occurred while processing the file: {pdf_file_path}, Error: {e}")

if __name__ == "__main__":
    pdf_file_paths = [
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]다문화가족.pdf',
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]비자ㆍ여권.pdf',
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]외국인근로자 고용·취업.pdf',
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]외국인유학생.pdf',
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]외국인투자자.pdf',
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]재외동포.pdf',
        r'C:\Users\Administrator\Desktop\chatbot\생활법령정보\[pdf]출입국검역.pdf',
    ]
    output_dir = r'C:\Users\Administrator\Desktop\chatbot\생활법령정보'
    os.makedirs(output_dir, exist_ok=True) 
    save_qa_to_excel(pdf_file_paths, output_dir)



# In[ ]:


# 국민건강보험제도 외국인 유학생 질의응답자료.pdf
pdf_path = 'C:/Users/Administrator/Desktop/chatbot/숭실대 외국인 건강보험/2. 국민건강보험제도 외국인 유학생 질의응답자료.pdf'

def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text


def extract_qna_pairs_from_text(text):
    qna_pairs = []
    pattern = r'Q\d+\n(.+?)\n(?:A\d+ )?(.+?)(?=\nQ\d+|$)'  # Adjust pattern for Q&A extraction
    matches = re.finditer(pattern, text, re.DOTALL) # Match questions and answers
    for match in matches:
        question = match.group(1)
        answer = match.group(2)
        qna_pairs.append((question.strip(), answer.strip()))

    return qna_pairs

# 1. Extract text from the PDF
extracted_text = extract_text_from_pdf(pdf_path)

# 2. Remove page numbers (e.g., '- 1 -')
pattern_page_number = r'- \d+ -'
modified_text = re.sub(pattern_page_number, '', extracted_text)

# 3. Remove lines containing the word '설명' and empty lines
lines = modified_text.splitlines()
filtered_lines = [line for line in lines if '설명' not in line]
modified_text = '\n'.join(filtered_lines).strip()

# 4. Extract Q&A pairs using the regex pattern
qna_pairs = extract_qna_pairs_from_text(modified_text)

# 5. Output results & save to an Excel file
data_list = []
for idx, (question, answer) in enumerate(qna_pairs, 1):
    print(f"Question {idx}: {question}")
    print(f"Answer {idx}: {answer}")
    print()
    data_list.append({"질문": question, "답변": answer})
    
df = pd.DataFrame(data_list)
df.to_excel("질문과답변.xlsx", index=False)


# In[ ]:




