terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.6.0"
    }
  }
}

resource "google_service_account" "service_account" {
  account_id   = "taras-de"
  display_name = "taras-de"
}

resource "google_project_iam_binding" "service_account" {
  project = var.project
  count   = length(var.rolesList)
  role    = var.rolesList[count.index]
  members = [
    "serviceAccount:${google_service_account.service_account.email}"
  ]
}
resource "google_compute_instance" "gcp_vm" {
  name = var.server_name

  machine_type = var.machine_type

  zone = var.location

  boot_disk {
    auto_delete = true

    initialize_params {
      image = "projects/ubuntu-os-cloud/global/images/ubuntu-2204-jammy-v20240223"
      size  = 30
      type  = "pd-balanced"
    }

    mode = "READ_WRITE"
  }

  can_ip_forward      = false
  deletion_protection = false
  enable_display      = false

  network_interface {
    network = "default"
    access_config {

    }
  }
  metadata_startup_script = file("../scripts/initial_script.sh")
  service_account {
    email  = google_service_account.service_account.email
    scopes = ["cloud-platform"]
  }
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
