### Cloud & DevOps Engineer — Final-year CSE @ LPU

Building cloud infrastructure with AWS, Azure, Terraform, Docker, and Kubernetes. 4x Oracle Cloud Certified. Open to Cloud/DevOps/SRE roles.

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat&logo=argo&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

---

### Projects

**[observability-fargate](https://github.com/SannidhiSriram-06/observability-fargate)**
Security observability pipeline on AWS ECS Fargate (zero EC2). Prometheus scrapes infrastructure metrics, Grafana visualizes across a 3-panel dashboard, alert rule fires on request-rate threshold breach. Full stack — VPC, subnets, IGW, security groups, ECR, least-privilege IAM roles, CloudWatch logging — provisioned via Terraform with zero manual console steps.
`AWS · Terraform · Prometheus · Grafana · Docker`

**[ai-test-generator-gitops](https://github.com/SannidhiSriram-06/ai-test-generator-gitops)**
FastAPI service generating pytest suites from Python code via Groq's LLaMA 3.1, rate-limited and input-validated. Jenkins pipeline enforces a 70% coverage gate (87% achieved), builds and tags Docker images by build number + commit SHA, pushes to AWS ECR, and updates a GitOps repo's Helm values — ArgoCD auto-syncs to Kubernetes with zero manual deployment steps.
`FastAPI · Jenkins · Docker · Kubernetes · Helm · ArgoCD · AWS ECR`

**[self-healing-microservice](https://github.com/SannidhiSriram-06/self-healing-microservice)**
Four-layer self-healing system on AWS — application health checks, container-level restart, ASG instance replacement, and ALB traffic isolation — recovers from failures without manual intervention. Multi-AZ VPC, load balancer, and Auto Scaling Group (2–4 instances, CPU-based) provisioned via Terraform. GitHub Actions CI integrates Snyk to block vulnerable images pre-push.
`AWS · Terraform · Docker · GitHub Actions · Snyk`

**[cloud-support-ticket-simulation](https://github.com/SannidhiSriram-06/cloud-support-ticket-simulation)**
Hands-on simulation of an AWS Cloud Support Engineering workflow — remote fault diagnosis via SSM Session Manager and Client VPN, log analysis with CloudWatch Logs Insights, point-in-time recovery with AWS Backup, and customer-facing incident documentation.
`AWS Backup · SSM · Client VPN · CloudWatch Logs Insights · EC2`

**[Infosys_AI_KYC_Compliance](https://github.com/SannidhiSriram-06/Infosys_AI_KYC_Compliance)**
Full-stack KYC document verification platform for BFSI — document classification, OCR extraction, GNN-based fraud detection. React frontend on S3, Node.js backend and Flask ML service on separate EC2 instances. Built during Infosys Springboard internship.
`AWS EC2/S3 · Flask · PyTorch · Node.js · MongoDB Atlas`

**[AI-Patient-Triage-System-on-Azure](https://github.com/SannidhiSriram-06/AI-Patient-Triage-System-on-Azure-CSA-Case-Study-)**
Flask app on Azure App Service — routes patient symptoms to Azure OpenAI for triage classification, logs every interaction to Azure Table Storage.
`Azure App Service · Azure OpenAI · Table Storage`

**[Bookstore-Microservice-Architecture-on-AWS](https://github.com/SannidhiSriram-06/Bookstore-Microservice-Architecture-on-AWS)**
Serverless case study translating a Node.js Express API into AWS-managed services — Lambda, API Gateway, MongoDB Atlas, CloudWatch.
`AWS Lambda · API Gateway · MongoDB Atlas`

---

### Experience

**AI Intern — Cloud Deployment Lead**, Infosys Springboard (Feb–Mar 2026)
Led cloud deployment for a 25-member cohort building a BFSI-sector AI KYC system under Agile methodology. Evaluated SageMaker, Lambda, and EC2 for the ML service, selecting EC2 for cost efficiency and deployment control. Managed Git workflow and access across the cohort.

### Certifications

Oracle Cloud Infrastructure — DevOps Professional, Observability Professional, Multicloud Architect Professional, Generative AI Professional (4x, 2025)
Microsoft Certified — Azure Fundamentals (AZ-900), Azure AI Fundamentals (AI-900)
Top 500 Globally, Oracle Race to Certification 2025

---

[LinkedIn](https://linkedin.com/in/sannidhi-sriram) · [Portfolio](https://sannidhisriram-06.github.io)
