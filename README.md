<div align="center">

<h3><code>sannidhi@cloud ~ $ ./contributions.sh</code></h3>

<img src="./assets/contrib-heatmap.svg" width="740" alt="Contribution heatmap" />

<br/><br/>

<h3><code>sannidhi@cloud ~ $ whoami</code></h3>

<table>
  <tr>
    <td valign="top"><img src="./assets/avi-ascii.svg" width="370" alt="ASCII portrait" /></td>
    <td valign="top"><img src="./assets/info-card.svg" width="490" alt="Info card" /></td>
  </tr>
</table>

<br/>

# Hi, I'm Sannidhi Sriram 👋

### Cloud & DevOps Engineer · Final-Year CSE @ Lovely Professional University

I design and deploy cloud infrastructure — AWS, Azure, Terraform, Docker, Kubernetes — and build the CI/CD and GitOps pipelines that ship it. 4× Oracle Cloud Certified. Open to Cloud / DevOps / SRE roles.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/sannidhi-sriram/)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=vercel&logoColor=white)](https://sannidhisriram-06.github.io/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:sannidhisriram8@gmail.com)
[![Location](https://img.shields.io/badge/Hyderabad,_India-4285F4?style=for-the-badge&logo=googlemaps&logoColor=white)](#)

</div>

<br/>

<div align="center">

![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat&logo=amazonaws&logoColor=white)
![Azure](https://img.shields.io/badge/Azure-0078D4?style=flat&logo=microsoftazure&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-7B42BC?style=flat&logo=terraform&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-326CE5?style=flat&logo=kubernetes&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat&logo=githubactions&logoColor=white)
![Jenkins](https://img.shields.io/badge/Jenkins-D24939?style=flat&logo=jenkins&logoColor=white)
![ArgoCD](https://img.shields.io/badge/ArgoCD-EF7B4D?style=flat&logo=argo&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)


</div>

---

## 🏗️ Featured DevOps & Cloud Infrastructure Projects

**[observability-fargate](https://github.com/SannidhiSriram-06/observability-fargate)**
Prometheus + Grafana observability stack on AWS ECS Fargate — zero EC2 instances. Prometheus scrapes infrastructure metrics, Grafana visualizes them across a live dashboard with a real-time alert rule on request-rate breach. Full stack — VPC, subnets, IGW, security groups, ECR, least-privilege IAM roles, CloudWatch logging — provisioned entirely via Terraform.
`AWS ECS Fargate · Terraform · Prometheus · Grafana · Docker`

**[self-healing-microservice](https://github.com/SannidhiSriram-06/self-healing-microservice)**
Four-layer self-healing system on AWS — application health checks, container-level restart, Auto Scaling Group instance replacement, and ALB traffic isolation. Multi-AZ VPC, Application Load Balancer, and Auto Scaling Group provisioned via Terraform. GitHub Actions CI integrates Snyk to block vulnerable dependencies and images before they ship.
`AWS EC2 & ALB · Terraform · Docker · GitHub Actions · Snyk`

**[cloud-support-ticket-simulation](https://github.com/SannidhiSriram-06/cloud-support-ticket-simulation)**
Hands-on simulation of an AWS Cloud Support Engineering workflow across two IAM personas. Diagnosed and resolved a live outage via SSM Session Manager and CloudWatch Logs Insights, and executed a point-in-time AWS Backup restore — surfacing and documenting a real snapshot-consistency gap rather than trusting a "completed" status blind.
`AWS Backup · SSM · Client VPN · CloudWatch Logs Insights · IaC`

**[ai-test-generator](https://github.com/SannidhiSriram-06/ai-test-generator)** + **[ai-pytest-generator-gitops](https://github.com/SannidhiSriram-06/ai-pytest-generator-gitops)**
End-to-end CI/CD → GitOps pipeline: Jenkins enforces a 70% test-coverage gate, builds and tags Docker images, and pushes to AWS ECR. A companion GitOps repo holds the Helm chart as pure deployment state — Jenkins updates `values.yaml`, ArgoCD reconciles the change to Kubernetes automatically. The FastAPI service it deploys uses Groq's LLM API to generate pytest suites from source code.
`Jenkins · Docker · Kubernetes · Helm · ArgoCD · AWS ECR`

**[Bookstore-Microservice-Architecture-on-AWS](https://github.com/SannidhiSriram-06/Bookstore-Microservice-Architecture-on-AWS)**
Cloud architecture case study translating a Node.js Express REST API into AWS-managed services — Lambda for compute, API Gateway for routing, MongoDB Atlas for storage — eliminating server management while staying on AWS's free tier.
`AWS Lambda · API Gateway · MongoDB Atlas · CloudWatch`

---

## 🤖 AI & Full-Stack Applications

**[PitchPulse](https://github.com/SannidhiSriram-06/PitchPulse)**
Full-stack B2B sales intelligence platform — React/Vite on Vercel, Flask backend on Render, CrewAI multi-agent orchestration via Groq. Three-agent pipeline researches a company, drafts sales talking points, and formats a structured brief in under a minute. Clerk JWT auth with JWKS key rotation, Supabase Postgres, Resend for scheduled email delivery.
`Flask · React · CrewAI · Supabase · Clerk Auth`

**[upi-anomaly-explainer](https://github.com/SannidhiSriram-06/upi-anomaly-explainer)**
Multi-agent fraud detection system for UPI transactions, containerized and deployed on Hugging Face Spaces. A rule-based heuristics layer pre-filters transactions before three sequential CrewAI agents — analyst, plain-English explainer, and adversarial red-teamer — assess and cross-challenge each flag.
`Docker · CrewAI · Groq LLM · Flask · Hugging Face Spaces`

**[AI-Patient-Triage-System-on-Azure](https://github.com/SannidhiSriram-06/AI-Patient-Triage-System-on-Azure-CSA-Case-Study-)**
Flask app on Azure App Service routing patient-reported symptoms to Azure OpenAI for triage classification, with every interaction persisted to Azure Table Storage for audit and traceability.
`Azure App Service · Azure OpenAI · Azure Table Storage`

**[Infosys_AI_KYC_Compliance](https://github.com/SannidhiSriram-06/Infosys_AI_KYC_Compliance)**
Full-stack KYC document verification platform for BFSI — document classification (TFLite CNN), OCR extraction (EasyOCR), structured parsing via Groq LLM, and fraud detection with Graph Neural Networks. React frontend on S3, Node.js API and Python ML service on separate EC2 instances. Built during my Infosys Springboard internship.
`AWS EC2 & S3 · Node.js · Flask · PyTorch · GNN`

**[MEAN_STACK_Ghosting_Tracker](https://github.com/SannidhiSriram-06/MEAN_STACK_Ghosting_Tracker)**
Serverless MEAN-stack job application tracker — Angular frontend, Express API, MongoDB — that detects recruiter "ghosting" via Vercel Cron scans and scores resume fit using Groq LLM calls. Clerk-authenticated, deployed serverlessly on Vercel.
`Angular · Express.js · MongoDB Atlas · Vercel Cron · Groq LLM`

---

## 💼 Experience

**AI Intern — Cloud Deployment Lead**, Infosys Springboard (Feb – Mar 2026)
Led cloud deployment for a 25-member cohort building a BFSI-sector AI KYC system under Agile methodology. Evaluated SageMaker, Lambda, and EC2 for the ML service, selecting EC2 for cost efficiency and deployment control. Managed Git workflow and access across the cohort.

## 🏆 Certifications

- **Oracle Cloud Infrastructure (2025):** DevOps Professional · Observability Professional · Multicloud Architect Professional · Generative AI Professional
- **Microsoft Certified:** Azure Fundamentals (AZ-900) · Azure AI Fundamentals (AI-900)
- **Top 500 Globally**, Oracle Race to Certification 2025

---

<div align="center">

### 📊 GitHub Stats

<img src="https://github-readme-stats-git-master-rickstaa.vercel.app/api?username=SannidhiSriram-06&show_icons=true&theme=default&hide_border=true" alt="GitHub Stats" height="165"/>
<img src="https://streak-stats.demolab.com/?user=SannidhiSriram-06&hide_border=true" alt="GitHub Streak" height="165"/>

<br/><br/>

**[LinkedIn](https://linkedin.com/in/sannidhi-sriram/) · [Portfolio](https://sannidhisriram-06.github.io/) · [Email](mailto:sannidhisriram8@gmail.com)**

</div>
