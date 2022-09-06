import avro.io, avro.schema, certifi, io, json, grpc, requests, threading, time
import pubsub_api_pb2 as pb2
import pubsub_api_pb2_grpc as pb2_grpc


access_token = ''
instance_url = ''
tenant_id = ''

auth_metadata = (
	('accesstoken', access_token),
	('instanceurl', instance_url),
	('tenantid', tenant_id))

clean_output = True
num_requested = 3
replay_id=b'\x00\x00\x00\x00\x03m#\x08'
replay_preset = pb2.ReplayPreset.LATEST
# replay_preset = pb2.ReplayPreset.CUSTOM
topic = "/data/OpportunityChangeEvent"
# topic = "/event/Log_Entry__e"

semaphore = threading.Semaphore(1)


def clean_dict(input_dict):
	output = {}

	for key, value in input_dict.items():
		if isinstance(value, dict):
			output[key] = clean_dict(value)
		elif isinstance(value, list):
			output[key] = []

			for item in value:
				if isinstance(value, dict):
					output[key].append(clean_dict(item))
				elif value not in [None, '']:
					output[key].append(item)
		else:
			if value:
				output[key] = value

	return output


def decode(schema, payload):
	schema = avro.schema.parse(schema)
	buf = io.BytesIO(payload)

	decoder = avro.io.BinaryDecoder(buf)
	reader = avro.io.DatumReader(schema)

	return reader.read(decoder)


def fetchReqStream(topic_name, replay_preset, replay_id, num_requested):
	while True:
		semaphore.acquire()

		yield pb2.FetchRequest(
			topic_name = topic_name,
			replay_preset = replay_preset,
			replay_id=replay_id,
			num_requested = num_requested)


def main():
	with open(certifi.where(), 'rb') as f:
		creds = grpc.ssl_channel_credentials(f.read())

	with grpc.secure_channel('api.pubsub.salesforce.com:7443', creds) as channel:
		stub = pb2_grpc.PubSubStub(channel)

		print(f"Subscribing to {topic}")

		substream = stub.Subscribe(
			fetchReqStream(topic, replay_preset, replay_id, num_requested),
			metadata=auth_metadata)

		for response in substream:
			if response.events:
				semaphore.release()
				print(f"Number of events received: {len(response.events)}")

				for e in response.events:
					payload_bytes = e.event.payload
					schema_id = e.event.schema_id
					schema = stub.GetSchema(
						pb2.SchemaRequest(schema_id=schema_id),
						metadata=auth_metadata).schema_json

					decoded_dict = decode(schema, payload_bytes)

					print("Event JSON:")

					output_dict = decoded_dict

					if clean_output:
						output_dict = clean_dict(output_dict)

					print(json.dumps(output_dict, indent=2, sort_keys=True))

					if 'Payload__c' in decoded_dict:
						print("Log Entry Payload:")

						payload = json.loads(decoded_dict['Payload__c'])

						print(json.dumps(payload, indent=2, sort_keys=True))
			else:
				print(
					f"[{time.strftime('%b %d, %Y %l:%M%p %Z')}] The subscription is active.")

			print(f'latest_replay_id: {response.latest_replay_id}')
			print(f'pending_num_requested: {response.pending_num_requested}')


if __name__=="__main__":
	main()