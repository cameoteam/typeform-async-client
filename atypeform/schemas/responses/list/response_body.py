# standart imports
from typing import Any
from typing import Dict
from typing import List
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field


class FieldModel(BaseModel):
    id_: str = Field(alias="id")
    ref: str
    type_: str = Field(alias="type")


class ChoicesModel(BaseModel):
    labels: List[str]


class ChoiceModel(BaseModel):
    label: str


class AnswerModel(BaseModel):
    field: FieldModel
    text: Optional[str] = None
    type_: str = Field(alias="type")
    boolean: Optional[bool] = None
    email: Optional[str] = None
    number: Optional[int] = None
    choices: Optional[ChoicesModel] = None
    date: Optional[str] = None
    choice: Optional[ChoiceModel] = None
    file_url: Optional[str] = None
    phone_number: Optional[str] = None


class CalculatedModel(BaseModel):
    score: int


class MetadataModel(BaseModel):
    browser: str
    network_id: str
    platform: str
    referer: str
    user_agent: str


class VariableModel(BaseModel):
    key: str
    number: Optional[int] = None
    type_: str = Field(alias="type")
    text: Optional[str] = None


class ItemModel(BaseModel):
    answers: List[AnswerModel]
    calculated: CalculatedModel
    hidden: Dict[str, Any]
    landed_at: str
    landing_id: str
    metadata: MetadataModel
    response_id: Optional[str] = None
    submitted_at: str
    token: str
    variables: Optional[List[VariableModel]] = None


class ResponseBodyModel(BaseModel):
    total_items: Optional[int]
    page_count: Optional[int]
    items: Optional[List[ItemModel]]
