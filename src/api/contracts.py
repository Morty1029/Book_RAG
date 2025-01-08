from typing import Optional

from pydantic import BaseModel


class BotAnswer(BaseModel):
    answer: str
    metadata: Optional[dict]
