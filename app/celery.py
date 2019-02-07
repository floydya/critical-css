import subprocess
import requests
from celery import Celery
from rest_framework import status


app = Celery('tasks', broker='amqp://localhost')


@app.task
def get_critical_css(css, url, width, height, post_type, term_id, post_id, hook, token):
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
        code = 400
    else:
        response = {
            'post_type': post_type,
            'term_id': term_id,
            'post_id': post_id,
            'styles': stdout,
            'status': 200
        }
        code = 200
    a = requests.post(hook, data=response, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
        'Authentication': f'Critical {token}'
    })
    print(a.content)
    return code
