import boto3
import json

# Initialize the Bedrock Runtime client natively
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-2")

def lambda_handler(event, context):
    # 1. IMMEDIATELY handle browser CORS preflight requests
    # If the browser is just asking for permission (OPTIONS), give it immediately
    if event.get("requestContext", {}).get("http", {}).get("method", "") == "OPTIONS":
        return build_response(200, {})

    try:
        # 2. Safely capture the question payload
        body = json.loads(event.get("body", "{}"))
        user_question = body.get("question", "")

        if not user_question:
            return build_response(400, {"error": "Missing question parameter"})

        # 3. Establish your professional background context profile
        system_prompt = """
        You are an AI Assistant representing a Cloud & Network Engineering student at Western Governors University (WGU).
        Use this data to guide responses:
        - Major: BS in Cloud and Network Engineering (AWS Track). Formerly a Computer Science major.
        - Core Skills: AWS, Linux Administration, DevOps Automation, Python, Git, Infrastructure as Code (AWS SAM).
        - Projects: Completed the Cloud Resume Challenge implementing a fully automated serverless pipeline (S3, CloudFront, API Gateway, Lambda, DynamoDB, GitHub Actions).
        - Achievements: Earned the Microsoft Applied Skills credential for Building Natural Language Processing solutions with Azure AI Language.
        Keep replies professional, friendly, and very short (1-3 sentences maximum). Pivot unrelated topics back to your qualifications.
        """

        # 4. Invoke the universal default Bedrock model
        response = bedrock.converse(
            modelId="amazon.titan-text-express-v1", # Native, zero-setup required model
            messages=[{
                "role": "user",
                "content": [{"text": user_question}]
            }],
            system=[{"text": system_prompt}],
            inferenceConfig={
                "maxTokens": 150,
                "temperature": 0.3
            }
        )

        # 5. Extract and parse generated text cleanly
        ai_reply = response["output"]["message"]["content"][0]["text"]
        return build_response(200, {"reply": ai_reply})

    except Exception as e:
        return build_response(500, {"error": str(e)})

def build_response(status_code, body_content):
    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Headers": "Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token",
            "Access-Control-Allow-Methods": "POST,OPTIONS",
            "Content-Type": "application/json"
        },
        "body": json.dumps(body_content)
    }