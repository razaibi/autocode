from zcore import data_mapper
import CONFIGS

def process_common_logic(task: dict, data_injector: dict) -> dict:
    if CONFIGS.DATA_KEY in data_injector:
        data = process_datatype_logic(
            task[CONFIGS.CATEGORY_KEY], 
            data_injector[CONFIGS.DATA_KEY]
        )
        return data
    else:
        return data_injector[CONFIGS.DATA_KEY]


def process_datatype_logic(category, data):
    type_based_solutions = [
        'postgresql',
        'sqlserver',
        'dotnet-webapi',
        'fastapi'
    ]
    if category in type_based_solutions:
        for db in data[CONFIGS.SOLUTIONS_TERM]:
            for table in db[CONFIGS.ENTITIES_TERM]:
                for column in table[CONFIGS.ATTRIBUTES_TERM]:
                    column['type'] = map_data_type(
                        column['type'],
                        category
                    )
    return data

def map_data_type(generic_type, target_category):
    datatypes = data_mapper.datatypes
    revised_data_type = datatypes[generic_type][target_category]
    return revised_data_type


    

