import json

import pandas as pd
from fastapi.responses import JSONResponse
from pandasai.responses.response_parser import ResponseParser


class PandasDataFrame(ResponseParser):

    def __init__(self, context) -> None:
        super().__init__(context)


    def parse(self, result):
        res_is_str_and_has_error = (isinstance(result["value"], str)) and (
            "invalid" in result["value"].lower()
            or "openai" in result["value"].lower()
            or "error" in result["value"].lower()
        )
        error_msg = (
            "Sorry, I am having trouble answering that question. Please try again."
        )
        df = pd.DataFrame([result]).to_json(lines=True, orient="records")
        main_msg = json.loads(df)

        return (
            JSONResponse(error_msg)
            if res_is_str_and_has_error
            else JSONResponse(main_msg)
        )
