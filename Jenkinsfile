pipeline {
//    tools {
//         maven 'Maven3'
//     }
    agent any
    // environment {
    //     registry = "account_id.dkr.ecr.us-east-2.amazonaws.com/my-docker-repo"
    // }
        environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_DEFAULT_REGION = "us-east-1"
        DOCKERHUB_CREDENTIALS= credentials('docker')
    }
   
    stages {
        stage('Cloning Git') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: '', url: 'https://github.com/anshumanhota1/polling.git']]])     
            }
        }
    //   stage ('Build') {
    //       steps {
    //         sh 'mvn clean install'           
    //         }
    //   }
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
    // Building Docker images
    stage('Building Docker image') {
      steps{
        script {
            dir('application'){
                //dockerImage = docker.build registry
                sh 'sudo docker build . -t vibhor07/polling'
            }
        }
      }
    }
   
    // Uploading Docker images into AWS ECR
    // stage('Pushing to Dockerhub') {
    //  steps{  
    //      script {
    //         dir('application'){
    //             sh 'aws ecr get-login-password --region us-east-2 | docker login --vibhor07 AWS --password-stdin account_id.dkr.ecr.us-east-2.amazonaws.com'
    //             sh 'docker push account_id.dkr.ecr.us-east-2.amazonaws.com/my-docker-repo:latest'
    //      }
    //      }
    //     }
    //  }
    stage('Push Image to Docker Hub') {         
    steps{  
     sh 'echo $DOCKERHUB_CREDENTIALS_PSW | sudo docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'                          
     sh 'sudo docker push vibhor07/polling'           
    echo 'Push Image Completed'       
    }            
}

    //    stage('K8S Deploy') {
    //     steps{   
    //         script {
    //             withKubeConfig([credentialsId: 'K8S', serverUrl: '']) {
    //             sh ('kubectl apply -f  eks-deploy-k8s.yaml')
    //             }
    //         }
    //     }
    //    }
     stage("Deploy to EKS") {
            steps {
                script {
                    dir('application') {
                        sh "pwd"
                        sh "aws eks update-kubeconfig --name myapp-eks-cluster"
                        sh "kubectl apply -f Deployment.yml"
                    }
                }
            }
        }
    }
}
