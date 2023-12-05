# Mentor-Matching ML Algorithm

This repository contains an ML algorithm that matches users with suitable mentors based on their profiles. The algorithm is designed to help users find mentors who can provide guidance and support in their respective fields. The project utilizes Docker for containerization and DBeaver for seamless database integration.

## Features

- **Matching Algorithm**: The ML algorithm compares user profiles (interests, experience) with mentor profiles (name, experience, and interests) to determine the suitability of mentors for users.
- **Docker Integration**: The project is containerized using Docker, ensuring easy deployment and scalability.
- **DBeaver Database Connectivity**: The algorithm connects to a database through DBeaver, allowing seamless integration with mentor and user data.
- **Prioritized Mentor List**: An ordered list of mentors, starting from the most suitable to the least suitable.

## Getting Started

### Prerequisites

- Docker: Install Docker to containerize the project.
- DBeaver: Set up DBeaver and configure the database connection.

### Installation

1. Clone the repository:
   git clone https://github.com/rakh1234/mentor-matching.git
2. Pull the Docker image from Docker Hub:
   docker pull razankh/mentor-matching-ml-algorithm
3. Set up the Docker container:
   docker run -d -p 5000:5000 razankh/mentor-matching-ml-algorithm
5. Configure the database connection in DBeaver using the provided credentials.
6. Run the algorithm.
