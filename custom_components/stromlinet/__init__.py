from homeassistant.config_entries import ConfigEntry
from homeassistant.const import Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    username = entry.options.get('username')
    password = entry.options.get('password')

    #api = Stromlinet(username, password)
    #await api.refresh()

    await hass.config_entries.async_forward_entry_setups(entry, [Platform.SENSOR])
    return True

