"""
    @Filename: session_wrapper.py
    @Author: Nullqwertyuiop, Silverowo
    @Time: 2023/1/24
"""

# pylint: disable=import-error

from contextlib import suppress

from aiohttp import ClientSession


class SessionContainer:
    """
    The session container
    """

    session: dict[str, ClientSession] = {}

    async def get(
        self, name: str = "universal", flush: bool = False, **kwargs
    ) -> ClientSession:
        """
        Get session from session name

        Args:
            name (str): The name of session (default: universal)
            flush (bool): The switch of flush (default: False)
        """
        if flush or name not in self.session or self.session[name].closed:
            self.session[name] = ClientSession(**kwargs)
        return self.session[name]

    async def close(self, name: str):
        """
        Close session from session name

        Args:
            name (str): The name of session
        """
        if name in self.session.copy():
            await self.session[name].close()
            del self.session[name]

    async def close_all(self):
        """
        Close all the sessions
        """
        for name in self.session.copy():
            with suppress(Exception):
                await self.close(name)


sessions = SessionContainer()
