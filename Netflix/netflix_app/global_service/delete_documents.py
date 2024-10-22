def delete_documents(queryset, json={}):
        obj = queryset(**json).delete()
        return True