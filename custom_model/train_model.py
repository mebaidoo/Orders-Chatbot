import spacy
from spacy.pipeline import EntityRuler
from spacy.training import Example
from spacy.util import minibatch, compounding

TRAIN_DATA = [
    ("I would like to order a product.", {"entities": [(16, 21, "order")]}),
    ("I would like to buy a product.", {"entities": [(16, 19, "order")]}),
    ("I would like to purchase a product.", {"entities": [(16, 24, "order")]}),
    ("Yes", {"entities": [(0, 3, "order")]}),
    ("No", {"entities": [(0, 2, "no_order")]}),
    ("no", {"entities": [(0, 2, "no_order")]}),
    ("Talk to staff.", {"entities": [(0, 7, "talk")]}),
    ("I would like to talk to someone.", {"entities": [(16, 23, "talk")]}),
    ("I would like to talk to a human.", {"entities": [(16, 23, "talk")]}),
    ("I would like to talk to staff.", {"entities": [(16, 23, "talk")]}),
    ("FirewoodTypeA", {"entities": [(0, 13, "product_name")]}),
    ("FirewoodTypeB", {"entities": [(0, 13, "product_name")]}),
    ("FirewoodTypeC", {"entities": [(0, 13, "product_name")]}),
    ("1", {"entities": [(0, 1, "product_quantity")]}),
    ("2", {"entities": [(0, 1, "product_quantity")]}),
    ("3", {"entities": [(0, 1, "product_quantity")]}),
    ("4", {"entities": [(0, 1, "product_quantity")]}),
    ("5", {"entities": [(0, 1, "product_quantity")]}),
    ("6", {"entities": [(0, 1, "product_quantity")]}),
    ("7", {"entities": [(0, 1, "product_quantity")]}),
    ("8", {"entities": [(0, 1, "product_quantity")]}),
    ("9", {"entities": [(0, 1, "product_quantity")]}),
    ("10", {"entities": [(0, 2, "product_quantity")]}),
    ("11", {"entities": [(0, 2, "product_quantity")]}),
    ("12", {"entities": [(0, 2, "product_quantity")]}),
    ("13", {"entities": [(0, 2, "product_quantity")]}),
    ("14", {"entities": [(0, 2, "product_quantity")]}),
    ("15", {"entities": [(0, 2, "product_quantity")]}),
    ("16", {"entities": [(0, 2, "product_quantity")]}),
    ("17", {"entities": [(0, 2, "product_quantity")]}),
    ("18", {"entities": [(0, 2, "product_quantity")]}),
    ("19", {"entities": [(0, 2, "product_quantity")]}),
    ("20", {"entities": [(0, 2, "product_quantity")]}),
    ("21", {"entities": [(0, 2, "product_quantity")]}),
    ("22", {"entities": [(0, 2, "product_quantity")]}),
    ("23", {"entities": [(0, 2, "product_quantity")]}),
    ("24", {"entities": [(0, 2, "product_quantity")]}),
    ("40 cm", {"entities": [(0, 5, "product_size")]}),
    ("33 cm", {"entities": [(0, 5, "product_size")]}),
    ("25 cm", {"entities": [(0, 5, "product_size")]}),
    ("40cm", {"entities": [(0, 4, "product_size")]}),
    ("33cm", {"entities": [(0, 4, "product_size")]}),
    ("25cm", {"entities": [(0, 4, "product_size")]}),
    ("I want size 40.", {"entities": [(7, 14, "product_size")]}),
    ("I want size 33.", {"entities": [(7, 14, "product_size")]}),
    ("I want size 25.", {"entities": [(7, 14, "product_size")]}),
    ("Order a second product.", {"entities": [(8, 22, "second_order")]}),
    ("Order second product.", {"entities": [(6, 20, "second_order")]}),
    ("I want to make a second order.", {"entities": [(17, 29, "second_order")]}),
    ("Order a third product.", {"entities": [(8, 21, "third_order")]}),
    ("Order third product.", {"entities": [(6, 19, "third_order")]}),
    ("I want to make a third order.", {"entities": [(17, 28, "third_order")]}),
    ("Provide delivery details.", {"entities": [(8, 24, "shipping_address")]}),
    ("Provide shipping details.", {"entities": [(8, 24, "shipping_address")]}),
    ("I want to provide my shipping address.", {"entities": [(21, 37, "shipping_address")]}),
    ("I want to provide my shipping details.", {"entities": [(21, 37, "shipping_address")]}),
]

# Load the large SpaCy model
nlp = spacy.load("en_core_web_lg")

# Get the NER component
ner = nlp.get_pipe("ner")

# Add new entity labels to the NER
ner.add_label("order")
ner.add_label("no_order")
ner.add_label("talk")
ner.add_label("product_name")
ner.add_label("product_quantity")
ner.add_label("product_size")
ner.add_label("second_order")
ner.add_label("third_order")
ner.add_label("shipping_address")

# Prepare training data and model for training
optimizer = nlp.resume_training()
n_iter = 150  # Number of iterations for training

for itn in range(n_iter):
    losses = {}
    # Batch up the examples using spaCy's utility functions
    batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        texts, annotations = zip(*batch)
        examples = [Example.from_dict(nlp.make_doc(text), ann) for text, ann in batch]
        nlp.update(examples, drop=0.5, sgd=optimizer, losses=losses)
    print(f"Iteration {itn + 1}: Losses {losses}")

# Save the trained model
nlp.to_disk("custom_spacy_lg_model")