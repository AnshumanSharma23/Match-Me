import streamlit as st
import openai
import json
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the OpenAI client with your API key from the .env file
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Function to load resume data from a JSON file
def load_resume_data(filepath):
    with open(filepath, 'r') as file:
        data = json.load(file)
    return data

# Function to format the resume data into a string that can be used as context
def format_resume_context(resume_data):
    context = ""
    for key, value in resume_data.items():
        if isinstance(value, list):
            items = []
            for item in value:
                if isinstance(item, dict):
                    item_str = ", ".join([f"{k}: {v}" for k, v in item.items()])
                    items.append(item_str)
                else:
                    items.append(item)
            context += f"{key}: " + "; ".join(items) + ". "
        else:
            context += f"{key}: {value}. "
    return context

# Function to get an answer from the ChatGPT model using the OpenAI API
def get_answer(question, context):
    full_question = f"{context}\n\n{question}"
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an assistant that knows everything about Anshuman Sharma's professional profile and recruiters are putting in their job profile here to see if anshuman would be a good fit for their role, you have to mention if Anshuman would be a good fit for the role by mentioning key points with background, if not mention why Anshuman woulndt be a good fit also see if it matches with his profile and work experience and years of experience required, anything which is analytical will always be a good fit, when the work experience required is beyond 5 years, you may mention though his skills area good match but his work experience is limited"},
            {"role": "user", "content": full_question}
        ]
    )
    
    if completion.choices:
        return completion.choices[0].message.content
    else:
        return "Sorry, I couldn't generate a response."

# Sidebar: Personal Profile
st.sidebar.image("anshuu.png")  # Update path_to_your_image.jpg with your image path
st.sidebar.markdown("<h1 style='text-align: center;'>Anshuman Sharma</h1>", unsafe_allow_html=True)

# Center the email and website details
st.sidebar.markdown("<p style='text-align: center;'>📧 anshums3@uci.edu</p>", unsafe_allow_html=True)  
st.sidebar.markdown("<p style='text-align: center;'><a href='https://anshumansharma23.github.io'>Website</a></p>", unsafe_allow_html=True)
# Main content area
st.title('Match My Talent!')

with st.container():
    st.header("Welcome, Recruiters!")
    st.write("Enter the job listing details below to see if I'm a good fit for the role.")

    # Load the resume data from the JSON file
    resume_data = load_resume_data("resume_data.json")

    user_question = st.text_area("Job Description", height=200, help="Paste the job description here.")
    if st.button('Evaluate Fit'):
        formatted_context = format_resume_context(resume_data)
        answer = get_answer(user_question, formatted_context)
        st.subheader("Fit Analysis:")
        st.write(answer)
