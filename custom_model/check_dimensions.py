import spacy

# Load the custom-trained SpaCy model
nlp = spacy.load("custom_spacy_lg_model")

# Get the Named Entity Recognizer (NER) component
ner = nlp.get_pipe("ner")

# Get the list of entity labels
entity_labels = ner.labels

# Print the entity labels (dimensions)
print("Recognized Entities (Dimensions):", entity_labels)
