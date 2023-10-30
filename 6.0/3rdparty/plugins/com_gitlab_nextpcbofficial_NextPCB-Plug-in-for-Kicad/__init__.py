try:
    from .plugin import NextPCBPlugin
    plugin = NextPCBPlugin()
    plugin.register()
except Exception as e:
    import logging
    root = logging.getLogger()
    root.debug(repr(e))
