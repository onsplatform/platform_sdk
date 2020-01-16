from .core_base_entity import CoreBaseEntity

class Map(BaseCoreEntity):

    def __init__(self,url):
        super.__init__(url,'map')

    