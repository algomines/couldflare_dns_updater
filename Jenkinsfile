#!/usr/bin/env groovy
@Library('jenkins_shared_library') _
pipeline {
    agent { kubernetes { yamlFile 'pod.yaml' } }
    environment {
        GITHUB_REPO = 'algomines'
        GITHUB_BRANCH = 'dev'
        GITHUB_CREDENTIALS_ID = 'GitHub_AlgoMine'
        SERVICE_NAME = 'couldflare_dns_updater'
        DEPLOYMENT_NAME = 'couldflare-dns-updater'
        CONTAINER_NAME = 'couldflare-dns-updater'
        CLUSTER_NAMESPACE = 'dns-updater'
        GIT_NODE = 'gitnode'
        DOCKER_NODE = 'dockernode'
        KUBECTL_NODE = 'kubectl'
        COMMIT_PROPERTIES = 'commit.properties'
        JOB_TYPE = 'deployment'
    }
    options {
        buildDiscarder(logRotator(numToKeepStr: '3', daysToKeepStr: '5'))
        skipDefaultCheckout(true)
        timestamps()
    }
    stages {
        stage('Checkout SCM') {
            steps {
                CheckoutSCM("$GITHUB_REPO","$GITHUB_BRANCH","$GITHUB_CREDENTIALS_ID","$SERVICE_NAME")
                GetCommitID("$GIT_NODE","$COMMIT_PROPERTIES")
            }
        }
        stage('Build Application') {
            steps {
                BuildApplication("$DOCKER_NODE","$SERVICE_NAME","$COMMIT_PROPERTIES")
            }
        }
        // stage('Apply Kubernetes files') {
        //     steps {
        //         withKubeConfig([namespace: "jenkins"]) {
        //             sh 'kubectl get pods'
        //             }
        //         // sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'
        //         // sh 'chmod u+x ./kubectl'
        //         // sh './kubectl get pods'
        //         // withKubeConfig([credentialsId: 'user1', serverUrl: 'https://api.k8s.my-company.com']) {
        //         // withKubeConfig() {
        //         //     sh 'curl -LO "https://storage.googleapis.com/kubernetes-release/release/v1.20.5/bin/linux/amd64/kubectl"'
        //         //     sh 'chmod u+x ./kubectl'
        //         //     sh './kubectl get pods'
        //         // }
        //     }
        // }
        stage('Deploying') {
            steps {
                //kubectl set image deployment/my-deployment mycontainer=myimage
                DeplyToCluster("$KUBECTL_NODE","$CLUSTER_NAMESPACE","$JOB_TYPE","$SERVICE_NAME","$DEPLOYMENT_NAME","$CONTAINER_NAME","$COMMIT_PROPERTIES")
                // Kubectl("$KUBECTL_NODE","get pods")
            }
        }
        // stage('Kubectl') {
        //     steps {
        //         Kubectl("$KUBECTL_NODE","get pods --all-namespaces")
        //         // Kubectl("$KUBECTL_NODE","get pods")
        //     }
        // }


        // stage('Clean Up') {
        //     steps {
        //         CleanUp("$AWSCLI_NODE","$DOCKER_NODE")
                
        //     }
        // }
        
        // stage('Checking ECR Repository') {
        //     steps {
        //         SetECR_Token("$AWSCLI_NODE","$DOCKER_NODE","$REGION","$ACCOUNT_ID")
        //         CheckECRRepo("$AWSCLI_NODE","$DOCKER_NODE","$REGION","$ECR_REPO","$SERVICE_NAME")
        //     }
        // }
        // stage('Preparing for Build') {
        //     steps {
        //         GetCommitID("$GIT_NODE","$COMMIT_PROPERTIES")
        //         DeleteImageFromECR("$AWSCLI_NODE","$DOCKER_NODE","$ACCOUNT_ID","$REGION","$ECR_REPO","$SERVICE_NAME","2")
        //     }
        // }
        
        // stage('Pushing Image to Registry') {
        //     steps {
        //         DeplyToECR("$DOCKER_NODE","$ACCOUNT_ID","$REGION","$ECR_REPO","$SERVICE_NAME","$COMMIT_PROPERTIES")
        //     }
        // }
    }
}



