from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated
from enum import Enum


class OutputTypeType(str, Enum):
    """
    Output type for the result text
    """
    file = "file"
    base64_string = "base64_string"
    both = "both"


class MethodTypes(str, Enum):
    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    DELETE = 'DELETE'


class InputModel(BaseModel):
#    model_config = ConfigDict(use_enum_values=True)

    url: str = Field(
        description="URL to make a request to."
    )
#    method: Annotated[MethodTypes | None, Field(alias='MethodTypes')] = None
#    method: str = Field(
#        description="HTTP method to use.", 
#        default = MethodTypes.GET,
#        json_schema_extra={"enum": [MethodTypes.GET, MethodTypes.POST, MethodTypes.PUT, MethodTypes.DELETE]}
#    )
    method: MethodTypes = Field(
        default=MethodTypes.GET,
        description="HTTP method to use."
    )
    bearer_token: str = Field(
        default=None,
        description="Bearer token to use for authentication."
    )
    body_json_data: str = Field(
        default="""{
    "key_1": "value_1",
    "key_2": "value_2"
}
""",
        description="JSON data to send in the request body.",
        json_schema_extra={
            'widget': "codeeditor-json",
        }
    )
    output_type: OutputTypeType = Field(
        default=OutputTypeType.both,
        description='Format of the output image. Options are: `file`, `base64_string`, `both`.',
    )


class OutputModel(BaseModel):
    image_base64_string: str = Field(
        default='',
        description='Base64 encoded string of the output image.',
    )
    image_file_path: str = Field(
        default='',
        description='Path to the output image file.',
    )
