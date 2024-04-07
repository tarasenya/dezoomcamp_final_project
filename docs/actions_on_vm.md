0. Log in into GCP VM using SSH:
1. Clone and go to a project directory
```bash
git clone https://github.com/tarasenya/dezoomcamp_final_project.git
cd dezoomcamp_final_project
```
2. Change the project id in a  project field in ```config.ini```
3. Install JDK, Spark and set the corresponding envrionment variables:
```bash
cd scripts
bash install_spark.sh
source ~/.bashrc
```   
4. Create the corresponding python environment:
```bash
cd ..
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pipenv install --deploy
pipenv shell
```
4. Start prefect server, deploying the corresponding pipelines and starting the initialization pipeline by:

```bash
cd scripts
bash prefect_script.sh
```