from celery import Celery
cel = Celery("AsynchronousTasks")

# def make_celery(app):
#     celery = Celery(app.import_name)
#     celery.conf.broker_url = app.config["BROKER"]
#     celery.conf.backend = app.config["BACKEND"]
#     celery.conf.enable_utc = app.config["ENABLE_UTC"]
#     celery.conf.timezone = app.config["TIMEZONE"]

#     class ContextTask(celery.Task):
#         def __call__(self,*args,**kwargs):
#             with app.app_context():
#                 return self.run(*args,**kwargs)

#     celery.Task = ContextTask
#     return celery


