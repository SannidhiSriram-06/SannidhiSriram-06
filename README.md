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

I design and deploy cloud infrastructure on AWS, Azure, and Kubernetes, and build the CI/CD and GitOps pipelines that ship it. 4× Oracle Cloud Certified. Open to Cloud / DevOps / SRE roles.

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

## 🧭 Repo Index

<div align="center">

```text
~/projects
├── cloud-infra/
│   ├── observability-fargate ············· Prometheus + Grafana on ECS Fargate
│   ├── self-healing-microservice ········· 4-layer self-healing on AWS
│   ├── cloud-support-ticket-simulation ··· AWS support workflow, SSM + Backup
│   ├── cloud-compliance-vendor-risk ······ AWS Config, Security Hub, ISO 27001
│   ├── identity-threat-detection-lab ····· Vault JIT + Wazuh SIEM + CloudTrail
│   └── Bookstore-Microservice-Architecture · Express → Lambda + API Gateway
├── ai-apps/
│   ├── ai-test-generator ················· FastAPI + Groq, pytest from source
│   ├── ai-pytest-generator-gitops ········ Helm + ArgoCD for the above
│   ├── AI-Patient-Triage-System-on-Azure ·· Azure OpenAI triage, audit logs
│   ├── perimeter ························· K8s incident correlation, on-call AI
│   ├── PitchPulse ························ B2B sales brief, CrewAI + Supabase
│   ├── upi-anomaly-explainer ············· multi-agent UPI fraud detection
│   └── Infosys_AI_KYC_Compliance ········· OCR + GNN fraud, BFSI KYC
└── site/
    └── SannidhiSriram-06.github.io ······· portfolio
```

</div>

<br/>

<div align="center">

### 📈 Languages (15 public repos)

</div>

```text
Python        █████████████████████░░░░░░░  5
HCL           ████████████░░░░░░░░░░░░░░░░  3
JavaScript    ████████░░░░░░░░░░░░░░░░░░░░  2
HTML          ████████░░░░░░░░░░░░░░░░░░░░  2
Shell         ████░░░░░░░░░░░░░░░░░░░░░░░░  1
Jupyter       ████░░░░░░░░░░░░░░░░░░░░░░░░  1
unlabelled    ████░░░░░░░░░░░░░░░░░░░░░░░░  1
```

---

## 🏗️ Cloud & DevOps Infrastructure

<details>
<summary><b>observability-fargate</b> · HCL · Prometheus + Grafana on ECS Fargate</summary>

Prometheus + Grafana observability stack on AWS ECS Fargate, zero EC2 instances. Prometheus scrapes infrastructure metrics, Grafana visualizes them on a live dashboard with a real-time alert rule on request-rate breach. VPC, subnets, IGW, security groups, ECR, least-privilege IAM, and CloudWatch logging are all provisioned via Terraform.

`AWS ECS Fargate · Terraform · Prometheus · Grafana · Docker`

