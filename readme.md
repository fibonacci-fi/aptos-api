# Fibonacci Finance Aptos API

## Overview

The Fibonacci Finance Aptos API provides seamless integration for accessing on-chain data and functionality related to Aptos pools. This document covers deployment details and a summary of available API endpoints.

### API Base URL

- **Base URL**: [https://aptos.fibonacci.fi](https://aptos.fibonacci.fi)

### API Documentation

Detailed API documentation can be found here:
- [https://aptos.fibonacci.fi/api/docs/](https://aptos.fibonacci.fi/api/docs/)

---

## API Endpoints Summary

### Health Check
- **GET /health**: Check the API health status.

### Resources
- **GET /api/resource**: Access rate-limited resources.

### Providers
- **GET /api/providers**: Get the latest statistics of all providers.
- **GET /api/providers/{provider_name}**: Retrieve details of a specific provider by name.

### Pools
- **GET /api/pools**: Fetch data of all current pools.
- **GET /api/pool/{pool_address}/current**: Get current data for a specific pool.
- **GET /api/pool/{pool_address}/history**: Access the historical data of a specific pool.
- **GET /top**: Retrieve the top 10 pools.

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

### Security and Rate Limits

- The API implements **rate limiting** to ensure fair usage across users. Make sure your application handles `429 Too Many Requests` responses gracefully.
- Use API keys where required to authenticate requests. Contact Fibonacci Finance support for obtaining your API key.

---

## Contributing

Contributions and issues are welcome. For bugs or feature requests, please open an issue in the repository or contact Fibonacci Finance support.

---

## Notes

- Ensure your `cloudbuild.yaml` is configured correctly for your project requirements, including environment variables and build steps.
- API uptime is dependent on Google Cloud services; monitor health metrics via the Cloud Console.
- Test API endpoints using tools like [Postman](https://www.postman.com/) or `curl` for efficient integration and debugging.
