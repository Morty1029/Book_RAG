from api.contracts import BotAnswer
from inference.Model import Model
from data_processing.ClientInputData import ClientInputData

from http import HTTPStatus
from typing import Optional

from fastapi import APIRouter

router = APIRouter()
model = Model()
model.load_model()


@router.get(
    "/get_answer",
    responses={
        HTTPStatus.OK: {"description": "Successfully returned answer"},
        HTTPStatus.NOT_FOUND: {"description": "Failed to return answer"},
    },
)
async def get_recommendations(
    prompt: Optional[str], book_num: Optional[int]
) -> Optional[BotAnswer]:
    data = ClientInputData(prompt, book_num)
    inference_data = model.inference(data)
    return inference_data