// ${BUILD_NUMBER}-$COMMIT_ID
        // // sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' .'
        // // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
        // // sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
        // sh 'docker image ls'
        // sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ') .'
        // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ') ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ')'
        // sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ')'
        // sh 'docker image ls'

// sh 'docker build --no-cache -t ' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ') .'
        // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ') ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ')'
        // ${BUILD_NUMBER}-$COMMIT_ID
        // // sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' .'
        // // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
        // // sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
        // sh 'docker image ls'
        // sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ') .'
        // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ') ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':${BUILD_NUMBER}-$(cat ' + COMMIT_PROPERTIES + ')'
        // sh 'docker image ls'

//         sh '''#!/bin/bash -eux
//         export COMMIT_ID=$(git rev-parse HEAD | cut -c 1-8)
//         echo "$COMMIT_ID" > commit.properties
//         # git tag jenkins-$BUILD_NUMBER
//         # git push --tags
//         '''

// set +e
//         imageDigest=$(aws ecr list-images --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + ''' --query "imageIds[0].imageDigest")
//         #export REPO_EXISTS=$(echo $?)
//         set -e
//         if [[ $imageDigest != null ]]; then
//             aws ecr batch-delete-image --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + ''' --image-ids imageDigest=${imageDigest}
//             fi
//         '''

//         stage('Build Application') {
//             steps {
//                 container("${DOCKER_NODE}") {
//                     sh 'if [ $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ' | wc -l) -eq 2 ]; then docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ECR_REPO + '/' + SERVICE_NAME + ':last; fi'
//                     sh 'docker images ' + ECR_REPO + '/' + SERVICE_NAME + ''


//                     // docker rmi $(docker images 'completeimagename' -a -q)

//                     sh 'docker images ' + ECR_REPO + '/' + SERVICE_NAME + ' | wc -l'        
//                     sh 'docker images ' + ECR_REPO + '/' + SERVICE_NAME + ''    
                            
//                     sh 'docker images ' + ECR_REPO + '/' + SERVICE_NAME + ' | wc -l'        
//                     sh 'docker images ' + ECR_REPO + '/' + SERVICE_NAME + ''        
//                     sh 'docker image ls'
//                     sh 'docker image rm ' + ECR_REPO + '/' + SERVICE_NAME + ''
//                     sh 'docker image ls'
//                     sh 'cat ecr.token | docker login --username AWS --password-stdin ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com'
//                     sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' . > build.info'
//                     sh 'docker image ls'
//                     // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                 }
//                 container("${AWSCLI_NODE}") {
//                     sh 'cat build.info'
//                     sh 'ls -la'
//                 }
//             }
//         }


// container("${DOCKER_NODE}") {
//                     // sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' .'
//                     // sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     // sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     sh 'docker image ls'
//                     sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ':last2 .'
//                     sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':last2 ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last2'
//                     sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last2'
//                     sh 'docker image ls'
//                 }

//                 test("${GIT_NODE}")
//                 container("${AWSCLI_NODE}") {
//                     sh '''#!/bin/bash -ex
//                     echo "Checking Repository, ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''"
//                     set +e
//                     aws ecr describe-repositories --region ''' + REGION + ''' --repository-names ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                     export REPO_EXISTS=$(echo $?)
//                     # REPO_EXISTS=$(echo $?)
//                     set -e

//                     if [[ "$REPO_EXISTS" -ne 0 ]];
//                         then
//                         echo "Repo doesn't exist, creating a new repository"
//                         aws ecr create-repository --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                         fi
//                     echo $(aws ecr get-login-password --region ''' + REGION + ''') > ecr.token
//                     '''
//                     // set +e
//                     // imageDigest=$(aws ecr list-images --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + ''' --query "imageIds[0].imageDigest")
//                     // #export REPO_EXISTS=$(echo $?)
//                     // set -e
//                     // if [[ $imageDigest != null ]]; then
//                     //     aws ecr batch-delete-image --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + ''' --image-ids imageDigest=${imageDigest}
//                     //     fi
//                     // '''
//                 }
//                 container("${DOCKER_NODE}") {
//                     sh 'cat ecr.token | docker login --username AWS --password-stdin ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com'
//                 }
//     stage('Cloning Repository') {

