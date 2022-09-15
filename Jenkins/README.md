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


### Installing Jenkins Ubuntu

...installation Java...<br>
...installation Jenkins...<br>

Dashboard > Manage Jenkins > Configure Global Security > Git Host Key Verification Configuration.
Then in Host Key Verification Strategy select Accept first connection.

### Jobs

Start job from URL
```bash
JENKINS_URL/job/Run%20tests%20after%20push/build?token=TOKEN_NAME
```

Start job from console
```bash
curl http://[user_name]:[user_token]@JENKINS_URL/job/Run%20tests%20after%20push/build?token=TOKEN_NAME
```