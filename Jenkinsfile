#!groovy
/* import shared library */
/*@Library('jenkins-shared-library')_*/

def branchName = env.BRANCH_NAME


pipeline {
    agent any

    stages {

        stage ('select deploy type'){
            def userInput = input(
                    message: "select the below parameter to specify deployment type"
                    parameters: [
                        choice(
                            name: 'deploytype',
                            choices: 'provision\ndestroy'
                        )
                    ]
                )
        }
        stage('Create IAM Role') {
            deploytype = userInput['deploytype']
            steps {
            sh'''
                terraform init
                terraform plan -out=plan
                terraform deploytype plan
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

