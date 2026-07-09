## 🎯 Summary
A serverless resume (and trying to improve!) website developed in the cloud to showcase my skills around infrastructure-as-code, CI/CD automation and cloud security best practices.# 

🏗️ Architecture .* **Frontend:** Static site on **AWS S3** + **CloudFront** (CDN) + HTTPS
* **Backend:** REST API with **API Gateway** and **AWS Lambda** (Python)
* **Database:** **DynamoDB** (NoSQL) for storing the number of visitors.
**Automation:** Infrastructure provided via **Terraform** / **AWS SAM**.
* **CI/CD:** Automated pipeline with **GitHub Actions**.

## 🛠️ Key Technical Choices* **Serverless First:** Leveraged Lambda and API Gateway to remove the burden of server management and assure cost-effectiveness (pay-per-request).
**IaC Implementation:** Used [Tool Name, e.g., Terraform] to manage all infrastructure, providing consistency and repeatability of environments.
**Security:** Employed **Origin Access Identity (OAI)** to restrict access to the S3 bucket through CloudFront only, prohibiting any public direct-access.

## ⚠️ Challenges & Troubleshooting (The “Support” Insight) * **Problem:** Facing CORS (Cross-Origin Resource Sharing) issues when the front-end calls the API Gateway.   
* **Issue:** Encountered CORS (Cross-Origin Resource Sharing) errors when the frontend attempted to call the API Gateway.
  * **Solution:** Configured the API Gateway response headers to explicitly allow traffic from my CloudFront distribution origin.
* **Issue:** Deployment failed due to IAM role permission errors.
  * **Solution:** Analyzed CloudTrail logs to identify the "AccessDenied" exception and applied the principle of least privilege by scoping the Lambda role permissions.
* **Issue:** Visitor count logic showed stale data.
  * **Solution:** Implemented atomic updates in DynamoDB to ensure increment operations were thread-safe.

* ## 🚀 Deploy 1. Clone your repo: `git clone [your-repo-link]`
2. Configure your AWS Credentials.
3. Run `[your-deploy-command, e.g., terraform apply]` to supply the backend.
4. Commit changes to the `main` branch to initiate the CI/CD process..

## 📈 Future Improvements
* Integrating **AWS X-Ray** for end-to-end request tracing and latency monitoring.
* Exploring **CloudWatch Alarms** to trigger alerts on API 4XX/5XX error spikes.
