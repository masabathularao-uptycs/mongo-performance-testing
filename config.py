from bson import ObjectId
import uuid
from datetime import datetime
from pymongo import UpdateOne,MongoClient

TAG="local"
database_name="database"
# collection_name="collection"
remote_node="s1cloudsim1c"

TOTAL_COLLECTIONS=10
NUM_DOCS_EACH_THREAD_TO_INSERT=10


# Largest document found in collection 'aws_principal_cloudaudit':
#size of largest doc = 7396 bytes
# largest_document={'_id': ObjectId('65b78ab1aafd33c71758b321'),'event_id': '7f008624-4563-44c8-b7fb-dc5480d889c5', 'upt_table_key_value': 'i-00e843dd029a80939', 'upt_table_name': 'aws_ec2_instance', 'event_name': 'RunInstances', 'event_source': 'ec2.amazonaws.com', 'event_time': '2024-01-29T11:19:40Z', 'event_type': 'AwsApiCall', 'request_parameters': {'tagSpecificationSet': {'items': [{'tags': [{'key': 'Jira ID', 'value': 'NOJIRA'}, {'key': 'purpose', 'value': 'Development'}, {'key': 'Purpose', 'value': 'Development'}, {'key': 'Name', 'value': 'kshuklak8scis-configdb1'}, {'key': 'Stack', 'value': 'ouDefault'}, {'key': 'Domains', 'value': 'kshuklak8scis'}, {'key': 'OS Version', 'value': 'Ubuntu 20'}, {'value': 'Kubernetes', 'key': 'Department'}, {'key': 'Requester', 'value': 'kshukla@uptycs.com'}, {'key': 'Type', 'value': 'SU Stack'}, {'key': 'Schedule', 'value': '24x7'}, {'key': 'Expire On', 'value': '2024-02-01'}, {'key': 'Spark', 'value': 'true'}], 'resourceType': 'instance'}, {'resourceType': 'volume', 'tags': [{'value': 'NOJIRA', 'key': 'Jira ID'}, {'key': 'purpose', 'value': 'Development'}, {'key': 'Purpose', 'value': 'Development'}, {'key': 'Name', 'value': 'kshuklak8scis-configdb1'}, {'key': 'Stack', 'value': 'ouDefault'}, {'key': 'Domains', 'value': 'kshuklak8scis'}, {'key': 'OS Version', 'value': 'Ubuntu 20'}, {'key': 'Department', 'value': 'Kubernetes'}, {'value': 'kshukla@uptycs.com', 'key': 'Requester'}, {'key': 'Type', 'value': 'SU Stack'}, {'key': 'Schedule', 'value': '24x7'}, {'key': 'Expire On', 'value': '2024-02-01'}, {'value': 'true', 'key': 'Spark'}]}]}, 'iamInstanceProfile': {'name': 'Role_DB'}, 'clientToken': 'kshuk-insta-15HJECBRGNUR1', 'disableApiStop': False, 'monitoring': {'enabled': False}, 'availabilityZone': 'us-east-1d', 'instancesSet': {'items': [{'imageId': 'ami-01b3a6ac6a20b3dc4', 'keyName': 'kshukla', 'maxCount': 1.0, 'minCount': 1.0}]}, 'networkInterfaceSet': {'items': [{'deleteOnTermination': True, 'description': 'Primary network interface', 'deviceIndex': 0.0, 'groupSet': {'items': [{'groupId': 'sg-0a27cf0a358bbd975'}, {'groupId': 'sg-09b405083a3c91c7e'}, {'groupId': 'sg-09bcc035c5bbade6b'}]}, 'subnetId': 'subnet-0c14845525abba1c6'}]}, 'userData': '<sensitiveDataRemoved>', 'ebsOptimized': True, 'disableApiTermination': False, 'instanceInitiatedShutdownBehavior': 'stop', 'instanceType': 'm5a.2xlarge', 'blockDeviceMapping': {'items': [{'deviceName': '/dev/sda1', 'ebs': {'volumeSize': 50.0, 'volumeType': 'gp3', 'deleteOnTermination': True, 'encrypted': True}}]}}, 'response_elements': {'instancesSet': {'items': [{'placement': {'availabilityZone': 'us-east-1d', 'tenancy': 'default'}, 'tagSet': {'items': [{'value': 'true', 'key': 'Spark'}, {'key': 'OS Version', 'value': 'Ubuntu 20'}, {'value': 'SU Stack', 'key': 'Type'}, {'value': 'Kubernetes', 'key': 'Department'}, {'key': 'purpose', 'value': 'Development'}, {'key': 'Domains', 'value': 'kshuklak8scis'}, {'key': 'Stack', 'value': 'ouDefault'}, {'key': 'Requester', 'value': 'kshukla@uptycs.com'}, {'key': 'Name', 'value': 'kshuklak8scis-configdb1'}, {'key': 'Schedule', 'value': '24x7'}, {'key': 'Expire On', 'value': '2024-02-01'}, {'key': 'Jira ID', 'value': 'NOJIRA'}, {'key': 'Purpose', 'value': 'Development'}]}, 'productCodes': {}, 'rootDeviceType': 'ebs', 'subnetId': 'subnet-0c14845525abba1c6', 'virtualizationType': 'hvm', 'amiLaunchIndex': 0.0, 'imageId': 'ami-01b3a6ac6a20b3dc4', 'launchTime': 1706527180000.0, 'keyName': 'kshukla', 'monitoring': {'state': 'disabled'}, 'privateDnsName': 'ip-10-252-3-100.ec2.internal', 'privateDnsNameOptions': {'enableResourceNameDnsAAAARecord': False, 'enableResourceNameDnsARecord': False, 'hostnameType': 'ip-name'}, 'capacityReservationSpecification': {'capacityReservationPreference': 'open'}, 'hypervisor': 'xen', 'instanceId': 'i-00e843dd029a80939', 'sourceDestCheck': True, 'blockDeviceMapping': {}, 'enclaveOptions': {'enabled': False}, 'maintenanceOptions': {'autoRecovery': 'default'}, 'metadataOptions': {'httpEndpoint': 'enabled', 'httpProtocolIpv4': 'enabled', 'httpProtocolIpv6': 'disabled', 'httpPutResponseHopLimit': 1.0, 'httpTokens': 'optional', 'instanceMetadataTags': 'disabled', 'state': 'pending'}, 'privateIpAddress': '10.252.3.100', 'rootDeviceName': '/dev/sda1', 'ebsOptimized': True, 'iamInstanceProfile': {'id': 'AIPA5HMYYUTIMNWCXKVBR', 'arn': 'arn:aws:iam::909242836176:instance-profile/Role_DB'}, 'instanceType': 'm5a.2xlarge', 'instanceState': {'code': 0.0, 'name': 'pending'}, 'stateReason': {'code': 'pending', 'message': 'pending'}, 'vpcId': 'vpc-0f3f5bde3b5e27131', 'architecture': 'x86_64', 'cpuOptions': {'coreCount': 4.0, 'threadsPerCore': 2.0}, 'enaSupport': True, 'clientToken': 'kshuk-insta-15HJECBRGNUR1', 'currentInstanceBootMode': 'legacy-bios', 'networkInterfaceSet': {'items': [{'description': 'Primary network interface', 'groupSet': {'items': [{'groupId': 'sg-09b405083a3c91c7e', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgOU-1VCQYRS9917S8'}, {'groupId': 'sg-09bcc035c5bbade6b', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgSSH-5Q5NZRAHC992'}, {'groupId': 'sg-0a27cf0a358bbd975', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgHTTPz-145KPHM2EMFBU'}]}, 'privateIpAddress': '10.252.3.100', 'status': 'in-use', 'vpcId': 'vpc-0f3f5bde3b5e27131', 'attachment': {'status': 'attaching', 'attachTime': 1706527180000.0, 'attachmentId': 'eni-attach-098f474f3e3ca4928', 'deleteOnTermination': True, 'deviceIndex': 0.0, 'networkCardIndex': 0.0}, 'networkInterfaceId': 'eni-0c65d03e13b7daaeb', 'ownerId': '909242836176', 'interfaceType': 'interface', 'macAddress': '0e:26:77:cd:08:85', 'privateDnsName': 'ip-10-252-3-100.ec2.internal', 'privateIpAddressesSet': {'item': [{'primary': True, 'privateDnsName': 'ip-10-252-3-100.ec2.internal', 'privateIpAddress': '10.252.3.100'}]}, 'sourceDestCheck': True, 'tagSet': {}, 'ipv6AddressesSet': {}, 'subnetId': 'subnet-0c14845525abba1c6'}]}, 'groupSet': {'items': [{'groupId': 'sg-09b405083a3c91c7e', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgOU-1VCQYRS9917S8'}, {'groupId': 'sg-09bcc035c5bbade6b', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgSSH-5Q5NZRAHC992'}, {'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgHTTPz-145KPHM2EMFBU', 'groupId': 'sg-0a27cf0a358bbd975'}]}}]}, 'ownerId': '909242836176', 'requestId': '34c1c356-025b-469e-b582-809f1e9d7fe3', 'requesterId': '043234062703', 'reservationId': 'r-0e5c3270f63551da6', 'groupSet': {}}, 'source_ip_address': 'cloudformation.amazonaws.com', 'upt_connector_type': 'aws', 'upt_parser_version': '1.0.0', 'upt_schema_version': '1.0.0', 'upt_table_key_name': 'instance_id', 'user_agent': 'cloudformation.amazonaws.com', 'user_identity_account_id': '909242836176', 'user_identity_arn': 'arn:aws:sts::909242836176:assumed-role/Administrators/kshukla@uptycs.com', 'user_identity_principal_id': 'AROA5HMYYUTIA73K2N5HG:kshukla@uptycs.com', 'user_identity_session_context_attributes_creation_date': '2024-01-29T11:14:34Z', 'user_identity_session_context_attributes_mfa_authenticated': 'false', 'user_identity_session_context_session_issuer_account_id': '909242836176', 'user_identity_session_context_session_issuer_arn': 'arn:aws:iam::909242836176:role/Administrators', 'user_identity_session_context_session_issuer_principal_id': 'AROA5HMYYUTIA73K2N5HG', 'user_identity_session_context_session_issuer_type': 'Role', 'user_identity_session_context_session_issuer_user_name': 'Administrators', 'user_identity_type': 'AssumedRole'}


