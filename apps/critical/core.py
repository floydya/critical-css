import subprocess

from rest_framework import status


def get_critical_css(css, url, width, height):
    penthouse = subprocess.Popen(
        f"node penthouse.js {css} {url} {width} {height}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = penthouse.communicate()
    penthouse.wait()
    if stderr:
        return {
            'content': stderr, 'status': status.HTTP_400_BAD_REQUEST
        }
    return {'content': stdout, 'status': 200}
