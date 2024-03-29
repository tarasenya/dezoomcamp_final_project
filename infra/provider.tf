provider "google" {
    project = var.project
    region = var.region
    zone = var.location
    credentials = "terraform.json"
}