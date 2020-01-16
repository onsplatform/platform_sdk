from core_api.base_entity import BaseCoreEntity

class Map(BaseCoreEntity):

    def __init__(self,url):
        super.__init__(url,'map')

    