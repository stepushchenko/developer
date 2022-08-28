# JENKINS

### Installation MacOS M1
Install Java 8
```bash
brew tap homebrew/cask-versions     
brew install homebrew/cask-versions/adoptopenjdk8 --cask
```
Check Java version
```bash
java -version     
```

Install Jenkins
```bash
brew install jenkins-lts  
```

### Jenkins service commands
Start the Jenkins service
```bash
brew services start jenkins-lts
```

Restart the Jenkins service
```bash
brew services restart jenkins-lts
```

Update the Jenkins version
```bash
brew upgrade jenkins-lts
```

Jenkins port
```bash
localhost:8080
```