# standart imports
from typing import List
from typing import Optional

# third-party imports
from pydantic import BaseModel
from pydantic import Field


class LinkModel(BaseModel):
    display: Optional[str]


class SelfModel(BaseModel):
    href: Optional[str]
    responses: Optional[str] = None


class ThemeModel(BaseModel):
    href: Optional[str]


class SettingsModel(BaseModel):
    is_public: Optional[bool]
    is_trial: Optional[bool]


class ItemModel(BaseModel):
    _links: Optional[LinkModel]
    created_at: Optional[str]
    id_: Optional[str] = Field(alias="id")
    last_updated_at: Optional[str]
    self_: Optional[SelfModel] = Field(alias="self")
    settings: Optional[SettingsModel]
    theme: Optional[ThemeModel]
    title: Optional[str]
    type_: Optional[str] = Field(alias="type")


class ResponseBodyModel(BaseModel):
    total_items: Optional[int]
    page_count: Optional[int]
    items: Optional[List[ItemModel]]
