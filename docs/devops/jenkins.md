# Jenkins

## Pipelines

### Declarative vs. Scripting Pipeline Syntax[^pipeline]

#### Declarative Pipeline Skeleton

```groovy
pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                //
            }
        }
        stage('Test') {
            steps {
                //
            }
        }
        stage('Deploy') {
            steps {
                //
            }
        }
    }
}
```

#### Scripting Pipeline Skeleton

```groovy
node {
    stage('Build') {
        //
    }
    stage('Test') {
        //
    }
    stage('Deploy') {
        //
    }
}
```

[^pipeline]: [Declarative versus Scripted Pipeline syntax | Jenkins Docs](https://jenkins.io/doc/book/pipeline/#declarative-versus-scripted-pipeline-syntax)
