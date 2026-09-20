"""Shared client factory for the cookbooks.

Reads TYPESAFE_API_KEY from the environment or a local .env file.
Set JEV_TLS12=1 if every call hangs and ends in TypeSafeAPITimeoutError:
some network paths drop the oversized post-quantum TLS 1.3 ClientHello
that OpenSSL 3.5 sends; capping at TLS 1.2 works around it.
"""

import os
import ssl

import httpx2
from dotenv import load_dotenv
from typesafe_sdk import TypeSafeClient

load_dotenv()


def make_client() -> TypeSafeClient:
    if os.getenv("JEV_TLS12"):
        tls = ssl.create_default_context()
        tls.maximum_version = ssl.TLSVersion.TLSv1_2
        return TypeSafeClient(http_client=httpx2.Client(verify=tls))
    return TypeSafeClient()
