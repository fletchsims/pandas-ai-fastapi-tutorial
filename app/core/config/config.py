from pandasai import Agent
from pandasai.connectors import PandasConnector
from pandasai.connectors.pandas import PandasConnectorConfig

from app.core.llm.openai import MyOpenAI
from app.core.parser.response_parser import PandasDataFrame
from app.core.services.helpers import get_env
from app.core.services.reader import read_data_with_dtype


def create_agent_instance() -> Agent:
    data = read_data_with_dtype(get_env("PATH_TO_DATA"))
    connector = PandasConnector(
        PandasConnectorConfig(original_df=data),
    )
    data_custom_head = data.head(25)
    openai = MyOpenAI(api_token=get_env("OPENAI_API"))
    return Agent(
        connector,
        config={
            "llm": openai,
            "response_parser": PandasDataFrame,
            "custom_head": data_custom_head,
        },
    )
