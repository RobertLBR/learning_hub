pipeline {
    agent {
        label 'maven'
    }

    stages {
        stage('拉取代码') {
            agent none
            steps {
                git(
                    url: 'https://gitee.com/robertlbr/study_hub.git',
                    credentialsId: 'gitee',
                    branch: 'master',
                    changelog: true,
                    poll: false
                )
                sh 'ls -tral'
            }
        }

        stage('构建镜像') {
            agent none
            steps {
                container('maven') {
                    sh '''pwd && ls -tral
                    docker build -t $REGISTRY/$APP_NAME:22.04 -f ./Dockerfile .
                    '''
                }
            }
        }

        stage('推送镜像') {
            agent none
            steps {
                container('maven') {
                    sh '''docker --version
                    docker images
                    docker push $REGISTRY/$APP_NAME:22.04
                    '''
                }
            }
        }

        stage('发布程序') {
            agent none
            steps {
                container('maven') {
                    withCredentials([kubeconfigFile(credentialsId: env.KUBECONFIG_CREDENTIAL_ID, variable: 'KUBECONFIG')]) {
                        sh 'envsubst < deploy-dev/deploy-ubuntu-dev.yaml | kubectl apply -f -'
                    }
                }
            }
        }
    }

    environment {
        DOCKER_CREDENTIAL_ID = 'dockerhub-id'
        KUBECONFIG_CREDENTIAL_ID = 'demo-kubeconfig'
        REGISTRY = '172.16.100.50:5000'
        DOCKERHUB_NAMESPACE = 'Docker Hub Namespace'
        APP_NAME = 'ubuntu-dev'
        BRANCH_NAME = 'dev'
        PROJECT_NAME = 'deploy-test'
    }

    parameters {
        string(name: 'TAG_NAME', defaultValue: '', description: '')
    }
}
