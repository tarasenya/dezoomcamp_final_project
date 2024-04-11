0. It is assumed that one has a Prefect Account. It could be created [here](https://app.prefect.cloud/auth/login). One should create an API key to log into the Prefect Server, this option could be found in the Profile Settings.
![prefect_api_key](/visualization/prefect_api_key.png)
1. Log in to prefect cloud using API key:
 ```bash
prefect cloud login
```
2. Create a new work pool on a development environment:
```bash
prefect work-pool create --type cloud-run cloud_work_pool
```
![prefect_worker](/visualization/prefect_worker_start.png)
2. In Prefect Cloud UI edit a work pool. We are going to modify just a few of the available fields.
* Specify the region for the cloud run job.
* Save the name of the service account created by terraform.
![prefect_worker_properties](/visualization/prefect_worker_properties.png)
The work pool is now ready to receive scheduled flow runs.
3. Deploy a Cloud Run worker. 
```bash
export PREFECT_API_URL='https://api.prefect.cloud/api/accounts/<ACCOUNT-ID>/workspaces/<WORKSPACE-ID>'
export PREFECT_API_KEY='<YOUR-API-KEY>'
```
where _ACCOUNT_ID_ is an account ID in Prefect Cloud and a _WORKSPACE_ID_ is an ID of a created workspace.
4. Once those variables are set, run the following shell command to deploy your worker as a service. 
```bash
 gcloud run deploy prefect-worker --image=prefecthq/prefect:2-latest \
--set-env-vars PREFECT_API_URL=$PREFECT_API_URL,PREFECT_API_KEY=$PREFECT_API_KEY \
--service-account <SERVICE-ACCOUNT-NAME> \
--no-cpu-throttling \
--min-instances 1 \
--args "prefect","worker","start","--install-policy","always","--with-healthcheck","-p","<WORK-POOL-NAME>","-t","cloud-run"
```
where  _SERVICE-ACCOUNT-NAME_ is an email of prefect-service-account created by terraform.
5. After running this command, you'll be prompted to specify a region. Choose the same region that you selected when creating the Cloud Run work pool in the second step of this guide. The next prompt will ask if you'd like to allow unauthentiated invocations to your worker, select "No".

After a few seconds, you'll be able to see your new prefect-worker service by navigating to the Cloud Run page of your Google Cloud console. 
![cloud_run](/visualization/google_cloud_run_prefect_worker.png)
Additionally, you should be able to see a record of this worker in the Prefect UI on the work pool's page by navigating to the Worker tab.
![worker](/visualization/prefect_worker.png)

6.  Authorize to docker artifactory (I use europe-west3 region):
```bash
gcloud auth configure-docker europe-west3-docker.pkg.dev
```
7. Deploy all pipelines executing from the root folder
```bash
prefect deploy --all
```
8. Go to Prefect Cloud, choose deployments and start an inital ingection:
![deployments](/visualization/prefect_cloud_deployments.png)
9. For this workflow the result looks as the following:
![initial_ingection](/visualization/initial_ingection.png)