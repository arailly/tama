import os
from flask import Flask, request, jsonify, render_template
import helper as h

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html',
                           passage_files=h.get_passage_files(),
                           trajectory_files=h.get_trajectory_files())


@app.route('/api')
def api_index():
    return jsonify({
        'message': 'hello world'
    })


@app.route('/passages', methods=['GET'])
def passages():
    passage = h.Passage()
    passage.load('data/passages/a202.csv')
    return render_template('passage.html', passage=passage.to_json())


@app.route('/api/passages', methods=['GET', 'POST'])
def api_passages():
    if request.method == 'GET':
        return jsonify({
            'files': h.get_passage_files()
        })

    elif request.method == 'POST':
        f = request.files['passage_file']
        h.upload_passage_file(f)
        return 'success'


@app.route('/api/trajectories', methods=['GET', 'POST'])
def api_trajectories():
    if request.method == 'GET':
        return jsonify({
            'files': h.get_trajectory_files()
        })

    elif request.method == 'POST':
        f = request.files['trajectory_file']
        h.upload_trajectory_file(f)
        return 'success'


if __name__ == '__main__':
    app.run(debug=True)
