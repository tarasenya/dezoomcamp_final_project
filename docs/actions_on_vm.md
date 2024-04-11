1. Log in to prefect cloud using API key:
 ```bash
prefect cloud login
```
1. Create a new work pool on a development environment:
```bash
prefect work-pool create --type cloud-run cloud_work_pool
```
2. In Prefect Cloud UI edit a work pool. We are going to modify just a few of the available fields.
* Specify the region for the cloud run job.
* Save the name of the service account created by terraform.
The work pool is now ready to receive scheduled flow runs.
3. Deploy a Cloud Run worker. 
```bash
export PREFECT_API_URL='https://api.prefect.cloud/api/accounts/<ACCOUNT-ID>/workspaces/<WORKSPACE-ID>'
export PREFECT_API_KEY='<YOUR-API-KEY>'
```
1. Once those variables are set, run the following shell command to deploy your worker as a service. 
```bash
   gcloud run deploy prefect-worker --image=prefecthq/prefect:2-latest \
--set-env-vars PREFECT_API_URL=$PREFECT_API_URL,PREFECT_API_KEY=$PREFECT_API_KEY \
--service-account <YOUR-SERVICE-ACCOUNT-NAME> \
--no-cpu-throttling \
--min-instances 1 \
--args "prefect","worker","start","--install-policy","always","--with-healthcheck","-p","<WORK-POOL-NAME>","-t","cloud-run"
```
2. After running this command, you'll be prompted to specify a region. Choose the same region that you selected when creating the Cloud Run work pool in the second step of this guide. The next prompt will ask if you'd like to allow unauthentiated invocations to your worker, select "No".

After a few seconds, you'll be able to see your new prefect-worker service by navigating to the Cloud Run page of your Google Cloud console. Additionally, you should be able to see a record of this worker in the Prefect UI on the work pool's page by navigating to the Worker tab.

3. 
```bash
gcloud auth configure-docker us-docker.pkg.dev
```