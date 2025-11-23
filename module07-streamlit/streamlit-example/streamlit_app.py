import streamlit as st

st.title("Hello Streamlit!")
st.header("This is a simple Streamlit app.")
st.subheader("Subheader Example")
st.text("This is a text element in Streamlit.")
st.markdown("### Markdown Example\nYou can use **Markdown** to format text.")
st.latex(r"E = mc^2")

image = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])
if image:
    st.image(image, caption="Uploaded Image", use_column_width=True)

selected_value = st.selectbox("Choose a number", options=[1, 2, 3, 4, 5])
slider_value = st.slider("Select a range of values", 0, 100, (25, 75))

st.write(f"You selected: {selected_value}")
st.write(f"Slider range: {slider_value}")

checkbox = st.checkbox("Check me!")
if checkbox:
    st.write("Checkbox is checked!")