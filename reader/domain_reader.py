from pony import orm
from platform_sdk.reader.orm_map import RemoteField, RemoteMap
from platform_sdk.schema.schema_api import SchemaApi

class DomainReader:
    def __init__(self, db):
        self.db = db
        self.schema_api = SchemaApi()

    def get_data(self, solution, app, _map):
        api_response = self.schema_api.get_schema(solution, app, _map)
        if api_response is None:
            return 

        model = self._get_model(api_response['model'], api_response['fields'])

        ret = self._execute_query(model)

        return self._get_response_data(ret, api_response['fields'])

    def _execute_query(self, model): # pragma: no cover
        proxy_model = model.build(self.db)
        self.db.generate_mapping(create_tables=True)
        with orm.db_session():
            return list(orm.select(d for d in proxy_model))

    def _get_response_data(self, entities, fields):
        if entities:
            return [{f['alias']: getattr(e, f['alias']) for f in fields} for e in entities]

    def _get_fields(self, fields):
        return [RemoteField(f['alias'], str, f['name']) for f in fields]

    def _get_model(self, model, fields):
        return RemoteMap(model['name'], model['table'], self._get_fields(fields))