import logging
import asyncio
from homeassistant.core import HomeAssistant
from homeassistant.components.button import ButtonEntity
from .media_player import SpeakerCraftZ
from . import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass: HomeAssistant, config, async_add_entities, discovery_info=None):
    _LOGGER.debug("async_setup_platform() entry")
    
    devices = []
    sc = hass.data[DOMAIN].sc
    
    devices.append(SpeakercraftMasterPower(hass, sc.controller))

    zones = None

    while zones is None:
        zones = hass.data[DOMAIN].zones
        await asyncio.sleep(1)

    for key in zones:
        devices.append(SpeakercraftTrebleFlat(hass, zones[key], sc.zones[key]))
        devices.append(SpeakercraftTrebleUp(hass, zones[key], sc.zones[key]))
        devices.append(SpeakercraftTrebleDown(hass, zones[key], sc.zones[key]))
        devices.append(SpeakercraftBassFlat(hass, zones[key], sc.zones[key]))       
        devices.append(SpeakercraftBassUp(hass, zones[key], sc.zones[key]))  
        devices.append(SpeakercraftBassDown(hass, zones[key], sc.zones[key]))
        devices.append(SpeakercraftVolumeUp(hass, zones[key], sc.zones[key]))
        devices.append(SpeakercraftVolumeDown(hass, zones[key], sc.zones[key]))

    async_add_entities(devices)
    _LOGGER.debug("async_setup_platform() exit")

class SpeakercraftMasterPower(ButtonEntity):
    # Existing code for Master Power button...

class SpeakercraftBassFlat(ButtonEntity):
    # Existing code for Bass Flat button...

class SpeakercraftTrebleFlat(ButtonEntity):
    # Existing code for Treble Flat button...

class SpeakercraftBassDown(ButtonEntity):
    # Existing code for Bass Down button...

class SpeakercraftBassUp(ButtonEntity):
    # Existing code for Bass Up button...

class SpeakercraftTrebleDown(ButtonEntity):
    # Existing code for Treble Down button...

class SpeakercraftTrebleUp(ButtonEntity):
    # Existing code for Treble Up button...

class SpeakercraftVolumeUp(ButtonEntity):
    def __init__(self, hass: HomeAssistant, name: str, scz):
        self._name = name + " Volume Up"
        _LOGGER.debug("Volume Up init, Zone " + str(scz.zone) + ", name: " + self._name)
        super().__init__()
        self._hass = hass
        self._zone = scz 

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return "speakercraft_zone" + str(self._zone.zone) + "_volumeup"

    async def async_press(self, **kwargs) -> None:
        _LOGGER.debug(self._name + " pressed")
        self._zone.cmdvolumeup()

class SpeakercraftVolumeDown(ButtonEntity):
    def __init__(self, hass: HomeAssistant, name: str, scz):
        self._name = name + " Volume Down"
        _LOGGER.debug("Volume Down init, Zone " + str(scz.zone) + ", name: " + self._name)
        super().__init__()
        self._hass = hass
        self._zone = scz 

    @property
    def name(self):
        return self._name

    @property
    def unique_id(self):
        return "speakercraft_zone" + str(self._zone.zone) + "_volumedown"

    async def async_press(self, **kwargs) -> None:
        _LOGGER.debug(self._name + " pressed")
        self._zone.cmdvolumedown()
