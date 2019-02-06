import subprocess

import requests
from celery import Celery
from rest_framework import status

from apps.critical.core import generate_data_for_response

app = Celery('tasks', broker='amqp://localhost')


@app.task
def get_critical_css(css, url, width, height, post_type, term_id, post_id, hook):
    penthouse = subprocess.Popen(
        f"node penthouse.js {css} {url} {width} {height}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = penthouse.communicate()
    penthouse.wait()
    if stderr:
        response = {
            'content': stderr, 'status': status.HTTP_400_BAD_REQUEST
        }
    else:
        response = generate_data_for_response(post_type, term_id, post_id, stdout)
    requests.post(hook, data=response)
    return True
