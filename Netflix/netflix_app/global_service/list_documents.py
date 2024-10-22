def list_documents(queryset,filter={},field_list = {}):
    obj=queryset(**filter).only(*field_list)
    return obj