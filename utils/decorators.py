# Agrega una Key 'title' al metodo get_contex_data de una View
def contex_data(**params):
    def _contex_data(fn):
        def set_title(*args, **kwargs):
            data = fn(*args, **kwargs)
            for key in params.keys():
                data[key] = params[key]
            return data

        return set_title

    return _contex_data
