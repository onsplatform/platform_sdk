
from enum import Enum

class Command:
    def __init__(self, model, fields, filters):
        self.model = model
        self.fields = fields
        self.filter = filters

    def get_filter(self):
        if not self.filter:
            return ''

        return self.str_where + self.filter.get_expression()


class SelectCommand(Command):

    str_select = 'select '
    str_from = ' from '
    str_where = ' where '

    def get_from(self):
        if not self.model:
            raise ValueError('Model is required.')

        return self.str_from + self.model

    def get_select_fields(self):
        if not self.fields:
            raise ValueError('At least one field is required.')

        return str.join(', ', [str(f) for f in self.fields])

    def get_command(self):
        fields = self.get_select_fields()
        str_from = self.get_from()
        str_filter = self.get_filter()
        return self.str_select + fields + str_from + str_filter


class Field:
    def __init__(self, name, alias=None):
        self.name = name
        self.alias = alias or name

    def __repr__(self):
        return f'{self.name} as {self.alias}'


class Filter:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression

    def get_expression(self):
        return self.expression


class Parameters:
    def __init__(self, name, value):
        self.name = name
        self.value = value
