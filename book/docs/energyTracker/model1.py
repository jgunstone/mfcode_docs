# generated by datamodel-codegen:
#   filename:  person1.json
#   timestamp: 2022-01-25T15:47:40+00:00

from __future__ import annotations

from typing import Any, Optional

from pydantic import BaseModel, Field, conint


class Shit(BaseModel):
    first_name: str = Field(..., description="The person's first name.")
    last_name: str = Field(..., description="The person's last name.")
    age: Optional[conint(ge=0)] = Field(None, description='Age in years.')
    comment: Optional[Any] = None