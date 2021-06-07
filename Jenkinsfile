#!/usr/bin/groovy

pipeline {
    agent any

    options {
        disableConcurrentBuilds()
    }

	environment {
		PYTHONPATH = "${WORKSPACE}/mnist-flask-app"
	}

    stages {

		//Download code from the repository
		stage("Checkout") {			 
            steps {
                git credentialsId: 'jenkins-user-ssh-key', url: 'git@bitbucket.org:mybitbucketuser/cats.git', branch: 'master' 
            }
	    } 
		
		stage("Test - Unit tests") {
			steps { runUnittests() }
		}

        //Building a Docker image with an application
        stage("Build") {
            steps { buildApp() }
		}

		stage("Push to Docker-repo") {
            steps { pushImage() }
                }

        stage("Deploy - Dev") {
            steps { deploy('dev') }
		}

		stage("Test - UAT Dev") {
            steps { runUAT(8888) }
		}

        stage("Deploy - Stage") {
            steps { deploy('stage') }
		}

		stage("Test - UAT Stage") {
            steps { runUAT(88) }
		}

        stage("Approve") {
            steps { approve() }
		}

        stage("Deploy - Live") {
            steps { deploy('live') }
		}

		stage("Test - UAT Live") {
            steps { runUAT(80) }
		}

	}
}


// steps

def pushImage(){
    withCredentials([usernamePassword(credentialsId: 'docker-login-password-authentification', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASSWORD')]) 
                {
                 sh "docker login --username ${DOCKER_USER} --password ${DOCKER_PASSWORD} https://mydocker.repo.servername"
                 sh "docker push mydocker.repo.servername/myapp:${BUILD_NUMBER}"
                }
}

def buildApp() {
	dir ('mnist-flask-app' ) {
		//def appImage = docker.build("mydocker.repo.servername/myapp:${BUILD_NUMBER}")
		def appImage = docker.build("mnist-flask-app:${BUILD_NUMBER}")
	}
}


def deploy(environment) {

	def containerName = ''
	def port = ''

	if ("${environment}" == 'dev') {
		containerName = "app_dev"
		port = "8888"
	} 
	else if ("${environment}" == 'stage') {
		containerName = "app_stage"
		port = "88"
	}
	else if ("${environment}" == 'live') {
		containerName = "app_live"
		port = "80"
	}
	else {
		println "Environment not valid"
		System.exit(0)
	}

	sh "docker ps -f name=${containerName} -q | xargs --no-run-if-empty docker stop"
	sh "docker ps -a -f name=${containerName} -q | xargs -r docker rm"
	sh "docker run -d -p ${port}:5000 --name ${containerName} mnist-flask-app:${BUILD_NUMBER}"

}


def approve() {

	timeout(time:1, unit:'DAYS') {
		input('Do you want to deploy to live?')
	}

}


def runUnittests() {
	sh "pip3 install --no-cache-dir -r ./mnist-flask-app/requirements.txt"
	sh "python3 mnist-flask-app/tests/test_flask_app.py"
}


def runUAT(port) {
	sh "mnist-flask-app/tests/runUAT.sh ${port}"
}