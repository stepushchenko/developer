# ALLURE

### Installation and usage with Behave framework

Run all features and collect results in the reports folder
```bash
behave -f allure_behave.formatter:AllureFormatter -o {path/to/the/reports/holder} features
```

Run specific feature file and collect results in the reports folder
```bash
behave -f allure_behave.formatter:AllureFormatter -o {path/to/the/reports/holder} features/sample.feature
```

Start Allure web-server and get a report
```bash
allure serve {path/to/the/reports/holder} --port {port_number}
```