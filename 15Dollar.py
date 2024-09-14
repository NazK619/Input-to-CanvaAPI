import requests
import json

# Canva API placeholder - Replace (input_key) with actual Canva API key when available
API_KEY = '(input_key)'

# Canva API URL placeholder - Replace (input_key) with the actual Canva API URL when available
API_URL = 'https://api.canva.com/v1/templates/{template_id}/update'  # check Canva's API docs


# Function to insert the amount into Canva template
def insert_into_template(template_id, amount):
    # Replace (input_key) with real data API KEY
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    # Data to send to Canva (Replace (input_key) with actual Canva fields)
    payload = {
        'amount': amount
    }

    # Sending the POST request to Canva API
    try:
        response = requests.post(API_URL.format(template_id=template_id), headers=headers, data=json.dumps(payload))

        if response.status_code == 200:
            print("Success: ${amount} inserted into Canva template.")
        else:
            print("Error: Unable to update template. Status code: {response.status_code}")
            print("Response:", response.text)

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)


# Main program to get user input and call the function
if __name__ == '__main__':
    try:
        template_id = '(input_key)'
        user_input = float(input("Enter the amount to insert into Canva template: "))
        insert_into_template(template_id, user_input)

    except ValueError:
        print("Invalid input. Please enter a valid number.")
