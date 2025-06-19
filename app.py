

# # # # # from langchain_google_genai import ChatGoogleGenerativeAI



# # # # # llm = ChatGoogleGenerativeAI(
# # # # #     model="gemini-1.5-flash",
# # # # #     google_api_key='AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE',
# # # # #     temperature=0.2)

# # # # # poem = llm.invoke("Write a poem on love for burger")
# # # # # print(poem)


# # # # import streamlit as st
# # # # from langchain_google_genai import ChatGoogleGenerativeAI

# # # # # Set up the AI model
# # # # llm = ChatGoogleGenerativeAI(
# # # #     model="gemini-1.5-flash",  # Free model
# # # #     google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
# # # #     temperature=0.5
# # # # )

# # # # # Streamlit UI
# # # # st.title("🩺 Healthcare AI Assistant")
# # # # st.write("Ask me anything about health, symptoms, diet, or general medical advice!")

# # # # # User Input
# # # # user_question = st.text_input("Enter your health-related question:")

# # # # # Process User Query
# # # # if st.button("Get Recommendation"):
# # # #     if user_question.strip():
# # # #         with st.spinner("Analyzing..."):
# # # #             response = llm.invoke(user_question)
# # # #         st.success("Recommendation:")
# # # #         st.write(response)
# # # #     else:
# # # #         st.warning("Please enter a question!")

# # # # # Footer
# # # # st.markdown("---")
# # # # st.markdown("💡 *Disclaimer: This AI assistant provides general health information. Always consult a doctor for medical concerns.*")



# # # import streamlit as st
# # # from langchain_google_genai import ChatGoogleGenerativeAI

# # # # Set up AI model
# # # llm = ChatGoogleGenerativeAI(
# # #     model="gemini-1.5-flash",  # Free model
# # #     google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
# # #     temperature=0.5
# # # )

# # # # Streamlit UI
# # # st.title("🩺 AI Healthcare Learning Assistant")
# # # st.write("Ask me anything about healthcare, symptoms, diet, or medical learning!")

# # # # User Input
# # # user_question = st.text_input("Enter your healthcare question:")

# # # # Function to filter AI disclaimers
# # # def is_valid_response(response):
# # #     disclaimers = [
# # #         "I am an AI and cannot give medical advice",
# # #         "Seek medical attention",
# # #         "Consult a doctor",
# # #         "Contact your doctor",
# # #         "Go to an emergency room",
# # #     ]
# # #     return not any(phrase.lower() in response.lower() for phrase in disclaimers)

# # # # Process User Query
# # # if st.button("Get Information"):
# # #     if user_question.strip():
# # #         with st.spinner("Analyzing..."):
# # #             response = llm.invoke(user_question)
        
# # #         # Check if response is valid
# # #         if is_valid_response(response):
# # #             st.success("Here is the relevant information:")
# # #             st.write(response)
# # #         else:
# # #             st.warning("AI provided a disclaimer. Trying again...")
# # #             # Modify prompt to avoid disclaimers
# # #             better_prompt = f"Give a well-explained answer for educational purposes only: {user_question}"
# # #             retry_response = llm.invoke(better_prompt)

# # #             # Display the retried response if it's valid
# # #             if is_valid_response(retry_response):
# # #                 st.success("Here is the refined information:")
# # #                 st.write(retry_response)
# # #             else:
# # #                 st.error("Unable to get a useful response. Try rephrasing your question.")

# # #     else:
# # #         st.warning("Please enter a question!")

# # # # Footer
# # # st.markdown("---")
# # # st.markdown("💡 *This AI provides learning-based medical insights, not actual medical advice.*")



# # import streamlit as st
# # from langchain_google_genai import ChatGoogleGenerativeAI

# # # Set up AI model
# # llm = ChatGoogleGenerativeAI(
# #     model="gemini-1.5-flash",  # Free model
# #     google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
# #     temperature=0.5
# # )

# # # Streamlit UI
# # st.title("🩺 AI Healthcare Learning Assistant")
# # st.write("Ask me anything about healthcare, symptoms, diet, or medical learning!")

