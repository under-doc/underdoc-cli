import click
import httpx
import json
import os
from enum import Enum
import base64
from typing import Dict

API_BASE_URL = "https://api.underdoc.io"
CONFIG_FILE = os.path.expanduser("~/.underdoc_config.json")

class UnderDocException(Exception):
    """Base exception for UnderDoc."""
    pass

class UnderDocUnsupportedFileFormatException(UnderDocException):
    """Exception raised when an unsupported file format is provided."""
    pass

class ImageFormat(str, Enum):
    jpeg = "jpeg"
    png = "png"

def load_config():
    try:
        with open(CONFIG_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_config(config):
    with open(CONFIG_FILE, 'w') as f:
        json.dump(config, f, indent=4)

def _get_request_from_file_name(file_name: str) -> Dict[str, str]:
    """Get a request from a file name.
    """

    # Read the image file
    with open(file_name, "rb") as image_file:
        # Get the image type
        file_extension = file_name.split(".")[-1]
        if file_extension in ['jpg', 'jpeg']:
            image_format = ImageFormat.jpeg
        elif file_extension == 'png':
            image_format = ImageFormat.png
        else:
            raise UnderDocUnsupportedFileFormatException(f"Unsupported file format: {file_extension}")

        image_data = image_file.read()

    # Encode the image data
    try:
        image_data_encoded = base64.b64encode(image_data).decode("utf-8")
    except Exception as e:
        raise UnderDocException(f"Error base64 encoding image data: {e}")

    # Return the request
    return {
        "image_format": image_format.value,
        "image_data": image_data_encoded
    }

@click.group()
def cli():
    """CLI for interacting with UnderDoc API SaaS."""
    pass

@cli.command()
@click.option('--api-key', prompt='Your UnderDoc API Key (get it free from dev-portal.underdoc.io)', hide_input=True)
def configure(api_key):
    """Configure API key."""
    config = load_config()
    config['api_key'] = api_key
    save_config(config)
    click.echo("UnderDoc API key configured successfully.")

@cli.command()
@click.argument('image_file')
def extract_expense_data(image_file):
    """Extract expense data from an image."""
    config = load_config()
    api_key = config.get('api_key')
    if not api_key:
        click.echo("Please configure your API key first using 'my-cli configure'.")
        return

    headers = {'UNDERDOC_API_KEY': api_key}
    url = f"{API_BASE_URL}/expenses/extract"

    try:
        request = _get_request_from_file_name(image_file)
    except UnderDocException as e:
        click.echo(f"Error preparing request: {e}")
        return
    
    click.echo(f"Extracting expense data from image: {image_file}")
    response = httpx.post(
        url,
        headers=headers,
        json=request,
        timeout=60.0
    )
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    click.echo(json.dumps(response.json(), indent=4, ensure_ascii=False))

if __name__ == '__main__':
    cli()
