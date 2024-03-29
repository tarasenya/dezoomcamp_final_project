variable "project" {
  description = "Project"
  # Change it for you project
  default     = "dataengineeringzoomcamp-409819"
}

variable "region" {
  description = "Region"
  default     = "europe-west3"
}

variable "location" {
  description = "Project Location"
  default     = "europe-west3-c"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "koala_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "koala_bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}

variable "server_name" {
  description = "Name of a GCP VM instance"
  default = "cloudshell"
}

variable "machine_type" {
  description = "GCP VM type"
  default = "e2-standard-4"
}

variable "service_account_email" {
  description  = "Existing service accoutn email adress"
  default = "data-engineering-user@dataengineeringzoomcamp-409819.iam.gserviceaccount.com"
}