# # # User Input
# # user_question = st.text_input("Enter your healthcare question:")

# # # Function to filter AI disclaimers
# # def is_valid_response(response_text):
# #     disclaimers = [
# #         "I am an AI and cannot give medical advice",
# #         "Seek medical attention",
# #         "Consult a doctor",
# #         "Contact your doctor",
# #         "Go to an emergency room",
# #     ]
# #     return not any(phrase.lower() in response_text.lower() for phrase in disclaimers)

# # # Process User Query
# # if st.button("Get Information"):
# #     if user_question.strip():
# #         with st.spinner("Analyzing..."):
# #             response = llm.invoke(user_question)

# #         # Extract the text content from AIMessage
# #         response_text = response.content if hasattr(response, "content") else str(response)

# #         # Check if response is valid
# #         if is_valid_response(response_text):
# #             st.success("Here is the relevant information:")
# #             st.write(response_text)
# #         else:
# #             st.warning("AI provided a disclaimer. Trying again...")
# #             # Modify prompt to avoid disclaimers
# #             better_prompt = f"Give a well-explained answer for educational purposes only: {user_question}"
# #             retry_response = llm.invoke(better_prompt)

# #             # Extract text from the retried response
# #             retry_response_text = retry_response.content if hasattr(retry_response, "content") else str(retry_response)

# #             # Display the retried response if it's valid
# #             if is_valid_response(retry_response_text):
# #                 st.success("Here is the refined information:")
# #                 st.write(retry_response_text)
# #             else:
# #                 st.error("Unable to get a useful response. Try rephrasing your question.")

# #     else:
# #         st.warning("Please enter a question!")

# # # Footer
# # st.markdown("---")
# # st.markdown("💡 *This AI provides learning-based medical insights, not actual medical advice.*")




# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Set up AI model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",  # Free model
#     google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
#     temperature=0.5
# )

# # Streamlit UI
# st.title("🩺 AI Healthcare Learning Assistant")
# st.write("Ask about symptoms, medicines, and alternative treatments.")

# # User Input
# user_question = st.text_input("Enter your health-related query:")

# # Function to filter AI disclaimers
# def is_valid_response(response_text):
#     disclaimers = [
#         "I am an AI and cannot give medical advice",
#         "Seek medical attention",
#         "Consult a doctor",
#         "Contact your doctor",
#         "Go to an emergency room",
#     ]
#     return not any(phrase.lower() in response_text.lower() for phrase in disclaimers)

# # Process User Query
# if st.button("Get Recommendation"):
#     if user_question.strip():
#         # Modify user input to ensure the model focuses on learning-based insights
#         formatted_question = f"Without any disclaimer, recommend me medicine for {user_question}. Only for learning purposes, not for treatment. Also, suggest some different ways to cure it."

#         with st.spinner("Analyzing..."):
#             response = llm.invoke(formatted_question)

#         # Extract text content
#         response_text = response.content if hasattr(response, "content") else str(response)

#         # # Check if response is valid
#         if is_valid_response(response_text):
#             st.success("Here is the relevant information:")
#             st.write(response_text)
#         else:
#             st.warning("AI provided a disclaimer. Trying again...")
#             # Retry with a refined prompt
#             better_prompt = f"Its only for leaning purpose not for treatment provide medicine names and alternative treatments for: {user_question}"
#             retry_response = llm.invoke(better_prompt)

#             # Extract text from retry response
#             retry_response_text = retry_response.content if hasattr(retry_response, "content") else str(retry_response)

#             # # Display the retried response if valid
#             # if is_valid_response(retry_response_text):
#             #     st.success("Here is the refined information:")
#             #     st.write(retry_response_text)
#             # else:
#             #     st.error("Unable to get a useful response. Try rephrasing your question.")

#     else:
#         st.warning("Please enter a question!")

# # Footer
# st.markdown("---")
# st.markdown("💡 *This AI provides learning-based medical insights, not actual medical advice.*")