//         }
//         stage('Cloning Project') {
//             steps {
//                 container("${DOCKER_NODE}") {
//                     sh 'cat ecr.token | docker login --username AWS --password-stdin ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com'
//                     sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' .'
//                     sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                 }

//                 container("${AWS_NODE}") {
//                    sh '''#!/bin/bash -ex
//                     set +e
//                     aws ecr describe-repositories --region ''' + REGION + ''' --repository-names ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                     export REPO_EXISTS=$(echo $?)
//                     set -e

//                     if [[ "$REPO_EXISTS" -ne 0 ]];
//                         then
//                         echo "Repo doesn't exist, creating a new repository"
//                         aws ecr create-repository --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                         fi
//                     echo $(aws ecr get-login-password --region ''' + REGION + ''') > ecr.token
//                    ''' 

//                 aws ecr list-images \
//     --repository-name cluster-autoscaler

//                 }
//                 container("${DOCKER_NODE}") {
//                     sh 'cat ecr.token | docker login --username AWS --password-stdin ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com'
//                     sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' .'
//                     sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
                
//                     COMMIT_ID = readFile('commit.properties').trim()
//                     docker.withRegistry("https://161101194600.dkr.ecr.us-west-2.amazonaws.com", "ecr:"+ REGION + ":service_user") {
//                         docker.build("converse3/${serviceName}", "--no-cache .")
//                         docker.image("converse3/${serviceName}").push("${BUILD_NUMBER}-$COMMIT_ID")
//                     }
//                     app = docker.build("fasautomation/recon", ".")
//                     sh 'cat /etc/os-release'
//                    sh '''#!/bin/bash -ex
//                     set +e
//                     aws ecr describe-repositories --region ''' + REGION + ''' --repository-names ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                     export REPO_EXISTS=$(echo $?)
//                     set -e

//                     if [[ "$REPO_EXISTS" -ne 0 ]];
//                         then
//                         echo "Repo doesn't exist, creating a new repository"
//                         aws ecr create-repository --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                         fi
//                     echo $(aws ecr get-login-password --region ''' + REGION + ''') > ecr.token
//                    ''' 
//                 }
//                 container("jenkinsslave") {
//                    sh '''#!/bin/bash -ex
//                     set +e
//                     cat /etc/os-release
//                     docker --version
//                     aws s3 ls
//                     yum install git -y
//                     set -e
//                    ''' 
//                 }
                
//                 git 'https://github.com/nginxinc/docker-nginx.git'

//                 container("${AGENT_NODE}") {
//                     sh 'systemctl start docker'
//                     sh 'docker version && cd stable/alpine/ && docker build -t nginx-example .'
//                     sh 'ls -la'
//                     // sh 'dockerd'
//                     // sh 'service docker start'
//                     sh 'cat ecr.token | docker login --username AWS --password-stdin ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com'
//                     sh 'docker build -t ' + ECR_REPO + '/' + SERVICE_NAME + ' .'
//                     sh 'docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     sh 'docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     // sh '''#!/bin/bash -ex
//                     // ls -la
//                     // cat ecr.token 
//                     // '''
//                 }
//                 container("${AWS_NODE}") {
//                     sh 'cat /etc/os-release'
//                     sh '''#!/bin/bash -ex
//                         set +e
//                         aws ecr describe-repositories --region ''' + REGION + ''' --repository-names ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                         export REPO_EXISTS=$(echo $?)
//                         set -e

//                         if [[ "$REPO_EXISTS" -ne 0 ]];
//                             then
//                             echo "Repo doesn't exist, creating a new repository"
//                             aws ecr create-repository --region ''' + REGION + ''' --repository-name ''' + ECR_REPO + '''/''' + SERVICE_NAME + '''
//                             fi

