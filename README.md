

---

# Messaging System Task - README

## Overview

This project is designed to create a basic messaging system that allows users to send and receive messages. The system supports user registration, authentication, and message management functionalities. This README provides an overview of the system, setup instructions, and details on how to use the system.

## Features

- **User Registration**: Users can create an account by providing a unique username and a password.
- **User Authentication**: Registered users can log in using their username and password.
- **Send Messages**: Authenticated users can send messages to other users.
- **Receive Messages**: Users can view messages sent to them by other users.
- **Message Management**: Users can delete messages they have received.

## Prerequisites

- Docker
- Docker Compose

## Project Structure

```
.
├── backend
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app.py
├── nginx
│   └── nginx.conf
└── docker-compose.yml
```

## Setup Instructions

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/messaging-system.git
    cd messaging-system
    ```

2. **Build and Start the Services**:
    ```bash
    docker-compose up --build
    ```

3. **Access the Application**:
    Open your web browser and go to `http://localhost`.

## Usage

### Registration

1. Go to the registration page.
2. Enter a unique username and a password.
3. Click on the "Register" button.

### Login

1. Go to the login page.
2. Enter your username and password.
3. Click on the "Login" button.

### Sending Messages

1. After logging in, go to the "Send Message" page.
2. Enter the recipient's username and your message.
3. Click on the "Send" button.

### Receiving Messages

1. Go to the "Inbox" page.
2. View messages sent to you by other users.

### Deleting Messages

1. In the inbox, click on the "Delete" button next to the message you want to delete.

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


