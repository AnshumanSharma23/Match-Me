
# Resume Matcher Tool



https://github.com/AnshumanSharma23/Match-Me/assets/158674716/5ae5725e-2493-43fc-9d67-5f95a4edf968





## Introduction
The Resume Matcher Tool is an innovative web application designed to revolutionize the recruitment process. Leveraging OpenAI's powerful API, this tool automates the matching of candidates' resumes with job postings, ensuring a high degree of alignment in terms of skills and requirements. This project aims to streamline the recruitment workflow, making it easier for recruiters to identify suitable candidates efficiently.

## Features
- **Resume Analysis**: Automatically analyzes the content of a resume to extract relevant skills and experience.
- **Job Matching**: Compares candidate profiles against job descriptions to find the best matches based on criteria such as skills, experience, and qualifications.
- **User-Friendly Interface**: Provides an intuitive web interface for both recruiters and candidates to submit resumes and job postings.
- **Feedback System**: Allows users to provide feedback on the match suggestions, which continuously improves the accuracy of the tool.

## Technologies Used
- **Streamlit**: Streamlit for creating interactive web applications with Python.
- **OpenAI API**: Utilized for resume and job description analysis.
- **Python**: Backend logic implemented in Python.
- **HTML/CSS/JavaScript**: Frontend interface developed using basic web technologies.
- **Git**: Version control system for collaborative development.

## Getting Started

### Prerequisites
- Python 3.8+
- An OpenAI API key

### Installation

1. **Clone the repository**
   

2. **Set up environment variables**
   - Create a `.env` file in the project root directory.
   - Add your OpenAI API key to the `.env` file:
     ```sh
     OPENAI_API_KEY="your-api-key"
     ```

3. **Install required Python packages**
   ```sh
   # Install Streamlit
   pip install streamlit
   # Install OpenAI library
   pip install openai
   ```

4. **Run the application**
   ```sh
   # Start the Streamlit application
   streamlit run app.py
   ```


### Additional Configuration
- **App Configuration (app.py)**: Update the file path for pictures and resume data in the `app.py` file to match your local directory structure.
- **Resume Data (resume_data.json)**: Edit the `resume_data.json` file with your resume data in JSON format. You can use ChatGPT to convert your resume into JSON format.

Remember to replace `your-api-key`, and adjust file paths according to your project's structure.

