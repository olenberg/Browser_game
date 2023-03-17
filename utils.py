# import json
# from constants import DATA_DIR, FILE_NAME
# import json
# from dataclasses import dataclass
# import marshmallow
# import marshmallow_dataclass
# from pathlib import Path
# from constants import DATA_DIR, FILE_NAME
#
# @dataclass
# class Person:
#     weapons: list
#     armors: list
#
#     class Meta:
#         unknown = marshmallow.EXCLUDE
#
#
# PersonSchema = marshmallow_dataclass.class_schema(Person)()
# with open(DATA_DIR / FILE_NAME, "r", encoding="utf-8") as f:
#     person = PersonSchema.load(json.load(f))
#     print(person)

# print(person.weapons)
