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

### Implementation Process

1. **Data Preparation**
   - Extracted text from PDFs using **pdfplumber**.
   - Organized the extracted text and converted it into Excel files before merging.

2. **Natural Language Processing**
   - Used **NLTK** library for text preprocessing and analysis.

3. **Chatbot Development**
   - Built an intuitive chatbot UI using the **Streamlit** framework.
   - The chatbot is designed to quickly provide critical information that foreign counselors frequently need.
  
### Tech Stack

- **Python**: For data processing and natural language processing
- **pdfplumber**: For extracting text from PDFs
- **NLTK**: For natural language processing
- **Streamlit**: For building the chatbot interface
