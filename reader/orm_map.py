from pony import orm


class RemoteMap:
    def __init__(self, name, table, fields):
        self.name = name
        self.table = table
        self.fields = fields

    def build(self, db):
        fields = {f.name: f.build() for f in self.fields}
        fields['_table_'] = self.table
        dyn_type = type(self.name, (db.Entity, ), fields)
        return dyn_type


class RemoteField:
    def __init__(self, name, field_type, column, required=True):
        self.name = name
        self.field_type = field_type
        self.column = column
        self.required = required

    def build(self):
        wrapper = orm.Required if self.required else orm.Optional
        return wrapper(self.field_type, column=self.column)
