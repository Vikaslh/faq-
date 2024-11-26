from pydantic import BaseModel
from typing import List, Optional

# Schema for input (document upload)
class DocumentInput(BaseModel):
    title: str
    description: str
    uploaded_by: str

# Schema for FAQ (output)
class FAQSchema(BaseModel):
    question: str
    answer: str

# Schema for Document output
class DocumentOutput(BaseModel):
    id: int
    title: str
    description: str
    upload_date: str
    faqs: Optional[List[FAQSchema]] = None
