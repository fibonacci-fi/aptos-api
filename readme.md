
# Fibonacci Finance Aptos API

## Overview

The Fibonacci Finance Aptos API provides seamless integration for accessing on-chain data and functionality related to Aptos pools. This document covers deployment details and links to the API and its documentation.

### API Base URL

- **Base URL**: [https://aptos.fibonacci.fi](https://aptos.fibonacci.fi)

### API Documentation

Detailed API documentation can be found here:
- [https://aptos.fibonacci.fi/api/docs/](https://aptos.fibonacci.fi/api/docs/)

---

## Deployment Details

The API is deployed using **Google Cloud Build** with the configuration defined in `cloudbuild.yaml`.

### Deployment Steps

1. **Ensure Required Tools are Installed**
   - Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) and authenticate:
     ```bash
     gcloud auth login
     gcloud config set project <PROJECT_ID>
     ```

2. **Deployment Command**
   Run the following command to deploy:
   ```bash
   gcloud builds submit --config cloudbuild.yaml
   ```

3. **Verify Deployment**
   - Once the deployment is successful, the service will be accessible at [https://aptos.fibonacci.fi](https://aptos.fibonacci.fi).
   - Check deployment logs in the Google Cloud Console for any issues.

---

## Contributing

Contributions and issues are welcome. For bugs or feature requests, please open an issue in the repository or contact Fibonacci Finance support.

---

## Notes

- Ensure your `cloudbuild.yaml` is configured correctly for your project requirements, including environment variables and build steps.
- API uptime is dependent on Google Cloud services; monitor health metrics via the Cloud Console.
