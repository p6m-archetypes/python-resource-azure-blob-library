from __future__ import annotations

from azure.storage.blob.aio import BlobServiceClient

_client: BlobServiceClient | None = None


async def init_azure_blob(settings) -> None:
    global _client
    conn_str = (
        f"DefaultEndpointsProtocol=http;"
        f"AccountName={settings.azure_account_name};"
        f"AccountKey={settings.azure_account_key};"
        f"BlobEndpoint={settings.azure_endpoint};"
    )
    _client = BlobServiceClient.from_connection_string(conn_str)


async def close_azure_blob() -> None:
    global _client
    if _client is not None:
        await _client.close()
        _client = None


def get_azure_blob() -> BlobServiceClient:
    if _client is None:
        raise RuntimeError("Azure Blob not initialized — call init_azure_blob() first")
    return _client
