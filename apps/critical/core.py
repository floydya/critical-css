import subprocess

from rest_framework import status


def get_critical_css(css, url, width, height, post_type, term_id, post_id):
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
    return generate_data_for_response(post_type, term_id, post_id, stdout)


def generate_data_for_response(post_type, term_id, post_id, styles):
    return {
        'content': {
            'post_type': post_type,
            'term_id': term_id,
            'post_id': post_id,
            'styles': styles
        }
    }
