stage("Run container (smoke test)") {
  steps {
    sh """
      docker rm -f ${APP_NAME} || true
      docker run -d --name ${APP_NAME} -p 0:8501 ${IMAGE_NAME}
      sleep 8

      PORT=\$(docker port ${APP_NAME} 8501/tcp | sed 's/.*://')
      echo "Streamlit is available on host port: \$PORT"

      curl -fsS http://localhost:\$PORT/_stcore/health || curl -fsS http://localhost:\$PORT/ || true
    """
  }
}
