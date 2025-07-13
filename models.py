from peewee import SqLiteDatabase, TextField, CharField,  Model

db = SqLiteDatabase(["translations.db"])

class TranslationModel(Model):
    text = TextField()
    base_lang_code = CharField()
    final_lang_model = CharField()
    translation = TextField(null=True)

    class Meta:
        database = db

db.connect()
db.create_tables([TranslationModel])
print("✅ Database Initialized")