#------------------------------------------------------------------------start
# import streamlit as st
# from langchain_google_genai import ChatGoogleGenerativeAI

# # Set up AI model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",  # Free model
#     google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
#     temperature=0.5
# )

# # Streamlit UI
# st.title("🩺 CureBot: AI-Driven Health Assistant")
# st.write("Welcome to CureBot – Your AI-Driven Health Assistant! Simply enter your symptoms or disease name, and get accurate medicine suggestions instantly. Stay informed, stay healthy!")

# # User Input
# user_question = st.text_input("Type your symptoms or disease name, and let CureBot unlock the right cure for you—fast, smart, and AI-powered")

# # Function to filter AI disclaimers
# def is_valid_response(response_text):
#     disclaimers = [
#         "I am an AI and cannot give medical advice",
#         "Seek medical attention",
#         "Consult a doctor",
#         "Contact your doctor",
#         "Go to an emergency room",
    # ]
#     return not any(phrase.lower() in response_text.lower() for phrase in disclaimers)

# # Process User Query
# if st.button("Get Recommendation"):
#     if user_question.strip():
#         # Ensure the AI provides both medicine and alternative treatments
#         formatted_question = (
#             f"Without any disclaimer, recommend medicine for {user_question}. "
#             f"5 medicine names "
#             f"Also, provide alternative treatments such as home remedies, lifestyle changes, exercises, or dietary suggestions. "
#             f"Only for learning purposes, not for treatment."
#         )

#         with st.spinner("Analyzing..."):
#         #     response = llm.invoke(formatted_question)

        # # Extract text content
        # response_text = response.content if hasattr(response, "content") else str(response)

        # # Check if response is valid
        # if is_valid_response(response_text):
        #     st.success("✨ Analysis complete! Here are the best medicine recommendations for you: 🔽")
        #     st.write(response_text)
        # else:
        #     st.warning("⚠️ Oops! It looks like the input is unclear or incorrect. Please enter a valid disease name or symptoms to get accurate recommendations")
        #     # Retry with a refined prompt
        #     better_prompt = (
        #         f"Strictly provide a detailed answer including:\n"
        #         f"1. Medicine names\n"
        #         f"2. Home remedies\n"
        #         f"3. Lifestyle changes\n"
        #         f"4. Exercises\n"
        #         f"5. Diet recommendations\n"
        #         f"Do not include any disclaimers. The response should be clear and structured."
        #     )
        #     retry_response = llm.invoke(better_prompt)

        #     # Extract text from retry response
        #     retry_response_text = retry_response.content if hasattr(retry_response, "content") else str(retry_response)

#             # Display the retried response if valid
#             if is_valid_response(retry_response_text):
#                 st.success("Here is the refined information:")
#                 st.write(retry_response_text)
#             else:
#                 st.error("Unable to get a useful response. Try rephrasing your question.")

#     else:
#         st.warning("Please enter a question!")


# # Emergency Contact Button
# if st.button("Emergency Contact"):
#     st.subheader("📞 Emergency Contacts")
#     st.write("- 🚑 *Ambulance:* 102")
#     st.write("- 🏥 *LPU Hospital:* 18001024432")
#     st.write("- 🏥 *National Health Helpline:* 108")
#     st.write("- ☎ *COVID-19 Helpline:* 1075")
#     st.write("- 🚓 *Police:* 100")

# # Footer
# st.markdown("---")

# st.markdown("🔹 Powered by Mayank, Wasim, Pravishank – Innovating Healthcare with AI! 💡 Your Health, Our Mission. 🚀")



#------------------------------------------------------------------------end



# 
# 
# 
# 


# 
# 
# 
# 
# 









