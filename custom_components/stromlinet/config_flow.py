"""Config flow for Strømlinet integration."""
from __future__ import annotations

from typing import Any, Dict, Optional

# import voluptuous as vol

#from homeassistant.core import callback
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult
from homeassistant.exceptions import HomeAssistantError
#from homeassistant.const import CONF_NAME
#from homeassistant.helpers.selector import selector

from .const import DOMAIN

import logging
_LOGGER = logging.getLogger(__name__)

#from datetime import datetime
from custom_components.stromlinet.pynovafos.novafos import Novafos, LoginFailed, HTTPFailed


async def validate_auth(data: dict[str, Any], hass: HomeAssistant) -> None:
    try:
        api = Novafos(data["username"], data["password"])
        await hass.async_add_executor_job(api.authenticate)
    except LoginFailed:
        raise InvalidAuth
    except HTTPFailed:
        raise CannotConnect


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):

    VERSION = 1

    data: Optional[Dict[str, Any]]
    #options: Optional[Dict[str, Any]]

    async def async_step_user(self, user_input: Optional[Dict[str, Any]] = None) -> FlowResult:
        """Invoked when a user initiates a flow via the user interface."""
        errors: Dict[str, str] = {}
        if user_input is not None:
            try:
                await validate_auth(user_input, self.hass)
            except ValueError:
                errors["base"] = "auth"
            if not errors:
                # Input is valid, set data.
                self.data = user_input
                # Return the form of the next step.
                #return await self.async_step_repo()
                return "TODO TODO"

        return self.async_show_form(
            step_id="user", data_schema=AUTH_SCHEMA, errors=errors
        )




class InvalidAuth(HomeAssistantError):
    """Error to indicate there is invalid auth."""
