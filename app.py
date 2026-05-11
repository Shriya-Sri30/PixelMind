%%writefile app.py
import streamlit as st
from huggingface_hub import InferenceClient

st.set_page_config(
    page_title="PixelMind",
    page_icon="🎨"
)

client = InferenceClient(token=st.secrets["HF_TOKEN"])
MODEL = "stabilityai/stable-diffusion-xl-base-1.0"

st.title("PixelMind 🎨")
st.write("✨ Describe your imagination to make it real...")

prompt = st.text_input("Describe your image...")

if st.button("Generate ✨"):
    with st.spinner("Creating your masterpiece..."):
        image = client.text_to_image(prompt, model=MODEL)
        st.image(image, caption=prompt)
        st.success("Your image is ready! 🎨")