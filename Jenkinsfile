#!groovy
/* import shared library */
/*@Library('jenkins-shared-library')_*/

def branchName = env.BRANCH_NAME

def userInput = input(

    message: "select the below parameter to specify deployment type"
    parameters: [
        choice(
            name: 'deploytype',
            choices: 'provision\ndestroy'
        )
    ]
)
pipeline {
    agent any

    stages {
        stage('Create IAM Role') {
            deploytype = userInput['deploytype']
            steps {
            sh'''
                terraform init
                terraform plan -out=plan
                terraform apply plan
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