🔗 [github.com/SannidhiSriram-06/observability-fargate](https://github.com/SannidhiSriram-06/observability-fargate)

</details>

<details>
<summary><b>self-healing-microservice</b> · HCL · four-layer self-healing on AWS</summary>

Four-layer self-healing system: application health checks, container restart, Auto Scaling Group instance replacement, and ALB traffic isolation. Multi-AZ VPC, ALB, and ASG provisioned via Terraform. GitHub Actions CI runs Snyk to block vulnerable dependencies and images before they ship.

`AWS EC2 & ALB · Terraform · Docker · GitHub Actions · Snyk`

🔗 [github.com/SannidhiSriram-06/self-healing-microservice](https://github.com/SannidhiSriram-06/self-healing-microservice)

</details>

<details>
<summary><b>cloud-support-ticket-simulation</b> · HCL · AWS support engineering workflow</summary>

Simulation of an AWS Cloud Support Engineering workflow across two IAM personas. Diagnosed and resolved a live outage via SSM Session Manager and CloudWatch Logs Insights, then ran a point-in-time AWS Backup restore. Documented a real snapshot-consistency gap rather than trusting a "completed" status.

`AWS Backup · SSM · Client VPN · CloudWatch Logs Insights · IaC`

🔗 [github.com/SannidhiSriram-06/cloud-support-ticket-simulation](https://github.com/SannidhiSriram-06/cloud-support-ticket-simulation)

</details>

<details>
<summary><b>cloud-compliance-vendor-risk</b> · Python · compliance monitoring and risk register</summary>

Automated AWS compliance monitoring with AWS Config and Security Hub, an ISO 27001 / NIST CSF risk register, and a vendor risk assessment workflow.

`AWS Config · Security Hub · ISO 27001 · NIST CSF`

🔗 [github.com/SannidhiSriram-06/cloud-compliance-vendor-risk](https://github.com/SannidhiSriram-06/cloud-compliance-vendor-risk)

</details>

<details>
<summary><b>identity-threat-detection-lab</b> · Shell · identity threat detection and IR</summary>

Identity threat detection and incident response lab with HashiCorp Vault JIT credentials, Wazuh SIEM, and AWS CloudTrail.

`HashiCorp Vault · Wazuh · AWS CloudTrail`

🔗 [github.com/SannidhiSriram-06/identity-threat-detection-lab](https://github.com/SannidhiSriram-06/identity-threat-detection-lab)

</details>

<details>
<summary><b>Bookstore-Microservice-Architecture-on-AWS</b> · JavaScript · serverless case study</summary>

Cloud architecture case study translating a Node.js Express REST API into AWS-managed services: Lambda for compute, API Gateway for routing, MongoDB Atlas for storage. No servers to manage, and it stays on AWS's free tier.

`AWS Lambda · API Gateway · MongoDB Atlas · CloudWatch`

🔗 [github.com/SannidhiSriram-06/Bookstore-Microservice-Architecture-on-AWS](https://github.com/SannidhiSriram-06/Bookstore-Microservice-Architecture-on-AWS)

</details>

---

## 🤖 AI & Full-Stack Applications

<details>
<summary><b>ai-test-generator</b> + <b>ai-pytest-generator-gitops</b> · CI/CD → GitOps</summary>

End-to-end CI/CD → GitOps pipeline. Jenkins enforces a 70% test-coverage gate, builds and tags Docker images, and pushes them to AWS ECR. A companion GitOps repo holds the Helm chart as deployment state: Jenkins updates `values.yaml`, and ArgoCD reconciles it to Kubernetes. The FastAPI service generates pytest suites from source code via Groq's LLM API.

`Jenkins · Docker · Kubernetes · Helm · ArgoCD · AWS ECR · Groq`

🔗 [ai-test-generator](https://github.com/SannidhiSriram-06/ai-test-generator) · [ai-pytest-generator-gitops](https://github.com/SannidhiSriram-06/ai-pytest-generator-gitops)

</details>

<details>
<summary><b>AI-Patient-Triage-System-on-Azure</b> · Python · Azure OpenAI triage</summary>

Flask app on Azure App Service that routes patient-reported symptoms to Azure OpenAI for triage classification. Every interaction is persisted to Azure Table Storage for audit and traceability.

`Azure App Service · Azure OpenAI · Azure Table Storage`

🔗 [github.com/SannidhiSriram-06/AI-Patient-Triage-System-on-Azure-CSA-Case-Study-](https://github.com/SannidhiSriram-06/AI-Patient-Triage-System-on-Azure-CSA-Case-Study-)

</details>

<details>
<summary><b>perimeter</b> · Python · incident correlation for Kubernetes</summary>

Self-hosted, auditable incident correlation and on-call intelligence for Kubernetes.

🔗 [github.com/SannidhiSriram-06/perimeter](https://github.com/SannidhiSriram-06/perimeter)

</details>

<details>
<summary><b>PitchPulse</b> · JavaScript · B2B sales intelligence</summary>

Full-stack B2B sales intelligence platform. React/Vite on Vercel, Flask backend on Render, CrewAI multi-agent orchestration via Groq. A three-agent pipeline researches a company, drafts talking points, and formats a brief in under a minute. Clerk JWT auth with JWKS key rotation, Supabase Postgres, and Resend for scheduled email.

`Flask · React · CrewAI · Supabase · Clerk Auth`

🔗 [github.com/SannidhiSriram-06/PitchPulse](https://github.com/SannidhiSriram-06/PitchPulse)

</details>

<details>
<summary><b>upi-anomaly-explainer</b> · HTML · multi-agent fraud detection</summary>

Multi-agent fraud detection for UPI transactions, containerized and deployed on Hugging Face Spaces. A rule-based layer pre-filters transactions before three sequential CrewAI agents (analyst, explainer, red-teamer) assess and cross-challenge each flag.

`Docker · CrewAI · Groq LLM · Flask · Hugging Face Spaces`

🔗 [github.com/SannidhiSriram-06/upi-anomaly-explainer](https://github.com/SannidhiSriram-06/upi-anomaly-explainer)

</details>

<details>
<summary><b>Infosys_AI_KYC_Compliance</b> · Jupyter · KYC document verification for BFSI</summary>

Full-stack KYC document verification for BFSI: document classification (TFLite CNN), OCR (EasyOCR), structured parsing via Groq LLM, and fraud detection with graph neural networks. React frontend on S3, Node.js API and Python ML service on EC2. Built during my Infosys Springboard internship.

`AWS EC2 & S3 · Node.js · Flask · PyTorch · GNN`

🔗 [github.com/SannidhiSriram-06/Infosys_AI_KYC_Compliance](https://github.com/SannidhiSriram-06/Infosys_AI_KYC_Compliance)

</details>

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
