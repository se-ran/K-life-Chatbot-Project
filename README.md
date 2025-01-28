# Chatbot Development to Assist Foreign Counselors in Handling Tasks Efficiently

### Project Background
This project addresses the challenges faced by foreign counselors at the Seoul Foreign Residents Support Center, who provide multilingual support in languages like Chinese, Mongolian, and Vietnamese. Despite their efforts, they often face inefficiencies due to limited expertise in legal and administrative matters, causing delays while verifying information. With a growing demand for non-Korean and non-English consultations, these issues impact service quality. To improve efficiency and support counselors, we developed a **chatbot** to provide quick access to critical information and streamline their workflow.

### Data Sources

The chatbot is built using reliable data from the following sources:

1. **Q&A Data on National Health Insurance for Foreign Students** (Source: National Health Insurance Service)
2. **Seoul Living Guide** (Source: Seoul Foreign Portal)
3. **100 FAQs on Major Foreign-Related Laws** (Source: Korea Ministry of Government Legislation)
4. **Q&A Data from the Korea Foreign Workers Support Center** (Source: Korea Foreign Workers Support Center)

### Implementation Process

1. **Data Preparation**
   - Extracted text from PDFs using **pdfplumber**.
   - Organized the extracted text and converted it into Excel files before merging.

2. **Natural Language Processing**
   - Used **NLTK** library for text preprocessing and analysis.

3. **Chatbot Development**
   - Built an intuitive chatbot UI using the **Streamlit** framework.
   - The chatbot is designed to quickly provide critical information that foreign counselors frequently need.
