import boto3

# Returns the active regions for the account. Does not included disabled regions
# to avoid issues when changing defaults. 
def get_active_regions():
    region_list = []

    ec2_client = boto3.client('ec2')
    response = ec2_client.describe_regions(AllRegions=False)['Regions']

    for region in response:
        region_list.append(region['RegionName'])

    print(f'Active regions in this account are: {region_list}')

    return region_list

# Iterates through regions that are active in the account and changes the metadata defaults.
# By default, will only modify the IMDS version to 2 and the hops to 2. All settings can be
# overrriden by user supplied values.
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/ec2/client/modify_instance_metadata_defaults.html

def set_metadata_defaults(regions, http_endpoint=None, http_tokens='required', hop_limit=2, metadata_tags=None):

    if http_endpoint == None:
        http_endpoint = 'no-preference'
    
    if metadata_tags == None:
        metadata_tags = 'no-preference'

    for region in regions:
        ec2_client = boto3.client('ec2', region)
        ec2_client.modify_instance_metadata_defaults(
            HttpTokens=http_tokens,
            HttpPutResponseHopLimit=hop_limit,
            HttpEndpoint=http_endpoint,
            InstanceMetadataTags=metadata_tags)
        print(f'Updated metadata defaults in {region}')
    
    return 
        


if __name__ == '__main__':

    ## Get active regions for account
    regions = get_active_regions()
    set_metadata_defaults(regions)