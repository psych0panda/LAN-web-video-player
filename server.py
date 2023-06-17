"""Module providing function of routing and request handler."""
import importlib
import os
import sys
from typing import Any

from flask import Flask
from flask import render_template
from flask import url_for

importlib.reload(sys)

app = Flask(__name__)

VIDEO_DIR = 'static/videos'
SUFFIX = ['avi', 'rmvb', 'mpg', 'mpeg', 'mpe', 'wmv', 'mp4', 'mkv']


@app.route('/', defaults={'syspath': ''})
@app.route('/<path:syspath>')
def dir_expand(syspath: Any) -> Any:
    """
    Entrypoint
    """
    server_path: str = f"{VIDEO_DIR}/{syspath}"
    if not os.path.exists(server_path):
        return render_template('404.html')
    if os.path.isfile(server_path):
        video_src: str = url_for('static', filename=f'videos/{syspath}')
        return render_template('player.html', video_path=video_src)

    if root := os.listdir(server_path):
        dirs = []
        videos = []
        for child in root:
            file_path: str = os.path.join(syspath, child)
            abs_file_path: str = os.path.join(server_path, child)
            abs_path: str = url_for(
                'dir_expand', syspath=file_path, _external=True)

            if os.path.isdir(abs_file_path):
                dirs.append([child, file_path, abs_path])
            else:
                if child.split('.')[-1].lower() not in SUFFIX:
                    continue
                videos.append([child, file_path, abs_path])
        return render_template('index.html', dirs=dirs, videos=videos)
    return render_template('404.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8888)
