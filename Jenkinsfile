pipeline {
  agent any

  environment {
    APP_NAME = "data-analyst-copilot"
    IMAGE_NAME = "data-analyst-copilot:latest"
  }

  stages {
    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("Build Docker image") {
      steps {
        sh "docker build -t ${IMAGE_NAME} ."
      }
    }

    stage("Run container (smoke test)") {
      steps {
        sh '''
          docker rm -f ${APP_NAME} || true

          # Map host port dynamically to avoid conflicts (0 chooses a free port)
          docker run -d --name ${APP_NAME} -p 0:8501 ${IMAGE_NAME}

          sleep 8

          PORT=$(docker port ${APP_NAME} 8501/tcp | sed 's/.*://')
          echo "Streamlit mapped to host port: $PORT"

          curl -fsS "http://localhost:${PORT}/_stcore/health" || curl -fsS "http://localhost:${PORT}/" || true
        '''
      }
    }

    stage("Stop container") {
      steps {
        sh "docker rm -f ${APP_NAME} || true"
      }
    }
  }

  post {
    always {
      sh "docker rm -f ${APP_NAME} || true"
    }
  }
}