def get_base_document():
    current_time = datetime.now()
    return {'event_time':current_time.strftime("%Y-%m-%dT%H:%M:%SZ"),'event_name': 'RunInstances', 'event_source': 'ec2.amazonaws.com',  'event_type': 'AwsApiCall', 'request_parameters': {'tagSpecificationSet': {'items': [{'tags': [{'key': 'Jira ID', 'value': 'NOJIRA'}, {'key': 'purpose', 'value': 'Development'}, {'key': 'Purpose', 'value': 'Development'}, {'key': 'Name', 'value': 'kshuklak8scis-configdb1'}, {'key': 'Stack', 'value': 'ouDefault'}, {'key': 'Domains', 'value': 'kshuklak8scis'}, {'key': 'OS Version', 'value': 'Ubuntu 20'}, {'value': 'Kubernetes', 'key': 'Department'}, {'key': 'Requester', 'value': 'kshukla@uptycs.com'}, {'key': 'Type', 'value': 'SU Stack'}, {'key': 'Schedule', 'value': '24x7'}, {'key': 'Expire On', 'value': '2024-02-01'}, {'key': 'Spark', 'value': 'true'}], 'resourceType': 'instance'}, {'resourceType': 'volume', 'tags': [{'value': 'NOJIRA', 'key': 'Jira ID'}, {'key': 'purpose', 'value': 'Development'}, {'key': 'Purpose', 'value': 'Development'}, {'key': 'Name', 'value': 'kshuklak8scis-configdb1'}, {'key': 'Stack', 'value': 'ouDefault'}, {'key': 'Domains', 'value': 'kshuklak8scis'}, {'key': 'OS Version', 'value': 'Ubuntu 20'}, {'key': 'Department', 'value': 'Kubernetes'}, {'value': 'kshukla@uptycs.com', 'key': 'Requester'}, {'key': 'Type', 'value': 'SU Stack'}, {'key': 'Schedule', 'value': '24x7'}, {'key': 'Expire On', 'value': '2024-02-01'}, {'value': 'true', 'key': 'Spark'}]}]}, 'iamInstanceProfile': {'name': 'Role_DB'}, 'clientToken': 'kshuk-insta-15HJECBRGNUR1', 'disableApiStop': False, 'monitoring': {'enabled': False}, 'availabilityZone': 'us-east-1d', 'instancesSet': {'items': [{'imageId': 'ami-01b3a6ac6a20b3dc4', 'keyName': 'kshukla', 'maxCount': 1.0, 'minCount': 1.0}]}, 'networkInterfaceSet': {'items': [{'deleteOnTermination': True, 'description': 'Primary network interface', 'deviceIndex': 0.0, 'groupSet': {'items': [{'groupId': 'sg-0a27cf0a358bbd975'}, {'groupId': 'sg-09b405083a3c91c7e'}, {'groupId': 'sg-09bcc035c5bbade6b'}]}, 'subnetId': 'subnet-0c14845525abba1c6'}]}, 'userData': '<sensitiveDataRemoved>', 'ebsOptimized': True, 'disableApiTermination': False, 'instanceInitiatedShutdownBehavior': 'stop', 'instanceType': 'm5a.2xlarge', 'blockDeviceMapping': {'items': [{'deviceName': '/dev/sda1', 'ebs': {'volumeSize': 50.0, 'volumeType': 'gp3', 'deleteOnTermination': True, 'encrypted': True}}]}}, 'response_elements': {'instancesSet': {'items': [{'placement': {'availabilityZone': 'us-east-1d', 'tenancy': 'default'}, 'tagSet': {'items': [{'value': 'true', 'key': 'Spark'}, {'key': 'OS Version', 'value': 'Ubuntu 20'}, {'value': 'SU Stack', 'key': 'Type'}, {'value': 'Kubernetes', 'key': 'Department'}, {'key': 'purpose', 'value': 'Development'}, {'key': 'Domains', 'value': 'kshuklak8scis'}, {'key': 'Stack', 'value': 'ouDefault'}, {'key': 'Requester', 'value': 'kshukla@uptycs.com'}, {'key': 'Name', 'value': 'kshuklak8scis-configdb1'}, {'key': 'Schedule', 'value': '24x7'}, {'key': 'Expire On', 'value': '2024-02-01'}, {'key': 'Jira ID', 'value': 'NOJIRA'}, {'key': 'Purpose', 'value': 'Development'}]}, 'productCodes': {}, 'rootDeviceType': 'ebs', 'subnetId': 'subnet-0c14845525abba1c6', 'virtualizationType': 'hvm', 'amiLaunchIndex': 0.0, 'imageId': 'ami-01b3a6ac6a20b3dc4', 'launchTime': 1706527180000.0, 'keyName': 'kshukla', 'monitoring': {'state': 'disabled'}, 'privateDnsName': 'ip-10-252-3-100.ec2.internal', 'privateDnsNameOptions': {'enableResourceNameDnsAAAARecord': False, 'enableResourceNameDnsARecord': False, 'hostnameType': 'ip-name'}, 'capacityReservationSpecification': {'capacityReservationPreference': 'open'}, 'hypervisor': 'xen', 'instanceId': 'i-00e843dd029a80939', 'sourceDestCheck': True, 'blockDeviceMapping': {}, 'enclaveOptions': {'enabled': False}, 'maintenanceOptions': {'autoRecovery': 'default'}, 'metadataOptions': {'httpEndpoint': 'enabled', 'httpProtocolIpv4': 'enabled', 'httpProtocolIpv6': 'disabled', 'httpPutResponseHopLimit': 1.0, 'httpTokens': 'optional', 'instanceMetadataTags': 'disabled', 'state': 'pending'}, 'privateIpAddress': '10.252.3.100', 'rootDeviceName': '/dev/sda1', 'ebsOptimized': True, 'iamInstanceProfile': {'id': 'AIPA5HMYYUTIMNWCXKVBR', 'arn': 'arn:aws:iam::909242836176:instance-profile/Role_DB'}, 'instanceType': 'm5a.2xlarge', 'instanceState': {'code': 0.0, 'name': 'pending'}, 'stateReason': {'code': 'pending', 'message': 'pending'}, 'vpcId': 'vpc-0f3f5bde3b5e27131', 'architecture': 'x86_64', 'cpuOptions': {'coreCount': 4.0, 'threadsPerCore': 2.0}, 'enaSupport': True, 'clientToken': 'kshuk-insta-15HJECBRGNUR1', 'currentInstanceBootMode': 'legacy-bios', 'networkInterfaceSet': {'items': [{'description': 'Primary network interface', 'groupSet': {'items': [{'groupId': 'sg-09b405083a3c91c7e', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgOU-1VCQYRS9917S8'}, {'groupId': 'sg-09bcc035c5bbade6b', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgSSH-5Q5NZRAHC992'}, {'groupId': 'sg-0a27cf0a358bbd975', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgHTTPz-145KPHM2EMFBU'}]}, 'privateIpAddress': '10.252.3.100', 'status': 'in-use', 'vpcId': 'vpc-0f3f5bde3b5e27131', 'attachment': {'status': 'attaching', 'attachTime': 1706527180000.0, 'attachmentId': 'eni-attach-098f474f3e3ca4928', 'deleteOnTermination': True, 'deviceIndex': 0.0, 'networkCardIndex': 0.0}, 'networkInterfaceId': 'eni-0c65d03e13b7daaeb', 'ownerId': '909242836176', 'interfaceType': 'interface', 'macAddress': '0e:26:77:cd:08:85', 'privateDnsName': 'ip-10-252-3-100.ec2.internal', 'privateIpAddressesSet': {'item': [{'primary': True, 'privateDnsName': 'ip-10-252-3-100.ec2.internal', 'privateIpAddress': '10.252.3.100'}]}, 'sourceDestCheck': True, 'tagSet': {}, 'ipv6AddressesSet': {}, 'subnetId': 'subnet-0c14845525abba1c6'}]}, 'groupSet': {'items': [{'groupId': 'sg-09b405083a3c91c7e', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgOU-1VCQYRS9917S8'}, {'groupId': 'sg-09bcc035c5bbade6b', 'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgSSH-5Q5NZRAHC992'}, {'groupName': 'ouDefault-sg-YN6ILX45E0K0-sgHTTPz-145KPHM2EMFBU', 'groupId': 'sg-0a27cf0a358bbd975'}]}}]}, 'ownerId': '909242836176', 'requestId': '34c1c356-025b-469e-b582-809f1e9d7fe3', 'requesterId': '043234062703', 'reservationId': 'r-0e5c3270f63551da6', 'groupSet': {}}, 'source_ip_address': 'cloudformation.amazonaws.com', 'upt_connector_type': 'aws', 'upt_parser_version': '1.0.0', 'upt_schema_version': '1.0.0', 'user_agent': 'cloudformation.amazonaws.com', 'user_identity_account_id': '909242836176', 'user_identity_arn': 'arn:aws:sts::909242836176:assumed-role/Administrators/kshukla@uptycs.com', 'user_identity_principal_id': 'AROA5HMYYUTIA73K2N5HG:kshukla@uptycs.com', 'user_identity_session_context_attributes_creation_date': '2024-01-29T11:14:34Z', 'user_identity_session_context_attributes_mfa_authenticated': 'false', 'user_identity_session_context_session_issuer_account_id': '909242836176', 'user_identity_session_context_session_issuer_arn': 'arn:aws:iam::909242836176:role/Administrators', 'user_identity_session_context_session_issuer_principal_id': 'AROA5HMYYUTIA73K2N5HG', 'user_identity_session_context_session_issuer_type': 'Role', 'user_identity_session_context_session_issuer_user_name': 'Administrators', 'user_identity_type': 'AssumedRole'}

def generate_update_filter(collection_name):
    upt_table_name = ('_'.join(list(collection_name.split('_')[:-1]))).strip()
    doc={}
    doc['event_id'] = str(uuid.uuid4())
    doc['upt_table_name']= upt_table_name if upt_table_name!="" else collection_name
    doc['upt_table_key_value'] = 'i-00e843dd029a80939'
    doc['upt_table_key_name']= 'instance_id'
    return doc


# Index Fields -> I SHOULD MAKE THEM VARIABLE FOR EVERY DOCUMENT INSERTION : 
# total 5 key names -> i should decide what values they take because since these are index fields, the performance of lookup depends on them. Hence i need to generate these values as closeset as possible to the real-world scenario.

# id = automatically handled
# event_time = current time of insertion ->no issues
# event_id = generate using uuid ->no issues
# upt_table_name = i think i can give the table name present in the collection
# upt_table_key_name
# upt_table_key_value

def upsert_documents(collection,collection_name):
    # update_filter = generate_update_filter(collection_name)
    # result = collection.update_one(update_filter, {"$set": get_base_document()}, upsert=True)
    update_operations = [
        UpdateOne(generate_update_filter(collection_name), {"$set": get_base_document()},upsert=True),
        UpdateOne(generate_update_filter(collection_name), {"$set": get_base_document()},upsert=True),
        UpdateOne(generate_update_filter(collection_name), {"$set": get_base_document()},upsert=True),
    ]

    result = collection.bulk_write(update_operations)

    # print("Modified count:", result.modified_count)
    # print("Inserted count:", result.upserted_count)

    if result.modified_count:
        print(f"****************** ERROR : Document updated while trying to insert into '{collection_name}', operation performed : {update_operations} *********************")

def start_upsertion(collection,collection_name):
    for _ in range(NUM_DOCS_EACH_THREAD_TO_INSERT):
        print(f"Inserting into '{collection_name}' , count : {_}")
        upsert_documents(collection,collection_name)


def connect(TAG):

    if TAG == "remote":
        mongo_uri = f"mongodb://root:rootpassword@{remote_node}:30001/{database_name}?authSource=admin&w=1"

        # Create a MongoClient instance with TLS settings
        client = MongoClient(
            mongo_uri,
            tls=True,
            tlsCAFile="ca.crt",  # Specify the path to the CA certificate file
            tlsAllowInvalidHostnames=True
        )
    elif TAG == "local":
        client = MongoClient("mongodb://localhost:27017")

    return client
