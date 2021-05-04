#!groovy
/* import shared library */
/*@Library('jenkins-shared-library')_*/

def branchName = env.BRANCH_NAME


pipeline {
  agent any

  parameters {
    choice(
      name: 'Deploytype',
      choices: ['apply', 'destroy'],
      description: 'Deploy Type'
    )
  }

    stages {

        stage('Create IAM Role') {
            steps {
            sh'''
                terraform init
                terraform plan -out=plan
                terraform ${params.Deploytype} plan
                '''   
            }
        }

        stage('send slack message') {
            steps{
                slackSend (
                channel: "devops", 
                color: "good", 
                message: "started ${env.JOB_NAME} ${env.BUILD_NUMBER} (<${env.BUILD_URL}|Open>) was successful", 
                teamDomain: "basa-corp", 
                tokenCredentialId: "akash-slack"
                )
            }  
        }
    }
}

