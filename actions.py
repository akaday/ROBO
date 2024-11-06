import requests

def custom_action(data):
    # Define the logic for your custom action
    result = data["input"] * 2
    return {"result": result}

# Example of invoking the custom action
data = {"input": 5}
response = custom_action(data)
print(response)  # Output: {'result': 10}