'''
import streamlit as st
import speech_recognition as sr
from deep_translator import GoogleTranslator
from langchain_google_genai import ChatGoogleGenerativeAI
import matplotlib.pyplot as plt
import numpy as np

# Set up AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
    temperature=0.5
)

# Custom CSS
st.markdown("""
    <style>
        .big-font { font-size:20px !important; }
        .stButton>button { background-color: #ff4b4b; color: white; font-size: 18px; }
        .stTextInput>div>div>input { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

# UI Setup
# st.image("healthcare_logo.png", width=150)
st.title("🩺 CureBot: AI-Driven Health Assistant")
st.write("Empowering healthcare with AI-driven insights and recommendations!")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
option = st.sidebar.radio("Select an option:", ["Home", "Symptom Checker", "Doctor Connect", "Health Stats"])
translator = GoogleTranslator(source='auto', target='en')

if option == "Home":
    user_question = st.text_input("Type your symptoms or disease name:")
    
    if st.button("🎤 Speak Symptoms"):
        recognizer = sr.Recognizer()
        with sr.Microphone() as source:
            st.info("Listening...")
            try:
                audio = recognizer.listen(source)
                user_question = recognizer.recognize_google(audio)
                st.success(f"Recognized: {user_question}")
            except sr.UnknownValueError:
                st.error("Could not understand audio")
            except sr.RequestError:
                st.error("Error in speech recognition service")
    
    lang = st.selectbox("Select Language", ["English", "Hindi", "Spanish"])
    if lang != "English":
        user_question = translator.translate(user_question, src="en", dest=lang.lower()).text
    
    if st.button("Get Recommendation"):
        if user_question.strip():
            formatted_question = (
                f"Provide medicine and alternative treatments for {user_question}. "
                f"List medicines, home remedies, lifestyle changes, exercises, and diet suggestions."
            )
            
            with st.spinner("Analyzing..."):
                response = llm.invoke(formatted_question)
            response_text = response.content if hasattr(response, "content") else str(response)
            st.success("✨ Analysis complete! Here are your recommendations:")
            st.markdown(response_text)
        else:
            st.warning("Please enter a symptom or disease name!")
    
elif option == "Symptom Checker":
    st.subheader("🔎 AI Symptom Checker")
    st.write("Find possible diseases based on symptoms.")
    symptoms = st.text_area("Enter symptoms separated by commas:")
    if st.button("Check Symptoms"):
        symptom_query = f"Analyze these symptoms: {symptoms}. List possible diseases."
        response = llm.invoke(symptom_query)
        st.write(response.content if hasattr(response, "content") else str(response))

elif option == "Doctor Connect":
    st.subheader("🏥 Find a Doctor Near You")
    st.write("Using Google Maps API to find the nearest hospitals and doctors.")
    st.write("(Feature Under Development)")

elif option == "Health Stats":
    st.subheader("📊 Health Trends & Data")
    
    diseases = ['Diabetes', 'Hypertension', 'Heart Disease', 'Asthma', 'Obesity']
    cases = np.random.randint(5000, 20000, size=len(diseases))
    
    fig, ax = plt.subplots()
    ax.barh(diseases, cases, color=['blue', 'green', 'red', 'purple', 'orange'])
    ax.set_xlabel("Number of Cases")
    ax.set_title("Disease Prevalence Statistics")
    st.pyplot(fig)

# Emergency Contact Section
st.sidebar.markdown("---")
st.sidebar.subheader("📞 Emergency Contacts")
st.sidebar.write("- 🚑 *Ambulance:* 102")
st.sidebar.write("- 🏥 *LPU Hospital:* 18001024432")
st.sidebar.write("- 🏥 *National Health Helpline:* 108")
st.sidebar.write("- ☎ *COVID-19 Helpline:* 1075")
st.sidebar.write("- 🚓 *Police:* 1000")

st.markdown("---")
st.markdown("🔹 Powered by Mayank, Wasim, Pravishank – Innovating Healthcare with AI! 💡 Your Health, Our Mission. 🚀")



'''




















import streamlit as st
import speech_recognition as sr
# import sounddevice as sd
from deep_translator import GoogleTranslator
from langchain_google_genai import ChatGoogleGenerativeAI
import matplotlib.pyplot as plt
import numpy as np
import folium
from streamlit_folium import folium_static
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import requests

