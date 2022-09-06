# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pubsub_api.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10pubsub_api.proto\x12\x0b\x65ventbus.v1\"\x83\x01\n\tTopicInfo\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x13\n\x0btenant_guid\x18\x02 \x01(\t\x12\x13\n\x0b\x63\x61n_publish\x18\x03 \x01(\x08\x12\x15\n\rcan_subscribe\x18\x04 \x01(\x08\x12\x11\n\tschema_id\x18\x05 \x01(\t\x12\x0e\n\x06rpc_id\x18\x06 \x01(\t\"\"\n\x0cTopicRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\")\n\x0b\x45ventHeader\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"j\n\rProducerEvent\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tschema_id\x18\x02 \x01(\t\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12)\n\x07headers\x18\x04 \x03(\x0b\x32\x18.eventbus.v1.EventHeader\"M\n\rConsumerEvent\x12)\n\x05\x65vent\x18\x01 \x01(\x0b\x32\x1a.eventbus.v1.ProducerEvent\x12\x11\n\treplay_id\x18\x02 \x01(\x0c\"E\n\rPublishResult\x12\x11\n\treplay_id\x18\x01 \x01(\x0c\x12!\n\x05\x65rror\x18\x02 \x01(\x0b\x32\x12.eventbus.v1.Error\":\n\x05\x45rror\x12$\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x16.eventbus.v1.ErrorCode\x12\x0b\n\x03msg\x18\x02 \x01(\t\"\x94\x01\n\x0c\x46\x65tchRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12\x30\n\rreplay_preset\x18\x02 \x01(\x0e\x32\x19.eventbus.v1.ReplayPreset\x12\x11\n\treplay_id\x18\x03 \x01(\x0c\x12\x15\n\rnum_requested\x18\x04 \x01(\x05\x12\x14\n\x0c\x61uth_refresh\x18\x05 \x01(\t\"\x84\x01\n\rFetchResponse\x12*\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1a.eventbus.v1.ConsumerEvent\x12\x18\n\x10latest_replay_id\x18\x02 \x01(\x0c\x12\x0e\n\x06rpc_id\x18\x03 \x01(\t\x12\x1d\n\x15pending_num_requested\x18\x04 \x01(\x05\"\"\n\rSchemaRequest\x12\x11\n\tschema_id\x18\x01 \x01(\t\"D\n\nSchemaInfo\x12\x13\n\x0bschema_json\x18\x01 \x01(\t\x12\x11\n\tschema_id\x18\x02 \x01(\t\x12\x0e\n\x06rpc_id\x18\x03 \x01(\t\"f\n\x0ePublishRequest\x12\x12\n\ntopic_name\x18\x01 \x01(\t\x12*\n\x06\x65vents\x18\x02 \x03(\x0b\x32\x1a.eventbus.v1.ProducerEvent\x12\x14\n\x0c\x61uth_refresh\x18\x03 \x01(\t\"a\n\x0fPublishResponse\x12+\n\x07results\x18\x01 \x03(\x0b\x32\x1a.eventbus.v1.PublishResult\x12\x11\n\tschema_id\x18\x02 \x01(\t\x12\x0e\n\x06rpc_id\x18\x03 \x01(\t*%\n\tErrorCode\x12\x0b\n\x07UNKNOWN\x10\x00\x12\x0b\n\x07PUBLISH\x10\x01*4\n\x0cReplayPreset\x12\n\n\x06LATEST\x10\x00\x12\x0c\n\x08\x45\x41RLIEST\x10\x01\x12\n\n\x06\x43USTOM\x10\x02\x32\xe7\x02\n\x06PubSub\x12\x46\n\tSubscribe\x12\x19.eventbus.v1.FetchRequest\x1a\x1a.eventbus.v1.FetchResponse(\x01\x30\x01\x12@\n\tGetSchema\x12\x1a.eventbus.v1.SchemaRequest\x1a\x17.eventbus.v1.SchemaInfo\x12=\n\x08GetTopic\x12\x19.eventbus.v1.TopicRequest\x1a\x16.eventbus.v1.TopicInfo\x12\x44\n\x07Publish\x12\x1b.eventbus.v1.PublishRequest\x1a\x1c.eventbus.v1.PublishResponse\x12N\n\rPublishStream\x12\x1b.eventbus.v1.PublishRequest\x1a\x1c.eventbus.v1.PublishResponse(\x01\x30\x01\x42g\n com.salesforce.eventbus.protobufB\x0bPubSubProtoP\x01Z4github.com/developerforce/pub-sub-api-pilot/go/protob\x06proto3')

_ERRORCODE = DESCRIPTOR.enum_types_by_name['ErrorCode']
ErrorCode = enum_type_wrapper.EnumTypeWrapper(_ERRORCODE)
_REPLAYPRESET = DESCRIPTOR.enum_types_by_name['ReplayPreset']
ReplayPreset = enum_type_wrapper.EnumTypeWrapper(_REPLAYPRESET)
UNKNOWN = 0
PUBLISH = 1
LATEST = 0
EARLIEST = 1
CUSTOM = 2


