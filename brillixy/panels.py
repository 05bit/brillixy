class BasePanel(object):
    """Base panel class for admin dashboard.
    """

    # Template used to render the panel
    template = None

    # User permissions required for the panel to be rendered
    permissions = []

    # Nice panel title used in template
    title = None

    # Integer value for defining panel width. Panel is rendered as
    # <dib class="spanX">...</div> block, if not specified 'span6'
    # class is used.
    span = None

    # Panel styles, e.g: 'panel-big'. The styles are not universal and
    # actually depends on particular panel template & css.
    styles = None

    def __init__(self, site, request):
        """Panel is instantiated per-request, `site` and `request`
        arguments are required.
        """
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
