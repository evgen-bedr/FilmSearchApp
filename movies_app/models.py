from db_connect import execute_query

class Media:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    @classmethod
    def get_by_query(cls, query, params=None):
        results, fields = execute_query(query, params)
        if not results:
            return []
        return [cls(**dict(zip(fields, result))) for result in results]

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dict(self):
        return {key: getattr(self, key) for key in self.__dict__.keys() if getattr(self, key) is not None}



