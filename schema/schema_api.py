import requests

from pony import orm


class SchemaApi:
    url_schema_api = "http://localhost/schema/{0}/{1}/{2}"

    def __init__(self, db):
        self.db = db

    def get_schema(self, solution, app, _map):
        api_response = self._get_schema_response(solution, app, _map)
        if api_response is None:
            return

        api_response = api_response.json()

        model = self._get_model(api_response['model'], api_response['fields'])

        proxy_model = model.build(self.db)
        self.db.generate_mapping(create_tables=True)

        with orm.db_session():
            ret = list(orm.select(d for d in proxy_model))
        
        return self.get_response_data(ret, api_response['fields'])

    def get_response_data(self, entities, fields):
        return [{f['alias']: getattr(e, f['alias']) for f in fields} for e in entities]

    def _get_schema_response(self, solution, app, _map):
        response = requests.get(self._get_schema_api_url(solution, app, _map))
        if response.ok:
            return response

    def _get_schema_api_url(self, solution, app, _map):
        return self.url_schema_api.format(solution, app, _map)

    def _get_filter(self, _filter):
        return Filter(_filter['name'], _filter['expression'])

    def _get_fields(self, fields):
        return [RemoteField(f['alias'], str, f['name']) for f in fields]

    def _get_model(self, model, fields):
        return RemoteMap(model['name'], model['table'], self._get_fields(fields))


class RemoteField:
    def __init__(self, name, field_type, column, required=True):
        self.name = name
        self.field_type = field_type
        self.column = column
        self.required = required

    def build(self):
        wrapper = orm.Required if self.required else orm.Optional
        return wrapper(self.field_type, column=self.column)


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
