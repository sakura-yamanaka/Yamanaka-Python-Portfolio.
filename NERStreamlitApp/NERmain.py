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
    text = st.text_area("Enter your text:", )

nlp = spacy.load("en_core_web_sm")

if "custom_patterns" not in st.session_state:
    st.session_state.custom_patterns = []

st.sidebar.header("Custom Entity Rules")

with st.sidebar.form("rule_form"):
    st.write("Add a new entity pattern:")
    label = st.text_input("Label", "COMPANY")
    pattern = st.text_input("Pattern (Separate multiple terms with commas)", "CompanyName1, CompanyName2") 
    submitted = st.form_submit_button("Add Pattern")

if submitted and label and pattern:
    for term in pattern.split(","):
        term = term.strip()
        if term:
            st.session_state.custom_patterns.append({"label": label, "pattern": term})
    st.success("Added new pattern!", icon="✅")

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

st.subheader("Sample Texts:")
st.write("Here are some fun example texts you could test out:")

st.write("""
**Text 1: Figure Skating Overview**  
Every morning before school, I head to the local ice rink in Virginia to practice figure skating. Figure skating is a graceful and athletic sport performed on ice. Skaters train for hours each day to master jumps like the axel, salchow, and toe loop. Skaters also wear custom costumes and rely on strong blades, boots, and music to bring their routines to life. At the Winter Olympics 2022 in Beijing, skaters competed under intense pressure to perfect their performances. Figure skating isn’t just about technique — it’s about telling a story on ice, whether it's during a local competition in Chicago or on the World Championship.

*Possible Patterns to Create:*  
- Label `JUMPS`, Pattern: axel, salchow, toe loop  
- Label `GEAR`, Pattern: blades, boots, costumes
""")

st.write("""
**Text 2: Exploring New York City**  
Living in New York City means there's always something exciting happening around every corner. Last weekend, I visited the Empire State Building with my cousin who had never been to the city before. We walked through Central Park, passed through Harlem, and browsed art galleries in SoHo. Later, we took the subway downtown, grabbed pizza from a local spot in the East Village, and ended the night with a visit to the Museum of Modern Art. I love how each neighborhood has its own character—from the historic charm of Greenwich Village to the towering lights of Times Square. It’s no wonder people say New York is the city that never sleeps!

*Possible Patterns to Create:*  
- Label `LANDMARKS`, Pattern: Empire State Building, Central Park, Museum of Modern Art, Times Square  
- Label `NEIGHBORHOODS`, Pattern: Harlem, SoHo, East Village, Greenwich Village 
""")