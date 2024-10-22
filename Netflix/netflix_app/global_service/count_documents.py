def count_documents(queryset,filter={}):
    obj=queryset(**filter).count()
    return obj

def count_documents(queryset,filter={}):
    count = queryset(**filter).count()
    return count