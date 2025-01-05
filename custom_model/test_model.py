# import spacy

# # Load the custom-trained SpaCy model
# nlp = spacy.load("custom_spacy_lg_model")

# # Define sample texts for testing
# texts = [
#     "You can reach me at +49 123 4567890 or send an email to john.doe@example.de.",
#     "Call me at 0049 170 1234567 or email me at jane.doe@example.de.",
#     "My phone number is (030) 1234567 and my email is test@example.com.",
#     "My name is Katelyn Lietcher.",
#     "I come from Munich.",
# ]

# # Process each text and print the entities recognized
# for text in texts:
#     doc = nlp(text)
#     print(f"Text: {text}")
#     for ent in doc.ents:
#         print(f"Entity: {ent.text}, Label: {ent.label_}")
#     print("\n")

import spacy

nlp = spacy.load("custom_spacy_lg_model")

# Access the EntityRuler
doc = nlp("Call me at +493012345678 and talk to me.")
ents = [(ent.text, ent.label_) for ent in doc.ents]
print(ents)
