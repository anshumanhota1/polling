pipeline {

    agent any

        environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = "us-east-2"
        DOCKERHUB_CREDENTIALS= credentials('docker')
    }
   
    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/anshumanhota1/polling.git']]])     
            }
        }

    stage("Create an EKS Cluster") {
            steps {
                script {
                    dir('terraform') {
                        sh "terraform init"
                        sh "terraform apply -auto-approve"
                    }
                }
            }
        }

    stage('Building Docker image') {
      steps{
        script {
            dir('application'){
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                //dockerImage = docker.build registry
                sh 'echo admin | sudo docker build -t anshuman123abc/polling .'
            }
        }
      }
    }
   

    stage('Push Image to Docker Hub') {         
    steps{           
     sh 'sudo docker push anshuman123abc/polling'           
    echo 'Push Image Completed'       
    }            
}


     stage("Deploy to EKS") {
            steps {
                script {
                    dir('application') {
                        sh "pwd"
                        sh "aws eks update-kubeconfig --name myapp-eks-cluster"
                        sh "kubectl delete -f Deployment.yml"
                        sh "kubectl apply -f Deployment.yml"
                        sh 'cat Deployment.yml'
                        sh "kubectl get svc"
                    }
                }
            }
        }
    }
}
