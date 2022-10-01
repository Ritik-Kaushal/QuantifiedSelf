# ---------------IMPORTS---------------
from flask_restful import Resource
from flask import make_response
import json
from utils.jwt_token_utils import token_required
from utils.celery.tasks import export_data
import time
# --------------Export API Class--------------
class ExportAPI(Resource):
    '''
    This is an API class for triggering the export job.
    '''

    @token_required
    def get(self,**kwargs):
        '''
        This function is called when a get request comes. 
        '''
        user = kwargs['user']
        res = export_data.delay(user.id)
        while not res.ready():
            print("Still in progress")
            time.sleep(2)
        if not res.get()[0] : 
            return make_response(json.dumps({"message" : res.get()[1]}),400)
        else:
            return make_response(json.dumps({"message" : res.get()[1]}),200)

        


