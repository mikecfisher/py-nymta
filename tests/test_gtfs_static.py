"""Tests for GTFSCache static feed downloads."""

import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, Mock

import pytest

from pymta.constants import STATIC_GTFS_URLS
from pymta.gtfs_static import GTFSCache


def test_static_gtfs_urls_use_mta_s3_bucket():
    """Static feeds should point at MTA's rrgtfsfeeds S3 bucket, not legacy web.mta.info URLs."""
    for name, url in STATIC_GTFS_URLS.items():
        assert url.startswith("https://rrgtfsfeeds.s3.amazonaws.com/gtfs_"), (
            f"{name} URL should be on rrgtfsfeeds: {url}"
        )
        assert "web.mta.info" not in url


@pytest.mark.asyncio
async def test_download_gtfs_rejects_non_zip_response():
    """Downloads that return HTML (e.g. after a redirect) should fail with a clear error."""
    html_body = b"<!DOCTYPE html><html><body>not a zip</body></html>"

    mock_response = AsyncMock()
    mock_response.read = AsyncMock(return_value=html_body)
    mock_response.raise_for_status = Mock()
    mock_response.headers = {"Content-Type": "text/html; charset=utf-8"}
    mock_response.__aenter__ = AsyncMock(return_value=mock_response)
    mock_response.__aexit__ = AsyncMock(return_value=None)

    mock_session = Mock()
    mock_session.get = Mock(return_value=mock_response)

    with tempfile.TemporaryDirectory() as tmpdir:
        cache = GTFSCache(cache_dir=Path(tmpdir), ttl_hours=0)
        with pytest.raises(ValueError, match="did not return a ZIP file"):
            await cache.download_gtfs(
                url="https://example.com/gtfs.zip",
                feed_name="bus_manhattan",
                session=mock_session,
            )

        assert not (Path(tmpdir) / "bus_manhattan.zip").exists()