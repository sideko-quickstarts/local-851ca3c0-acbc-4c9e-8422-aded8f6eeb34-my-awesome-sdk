import pydantic


class HealthCheckResponse(pydantic.BaseModel):
    """
    HealthCheckResponse
    """

    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
    )

    ok: bool = pydantic.Field(
        alias="ok",
    )
