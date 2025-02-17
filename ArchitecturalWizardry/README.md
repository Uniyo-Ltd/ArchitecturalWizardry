## Code for Configuration Engine

### How to Run the Project

1. Install dependencies:
2. Run the Flask application:



## Design Decisions

- **Modular Architecture**: Code separation ensures maintainability and ease of testing.
- **SQLAlchemy ORM**: Provides abstraction for database operations.
- **Flask**: Simple yet powerful for building REST APIs.
- **Mock Services**: Simulates external API interactions for testing.

## Deployment

- **Platform**: Consider Heroku or AWS Elastic Beanstalk for Flask deployment.
- **Environment Variables**: Use for sensitive configurations.
- **CI/CD**: GitHub Actions or similar for automated testing and deployment.
