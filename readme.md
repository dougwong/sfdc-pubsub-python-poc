# Python Proof of Concept for Using the Salesforce Pub/Sub API

This proof of concept was built off of the [example code provided by Salesforce](https://github.com/developerforce/pub-sub-api).

Before running `main.py`, you will need to install the python packages as described in [Prerequisites Step 1](https://developer.salesforce.com/docs/platform/pub-sub-api/guide/qs-generate-stub.html):

```pip3 install grpcio grpcio-tools avro-python3```

The stub files have already been generated and provided in this repo (`pubsub_api_pb2.py` and `pubsub_api_pb2_grpc.py`).

You will also need to update the following values in `main.py`:

* access_token
* instance_url
* tenant_id

You can get these values for your sandbox with a [curl command](https://developer.salesforce.com/docs/atlas.en-us.api_rest.meta/api_rest/quickstart_oauth.htm). The `tenant_id` can be found in the curl response body. If the response has the following:

```json
{
	"...": "...",
	"id": "https://login.salesforce.com/id/00D5e000001N20QEAS/0055e000003E8ooAAC",
	"...": "...",
}

```

the `tenant_id` would be `00D5e000001N20QEAS`.