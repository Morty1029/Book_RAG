import yaml


class InferenceConfig:
    def __init__(self):
        with open("src/inference/configs/InferenceConfig.yaml") as file:
            data = yaml.safe_load(file)
            self.api_key = data["API_KEY"]
            self.api_url = data["API_URL"]
            self.model = data["model"]
            self.retriever_model = data["retriever_model"]
