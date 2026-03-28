**Assignment Round: DevOps Engineer, TUMMOC**

This project demonstrates:
Application containerization using Docker, Multi-container orchestration using Docker Compose,
Monitoring setup with Prometheus and Grafana,Infrastructure provisioning using Terraform (AWS),
CI/CD pipeline using Jenkins

Docker Setup Build & Run: docker compose up --build 

Services
Flask App → http://localhost:5000
Prometheus → http://localhost:9090
Grafana → http://localhost:3000

Prometheus scrapes metrics from Flask app (/metrics) and grafana visualizes metrics
Steps:
Open Grafana → http://localhost:3000
Add Prometheus data source: http://prometheus:9090
Create dashboard with query: request_count

Jenkins Pipeline stages:
Clone code from GitHub
Lint code 
Run tests 
Build Docker image
Push image to Docker Hub
Deploy using Docker Compose

Terraform provisioned resources:
VPC
Subnet
Internet Gateway
Route Table
Security Group
EC2 Instance

Deploy Infrastructure
cd terraform
terraform init
terraform plan
terraform apply
