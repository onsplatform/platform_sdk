from .core_base_entity import CoreBaseEntity

class App(CoreBaseEntity):

    def __init__(self,url):
        super.__init__(url,'installedApp')
