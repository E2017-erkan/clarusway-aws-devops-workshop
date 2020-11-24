project-: Docker Swarm Deployment of Phonebook Application (Python Flask) with

- infrastructure
    - Public Repository on Gitthub (Codebase, Versioning system)
    - Docker Swarm os Orchestrator
        - 3 Manager
        - 2 Worker
- Image repository (AWS ECR)
- Should be eble to
    -Every ECR is able to talk each other (EC2 Connect CLI, IAM Policy)        
    - Grand Master can pull image from ECR and push image to AWS ECR
    - Mangers and Workers can pull image from AWS ECR.
- Application Deployement
    - Dockerfile
    - docker-compose.yml (Web server and Mysql)