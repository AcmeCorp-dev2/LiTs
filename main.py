import streamlit as st
from PIL import Image
import os
# from net import CallNetwork

# Function to process CT scan image
def process_image(image, output_folder):

    # print(image.filename)
    # Placeholder function, you would replace this with your actual processing code
    # Here, it just displays the uploaded image
    
    output_path = os.path.join(output_folder, image)
    # CallNetwork.InduceProcess()
    
    # image.save(output_path)
    return output_path

# Function to display information about liver tumors
def display_tumor_info():
    # Placeholder function, you would replace this with actual information about liver tumors
    st.subheader("Liver Tumors Information")
    st.write("Here's some information about liver tumors:")
    st.write("Liver tumors can be benign or malignant growths in the liver.")
    st.write("Common types of liver tumors include hepatocellular carcinoma, cholangiocarcinoma, and metastatic liver cancer.")
    st.write("Effects of liver tumors may include:")
    st.write("- Jaundice (yellowing of the skin and eyes)")
    st.write("- Abdominal pain or swelling")
    st.write("- Unexplained weight loss")
    st.write("- Loss of appetite")
    st.write("- Fatigue or weakness")
    st.write("- Nausea and vomiting")
    st.write("- Changes in stool color")
    st.write("- Enlarged liver or spleen")
    st.write("- Easy bruising or bleeding")

def main():
    st.title("Liver CT Scan Analysis")

    # Sidebar with basic options
    st.sidebar.title("Options")
    selected_option = st.sidebar.radio("", ["Home", "About", "Contact"])

    if selected_option == "Home":
        st.write("Welcome to Liver CT Scan Analysis!")
        st.write("This application allows you to upload a liver CT scan image and analyze it for tumors.")
        st.write("To get started, use the sidebar to select options or upload your CT scan image.")
        display_tumor_info()

    elif selected_option == "About":
        st.write("You selected About")
    elif selected_option == "Contact":
        st.write("You selected Contact")


    st.subheader("Provide a CT scan image for analysis")
    uploaded_file = st.file_uploader("Upload CT scan image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Process the image
        image = Image.open(uploaded_file)
        name = uploaded_file.name
        # st.subheader(uploaded_file.name)
        st.subheader("**Uploaded CT Scan Image**")
        st.image(image, caption='Uploaded CT scan image')
        # st.subheader(image.filename)
        output_folder = "outputs"
        processed_image_path = process_image(name, output_folder)

        # Display tumor analysis results
        st.subheader("**Analysis Results**")
        # Placeholder for displaying analysis results
          # Display processed image
        processed_image = Image.open(processed_image_path)
        st.image(processed_image, caption='Processed CT scan image')


        # Display information about liver tumors
        # display_tumor_info()

# Customizing page layout and design
st.markdown(
"""
<style>
body {
    background-color: #f0f2f6;
}
.st-bw {
    background-color: #ffffff;
    padding: 8px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #888888;
    margin-bottom: 5px;
}
.st-c3 {
    color: #2c3e50;
}
.sidebar .sidebar-content {
    background-color: #f0f2f6;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px #888888;
}
/* Decrease size of radio buttons */
.sidebar .radio-box span {
    width: 12px !important;
    height: 12px !important;
}
</style>
""",
unsafe_allow_html=True)

if __name__ == "__main__":
    main()
