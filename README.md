# Content_Generation_with_Claude2_Using_AWS_Bedrock

This project demonstrates how to use the Claude model via the AWS Bedrock service to generate content/ The project involves setting up AWS CLI, configuring the necessary environment, and running a Python script to invoke the model.

## Prerequisites

Before running this script, ensure you have the following:

- Python 3.11 or higher
- AWS SDK for Python (`boto3`)
- AWS credentials configured with necessary permissions to use Bedrock service

## Installation

1. **Install boto3**:

    ```bash
    pip install boto3
    ```

2. **Configure AWS credentials**:

    Ensure your AWS credentials are configured. You can do this by setting up the `~/.aws/credentials` file or by using environment variables.

## Usage

1. **Script Overview**:

    This script sends a prompt to the Claude API and receives a poetic response. The prompt asks Claude to act as Shakespeare and write a poem about machine learning.

2. **Script Execution**:

    ```python
    import boto3
    import json

    ### Call Claude API

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
    ```

3. **Parameters**:

    - `prompt_data`: The input prompt for the Claude API.
    - `max_tokens_to_sample`: Maximum number of tokens to generate in the response.
    - `temperature`: Controls the randomness of the response (0.0 to 1.0).
    - `top_p`: Controls the diversity of the response (0.0 to 1.0).
    - `model_id`: The ID of the model to be used (`anthropic.claude-v2` by default).

4. **Running the Script**:

    To run the script, execute the following command:

    ```bash
    python app.py
    ```

    Replace `app.py` with the name of your Python file containing the above code.

## Notes

- The script uses the `anthropic.claude-v2` model by default. You can switch to a different model by uncommenting and updating the `model_id`.
- The `accept` and `contentType` parameters can be commented out if not required.

## Example Output

After running the script, you should see a Shakespearean poem about machine learning printed to the console.

## Troubleshooting

- Ensure that your AWS credentials are correctly configured.
- Verify that you have the necessary permissions to access the Bedrock service.
- Check for any network connectivity issues that may prevent reaching the AWS services.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss your ideas.
