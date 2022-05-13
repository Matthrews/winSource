from django.apps import AppConfig


class BackgroundTasksAppConfig(AppConfig):
    name = 'background_task'
    # from background_task import __version__ as version_info
    # verbose_name = 'Background Tasks ({})'.format(version_info)
    verbose_name = "后台任务"

    def ready(self):
        import background_task.signals  # noqa
