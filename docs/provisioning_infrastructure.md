# Provisioning the Infrastructure on GCP.
The following is assumed:
0. The project has been cloned into a local environment (laptop):
   ```git clone https://github.com/tarasenya/dezoomcamp_final_project.git```
1. CLI ```gcloud``` is installed and authorised to a GCP account.
2. The project you want to use for the project has been created (then change the variable "project" ```infra/variables.tf``` to the defined name).
3. The following APIs has been activated for the project:
| NAME                                | TITLE                                    |
|-------------------------------------|------------------------------------------|
| analyticshub.googleapis.com         | Analytics Hub API                        |
| bigquery.googleapis.com             | BigQuery API                             |
| bigqueryconnection.googleapis.com   | BigQuery Connection API                  |
| bigquerydatapolicy.googleapis.com   | BigQuery Data Policy API                 |
| bigquerymigration.googleapis.com    | BigQuery Migration API                   |
| bigqueryreservation.googleapis.com  | BigQuery Reservation API                 |
| bigquerystorage.googleapis.com      | BigQuery Storage API                     |
| cloudapis.googleapis.com            | Google Cloud APIs                        |
| cloudresourcemanager.googleapis.com | Cloud Resource Manager API               |
| cloudtrace.googleapis.com           | Cloud Trace API                          |
| compute.googleapis.com              | Compute Engine API                       |
| dataform.googleapis.com             | Dataform API                             |
| dataplex.googleapis.com             | Cloud Dataplex API                       |
| datastore.googleapis.com            | Cloud Datastore API                      |
| datastudio.googleapis.com           | Looker Studio API                        |
| iam.googleapis.com                  | Identity and Access Management (IAM) API |
| iamcredentials.googleapis.com       | IAM Service Account Credentials API      |
| logging.googleapis.com              | Cloud Logging API                        |
| looker.googleapis.com               | Looker (Google Cloud core) API           |
| monitoring.googleapis.com           | Cloud Monitoring API                     |
| oslogin.googleapis.com              | Cloud OS Login API                       |
| servicemanagement.googleapis.com    | Service Management API                   |
| serviceusage.googleapis.com         | Service Usage API                        |
| sql-component.googleapis.com        | Cloud SQL                                |
| storage-api.googleapis.com          | Google Cloud Storage JSON API            |
| storage-component.googleapis.com    | Cloud Storage                            |
| storage.googleapis.com              | Cloud Storage API                        |