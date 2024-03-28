# aws-imds-defaults

This is a simple utility to set the EC2 Instance Metadata Service default settings for an account across all active regions. 

On March 25, 2024, [AWS announced](https://aws.amazon.com/about-aws/whats-new/2024/03/set-imdsv2-default-new-instance-launches/) that users can now configure defaults for the Instance Metadata Service at the account level. Normally, this would involve going into the EC2 console for each region and manually changing the settings, or running the [`modify-instance-metadata-defaults`](https://docs.aws.amazon.com/cli/latest/reference/ec2/modify-instance-metadata-defaults.html) CLI command for each region that was introduced in version 2.15.33 of the AWS CLI. 

This script aims to automate that process. It makes use of your [AWS credentials that are passed to boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html) to authenticate to an account and then issue the command to change the default metadata settings in each region in that account. 

By default, the script will only change two defaults:

1. It will change the Metadata version to **V2 only (token required)
2. It will change the Metadata response hop limit to 2

You can override either value by passing in the parameter and the desired value to the `set_metadata_defaults` function. You can also set values for the Instance Metadata Service setting (which enables or disables the IMDS endpoint by default) and the Access to tags in Metadata. For more information on these settings, reference the [Boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_metadata_defaults.html) for `modify_instance_metadata_defaults`. 


## Pre-Requisites
1. Your Boto3 version must be 1.34.70 or later, which added support for `ModifyInstanceMetadataDefaults`.