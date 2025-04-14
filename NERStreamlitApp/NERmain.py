import streamlit as st
import spacy
from spacy.pipeline import EntityRuler
import pandas as pd
from spacy import displacy

st.title("Interactive NER Analyzer 🔍")

st.write("""
    Welcome to the easy-to-use **Interactive NER Analyzer**! With this app, you can quickly input text, 
    upload files, add custom entity patterns, and visualize the entities detected in your text—all in one place!
""")

st.subheader("Upload/Input Text:")
# File upload or text input
input_method = st.radio("Input method:", ("Upload file", "Enter text directly"))

text = ""
if input_method == "Upload file":
    uploaded_file = st.file_uploader("Choose a text file", type=["txt"])
    if uploaded_file:
        with open(uploaded_file, 'r', encoding='utf-8') as f:
            text = f.read()
else:
    text = st.text_area("Enter your text:", 
                       "Sakura Yamanaka is looking at buying a house in NYC for $1 billion.")

nlp = spacy.load("en_core_web_sm")

if "custom_patterns" not in st.session_state:
    st.session_state.custom_patterns = []

st.sidebar.header("Custom Entity Rules")

with st.sidebar.form("rule_form"):
    st.write("Add a new entity pattern:")
    label = st.text_input("Label (e.g., PRODUCT, COMPANY)", "COMPANY")
    pattern = st.text_input("Pattern", "CompanyName") 
    submitted = st.form_submit_button("Add Pattern")

if submitted and label and pattern:
    st.session_state.custom_patterns.append({"label": label, "pattern": pattern})
    st.success('Added new pattern!', icon="✅")

if st.session_state.custom_patterns: 
    st.sidebar.subheader("Current Patterns")
    for i, p in enumerate(st.session_state.custom_patterns, 1):
        st.sidebar.text(f"{i}. {p['label']}: {p['pattern']}")

# Check if the "ner" pipe exists. If it does, add the EntityRuler before it.
if "ner" in nlp.pipe_names:
    # If entity_ruler already exists, simply add patterns to it.
    try:
        ruler = nlp.get_pipe("entity_ruler")
    except Exception:
        ruler = nlp.add_pipe("entity_ruler", before="ner")
    ruler.add_patterns(st.session_state.custom_patterns)
else:
    # If the NER component does not exist, add both the EntityRuler and the NER component.
    ruler = nlp.add_pipe("entity_ruler")
    ruler.add_patterns(st.session_state.custom_patterns)
    ner = nlp.add_pipe("ner")

nlp.max_length = len(text)
doc = nlp(text)

st.subheader("Entity Visualization:")
visualization = displacy.render(doc, style="ent", page=False)
st.markdown (visualization, unsafe_allow_html=True)

st.subheader("Detected Entities:")

for ent in doc.ents:
    st.write(f"Entity: {ent.text} | Type: {ent.label_} | Position: Starts at character {ent.start_char} and ends at character {ent.end_char}.")