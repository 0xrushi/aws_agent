from dotenv import load_dotenv
load_dotenv()

from crewai import Crew
from tasks import AWSTasks
from agents import AWSAgents

tasks = AWSTasks()
agents = AWSAgents()

print("## Welcome to the Game Crew")
print('-------------------------------')
prompt = """
Create a detailed diagram depicting the underlying AWS architecture for an online food delivery application. The diagram should consider all the essential components and interactions necessary to explain the system. The architecture should include the following AWS services and components:
1. Amazon API Gateway for handling incoming API requests and routing them to appropriate services.
2. AWS Lambda functions for serverless computing, allowing the app to process and manage orders, user authentication, and other core functionalities.
3. Amazon RDS for storing and managing customer, restaurant, and order data in a relational database.
4. Amazon S3 for storing static assets, such as images and other media files associated with the app.
5. Amazon CloudFront as a content delivery network (CDN) to distribute static assets and cache API responses for faster delivery.
6. Amazon Cognito for handling user authentication and authorization, managing user accounts and social logins.
7. AWS Elastic Load Balancer to distribute incoming traffic across multiple EC2 instances to maintain availability and performance.
8. Amazon EC2 instances for running the application server and any additional services required.
9. Additionally, illustrate the interaction between these components and services to represent the request and response flow. Also, include any external services, such as third-party authentication providers or payment gateways, and their interactions with the AWS architecture.
Please ensure that the diagram is clear, well-organized, and easy to understand, effectively showcasing the relationships between the various components and services within the AWS infrastructure.
"""
# Create Agents
senior_engineer_agent = agents.senior_engineer_agent()
code_reviewer_agent = agents.code_reviewer_agent()

# Create Tasks
tcode = tasks.code_task(senior_engineer_agent, prompt)
rcode = tasks.review_task(code_reviewer_agent, prompt)

crew = Crew(
	agents=[
		senior_engineer_agent,
		code_reviewer_agent,
		# chief_qa_engineer_agent
	],
	tasks=[
		tcode,
		rcode,
	],
	verbose=True
)

run = crew.kickoff()

print("\n\n########################")
print("## Here is the result")
print("########################\n")
print("final code for the AWS solution is mm:")
print(run)
