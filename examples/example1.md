For AWS there are packages already defined,

here are some examples to define aws resources

## For aws lambda
```
Lambda(LambdaTrigger, "AWS Lambda Trigger Function", " ")
```

## For aws S3
```
SimpleStorageService(S3, "Amazon S3 Images Bucket", " ")
```

## For aws EC2
```
EC2(EC2, "App on EC2", " ")
```

## For SQSQueue
```
SQSQueue(SQSQueue, "SQSQueue", " ")
```

### For RelationalDatabaseService
```
RDS(RDS, "Amazon RDS", " ")
```

Similarly all other services follow the same style

ElasticLoadBalancing(elb, "Elastic Load Balancer", "Distributes Incoming Traffic")
CloudWatch(CloudWatch, "Amazon Cloudwatch", " ")
AutoScalingGroup(AutoScalingGroup1, "Auto Scaling Group", "")
ELBNetworkLoadBalancer(ELBNetworkLoadBalancer, "Network Load Balancer", " ")
VPCInternetGateway(VPCInternetGateway, "Internet Gateway", " ")
VPCInternetGateway -u-> InternetAlt1
VPCVPNConnection(VPCVPNConnection, "VPN\nConnection", " ")
DirectConnect(DirectConnect, "Direct\nConnect", " ")
TransitGateway(S3TransitGatewayStaging, "TransitGateway", " ")
VPCCustomerGateway(VPCCustomerGateway, " ", " ")





now using that same language write me a puml script for 

an online food delivery application. The diagram should consider all the essential components and interactions necessary to explain the system. The architecture should include the following AWS services and components:
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






### output

```
@startuml OnlineFoodDeliveryApplication
!include importall.puml

' Define components
APIGateway(apiGateway, "Amazon API Gateway", "Routes API Requests")
Lambda(orderFunction, "Order Management Lambda", "Processes Orders")
Lambda(authFunction, "User Authentication Lambda", "Handles User Auth")
RDS(customerDatabase, "Customer & Order Database", "Stores Customer, Restaurant, Order Data")
SimpleStorageService(imageStorage, "Image Storage Bucket", "Stores Images & Media")
CloudFront(contentDelivery, "Content Delivery Network", "Distributes Static Assets")
Cognito(userAuth, "User Authentication Service", "Manages User Accounts & Social Logins")
ElasticLoadBalancing(loadBalancer, "Traffic Load Balancer", "Distributes Incoming Traffic to EC2")
EC2(applicationServer, "Application Server", "Runs Application & Services")

' Define relationships
apiGateway -down-> orderFunction : routes
apiGateway -down-> authFunction : routes
orderFunction -down-> customerDatabase : accesses
authFunction -down-> customerDatabase : accesses
imageStorage -left-> contentDelivery : caches
apiGateway -right-> contentDelivery : caches API responses
apiGateway --> userAuth : authenticates
loadBalancer --> applicationServer : balances
applicationServer --> customerDatabase : accesses
applicationServer --> imageStorage : uses

' Additions for clarity and missing components
SimpleQueueService(sqs, "Message Queue", "Decouples between components")
Lambda(notificationFunction, "Notification Lambda", "Handles Notifications")
SimpleNotificationService(notificationService, "Notification Service", "Sends notifications")

' Integrating new components
orderFunction -down-> sqs : sends messages
sqs -down-> notificationFunction : triggers
notificationFunction --> notificationService : sends notifications

' Clarifying Elastic Load Balancing
' Assuming it primarily routes traffic to EC2 instances which can then interact with other services
loadBalancer -[hidden]-> apiGateway : Clarify relationship
applicationServer -[hidden]-> lambda : EC2 to Lambda interaction not direct but via API Gateway or other triggers

@enduml

```


### Agent generated
![](example1.png)

### Actual 
![](https://docs.aws.amazon.com/images/solutions/latest/qnabot-on-aws/images/Architecture_Diagram.png)

https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/architecture-overview.html