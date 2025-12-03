# A serverless MLOps project that predicts and auto-dispatches incident tickets using AWS SageMaker, Lambda, and DynamoDB.
This sample machine learning project demonstrates how we automate ticket dispatching using a serverless, production-ready MLOps workflow on AWS. It showcases how an end-to-end system can classify incoming incident tickets, predict the correct support team, and automatically dispatch them to Microsoft Teams and assign agent to the ticket on the company ITSM (iTop).

The solution uses Amazon SageMaker, AWS Lambda, S3, DynamoDB, and EFS, along with event-driven orchestration. It also illustrates how data preprocessing, model training, inference, and ticket routing can be integrated into a scalable pipeline suitable for real-world IT operations.

# Architecture
<p align="center">
  <img src="docs/ml-ticket-dispatcher.png" alt="ML Ticket Dispatcher Architecture" width="700">
</p>