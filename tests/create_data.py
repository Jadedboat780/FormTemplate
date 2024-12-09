import asyncio
from src.database import mongo_collection

data = [
    {
        "name": "Form1",
        "fields": {"email": "test1@example.com", "phone": "+7-123-456-78-90"}
    },
    {
        "name": "Form2",
        "fields": {"phone": "+7-123-456-78-90", "date": "2023-12-01"}
    },
    {
        "name": "Form3",
        "fields": {"email": "test3@example.com", "mes": "hello"}
    }

]


async def create_data():
    for d in data:
        await mongo_collection.insert_doc(d)


asyncio.run(create_data())
