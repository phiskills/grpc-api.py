# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: example.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='example.proto',
  package='example',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\rexample.proto\x12\x07\x65xample\"\x18\n\x07Request\x12\r\n\x05value\x18\x01 \x01(\t\"\x19\n\x08Response\x12\r\n\x05value\x18\x01 \x01(\t2\xe6\x01\n\x07Service\x12-\n\x06Simple\x12\x10.example.Request\x1a\x11.example.Response\x12\x35\n\x0cServerStream\x12\x10.example.Request\x1a\x11.example.Response0\x01\x12\x35\n\x0c\x43lientStream\x12\x10.example.Request\x1a\x11.example.Response(\x01\x12>\n\x13\x42idirectionalStream\x12\x10.example.Request\x1a\x11.example.Response(\x01\x30\x01\x62\x06proto3'
)




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='example.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='example.Request.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=50,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='example.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='example.Response.value', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=52,
  serialized_end=77,
)

DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Request)
  })
_sym_db.RegisterMessage(Request)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'example_pb2'
  # @@protoc_insertion_point(class_scope:example.Response)
  })
_sym_db.RegisterMessage(Response)



_SERVICE = _descriptor.ServiceDescriptor(
  name='Service',
  full_name='example.Service',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=80,
  serialized_end=310,
  methods=[
  _descriptor.MethodDescriptor(
    name='Simple',
    full_name='example.Service.Simple',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ServerStream',
    full_name='example.Service.ServerStream',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ClientStream',
    full_name='example.Service.ClientStream',
    index=2,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='BidirectionalStream',
    full_name='example.Service.BidirectionalStream',
    index=3,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_SERVICE)

DESCRIPTOR.services_by_name['Service'] = _SERVICE

# @@protoc_insertion_point(module_scope)