//                         aws ecr get-login-password --region ''' + REGION + ''' | docker login --username AWS --password-stdin ''' + ACCOUNT_ID + '''.dkr.ecr.''' + REGION + '''.amazonaws.com
//                     '''
//                     // sh 'aws ecr get-login-password --region ap-south-1 | docker login --username AWS --password-stdin 153617516468.dkr.ecr.ap-south-1.amazonaws.com'
//                 }
//                 container("${AGENT_NODE}") {
//                     sh 'cat /etc/os-release'
//                     sh '''#!/bin/bash -ex
//                     set +e
//                     curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
//                     sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian buster stable"
//                     sudo apt-get update
//                     sudo apt-get install docker-ce docker-ce-cli containerd.io
//                     sudo systemctl status docker
//                     add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian buster stable"
//                     apt-get update
//                     apt-get install docker-ce docker-ce-cli containerd.io
//                     systemctl status docker
//                     docker --version
//                     aws s3 ls
//                     set -e

//                     #docker build -t ''' + ECR_REPO + '''/''' + SERVICE_NAME + ''' .
//                     #docker tag ''' + ECR_REPO + '''/''' + SERVICE_NAME + ''':latest ''' + ACCOUNT_ID + '''.dkr.ecr.''' + REGION + '''.amazonaws.com/''' + ECR_REPO + '''/''' + SERVICE_NAME + ''':latest
//                     '''
//                 }
//                 container("amazonlinux") {
//                     sh '''#!/bin/bash -ex
//                     set +e
//                     #yum install -y yum-utils
//                     #yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
//                    # yum-config-manager --enable docker-ce-nightly
//                     #yum-config-manager --enable docker-ce-test
//                    # yum-config-manager --disable docker-ce-nightly
//                    # yum install docker-ce docker-ce-cli containerd.io
//                     #yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io
//                     docker --version

//                     aws s3 ls
                    
//                     sudo yum install docker -y 
//                     sudo systemctl start docker
//                     yum install docker -y 
//                     systemctl start docker
//                     set -e
//                     ''' 
//                 }
                
//                 CloningProject()
//             }

//                 container("${DOCKER_NODE}") {
//                     sh 'if [ $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ':last | wc -l) -gt 1 ]; then docker rmi -f $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ':last -a -q);  fi' 
//                     // sh 'if [ $(docker images ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last | wc -l) -gt 1 ]; then docker tag ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last; docker rmi ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest; docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last; fi' 
//                     sh 'if [ $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ':latest | wc -l) -gt 1 ]; then docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ECR_REPO + '/' + SERVICE_NAME + ':last; docker rmi ' + ECR_REPO + '/' + SERVICE_NAME + ':latest;  fi' 
//                     sh 'if [ $(docker images ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest | wc -l) -gt 1 ]; then docker tag ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + '; docker rmi ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest; docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + '; fi' 
//                 }


//                 docker tag 518a41981a6a myRegistry.com/myImage
//                 docker push myRegistry.com/myImage




//                 container("${DOCKER_NODE}") {
//                     sh 'cat ecr.token | docker login --username AWS --password-stdin ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com'
//                     sh 'docker image ls'
//                     sh 'docker images ' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     sh 'docker images ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest'
//                     sh 'if [ $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ':latest | wc -l) -gt 1 ]; then docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ECR_REPO + '/' + SERVICE_NAME + ':last; docker rmi ' + ECR_REPO + '/' + SERVICE_NAME + ':latest;  fi' 
//                     sh 'if [ $(docker images ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest | wc -l) -gt 1 ]; then docker tag ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last; docker rmi ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':latest; docker push ' + ACCOUNT_ID + '.dkr.ecr.' + REGION + '.amazonaws.com/' + ECR_REPO + '/' + SERVICE_NAME + ':last; fi' 
//                     sh 'docker rmi -f $(docker images "' + ECR_REPO + '/' + SERVICE_NAME + '" -a -q)'
//                     sh 'docker image ls'
//                     }
                
//                 container("${DOCKER_NODE}") {
//                     docker build -t whenry/fedora-jboss:latest -t whenry/fedora-jboss:v2.1 
//                     sh 'docker image ls'
//                     sh 'if [ $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ' | wc -l) -ne 0 ]; then docker tag ' + ECR_REPO + '/' + SERVICE_NAME + ':latest ' + ECR_REPO + '/' + SERVICE_NAME + ':last; docker rmi -f $(docker images ' + ECR_REPO + '/' + SERVICE_NAME + ':latest -a -q); fi'
//                     sh 'docker image ls'
//                 }