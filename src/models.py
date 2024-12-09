from pydantic import BaseModel, EmailStr
from pydantic_extra_types.phone_numbers import PhoneNumber
import phonenumbers
import re
from datetime import datetime

Filed = dict[str, datetime | PhoneNumber | EmailStr | str]


class IsEmail(BaseModel):
    email: EmailStr


class FormTemplate(BaseModel):
    name: str
    fields: Filed

    def find_match(self, other_fields: 'FormTemplate') -> bool:
        if self.name != other_fields.name:
            return False

        for key, expected_type in self.fields.items():
            if (key not in other_fields.fields) or (self.match_type(other_fields.fields[key]) != self.match_type(expected_type)):
                return False
        return True

    @staticmethod
    def match_type(value: str) -> str:
        try:
            if re.match(r"^\d{2}\.\d{2}\.\d{4}$", value):
                datetime.strptime(value, "%d.%m.%Y")
                return "date"
            elif re.match(r"^\d{4}-\d{2}-\d{2}$", value):
                datetime.strptime(value, "%Y-%m-%d")
                return "date"
        except ValueError:
            pass

        try:
            phone_number = phonenumbers.parse(value, "RU")
            if phonenumbers.is_valid_number(phone_number):
                return "phone"
        except phonenumbers.NumberParseException:
            pass

        try:
            IsEmail(email=value)
            return "email"
        except ValueError:
            pass

        return "text"
