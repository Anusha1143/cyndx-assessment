```mermaid
flowchart TD

    User --> FastAPI
    FastAPI --> Routes
    Routes --> LangGraph
    LangGraph --> Nodes
    Nodes --> Tools
    Nodes --> State

    FastAPI --> Middleware
    FastAPI --> Metrics

    subgraph Google_Cloud
        CloudRun
        ArtifactRegistry
        SecretManager
        CloudMonitoring
    end
