# Devops Test 01


## Containerize an application

This repository contains a very simple flask application written in Python.
Your goal is to improve this application to be able to run in kubernetes.


## Deliverables

- New files and modifications to the application to be able to run in Minikube (Linux) or Docker desktop for Mac (macOS)
- Instructions on how to run the application
- BONUS: configure GitLab CI


## Notes

- Don't spend more than 2 hours on this assignment.
- Think about logging and monitoring. Suggest and implement improvement.
- Security is one of our priorities: What should be improved or changed? If you can, implement the changes.
- You should explain, why you made a specific technical decision.


## Instructions for running the app locally

```
> pip install -r requirements.txt
> python -m app
```

Once it's running you can test the endpoints with

```
> curl http://localhost:5000/sergei
> curl http://localhost:5000/raditya
```
