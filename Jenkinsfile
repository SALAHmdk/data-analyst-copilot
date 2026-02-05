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
      set -e
      docker network create jenkins-net >/dev/null 2>&1 || true

      docker rm -f ${APP_NAME} >/dev/null 2>&1 || true

      # Lance l'app sur un réseau Docker dédié (pas besoin de publier un port)
      docker run -d --name ${APP_NAME} --network jenkins-net ${IMAGE_NAME}

      # Attendre un peu
      sleep 10

      # Test depuis un conteneur curl dans le même réseau (ça marche toujours)
      docker run --rm --network jenkins-net curlimages/curl:8.6.0 \
        -fsS http://${APP_NAME}:8501/_stcore/health
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
