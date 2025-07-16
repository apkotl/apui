# APUI Project (API - UI web kit project)

Welcome to the [APUI project](https://github.com/apkotl/apui)! This guide will help you get started quickly.

---

## 🚀 Quick Start

To set up and run the APUI project locally, follow these steps:

### 1. Environment Variables Setup

Before running the project, you need to configure the environment variables.

* **Copy the environment variable template file:**
    ```bash
    cp .env.template .env
    ```
* **Edit the `.env` file:** Open the newly created `.env` file in your preferred text editor and make any necessary adjustments according to your environment (e.g., database parameters, API keys, etc.).

### 2. Running the Project

Once your environment variables are configured, you can run the project using the provided scripts.

#### For Linux Users:

Execute the `run-docker-compose.sh` script with the desired command.
```Bash
./run-docker-compose.sh [command]
```

#### For Windows Users:

Execute the `run-docker-compose.ps1` script with the desired command.
```Bash
./run-docker-compose.ps1 [command]
```

Available Commands:
- `up-dev` - Builds and starts containers in development mode.
- `up-prod` - Builds and starts containers in production mode.
- `stop` - Stops running containers without removing them.
- `start` - Starts stopped containers.
- `down` - Stops and removes containers(, networks, and images *).
- `down-volumes` - Stops and removes containers(, networks, images,*) and volumes.

---

## 🚀 🛠️ Additional Information (Optional)

- Requirements: .
- Project Structure: .
- Development: .
- Contributing: .
- Contact: .

---

Happy coding with **APUI**!