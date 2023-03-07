from dataclasses import dataclass
from typing import Final


@dataclass
class CorsConstants:
    DEV_ORIGINS: Final = "https://72wjbp.deta.dev/"
    DEV_HEADERS: Final = (
        "Content-Type",
        "X-Amz-Date",
        "X-Amz-Security-Token",
        "Authorization",
        "X-Api-Key",
        "X-Requested-With",
        "Accept",
        "Access-Control-Allow-Methods",
        "Access-Control-Allow-Origin",
        "Access-Control-Allow-Headers",
    )
    METHODS: Final = ("GET", "OPTIONS", "POST", "PUT", "DELETE", "HEAD", "PATCH")
