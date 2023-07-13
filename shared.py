def map_to_sql_row_values(object_values):
    values = map(lambda value: map_value_by_type(value), object_values)
    return ','.join(list(values))

def map_value_by_type(value):
    value_type = type(value)
    if value_type is str:
        return f"'{value}'"
    else:
        return f'{value}'