# Set up AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="AIzaSyC7Rhv4L6_oNl-nW3Qeku2SPRkxL5hhtoE",
    temperature=0.5
)

# Custom CSS
st.markdown("""
    <style>
        .big-font { font-size:20px !important; }
        .stButton>button { background-color: #ff4b4b; color: white; font-size: 18px; }
        .stTextInput>div>div>input { font-size: 16px; }
    </style>
""", unsafe_allow_html=True)

# UI Setup
st.title("🩺 CureBot: AI-Driven Health Assistant")
st.write("Empowering healthcare with AI-driven insights and recommendations!")

# Sidebar Navigation
st.sidebar.title("🔍 Navigation")
option = st.sidebar.radio("Select an option:", ["Home", "Symptom Checker", "Doctor Connect", "Health Stats", "Health Risk Calculator"])
translator = GoogleTranslator(source='auto', target='en')

# Function to Get User Location
def get_user_location():
    try:
        response = requests.get("https://ipinfo.io/json").json()
        location = response["loc"].split(",")
        return float(location[0]), float(location[1])
    except:
        return None, None

if option == "Home":
    user_question = st.text_input("Type your disease name:")
    
#     st.title("🎤 AI Health Assistant - Speech to Text")

# uploaded_file = st.file_uploader("Upload an audio file (.wav)", type=["wav"])

# if uploaded_file:
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(uploaded_file) as source:
#         st.info("Processing audio...")
#         audio = recognizer.record(source)
    
#     try:
#         text = recognizer.recognize_google(audio)
#         st.success(f"Recognized Text: {text}")
#     except sr.UnknownValueError:
#         st.error("Could not understand the audio")
#     except sr.RequestError:
#         st.error("Error with the speech recognition service")
    
    # lang = st.selectbox("Select Language", ["English", "Hindi", "Spanish"])
    # if lang != "English":
    #     user_question = translator.translate(user_question, src="en", dest=lang.lower()).text
    
    if st.button("Get Recommendation"):
        if user_question.strip():
            formatted_question = (
                f"Provide medicine and alternative treatments for {user_question}. "
                f"List medicines, home remedies, lifestyle changes, exercises, and diet suggestions."
            )
            
            with st.spinner("Analyzing..."):
                response = llm.invoke(formatted_question)
            response_text = response.content if hasattr(response, "content") else str(response)
            st.success("✨ Analysis complete! Here are your recommendations:")
            st.markdown(response_text)
        else:
            st.warning("Please enter a symptom or disease name!")
    
elif option == "Symptom Checker":
    st.subheader("🔎 AI Symptom Checker")
    st.write("Find possible diseases based on symptoms.")
    symptoms = st.text_area("Enter symptoms separated by commas:")
    if st.button("Check Symptoms"):
        symptom_query = f"Analyze these symptoms: {symptoms}. List possible diseases."
        response = llm.invoke(symptom_query)
        st.write(response.content if hasattr(response, "content") else str(response))


elif option == "Symptom Checker":
    st.subheader("🔎 AI Symptom Checker")
    st.write("Find possible diseases based on symptoms.")
    symptoms = st.text_area("Enter symptoms separated by commas:")
    if st.button("Check Symptoms"):
        symptom_query = f"Analyze these symptoms: {symptoms}. List possible diseases."
        response = llm.invoke(symptom_query)
        st.write(response.content if hasattr(response, "content") else str(response))


elif option == "Doctor Connect":
    st.subheader("🏥 Find a Doctor Near You")

    address = st.text_input("Enter your location (City, State or Latitude, Longitude):")

    if address:
        geolocator = Nominatim(user_agent="geoapi")
        location = geolocator.geocode(address)
        if location:
            lat, lon = location.latitude, location.longitude
            st.success(f"📍 Location detected: {location.address} ({lat}, {lon})")

            map_ = folium.Map(location=[lat, lon], zoom_start=13)
            folium.Marker([lat, lon], popup="You are here!", icon=folium.Icon(color="blue")).add_to(map_)
            folium_static(map_)
        else:
            st.error("❌ Invalid address! Please try a different one.")
    else:
        st.info("ℹ️ Please enter a location to view it on the map.")





