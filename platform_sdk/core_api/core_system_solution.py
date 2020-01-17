from .core_base_entity import CoreBaseEntity


class SystemSolution(CoreBaseEntity):

    def __init__(self, url):
        super().__init__(url, 'system')
