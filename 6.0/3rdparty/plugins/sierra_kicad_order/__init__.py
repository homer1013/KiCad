try:
    from .action_sierra_quote import RequestQuote
    RequestQuote().register()
     # Instantiate and register to Pcbnew
except Exception as e:
    import os
    plugin_dir = os.path.dirname(os.path.realpath(__file__))
    try:
        log_file = 'D:\Practice\SierraQuoteError.log'
        with open(log_file, 'w+') as f:
            f.write(repr(e) + "\n")
    except:
        pass
