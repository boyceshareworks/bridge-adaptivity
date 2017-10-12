from uuid import uuid4

from locust import HttpLocust, task, TaskSet
from lti import ToolConsumer

LTI_LAUNCH = {
    # Please configure valid consumer key and secret
    'consumer_key': '3149ebc75747053890e9',
    'consumer_secret': '8e2d4ee82bc81cd96b2a',
    'launch_url': 'http://127.0.0.1:8008/lti/launch/1',  # Need to be the same as LTI request in the test
    'params': {
        'lti_message_type': 'basic-lti-launch-request',
        'lti_version': 'LTI-1p0',
        'resource_link_id': 'edx-demo-stage.raccoongang.com-4dcd9db5453244c390dea374376389dc',
        'roles': 'Student',  # To check only LMS bridge connection Student should be replaced with Instructor
        'oauth_callback': 'about:blank',
        'context_id': 'course-v1:Raccoon_Gang+RG_001+2017_T3',
    }
}


def generate_data():
    LTI_LAUNCH['params'].update({'user_id': uuid4().hex})
    return ToolConsumer(**LTI_LAUNCH).generate_launch_data()


class UserBehavior(TaskSet):
    @task(1)
    def lti_request(self):
        self.client.post("/lti/launch/1", data=generate_data())


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 6000
