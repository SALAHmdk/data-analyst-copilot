pipeline {
  agent any

  environment {
    APP_NAME = "data-analyst-copilot"
    IMAGE_NAME = "data-analyst-copilot:latest"
    STREAMLIT_PORT = "8501"
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
        sh """
          docker rm -f ${APP_NAME} || true
          docker run -d --name ${APP_NAME} -p ${STREAMLIT_PORT}:8501 ${IMAGE_NAME}
          sleep 8
          curl -fsS http://localhost:${STREAMLIT_PORT}/_stcore/health || curl -fsS http://localhost:${STREAMLIT_PORT}/ || true
        """
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
