from pandasai import SmartDataframe
from pandasai.llm import OpenAI

from app.core.parser.response_parser import PandasDataFrame


class MyOpenAI(OpenAI):

    def __init__(
        self,
        api_token,
        model: str = "gpt-3.5-turbo",
        name: str = None,
        description: str = None,
        config=None,
        **kwargs
    ):
        super().__init__(api_token, **kwargs)
        self.llm = OpenAI(api_token=api_token, model=model)

        if name is None:
            name = "DataFrame"

        if description is None:
            description = "Rows of data"

        if config is None:
            config = {
                "enforce_privacy": False,
                "llm": self.llm,
                "verbose": True,
                "response_parser": PandasDataFrame,
            }

        self.name = name
        self.description = description
        self.config = config

    def chat(self, df, prompt, config):
        df = SmartDataframe(
            df, name=self.name, description=self.description, config=config
        )
        return df.chat(prompt)
