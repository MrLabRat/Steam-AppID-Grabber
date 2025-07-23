import Millennium, PluginUtils # type: ignore
from settings import PluginSettings
from logger import logger
import time

# Minimal backend implementation for the Steam AppID Display plugin
class Backend:
    @staticmethod 
    def receive_frontend_message(message: str, status: bool, count: int):
        """
        Example method that can be called from the frontend.
        Not used in this plugin but required for compatibility.
        """
        logger.log(f"Received message: {message}, status: {status}, count: {count}")
        return True

class Plugin:

    # if steam reloads, i.e. from a new theme being selected, or for other reasons, this is called. 
    # with the above said, that means this may be called more than once within your backends lifespan 
    def _front_end_loaded(self):
        """
        Called when the frontend has loaded.
        We don't need to do anything here for this simple plugin.
        """
        logger.log("Steam AppID Display frontend loaded")

    def _load(self):
        """
        Called when the plugin is loaded.
        We'll just log that the plugin has loaded and mark as ready.
        """
        logger.log("Steam AppID Display plugin loaded")
        
        # Mark the plugin as ready
        Millennium.ready()


    def _unload(self):
        logger.log("unloading")