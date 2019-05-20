# AWS Account Creation

Amazon Web Services (AWS) provides a wide variaty of cloud-based
products including analytics, application integration, AR and VR, cost
management, blockchain, business applications, compute, customer
engagement, database, developer tools, end user computing, game tech,
IoT, machine learning, management and governance, media services,
migration and transfer, mobile, networking and content delivery,
robotics, satellite, security, identity and compliance, and storage.
Here at cloudmesh, we develop services through providers to support your
utilization of many of these products.

Here we are especially interested in using the following services:

-   **Amazon Elastic Compute Cloud (EC2)** Amazon EC2 is web service
    that enables users to perform elastic web-scable computing while
    having complete control over instances. It is integrated with most
    AWS services such as Amazon S3, RDS, and VPC.
-   **Amazon Simple Storage Service (S3)** Amazon S3 an object storage
    service that offers a wide range of storage classes.

We provide a step-by-step guide on how to create an AWS account through
the AWS webpage to utilize these services.

First, we go to the AWS website

-   <https://aws.amazon.com>

and click on `Create an AWS Account`.

![Create Account](images/aws/image1.png)

This will direct you to the account creation page. Now we fill out your
information and click `Continue`.

![Continue](images/aws/image2.png)

Next, you will need to fill out your contact information. You can choose
`Professional` or `Personal` as your account type. Here in this
tutorial, we selected `Personal`. Read the *AWS Customer Agreement*, and
check the box if agreed. Click on `Create Account and Continue` to
continue.

![Contact Information](images/aws/image3.png)

Fill out your payment information and proceed. Dependent on your level
of security, you may want to explore using a prepaid credit card if you
do not want to use your regular credit card.

If you just started using AWS, you will have a free account for a while
as AWS will state:

> We will not charge you unless your usage exceeds the AWS Free Tier
> Limits. - Amazon AWS

Please review the terms of the free tier carefully.

![Payment](images/aws/image4.png)

Next your need to confirm your identity. You can choose either
`Text message (SMS)` or `Voice call` to receive your verification code.
Here we choose `Text message (SMS)`. Enter your phone number and the
security check code and click `Send SMS`.

![Identity confirmation](images/aws/image5.png)

Enter the 4-digit verification code you received from your phone, and
click on `Verify Code`.

![Verification](images/aws/image6.png)

If you entered the correct verification code, you will see this page.
Click on `Continue`.

![Continue](images/aws/image7.png)

You will need to choose your support plan. We chose Amazon's free tier
`Basic Plan`.

![Select a Plan](images/aws/image8.png)

Congratulations! You have successfully created an AWS account. Now you
can click on `Sign In to the Console` to sign in.

![Personalize](images/aws/image9.png)

Enter the email address you used for registration, and click on `Next`.

![email](images/aws/image10.png)

Enter the password you used for registration, and click on `Sign In`.

![Password](images/aws/image11.png)

Now you've successfully signed in to the AWS Management Console.

![AWS Services](images/aws/image12.png)

You can click on `Services` to explore AWS services through their
webpage.

![Explore services](images/aws/image13.png)

You can also start managing your account and instances through our
cloudmesh services. This is especially of interest if you use cloudmesh
to manage your storage and computational needs while laso being able to
leverage other clouds.


## Access key

Now that you have an account it is necessarry that you can authenticate to your 
cloud account from a program or a command line. The isntructions for this are
 copied from 

* <https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html>

You will need to open the IAM console at

* <https://console.aws.amazon.com/iam/home?#home>

Here you do the following:

1. In the navigation pane of the console, choose Users.

2. Choose your IAM user name (not the check box).

3. Choose the Security credentials tab and then choose Create access key.

4. To see the new access key, choose Show. Your credentials will look something
   like this:

   Access key ID: AKIAIOSFODNN7EXAMPLE
   Secret access key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY

To download the key pair, choose Download .csv file. Store the keys in a 
secure location and do not by default store them in the Downloads folder. 
We recommend that you store is in ~/.cloudmesh, but before doing so make sure
 the permissions for ~/.cloudmesh are restricted,
 
You can locate the page also by replacing YOURUSERNAME with your AWS username
 in the following link 

* <https://console.aws.amazon
.com/iam/home?#/users/YOURUSERNAME?section=security_credentials>


## Compute Service

- [ ] TODO: Aws EC2 account. Describe here if there is anything to be done for
  accessing EC2

## Storage Service

- [ ] TODO: Aws S3 account. Describe here if there is anything to be done for
  accessing S3

## References

Additional information about the services can be found at:

-   Open Distro for Elastic Search, <https://aws.amazon.com/?nc2=h_lg>
-   Amazon EC2, <https://aws.amazon.com/ec2/?nc2=h_m1>
-   Amazon S3, <https://aws.amazon.com/s3/?c=23&pt=1>
