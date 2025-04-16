from flask import Blueprint, request, jsonify
import subprocess
import uuid
import os

r_runner = Blueprint('r_runner', __name__)
SCRIPTS_DIR = 'scripts'
OUTPUT_DIR = 'static/plots'


@r_runner.route('', methods=['POST'])
def run_r_code():
    data = request.get_json()
    code: str = data.get('code', '').strip()

    if not code:
        return jsonify({'error': 'Missing R code'}), 400

    file_id = str(uuid.uuid4())
    output_filename = f'{file_id}.html'

    backend_root = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '..'))
    output_path = os.path.join(
        backend_root, OUTPUT_DIR, output_filename).replace('\\', '/')
    script_path = os.path.join(backend_root, SCRIPTS_DIR, f'{file_id}.R')

    full_code = f'''
tryCatch({{
{code}
htmlwidgets::saveWidget(fig, "{output_path}", selfcontained = TRUE)
}}, error = function(e) {{
  cat("Error:", conditionMessage(e), "\\n")
  quit(save='no', status=1)
}})
'''

    with open(script_path, 'w') as f:
        f.write(full_code)

    try:
        result = subprocess.run(
            ['Rscript', '--vanilla', script_path],
            cwd=backend_root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
            text=True,
        )

        if result.returncode != 0:
            return jsonify({
                'error': 'R execution failed',
                'stdout': result.stdout,
                'stderr': result.stderr,
                'script_path': script_path
            }), 500

    except subprocess.TimeoutExpired:
        return jsonify({'error': 'R script timed out'}), 500
    except Exception as e:
        return jsonify({'error': f'Unexpected server error: {str(e)}'}), 500
    finally:
        os.remove(script_path)

    return jsonify({'file_url': f'/static/plots/{output_filename}'}), 200
