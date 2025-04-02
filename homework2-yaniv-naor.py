import boto3
from flask import Flask, request, jsonify
from datetime import datetime, timedelta


app = Flask(__name__)

session = None
expiration_time = None


@app.post("/api/v1/auth/login")
def login():
    global session, expiration_time

    login_data = request.json
    access_key_id = login_data["aws_access_key_id"]
    secret_access_key = login_data["aws_secret_access_key"]
    region = login_data["region_name"]
    if not access_key_id or not secret_access_key or not region:
        return jsonify({"error": "Missing access details"}), 400
    
    try:
        session = boto3.client(
            's3',
        aws_access_key_id = access_key_id,
        aws_secret_access_key = secret_access_key,
        region_name = region
        )

        expiration_time = datetime.now() + timedelta(minutes=5)

        session.list_buckets()

        return jsonify({"expires_at":f"{expiration_time}"}), 200

    except Exception as error:
        session = None
        return jsonify({"Unable to login to aws": str(error)}), 401


def get_session():
    global session, expiration_time
    if not session or datetime.now() > expiration_time:
        session = None
        return session
    return session


@app.get("/api/v1/s3/buckets")
def all_buckets():

    if not get_session():
        return jsonify({"error": "Session expired. Please login again."}), 401
    
    response = session.list_buckets()
    buckets_list = []

    for bucket in response['Buckets']:
        bucket_name = bucket["Name"]
        bucket_location = session.get_bucket_location(Bucket=bucket_name)
        bucket_region = bucket_location["LocationConstraint"]


        try:
            creation_date = bucket["CreationDate"]
            public_access_blocked = session.get_public_access_block(Bucket=bucket_name).get("PublicAccessBlockConfiguration").get("BlockPublicPolicy", False)
            bucket_versioning = session.get_bucket_versioning(Bucket=bucket_name).get("Status", "Disable")
            bucket_objects = session.list_objects(Bucket=bucket_name).get("Contents", [])
            object_count = len(bucket_objects)

            bucket_objects_size = 0
            for bucket_object in bucket_objects:
                bucket_objects_size += bucket_object["Size"]

            buckets_list.append({
                "name": bucket_name,
                "creation_date": creation_date,
                "region": bucket_region,
                "object_count": object_count,
                "total_size_bytes": bucket_objects_size,
                "versioning_enabled": bucket_versioning,
                "public_access_blocked": public_access_blocked
            })

        except Exception as error:
            print(f"Unable to export {bucket_name} data : {error}")
            continue

    return jsonify({"buckets": buckets_list}),200



@app.get("/api/v1/s3/buckets/<bucket_name>/details")
def bucket_detail(bucket_name):

    if not session:
        return jsonify({"error": "Session expired. Please login again."}), 401

    response = session.list_buckets()

    bucket_details = {}
    bucket_details["name"] = bucket_name
    for bucket in response['Buckets']:
        if bucket["Name"] == bucket_name:
            bucket_location = session.get_bucket_location(Bucket=bucket_name)
            bucket_region = bucket_location["LocationConstraint"]
            bucket_details["region"] = bucket_region

            try:
                creation_date = bucket["CreationDate"]
                bucket_details["creation_date"] = creation_date
            except:
                print(f"Unable to export the creation date of {bucket_name} bucket")

            try:
                bucket_lifecycle_configuration = session.get_bucket_lifecycle_configuration(Bucket=bucket_name)
                bucket_lifecycles = bucket_lifecycle_configuration["Rules"]
                bucket_lifecycle_list = []
                for bucket_lifecycle in bucket_lifecycles:
                    bucket_lifecycle_id = bucket_lifecycle["ID"]
                    bucket_lifecycle_status = bucket_lifecycle["Status"]
                    if "Transitions" in bucket_lifecycle:
                        bucket_lifecycle_transitions = bucket_lifecycle["Transitions"]
                bucket_lifecycle_list.append({"id": bucket_lifecycle_id, "status": bucket_lifecycle_status, "transitions": bucket_lifecycle_transitions})
                bucket_details["lifecycle_rules"] = bucket_lifecycle_list
            except:
                print(f"Unable to export the lifecycle of {bucket_name} bucket")

            try:
                bucket_encryptions = session.get_bucket_encryption(Bucket=bucket_name)
                bucket_encryptions = bucket_encryptions["ServerSideEncryptionConfiguration"]["Rules"]
                bucket_encryption_list = []
                for bucket_encryption in bucket_encryptions:
                    encryption_type = bucket_encryption["ApplyServerSideEncryptionByDefault"]["SSEAlgorithm"]
                    encryption_enable = bucket_encryption["BucketKeyEnabled"]
                    bucket_encryption_list.append({"enabled": encryption_enable, "type": encryption_type})
                bucket_details["encryption"] = bucket_encryption_list
            except:
                print(f"Unable to export the encryption of {bucket_name} bucket")

            try:
                bucket_objects = session.list_objects(Bucket=bucket_name).get("Contents", [])

                standard_objects_size = 0
                standardia_objects_size = 0
                glacier_objects_size = 0

                for bucket_object in bucket_objects:
                    if bucket_object["StorageClass"] == "STANDARD":
                        standard_objects_size += bucket_object["Size"]
                    elif bucket_object["StorageClass"] == "STANDARD_IA":
                        standardia_objects_size += bucket_object["Size"]
                    elif bucket_object["StorageClass"] == "GLACIER":
                        glacier_objects_size += bucket_object["Size"]
                bucket_details["storage_class_summary"] = {"STANDARD": standard_objects_size, "STANDARD_IA": standardia_objects_size, "GLACIER": glacier_objects_size}
            except:
                print(f"Unable to export the storage objects_size of {bucket_name} bucket")

            return jsonify(bucket_details),200
    return jsonify({"error": f"Bucket '{bucket_name}' not found"}), 404


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=6767, debug=True)
