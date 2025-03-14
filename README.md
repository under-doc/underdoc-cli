# UnderDoc CLI

UnderDoc CLI

## What is UnderDoc?

UnderDoc is a simple, easy to use and cost effective document understanding platform.

With the latest GenAI technologies, many LLMs can now accept multi-modal inputs (e.g. images) and produce structured output base user instructions and the content/layout appeared on images.

Our mission is to leverage these exciting technologies to re-imagine how document understanding can be done.

## What services we provide?

* Our first service is an API SaaS that can use to extract structured data from any expense images (e.g. invoice, receipt, demand notes, etc.)
* We also provide professional services for customers who want to extract structured data from their documents and images
* Our focus is in Asia market and we test our platform with a combination of English and Asian (e.g. Chinese, Japanese, etc.) languages

## Getting Started

To get start, simply visit our UnderDoc Developer Portal (https://dev-portal.underdoc.io), signup for an account (free and no credit card required).

In our Developer Portal, there is a Playground that you can try out your own images and view the extracted output.

For our Expense Document Understanding API, you can see the API Spec at https://api.underdoc.io/docs

## Using our CLI

* Sign up at our developer portal and get a key.
* Install the UnderDoc CLI tool

```bash
brew tap under-doc/homebrew-underdoc
brew install underdoc
```

* Configure the API Key:

```bash
underdoc configure
```

* Extract expense data from an image file (invoice/receipt/demand-note)

```bash
underdoc extract-expense-data <image_file_name>

# Example
underdoc extract-expense-data receipt-image/my-receipt.png
```

## Contact us

Feel free to contact us at support@underdoc.io for any questions.