# elif option == "Doctor Connect":
#     st.subheader("📍 Doctor Connect - Find Nearby Hospitals")
    
#     def get_user_location():
#         geolocator = Nominatim(user_agent="geoapi")
#         location = geolocator.geocode("Phagwara")  # Replace with dynamic location if needed
#         if location:
#             return location.latitude, location.longitude
#         return None
    
    # def find_nearby_hospitals(user_location):
    #     hospitals = [
    #         {"name": "Apollo Hospital", "location": (30.7333, 76.7794)},
    #         {"name": "Fortis Hospital", "location": (30.7194, 76.7644)},
    #         {"name": "Max Hospital", "location": (30.7086, 76.7853)},
    #         {"name": "AIIMS Hospital", "location": (30.7500, 76.7800)}
    #     ]
        
    #     nearby_hospitals = []
    #     for hospital in hospitals:
    #         distance = geodesic(user_location, hospital["location"]).km
    #         if distance <= 10:
    #             nearby_hospitals.append(hospital)
    #     return nearby_hospitals
    
    # user_location = get_user_location()
    # if user_location:
    #     st.success(f"📍 Your Location: {user_location}")
        
    #     m = folium.Map(location=user_location, zoom_start=13)
    #     folium.Marker(user_location, tooltip="Your Location", icon=folium.Icon(color="blue")).add_to(m)
        
    #     hospitals = find_nearby_hospitals(user_location)
    #     if hospitals:
    #         st.write("🏥 Nearby Hospitals:")
    #         for hospital in hospitals:
    #             st.write(f"🔹 {hospital['name']}")
    #             folium.Marker(hospital["location"], tooltip=hospital["name"], icon=folium.Icon(color="red")).add_to(m)
    #     else:
    #         st.write("⚠️ No nearby hospitals found within 10 km.")
        
    #     folium_static(m)
    # else:
    #     st.error("⚠️ Unable to fetch location. Please allow location access or enter manually.")
    
elif option == "Health Stats":
    st.subheader("📊 Health Trends & Data")
    diseases = ['Diabetes', 'Hypertension', 'Heart Disease', 'Asthma', 'Obesity']
    cases = np.random.randint(5000, 20000, size=len(diseases))
    fig, ax = plt.subplots()
    ax.barh(diseases, cases, color=['blue', 'green', 'red', 'purple', 'orange'])
    ax.set_xlabel("Number of Cases")
    ax.set_title("Disease Prevalence Statistics")
    st.pyplot(fig)

