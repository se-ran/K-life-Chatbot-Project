# Chatbot Development to Assist Foreign Counselors in Handling Tasks Efficiently

### Project Background
This project addresses the challenges faced by foreign counselors at the Seoul Foreign Residents Support Center, who provide multilingual support in languages like Chinese, Mongolian, and Vietnamese. Despite their efforts, they often face inefficiencies due to limited expertise in legal and administrative matters, causing delays while verifying information. With a growing demand for non-Korean and non-English consultations, these issues impact service quality. To improve efficiency and support counselors, we developed a **chatbot** to provide quick access to critical information and streamline their workflow.

### Data Sources

The chatbot is built using reliable data from the following sources:

1. **Q&A Data on National Health Insurance for Foreign Students** (Source: National Health Insurance Service)      
   국민건강보험제도 외국인 유학생 질의응답자료 (출처: 건강보험공단)      
3. **Seoul Living Guide** (Source: Seoul Foreign Portal)      
   서울 생활 안내 (출처: 서울 외국인 포털)      
5. **100 FAQs on Major Foreign-Related Laws** (Source: Korea Ministry of Government Legislation)      
   사례로 보는 백문백답 외국인 관련 주요 법령 (출처: 법제처)      
7. **Q&A Data from the Korea Foreign Workers Support Center** (Source: Korea Foreign Workers Support Center)      
   한국 외국인 노동자 지원센터 Q&A 자료 (출처: 한국외국인 노동자 지원센터)      

### Data Processing
Extracted, processed, and analyzed PDF data using pdfplumber and NLTK, then consolidated it into Excel files for streamlined usage.

### Core Technologies
- BM25 Algorithm: Applied to build a retrieval-based model for matching user queries with data.
- SentenceTransformer: Utilized the klue/roberta-base model to generate embeddings for similarity analysis.
- Streamlit: Developed the user interface for real-time chatbot interaction.
- OpenAI GPT-3.5-Turbo: Used for generating responses to queries not covered in the dataset.

### Application Workflow
1. The user enters a query through the chatbot interface.
2. The query is matched against existing Q&A data using the BM25 algorithm.
3. Response Generation
- If a high-similarity match is found (similarity > 0.85), the system retrieves the corresponding answer from the dataset.
- If no close match exists, the query is sent to GPT-3.5-Turbo for a generated response.
4. The conversation is displayed interactively, maintaining a seamless user experience.
