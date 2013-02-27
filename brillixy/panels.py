class BasePanel(object):
    title = None
    template = None
    span = None
    permissions = []

    def __init__(self, site, request):
        self.has_perm = True
        if self.permissions:
            self.has_perm = request.user.has_perm(*self.permissions)                


class ModelsListPanel(BasePanel):
    template = 'brillixy/_model_index.html'


class AllModelsPanel(BasePanel):
    template = 'brillixy/_model_index.html'

    def app_groups(self):
        pass


class ObjectsListPanel(BasePanel):
    template = 'brillixy/_object_index.html'