elif option == "Health Risk Calculator":
    st.subheader("🧮 Health Risk Calculator")
    tabs = st.tabs(["🏋️ BMI Calculator", "❤️ Heart Risk Estimator", "🩸 Diabetes Risk Score"])

    # --- BMI CALCULATOR ---
    with tabs[0]:
        st.markdown("### 🏋️ Body Mass Index (BMI) Calculator")
        height_cm = st.number_input("Enter height (in cm):", min_value=50.0, max_value=250.0, step=0.1)
        weight_kg = st.number_input("Enter weight (in kg):", min_value=10.0, max_value=300.0, step=0.1)

        if st.button("Calculate BMI"):
            if height_cm > 0:
                height_m = height_cm / 100
                bmi = weight_kg / (height_m ** 2)
                st.success(f"Your BMI is: **{bmi:.2f}**")
                if bmi < 18.5:
                    st.info("Underweight")
                elif 18.5 <= bmi < 24.9:
                    st.success("Normal weight")
                elif 25 <= bmi < 29.9:
                    st.warning("Overweight")
                else:
                    st.error("Obese")
            else:
                st.warning("Height must be greater than 0.")

    # --- HEART ATTACK RISK ---
    with tabs[1]:
        st.markdown("### ❤️ Heart Attack Risk Estimator")
        age = st.slider("Age", 18, 100, 30)
        gender = st.radio("Gender", ["Male", "Female"])
        smoker = st.radio("Do you smoke?", ["Yes", "No"])
        systolic_bp = st.slider("Systolic Blood Pressure (mmHg)", 80, 200, 120)
        cholesterol = st.slider("Cholesterol Level (mg/dL)", 100, 400, 200)

        if st.button("Estimate Heart Attack Risk"):
            risk_score = 0
            if age > 45: risk_score += 1
            if smoker == "Yes": risk_score += 1
            if systolic_bp > 140: risk_score += 1
            if cholesterol > 240: risk_score += 1
            if gender == "Male": risk_score += 0.5

            if risk_score <= 1:
                st.success("Low Risk ✅")
            elif 2 <= risk_score <= 3:
                st.warning("Moderate Risk ⚠️")
            else:
                st.error("High Risk ❌")

    # --- DIABETES RISK ---
    with tabs[2]:
        st.markdown("### 🩸 Diabetes Risk Score Estimator")
        age_d = st.slider("Age", 10, 100, 30, key="d1")
        bmi_d = st.slider("BMI", 10.0, 50.0, 22.0, step=0.1, key="d2")
        family_history = st.radio("Family History of Diabetes?", ["Yes", "No"], key="d3")
        physical_activity = st.radio("Do you exercise regularly?", ["Yes", "No"], key="d4")
        diet = st.radio("Do you consume sugary or high-carb food often?", ["Yes", "No"], key="d5")

        if st.button("Estimate Diabetes Risk"):
            d_score = 0
            if age_d > 45: d_score += 1
            if bmi_d > 30: d_score += 1
            if family_history == "Yes": d_score += 1
            if physical_activity == "No": d_score += 1
            if diet == "Yes": d_score += 1

            if d_score <= 1:
                st.success("Low Risk ✅")
            elif 2 <= d_score <= 3:
                st.warning("Moderate Risk ⚠️")
            else:
                st.error("High Risk ❌")       
# Emergency Contact Section
st.sidebar.markdown("---")
st.sidebar.subheader("📞 Emergency Contacts")
st.sidebar.write("- 🚑 *Ambulance:* 102")
st.sidebar.write("- 🏥 *LPU Hospital:* 18001024432")
st.sidebar.write("- 🏥 *National Health Helpline:* 108")
st.sidebar.write("- ☎ *COVID-19 Helpline:* 1075")
st.sidebar.write("- 🚓 *Police:* 100")

st.markdown("---")
st.markdown("🔹 Powered by Mayank, Wasim, Pravisank, Ananya – Innovating Healthcare with AI! 💡 Your Health, Our Mission. 🚀")








# '''
# import streamlit as st
# import speech_recognition as sr
# from deep_translator import GoogleTranslator
# from langchain_google_genai import ChatGoogleGenerativeAI
# import matplotlib.pyplot as plt
# import numpy as np
# import folium
# from streamlit_folium import folium_static
# import requests
# from geopy.geocoders import Nominatim

# # Initialize AI Model
# llm = ChatGoogleGenerativeAI(
#     model="gemini-1.5-flash",
#     google_api_key="YOUR_GOOGLE_API_KEY",
#     temperature=0.5
# )

# # Custom CSS
# st.markdown("""
#     <style>
#         .big-font { font-size:20px !important; }
#         .stButton>button { background-color: #ff4b4b; color: white; font-size: 18px; }
#         .stTextInput>div>div>input { font-size: 16px; }
#     </style>
# """, unsafe_allow_html=True)

# # App Title & Description
# st.title("🩺 CureBot: AI-Driven Health Assistant")
# st.write("Empowering healthcare with AI-driven insights and recommendations!")

# # Sidebar Navigation
# st.sidebar.title("🔍 Navigation")
# option = st.sidebar.radio("Select an option:", ["Home", "Symptom Checker", "Doctor Connect", "Health Stats"])
# translator = GoogleTranslator(source='auto', target='en')

# Function to Get User Location
# def get_user_location():
#     try:
#         response = requests.get("https://ipinfo.io/json").json()
#         location = response["loc"].split(",")
#         return float(location[0]), float(location[1])
#     except:
#         return None, None

