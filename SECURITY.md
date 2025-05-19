# Security Policy

## Supported Versions

We currently support the following versions of the project:

| Version | Supported          |
| ------- | ------------------ |
| 1.0.x   | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability within this project, please send an email to [your-email@example.com](mailto:your-email@example.com). All security vulnerabilities will be promptly addressed.

## Security Practices

- **Environment Variables**: Sensitive information such as API keys and account IDs should be stored in the `.env` file, which is not committed to the repository.
- **Mock Data**: Use mock data in development environments (`USE_MOCK=true`) and real data in production (`USE_MOCK=false`).
- **Environment**: Ensure the `ENVIRONMENT` variable is set to `production` in production environments.
- **Firewall and HTTPS**: Protect the server with a firewall and use HTTPS in production.
- **GitHub Dependabot**: The project relies on GitHub Dependabot for security updates and vulnerability checks.
- **Safety Tool**: The Safety tool will be used for security checks once it is updated to be compatible with the latest pydantic version.

## Security Workflow

The project uses a GitHub Actions workflow for security checks:

- **TruffleHog OSS**: Scans for secrets and sensitive information.
- **Bandit**: Performs static analysis to find common security issues in Python code.
- **Safety**: Checks for known vulnerabilities in dependencies.
- **Snyk**: Scans for vulnerabilities in Python dependencies.

This workflow runs on every push to the `main` and `develop` branches, as well as on pull requests to these branches. It also runs weekly on Sundays.

## Responsible Disclosure

We appreciate responsible disclosure and will credit reporters if desired.

## Found a bug or have an idea? 🐛💡

If you find a bug, have a feature request, or notice something odd, **please open an issue on GitHub!**

👉 [Open an issue](https://github.com/yourusername/ibkr-portfolio-backend/issues/new/choose)

We welcome all feedback and contributions! 🙏

## Further Information

For general questions, open an issue or contact the maintainers.

## Additional Resources

- [GitHub Security](https://github.com/yourusername/ibkr-portfolio-backend/security)
- [GitHub Dependabot](https://github.com/yourusername/ibkr-portfolio-backend/security/dependabot) 