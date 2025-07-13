from models import TranslationModel
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# initialize model and tokenizer
model_name = "Helsinki-NLP/opus-mt-en-hi"
tokenizer = AutoTokenizer.from_pretrained(model_name, model_max_length=512)
translator = AutoModelForSeq2SeqLM.from_pretrained(model_name)

# task 1: store_translation()
def store_translation(t):
    model = TranslationModel(
        text = t.text
    )
    model.save()
    return model.id

# task2: run_translation()
def run_translation(task_id: int):
    model = TranslationModel.get_by_id(task_id)
    tokens = tokenizer(model.text, return_tensors="pt").input_ids
    outputs = translator.generate(tokens, max_new_tokens=512)
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    model.translation = translation
    model.save()
    

# task3: find_translation()
def find_translation(task_id):
    model = TranslationModel.get_by_id(task_id)
    translation = model.translation
    if translation is None:
        return "Processing, Check Back Later ..."
    return translation