# if option == "Home":
#     user_question = st.text_input("Type your symptoms or disease name:")
    
#     if st.button("🎤 Speak Symptoms"):
#         recognizer = sr.Recognizer()
#         with sr.Microphone() as source:
#             st.info("Listening...")
#             try:
#                 audio = recognizer.listen(source)
#                 user_question = recognizer.recognize_google(audio)
#                 st.success(f"Recognized: {user_question}")
#             except sr.UnknownValueError:
#                 st.error("Could not understand audio")
#             except sr.RequestError:
#                 st.error("Error in speech recognition service")
    
#     lang = st.selectbox("Select Language", ["English", "Hindi", "Spanish"])
#     if lang != "English":
#         user_question = translator.translate(user_question, src="en", dest=lang.lower())
    
#     if st.button("Get Recommendation"):
#         if user_question.strip():
#             formatted_question = (
#                 f"Provide medicine and alternative treatments for {user_question}. "
#                 f"List medicines, home remedies, lifestyle changes, exercises, and diet suggestions."
#             )
            
#             with st.spinner("Analyzing..."):
#                 response = llm.invoke(formatted_question)
#             response_text = response.content if hasattr(response, "content") else str(response)
#             st.success("✨ Analysis complete! Here are your recommendations:")
#             st.markdown(response_text)
#         else:
#             st.warning("Please enter a symptom or disease name!")
    
# elif option == "Symptom Checker":
#     st.subheader("🔎 AI Symptom Checker")
#     symptoms = st.text_area("Enter symptoms separated by commas:")
#     if st.button("Check Symptoms"):
#         symptom_query = f"Analyze these symptoms: {symptoms}. List possible diseases."
#         response = llm.invoke(symptom_query)
#         st.write(response.content if hasattr(response, "content") else str(response))

# elif option == "Doctor Connect":
#     st.subheader("🏥 Find a Doctor Near You")
#     lat, lon = get_user_location()
    
    # if lat is None or lon is None:
#         st.warning("Unable to fetch location. Please allow location access or enter manually.")
#         address = st.text_input("Enter your location (City, State or Latitude, Longitude):")
#         if address:
#             geolocator = Nominatim(user_agent="geoapi")
#             location = geolocator.geocode(address)
#             if location:
#                 lat, lon = location.latitude, location.longitude
#             else:
#                 st.error("Invalid address! Try again.")
    
#     if lat and lon:
#         st.success(f"📍 Location detected: {lat}, {lon}")
#         map_ = folium.Map(location=[lat, lon], zoom_start=13)
#         folium.Marker([lat, lon], popup="You are here!", icon=folium.Icon(color="blue")).add_to(map_)
#         folium_static(map_)

# elif option == "Health Stats":
#     st.subheader("📊 Health Trends & Data")
#     diseases = ['Diabetes', 'Hypertension', 'Heart Disease', 'Asthma', 'Obesity']
#     cases = np.random.randint(5000, 20000, size=len(diseases))
#     fig, ax = plt.subplots()
#     ax.barh(diseases, cases, color=['blue', 'green', 'red', 'purple', 'orange'])
#     ax.set_xlabel("Number of Cases")
#     ax.set_title("Disease Prevalence Statistics")
#     st.pyplot(fig)

# # Emergency Contacts
# st.sidebar.markdown("---")
# st.sidebar.subheader("📞 Emergency Contacts")
# st.sidebar.write("- 🚑 *Ambulance:* 102")
# st.sidebar.write("- 🏥 *LPU Hospital:* 18001024432")
# st.sidebar.write("- 🏥 *National Health Helpline:* 108")
# st.sidebar.write("- ☎ *COVID-19 Helpline:* 1075")
# st.sidebar.write("- 🚓 *Police:* 1000")

# st.markdown("---")
# st.markdown("🔹 Powered by Mayank, Wasim, Pravishank – Innovating Healthcare with AI! 💡 Your Health, Our Mission. 🚀")

# '''