import subprocess


def get_critical_css(css, url, width, height):
    penthouse = subprocess.Popen(
        f"node penthouse.js {css} {url} {width} {height}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    stdout, stderr = penthouse.communicate()
    penthouse.wait()
    print(stderr)
    assert not penthouse.returncode, \
        f'Penthouse command failed ({penthouse.returncode}): {stderr}'
    return stdout

