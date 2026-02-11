# Secrets Management Guide

## Purpose
This project uses environment variables to securely manage sensitive data.

---

## Required Environment Variables

| Variable | Description |
|----------|------------|
| OPENAI_API_KEY | API key for OpenAI access |
| REDIS_HOST | Redis server hostname |
| REDIS_PORT | Redis port |
| APP_NAME | Application display name |

---

## Security Rules

1. Never commit `.env` files to GitHub
2. Use `.env.example` instead
3. Use Docker secrets or environment variables in production
4. Rotate API keys regularly
5. Restrict API key permissions

---

## Local Development

Create `.env` file manually.

---

## Production Deployment

Secrets should be injected through:

- Docker Compose environment variables
- Cloud secret managers
- CI/CD pipeline secret storage
