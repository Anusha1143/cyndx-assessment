resource "google_secret_manager_secret" "llm_api_key" {
  secret_id = "llm-api-key"

  replication {
    auto {}
  }
}

resource "google_secret_manager_secret_version" "llm_api_key_version" {
  secret      = google_secret_manager_secret.llm_api_key.id
  secret_data = var.llm_api_key
}
