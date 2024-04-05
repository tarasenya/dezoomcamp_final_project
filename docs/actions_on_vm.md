0. Log on int GCP VM:
1. Clone and go to a project directory
```bash
git clone https://github.com/tarasenya/dezoomcamp_final_project.git
cd dezoomcamp_final_project
```
2. Install JDK, Spark and set the corresponding envrionment variables:
```bash
cd scripts
bash install_spark.sh
source ~/.bashrc
```   
3. Create the corresponding python environment:
```bash
cd ..
export PYTHONPATH="${PYTHONPATH}:$(pwd)"
pipenv install --deploy
pipenv shell
```
4. Start prefect server, deploying the ocrresponding pipelines and starting the initialization pipeline by:

```bash
cd scripts
bash prefect_script.sh
```