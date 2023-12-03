# Mentor-Matching ML Algorithm

This repository contains an ML algorithm that matches users with suitable mentors based on their profiles. The algorithm is designed to help users find mentors who can provide guidance and support in their respective fields. The project utilizes Docker for containerization and DBeaver for seamless database integration.

## Features

- **Matching Algorithm**: The ML algorithm compares user profiles (interests, experience) with mentor profiles (name, experience, and interests) to determine the suitability of mentors for users.
- **Docker Integration**: The project is containerized using Docker, ensuring easy deployment and scalability.
- **DBeaver Database Connectivity**: The algorithm connects to a database through DBeaver, allowing seamless integration with mentor and user data.
- **Prioritized Mentor List "Soon"**: The algorithm provides an ordered list of mentors, starting from the most suitable to the least suitable, to guide users effectively.

## Getting Started

### Prerequisites

- Docker: Install Docker to containerize the project.
- DBeaver: Set up DBeaver and configure the database connection.

### Installation

1. Clone the repository:
   git clone https://github.com/rakh1234/mentor-matching.git
2. Set up the Docker container:
   docker build -t mentor-matching .
   docker run -d -p 5000:5000 mentor-matching
3. Configure the database connection in DBeaver using the provided credentials.
4. Run the algorithm:
   python mentor_matching.py
