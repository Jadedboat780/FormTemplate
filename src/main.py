from fastapi import FastAPI, HTTPException
from src.models import FormTemplate
from src.database import mongo_collection

app = FastAPI()


@app.post("/get_form")
async def get_form(incoming_fields: FormTemplate):
    templates = await mongo_collection.get_all_docs()

    for template in templates:
        form_template = FormTemplate(name=template["name"], fields=template["fields"])
        if form_template.find_match(incoming_fields):
            return {"form_template_name": form_template.name}

    raise HTTPException(
        status_code=404,
        detail={key: FormTemplate.match_type(value) for key, value in incoming_fields.fields.items()}
    )
