terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

resource "google_service_account" "prefect-service-account" {
  account_id   = "prefect-service-account"
  display_name = "prefect-service-account"
}

resource "google_project_iam_binding" "prefect-service-account" {
  project = var.project
  count   = length(var.rolesList)
  role    = var.rolesList[count.index]
  members = [
    "serviceAccount:${google_service_account.prefect-service-account.email}"
  ]
}

resource "google_storage_bucket" "koala-bucket" {
  name          = var.gcs_bucket_name
  location      = var.region
  force_destroy = true


  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}



resource "google_bigquery_dataset" "koala_dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.region
}

resource "google_artifact_registry_repository" "prefect-repo" {
  location      = var.region
  repository_id = "prefect-repo"
  description   = "Prefect repository"
  format        = "DOCKER"
}