_TOPICINFO = DESCRIPTOR.message_types_by_name['TopicInfo']
_TOPICREQUEST = DESCRIPTOR.message_types_by_name['TopicRequest']
_EVENTHEADER = DESCRIPTOR.message_types_by_name['EventHeader']
_PRODUCEREVENT = DESCRIPTOR.message_types_by_name['ProducerEvent']
_CONSUMEREVENT = DESCRIPTOR.message_types_by_name['ConsumerEvent']
_PUBLISHRESULT = DESCRIPTOR.message_types_by_name['PublishResult']
_ERROR = DESCRIPTOR.message_types_by_name['Error']
_FETCHREQUEST = DESCRIPTOR.message_types_by_name['FetchRequest']
_FETCHRESPONSE = DESCRIPTOR.message_types_by_name['FetchResponse']
_SCHEMAREQUEST = DESCRIPTOR.message_types_by_name['SchemaRequest']
_SCHEMAINFO = DESCRIPTOR.message_types_by_name['SchemaInfo']
_PUBLISHREQUEST = DESCRIPTOR.message_types_by_name['PublishRequest']
_PUBLISHRESPONSE = DESCRIPTOR.message_types_by_name['PublishResponse']
TopicInfo = _reflection.GeneratedProtocolMessageType('TopicInfo', (_message.Message,), {
  'DESCRIPTOR' : _TOPICINFO,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.TopicInfo)
  })
_sym_db.RegisterMessage(TopicInfo)

TopicRequest = _reflection.GeneratedProtocolMessageType('TopicRequest', (_message.Message,), {
  'DESCRIPTOR' : _TOPICREQUEST,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.TopicRequest)
  })
_sym_db.RegisterMessage(TopicRequest)

EventHeader = _reflection.GeneratedProtocolMessageType('EventHeader', (_message.Message,), {
  'DESCRIPTOR' : _EVENTHEADER,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.EventHeader)
  })
_sym_db.RegisterMessage(EventHeader)

ProducerEvent = _reflection.GeneratedProtocolMessageType('ProducerEvent', (_message.Message,), {
  'DESCRIPTOR' : _PRODUCEREVENT,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.ProducerEvent)
  })
_sym_db.RegisterMessage(ProducerEvent)

ConsumerEvent = _reflection.GeneratedProtocolMessageType('ConsumerEvent', (_message.Message,), {
  'DESCRIPTOR' : _CONSUMEREVENT,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.ConsumerEvent)
  })
_sym_db.RegisterMessage(ConsumerEvent)

PublishResult = _reflection.GeneratedProtocolMessageType('PublishResult', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHRESULT,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.PublishResult)
  })
_sym_db.RegisterMessage(PublishResult)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), {
  'DESCRIPTOR' : _ERROR,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.Error)
  })
_sym_db.RegisterMessage(Error)

FetchRequest = _reflection.GeneratedProtocolMessageType('FetchRequest', (_message.Message,), {
  'DESCRIPTOR' : _FETCHREQUEST,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.FetchRequest)
  })
_sym_db.RegisterMessage(FetchRequest)

FetchResponse = _reflection.GeneratedProtocolMessageType('FetchResponse', (_message.Message,), {
  'DESCRIPTOR' : _FETCHRESPONSE,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.FetchResponse)
  })
_sym_db.RegisterMessage(FetchResponse)

SchemaRequest = _reflection.GeneratedProtocolMessageType('SchemaRequest', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMAREQUEST,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.SchemaRequest)
  })
_sym_db.RegisterMessage(SchemaRequest)

SchemaInfo = _reflection.GeneratedProtocolMessageType('SchemaInfo', (_message.Message,), {
  'DESCRIPTOR' : _SCHEMAINFO,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.SchemaInfo)
  })
_sym_db.RegisterMessage(SchemaInfo)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

PublishResponse = _reflection.GeneratedProtocolMessageType('PublishResponse', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHRESPONSE,
  '__module__' : 'pubsub_api_pb2'
  # @@protoc_insertion_point(class_scope:eventbus.v1.PublishResponse)
  })
_sym_db.RegisterMessage(PublishResponse)

_PUBSUB = DESCRIPTOR.services_by_name['PubSub']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n com.salesforce.eventbus.protobufB\013PubSubProtoP\001Z4github.com/developerforce/pub-sub-api-pilot/go/proto'
  _ERRORCODE._serialized_start=1159
  _ERRORCODE._serialized_end=1196
  _REPLAYPRESET._serialized_start=1198
  _REPLAYPRESET._serialized_end=1250
  _TOPICINFO._serialized_start=34
  _TOPICINFO._serialized_end=165
  _TOPICREQUEST._serialized_start=167
  _TOPICREQUEST._serialized_end=201
  _EVENTHEADER._serialized_start=203
  _EVENTHEADER._serialized_end=244
  _PRODUCEREVENT._serialized_start=246
  _PRODUCEREVENT._serialized_end=352
  _CONSUMEREVENT._serialized_start=354
  _CONSUMEREVENT._serialized_end=431
  _PUBLISHRESULT._serialized_start=433
  _PUBLISHRESULT._serialized_end=502
  _ERROR._serialized_start=504
  _ERROR._serialized_end=562
  _FETCHREQUEST._serialized_start=565
  _FETCHREQUEST._serialized_end=713
  _FETCHRESPONSE._serialized_start=716
  _FETCHRESPONSE._serialized_end=848
  _SCHEMAREQUEST._serialized_start=850
  _SCHEMAREQUEST._serialized_end=884
  _SCHEMAINFO._serialized_start=886
  _SCHEMAINFO._serialized_end=954
  _PUBLISHREQUEST._serialized_start=956
  _PUBLISHREQUEST._serialized_end=1058
  _PUBLISHRESPONSE._serialized_start=1060
  _PUBLISHRESPONSE._serialized_end=1157
  _PUBSUB._serialized_start=1253
  _PUBSUB._serialized_end=1612
# @@protoc_insertion_point(module_scope)