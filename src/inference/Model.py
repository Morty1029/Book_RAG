from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain_core.vectorstores import VectorStoreRetriever
from openai import OpenAI
from constants import RECOMMENDATION_COUNT
from typing import Optional
from data_processing.ClientInputData import ClientInputData
from api.contracts import BotAnswer
from inference.configs.InferenceConfig import InferenceConfig


class Model:
    def __init__(self, retriever: Optional[VectorStoreRetriever] = None):
        self.retriever = retriever
        self.config = InferenceConfig()
        self.client = OpenAI(api_key=self.config.api_key, base_url=self.config.api_url)
        self.sys_prompt = """
Ты часть RAG системы по поиску информации по книгам о Гарри Поттере.\n
Пользователь задает вопросы по сюжету/персонажам книги, ты предоставляешь ответ на основе базы знаний по книге, с указанием глав/частей книги, на основе которых был сформирован ответ.\n
Информация о частях книги тебе будет подаваться RAG составляющей, не забудь ее упомянуть при ответе.\n
Перед ответом проверяй себя - из-за неверных твоих ответов пользователь может не выжить, ты же не хочешь, чтобы кто-то из-за тебя умер.\n
"""

    def load_model(self):
        self.set_retriever()

    def set_retriever(self):
        embeddings = HuggingFaceEmbeddings(model_name=self.config.retriever_model)
        self.retriever = FAISS.load_local(
            "src/inference/HP_vector_store",
            embeddings=embeddings,
            allow_dangerous_deserialization=True,
        ).as_retriever()

    def inference(self, data: ClientInputData) -> BotAnswer:
        if data.book_num == 0:
            retriever_res = self.retriever.invoke(data.prompt, k=RECOMMENDATION_COUNT)
        else:
            retriever_res = self.retriever.invoke(
                data.prompt,
                k=RECOMMENDATION_COUNT,
                filter={"Номер книги": data.book_num},
            )
        response = self.client.chat.completions.create(
            model=self.config.model,
            messages=[
                {
                    "role": "user",
                    "content": f"""
                        {self.sys_prompt}]\n
                        'Запрос пользователя: {data.prompt}\n
                        'Результаты rag: {"".join(res.page_content for res in retriever_res)}
                        'Использованные части: {"".join(str(res.metadata) for res in retriever_res)}
                                    """,
                }
            ],
        )
        return BotAnswer(answer=response.choices[0].message.content, metadata=None)
