# Cyndx LangGraph API

Production-ready LangGraph API deployed via Docker and Terraform to Google Cloud Run.

---

# 1. Architecture Overview

## System Architecture Diagram

```mermaid
flowchart TD
    User -->|HTTP Request| FastAPI
    FastAPI --> Routes
    Routes --> LangGraph
    LangGraph --> Nodes
    Nodes --> Tools
    Nodes --> State

    FastAPI --> Middleware
    FastAPI --> Metrics

    subgraph Google Cloud
        CloudRun
        ArtifactRegistry
        SecretManager
        CloudMonitoring
    end

    Terraform --> CloudRun
    Terraform --> SecretManager
    Terraform --> IAM
    Terraform --> Monitoring
