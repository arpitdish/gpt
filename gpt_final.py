import streamlit as st
import os
import replicate



st.title("Dish GPT")

# Create a text input box
user_input = st.text_area("Enter your text prompt here:")

# Display the user's input
if user_input:
    st.write("You entered:", user_input)

os.environ["REPLICATE_API_TOKEN"] = "r8_H7CLxvh7kI0IPk6nmjO10Lyq844IuIs0L1Sdg"


output = replicate.run(
    "meta/llama-2-7b:73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9",
    input={"prompt": user_input}
)

# for item in output:
#     # https://replicate.com/meta/llama-2-7b/versions/73001d654114dad81ec65da3b834e2f691af1e1526453189b7bf36fb3f32d0f9/api#output-schema
#     print(item, end="")

st.subheader("Output")


for item in output:
    st.write(item)