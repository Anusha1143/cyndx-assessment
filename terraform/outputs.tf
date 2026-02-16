output "cloud_run_url" {
  value = google_cloud_run_service.api.status[0].url
}

output "service_account_email" {
  value = google_service_account.api_sa.email
}
