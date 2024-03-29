export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pipenv install --deploy
pipenv shell