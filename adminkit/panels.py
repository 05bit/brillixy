class BasePanel(object):
    title = None
    template = None
    span = None
    permissions = []


class ModelsListPanel(BasePanel):
    template = 'adminkit/_model_index.html'


class AllModelsPanel(BasePanel):
    template = 'adminkit/_model_index.html'
