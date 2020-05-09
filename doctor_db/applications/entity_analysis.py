import spacy

def get_entities(sentence):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(sentence)
    entity_list = []
    for entity in doc.ents:
        entity_list.append(ent.text, ent.label_)

    return entity_list