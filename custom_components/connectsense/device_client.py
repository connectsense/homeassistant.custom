from __future__ import annotations

from rebooterpro_async import RebooterProClient

from homeassistant.const import CONF_HOST
from homeassistant.helpers.aiohttp_client import async_get_clientsession

from .const import DOMAIN
from .ssl_utils import get_aiohttp_ssl


async def async_get_client(hass, entry) -> RebooterProClient:
    """Return a shared client for this entry, creating it if needed."""
    store = hass.data.setdefault(DOMAIN, {}).setdefault(entry.entry_id, {})
    if (client := store.get("client")) is None:
        session = async_get_clientsession(hass)
        ssl_ctx = await get_aiohttp_ssl(hass, entry)
        client = RebooterProClient(entry.data[CONF_HOST], session=session, ssl_context=ssl_ctx)
        store["client"] = client
    return client


async def async_close_client(hass, entry_id: str) -> None:
    """Close and drop the shared client for an entry, if present."""
    client = hass.data.get(DOMAIN, {}).get(entry_id, {}).pop("client", None)
    if client:
        await client.aclose()


def build_probe_client(hass, host: str) -> RebooterProClient:
    """Construct a transient client for probing a host during flows."""
    session = async_get_clientsession(hass)
    return RebooterProClient(host, session=session)
