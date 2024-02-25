from textwrap import dedent
from crewai import Task

class AWSTasks():
	def code_task(self, agent, text):
		return Task(description=dedent(f"""
		Create a PlantUML diagram illustrating a solution based on AWS services. The solution should showcase key AWS services enabling remote access, application streaming, network architecture, and security measures to support a distributed workforce.

        **Instructions**: Utilize the following AWS PlantUML library imports to ensure compatibility and comprehensive representation of AWS services in your diagram. Even if not all libraries are used, include them to maintain a standard format:


        **Blog example of aws services using PlantUML**
        ```plaintext
        @startuml
        !include <awslib/AWSCommon>
        !include <awslib/AWSSimplified.puml>
        !include <awslib/Compute/all.puml>
        !include <awslib/mobile/all.puml>
        !include <awslib/general/all.puml>
        !include <awslib/GroupIcons/all.puml>
        !include <awslib/Storage/all.puml>
        !include <awslib/ManagementAndGovernance/all.puml>
        !include <awslib/CustomerEngagement/all.puml>
        !include <awslib/MachineLearning/all.puml>
        !include <awslib/NetworkingAndContentDelivery/all.puml>
        !include <awslib/Database/all.puml>
        !include <awslib/ApplicationIntegration/all.puml>

        'Compute/General
        'Storage/SimpleStorageServiceS3.png
        'ApplicationIntegration/SQS.png
        'Compute/Lambda.png
        'Compute/EC2
        'ManagementAndGovernance/CloudWatch.png
        'CustomerEngagement/SESEmail.png
        'MachineLearning/SageMaker.png
        ''Mobile/APIGateway.png
        'NetworkingAndContentDelivery/APIGateway2.png
        'Database/Aurora.png
        'ApplicationIntegration/SQSQueue.png


        skinparam linetype polyline
        ' skinparam linetype ortho

        'top left section
        '-------------------------------------------------------------
        package EC2_Instance {{
        General(IngestionApp, "Ingestion App", " ")
        General(ChunkingApp, "Chunking Orchestration App", " ")
        }}

        SimpleStorageServiceS3(S3Staging, "Amazon S3 Staging Bucket", " ")
        SQS(SQSIngest, "Amazon SQS Ingest Queue", " ")

        Lambda(LambdaTrigger, "AWS Lambda Trigger Function", " ")

        LambdaTrigger -up-> IngestionApp
        IngestionApp -up-> SQSIngest
        SQSIngest -down-> ChunkingApp
        S3Staging <-down-> EC2_Instance

        'top right section
        '-------------------------------------------------------------
        together {{
        SQS(SQSLargeFileQueue, "Amazon SQS Large File Queue", " ")
        SQS(SQSSmallFileQueue, "Amazon SQS Small File Queue", " ")
        SQS(SQSSingleFileQueue, "Amazon SQS Single File Queue", " ")

        EC2(LargeFileChunkingAppEC2, "Large File Chunking App on EC2", " ")
        Lambda(LambdaSmallFileChunking, "Small File Chunking Lambda", " ")
        Lambda(ImageConversionLambdaFunction, "Image Conversion Lambda Function", " ")
        }}
        'todo dashed line boundary
        package DLQ {{
        SQSQueue(DLQ1, "DLQ", " ")
        SQSQueue(DLQ2, "DLQ", " ")
        SQSQueue(DLQ3, "DLQ", " ")
        }}

        ChunkingApp -right-> SQSLargeFileQueue
        ChunkingApp -right-> SQSSmallFileQueue
        ChunkingApp -right-> SQSSingleFileQueue

        SQSLargeFileQueue -right-> LargeFileChunkingAppEC2
        LargeFileChunkingAppEC2 -down-> SQSSmallFileQueue
        SQSSmallFileQueue -right-> LambdaSmallFileChunking
        LambdaSmallFileChunking -down-> SQSSingleFileQueue
        SQSSingleFileQueue -right-> ImageConversionLambdaFunction

        'todo dashed line
        SQSLargeFileQueue -down-> DLQ1
        SQSSmallFileQueue -down-> DLQ2
        SQSSingleFileQueue -down-> DLQ3


        'bottom right section
        '-------------------------------------------------------------

        SimpleStorageServiceS3(S3Images, "Amazon S3 Images Bucket", " ")
        EC2(EC2DLQFailsafeApp, "DLQ Failsafe App on EC2", " ")
        SQS(SQSConvertedImageQueue, "Amazon SQS Converted Image Queue", " ")
        Lambda(LambdaInferenceInvocation, "Inference Invocation Lambda Function", " ")
        Aurora(Aurora, "Amazon Aurora", " ")
        APIGateway(AmazonAPIGateway, "Amazon API Gateway", "")
        SageMaker(AmazonSageMaker, "Amazon SageMaker Endpoint", "")

        DLQ1 -down-> EC2DLQFailsafeApp
        DLQ2 -down-> EC2DLQFailsafeApp
        DLQ3 -down-> EC2DLQFailsafeApp

        EC2DLQFailsafeApp -right-> S3Images

        ImageConversionLambdaFunction -down-> S3Images
        S3Images -down-> SQSConvertedImageQueue
        SQSConvertedImageQueue -left-> LambdaInferenceInvocation
        LambdaInferenceInvocation -down-> Aurora
        LambdaInferenceInvocation <-left-> AmazonAPIGateway
        AmazonAPIGateway <-left-> AmazonSageMaker


        'bottom left section
        '-------------------------------------------------------------

        CloudWatch(CloudWatch, "Amazon Cloudwatch", " ")
        SNS(SNS1, "Amazon SNS", "")
        SESEmail(SESEmail, "Email Notification", "")

        CloudWatch -right-> DLQ
        CloudWatch -left-> SNS1
        SNS1 -left-> SESEmail

        footer %filename() rendered with PlantUML version %version()\nThe Hitchhiker’s Guide to PlantUML
        @enduml
        ```

        **Task**

        {text}

        Your final submission should be the complete PlantUML (.puml) code, focusing solely on the puml code without additional commentary.

        Avoid mistakes like
			- using SimpleStorageServiceS3 instead of SimpleStorageService
			- using IAM instead of IdentityandAccessManagement
			- using S3 instead of SimpleStorageService
			"""),
			agent=agent
		)

	def review_task(self, agent, text):
		return Task(description=dedent(f"""\
			You are helping to create a AWS solution using AWS services using PlantUML script.
			It's not a UML diagram but AWS solution architecture.

			Instructions
			------------
			{text}

			Using the code you got, check for errors. Check for logic errors,
			syntax errors, missing imports. Also make sure if the AWS solution is a good practice.

			Your Final answer must be the full puml code, only the puml code and nothing else.
			"""),
			agent=agent
		)

	# def evaluate_task(self, agent, text):
	# 	return Task(description=dedent(f"""\
	# 		You are helping create a game using python, these are the instructions:

	# 		Instructions
	# 		------------
	# 		{text}

	# 		You will look over the code to insure that it is complete and
	# 		does the job that it is supposed to do.

	# 		Your Final answer must be the full python code, only the python code and nothing else.
	# 		"""),
	# 		agent=agent
	# 	)
