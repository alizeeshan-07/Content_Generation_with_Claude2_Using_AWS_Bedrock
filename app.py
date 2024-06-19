import boto3
import json


### Call claude API

prompt_data = """
Act as Shakespeare and write a poem on machine learning
"""

bedrock = boto3.client(service_name="bedrock-runtime")

payload= {

    "prompt":"Human:"+prompt_data+"Assistant:",
    "max_tokens_to_sample": 512,
    "temperature": 0.8,
    "top_p": 0.8
}

body = json.dumps(payload)
model_id = "anthropic.claude-v2"
# model_id = "ai21.j2-mid-v1"
response = bedrock.invoke_model(
    body=body,
    modelId=model_id,
    accept='application/json', # can be commented
    contentType='application/json' # can be commented
)

response_body = json.loads(response.get("body").read())

response_text = response_body["completion"]
print(response_text)
