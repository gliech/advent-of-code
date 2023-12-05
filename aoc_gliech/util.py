def data():
    import logging
    logging.basicConfig(level=logging.DEBUG)
    import traceback
    from aocd import data
    return traceback.extract_stack()
