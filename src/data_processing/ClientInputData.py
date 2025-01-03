from dataclasses import dataclass


@dataclass
class ClientInputData:
    prompt: str
    book_num: int
