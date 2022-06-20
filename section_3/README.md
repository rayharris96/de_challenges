Section 3 - System Design
The following is the system architecture elaboration on the cloud-hosted data infrastructure of the image processing application.

1. Image is uploaded by the web client. Assuming that load balancing is taken care of, EC2 instances carry out the following tasks: it first displays the uploaded image to the web client, then the data is transferred and stored to S3 bucket. Image metadata and user information is inserted into an RDS service for BI and analytics.
2. Once the image is successfully stored to S3, Amazon S3 invokes Lambda function asynchronously with an event that contains details about the object in S3 bucket.
3. AWS Lambda produces messages and publishes them to Kafka brokers. The message includes the file S3 URI as well as details about the S3 object.
4. AWS MSK manages the Kafka topics and publishes the streams of tasks to the consumer groups that are subscribed to the respective topic. Each consumer reads the message in the task offset in Kafka partition queue, subsequently downloads the image from S3 and process the images. The consumers are namely containerized ECS instances which are managed by Fargate for scalability.
5. The processed images are uploaded to two different S3 buckets: the archival bucket with retention period set to 7 days and the production bucket.
6. Processed images are then made available from Cloudfront Delivery Network - displays processed images back to the web client


Pros:
- It has a higher throughput as Kafka can handle high velocity and volume data.
- Image processing is scalable as they are run on distributed containerized application. 
- It is fault-tolerant as Kafka provides semi-persistent message queue.

Cons:
- S3 event trigger to Lambda does not guarantee delivery, however through implementation of dead-letter-queue, retry and error-handling mechanism can be applied
- S3 event trigger doesn't support fan-out. In case in the future there is a need to trigger multiple Lambda function, SNS queue might be needed as an intermediary