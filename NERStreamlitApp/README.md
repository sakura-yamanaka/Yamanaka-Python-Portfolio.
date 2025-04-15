# Named Entity Recognition (NER) App Project

![NER](https://rallyrd.com/wp-content/uploads/2023/02/Rally-3.jpg)

## Project Overview 
This project focuses on building a **Customaizable Named Entity Recognition (NER) App**. The goal was to create an interactive app that allows users to upload or input their own text data, define custom entity patterns, and view highlighted entities in the output. 

**Named Entity Recognition (NER)** is a key task in Natural Language Processing (NLP) that involves identifying and classifying specific pieces of information in text—such as names of people, organizations, dates, locations, and monetary values.

### What is spaCy's approach to NER?

spaCy uses a dictionary-based approach for NER, relying on patterns and labels to identify entities. By using the **EntityRuler** component, users can define custom patterns that the app will use to recognize entities in a given text. The EntityRuler matches text against a predefined set of patterns, and if a match is found, it assigns the relevant label (e.g., `PERSON`, `PRODUCT`, `DATE`) to the entity.

- **EntityRuler**: A component in spaCy used to add custom patterns to the NER pipeline. It works by analyzing text and matching predefined patterns, making it possible to recognize domain-specific entities.
- **Patterns**: A list of dictionaries where each dictionary contains:
  - `label`: The type of entity (e.g., `PERSON`, `PRODUCT`, `DATE`).
  - `pattern`: The exact words or terms that should be matched (e.g., "iPhone", "Sakura Yamanaka").


### This project provides an interactive interface to:
- Explore spaCy’s pre-trained NER model (en_core_web_sm)
- Add custom patterns using EntityRuler (define custom entity recognition rules using label and pattern)
- Visualize entity spans and their types

Together, these features give users the ability to analyze text with a high degree of flexibility, customization, and precision.

## Instructions 
To run this app, you can either run the app locally or access the deployed version. The instructions for each are below.  

### Option 1: Running the App Locally 

1. Clone or download the `NERmain.py` file from this GitHub repository to your local machine.

2. Install the necessary libraries by running the following commands in your terminal:

    ```bash
    pip install streamlit
    pip install pandas
    pip install spacy
    python -m spacy download en_core_web_sm
    ```

3. Run the app:
    ```bash
    streamlit run NERmain.py
    ```

4. Open your browser and go to `http://localhost:8501` to interact with the app.

### Option 2: Accessing the Deployed Version


## Visuals 

### App Interface

### Example 

## References