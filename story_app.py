import streamlit as st
import openai

# Set your OpenAI API key here
client = openai.OpenAI(api_key= "your_open_AI_key")

st.title("🧚 AI Story Generator for Kids")

character = st.text_input("Who is the main character?")
setting = st.text_input("Where does the story take place?")
tone = st.selectbox("What kind of story?", ["Funny", "Adventure", "Magical", "Sleepy"])

max_words = 150  # define this before the with, it's not code that needs the spinner

if st.button("✨ Tell me a story!"):
    if not character or not setting:
        st.warning("Please enter a character and setting.")
    else:
        with st.spinner("Writing your magical story..."):    
            prompt = (
                f"Write a short {tone.lower()} story for a child about a {character} in {setting}. "
                f"The story should be cute, engaging, and appropriate for young children. "
                f"Limit the story to no more than {max_words} words."
            )
            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a creative children's story writer."},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    max_tokens=500
                )
                story = response.choices[0].message.content
                st.success("Here's your story!")
                st.markdown(f"""
<div style="background-color:#f0f8ff; padding:20px; border-radius:10px;
            border:2px solid #add8e6; color:#1a232f; 
            max-height: 400px; overflow-y: auto;
            font-size:22px;  /* Bigger text for kids */
">
<h3 style="color:#4682b4;">The {tone.lower()} tale of the {character} in {setting}</h3>
<p>{story}</p>
</div>
""", unsafe_allow_html=True)
            except Exception as e:
                st.error(f"Error: {e}")
