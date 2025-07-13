from peewee import SqliteDatabase, TextField, Model

db = SqliteDatabase("translations.db")

class TranslationModel(Model):
    text = TextField()
    translation = TextField(null=True)

    class Meta:
        database = db


db.connect()
db.create_tables([TranslationModel])
print("✅ Database Initialized")
