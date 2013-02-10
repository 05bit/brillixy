from adminkit.panels import AllModelsPanel


class MyModelsPanel(AllModelsPanel):
    def app_groups(self):
        return (
            # No title for group
            # (u"", ('auth', 'sites')),

            # With title for group
            (u"Auth & Sites", ('auth', 'sites')),
        )
