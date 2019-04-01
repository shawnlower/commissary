# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/library.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/library.proto',
  package='proto',
  syntax='proto3',
  serialized_pb=_b('\n\x11\x61pi/library.proto\x12\x05proto\x1a\x1cgoogle/api/annotations.proto\"\x07\n\x05\x45mpty\"(\n\x0fVersionResponse\x12\x15\n\rVersionString\x18\x01 \x01(\t\"B\n\x04\x42ook\x12\x0c\n\x04ISBN\x18\x01 \x01(\t\x12\r\n\x05Title\x18\x02 \x01(\t\x12\x1d\n\x06\x61uthor\x18\x03 \x03(\x0b\x32\r.proto.Author\"?\n\x06\x41uthor\x12\x10\n\x08\x41uthorId\x18\x01 \x01(\r\x12\x11\n\tFirstName\x18\x02 \x01(\t\x12\x10\n\x08LastName\x18\x03 \x01(\t\"&\n\x05\x45rror\x12\x0c\n\x04\x43ode\x18\x01 \x01(\r\x12\x0f\n\x07Message\x18\x02 \x01(\t\".\n\x11\x43reateBookRequest\x12\x19\n\x04\x62ook\x18\x01 \x03(\x0b\x32\x0b.proto.Book\">\n\x12\x43reateBookResponse\x12\x1b\n\x05\x65rror\x18\x01 \x01(\x0b\x32\x0c.proto.Error\x12\x0b\n\x03IRI\x18\x02 \x01(\t\" \n\x11UpdateBookRequest\x12\x0b\n\x03IRI\x18\x01 \x01(\t\"/\n\x12UpdateBookResponse\x12\x19\n\x04item\x18\x01 \x01(\x0b\x32\x0b.proto.Book\"\x1d\n\x0eGetBookRequest\x12\x0b\n\x03IRI\x18\x01 \x01(\t\",\n\x0fGetBookResponse\x12\x19\n\x04item\x18\x01 \x01(\x0b\x32\x0b.proto.Book\" \n\x11\x44\x65leteBookRequest\x12\x0b\n\x03IRI\x18\x01 \x01(\t\"/\n\x12\x44\x65leteBookResponse\x12\x19\n\x04item\x18\x01 \x01(\x0b\x32\x0b.proto.Book2\xd1\x03\n\x03\x41PI\x12`\n\nCreateBook\x12\x18.proto.CreateBookRequest\x1a\x19.proto.CreateBookResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/api/CreateBook:\x01*\x12T\n\x07GetBook\x12\x15.proto.GetBookRequest\x1a\x16.proto.GetBookResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\"\x0f/v1/api/GetBook:\x01*\x12`\n\nUpdateBook\x12\x18.proto.UpdateBookRequest\x1a\x19.proto.UpdateBookResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/api/UpdateBook:\x01*\x12`\n\nDeleteBook\x12\x18.proto.DeleteBookRequest\x1a\x19.proto.DeleteBookResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/api/DeleteBook:\x01*\x12N\n\nGetVersion\x12\x0c.proto.Empty\x1a\x16.proto.VersionResponse\"\x1a\x82\xd3\xe4\x93\x02\x14\x12\x12/v1/api/GetVersionb\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='proto.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=65,
)


_VERSIONRESPONSE = _descriptor.Descriptor(
  name='VersionResponse',
  full_name='proto.VersionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='VersionString', full_name='proto.VersionResponse.VersionString', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=107,
)


_BOOK = _descriptor.Descriptor(
  name='Book',
  full_name='proto.Book',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ISBN', full_name='proto.Book.ISBN', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Title', full_name='proto.Book.Title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='proto.Book.author', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=175,
)


_AUTHOR = _descriptor.Descriptor(
  name='Author',
  full_name='proto.Author',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AuthorId', full_name='proto.Author.AuthorId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='FirstName', full_name='proto.Author.FirstName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='LastName', full_name='proto.Author.LastName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=240,
)


_ERROR = _descriptor.Descriptor(
  name='Error',
  full_name='proto.Error',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='Code', full_name='proto.Error.Code', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Message', full_name='proto.Error.Message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=242,
  serialized_end=280,
)


_CREATEBOOKREQUEST = _descriptor.Descriptor(
  name='CreateBookRequest',
  full_name='proto.CreateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='book', full_name='proto.CreateBookRequest.book', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=282,
  serialized_end=328,
)


_CREATEBOOKRESPONSE = _descriptor.Descriptor(
  name='CreateBookResponse',
  full_name='proto.CreateBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='error', full_name='proto.CreateBookResponse.error', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='IRI', full_name='proto.CreateBookResponse.IRI', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=330,
  serialized_end=392,
)


_UPDATEBOOKREQUEST = _descriptor.Descriptor(
  name='UpdateBookRequest',
  full_name='proto.UpdateBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='IRI', full_name='proto.UpdateBookRequest.IRI', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=394,
  serialized_end=426,
)


_UPDATEBOOKRESPONSE = _descriptor.Descriptor(
  name='UpdateBookResponse',
  full_name='proto.UpdateBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='proto.UpdateBookResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=428,
  serialized_end=475,
)


_GETBOOKREQUEST = _descriptor.Descriptor(
  name='GetBookRequest',
  full_name='proto.GetBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='IRI', full_name='proto.GetBookRequest.IRI', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=477,
  serialized_end=506,
)


_GETBOOKRESPONSE = _descriptor.Descriptor(
  name='GetBookResponse',
  full_name='proto.GetBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='proto.GetBookResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=508,
  serialized_end=552,
)


_DELETEBOOKREQUEST = _descriptor.Descriptor(
  name='DeleteBookRequest',
  full_name='proto.DeleteBookRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='IRI', full_name='proto.DeleteBookRequest.IRI', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=554,
  serialized_end=586,
)


_DELETEBOOKRESPONSE = _descriptor.Descriptor(
  name='DeleteBookResponse',
  full_name='proto.DeleteBookResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item', full_name='proto.DeleteBookResponse.item', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=635,
)

_BOOK.fields_by_name['author'].message_type = _AUTHOR
_CREATEBOOKREQUEST.fields_by_name['book'].message_type = _BOOK
_CREATEBOOKRESPONSE.fields_by_name['error'].message_type = _ERROR
_UPDATEBOOKRESPONSE.fields_by_name['item'].message_type = _BOOK
_GETBOOKRESPONSE.fields_by_name['item'].message_type = _BOOK
_DELETEBOOKRESPONSE.fields_by_name['item'].message_type = _BOOK
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['VersionResponse'] = _VERSIONRESPONSE
DESCRIPTOR.message_types_by_name['Book'] = _BOOK
DESCRIPTOR.message_types_by_name['Author'] = _AUTHOR
DESCRIPTOR.message_types_by_name['Error'] = _ERROR
DESCRIPTOR.message_types_by_name['CreateBookRequest'] = _CREATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['CreateBookResponse'] = _CREATEBOOKRESPONSE
DESCRIPTOR.message_types_by_name['UpdateBookRequest'] = _UPDATEBOOKREQUEST
DESCRIPTOR.message_types_by_name['UpdateBookResponse'] = _UPDATEBOOKRESPONSE
DESCRIPTOR.message_types_by_name['GetBookRequest'] = _GETBOOKREQUEST
DESCRIPTOR.message_types_by_name['GetBookResponse'] = _GETBOOKRESPONSE
DESCRIPTOR.message_types_by_name['DeleteBookRequest'] = _DELETEBOOKREQUEST
DESCRIPTOR.message_types_by_name['DeleteBookResponse'] = _DELETEBOOKRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.Empty)
  ))
_sym_db.RegisterMessage(Empty)

VersionResponse = _reflection.GeneratedProtocolMessageType('VersionResponse', (_message.Message,), dict(
  DESCRIPTOR = _VERSIONRESPONSE,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.VersionResponse)
  ))
_sym_db.RegisterMessage(VersionResponse)

Book = _reflection.GeneratedProtocolMessageType('Book', (_message.Message,), dict(
  DESCRIPTOR = _BOOK,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.Book)
  ))
_sym_db.RegisterMessage(Book)

Author = _reflection.GeneratedProtocolMessageType('Author', (_message.Message,), dict(
  DESCRIPTOR = _AUTHOR,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.Author)
  ))
_sym_db.RegisterMessage(Author)

Error = _reflection.GeneratedProtocolMessageType('Error', (_message.Message,), dict(
  DESCRIPTOR = _ERROR,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.Error)
  ))
_sym_db.RegisterMessage(Error)

CreateBookRequest = _reflection.GeneratedProtocolMessageType('CreateBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _CREATEBOOKREQUEST,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.CreateBookRequest)
  ))
_sym_db.RegisterMessage(CreateBookRequest)

CreateBookResponse = _reflection.GeneratedProtocolMessageType('CreateBookResponse', (_message.Message,), dict(
  DESCRIPTOR = _CREATEBOOKRESPONSE,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.CreateBookResponse)
  ))
_sym_db.RegisterMessage(CreateBookResponse)

UpdateBookRequest = _reflection.GeneratedProtocolMessageType('UpdateBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEBOOKREQUEST,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdateBookRequest)
  ))
_sym_db.RegisterMessage(UpdateBookRequest)

UpdateBookResponse = _reflection.GeneratedProtocolMessageType('UpdateBookResponse', (_message.Message,), dict(
  DESCRIPTOR = _UPDATEBOOKRESPONSE,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.UpdateBookResponse)
  ))
_sym_db.RegisterMessage(UpdateBookResponse)

GetBookRequest = _reflection.GeneratedProtocolMessageType('GetBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETBOOKREQUEST,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBookRequest)
  ))
_sym_db.RegisterMessage(GetBookRequest)

GetBookResponse = _reflection.GeneratedProtocolMessageType('GetBookResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETBOOKRESPONSE,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.GetBookResponse)
  ))
_sym_db.RegisterMessage(GetBookResponse)

DeleteBookRequest = _reflection.GeneratedProtocolMessageType('DeleteBookRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEBOOKREQUEST,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteBookRequest)
  ))
_sym_db.RegisterMessage(DeleteBookRequest)

DeleteBookResponse = _reflection.GeneratedProtocolMessageType('DeleteBookResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEBOOKRESPONSE,
  __module__ = 'api.library_pb2'
  # @@protoc_insertion_point(class_scope:proto.DeleteBookResponse)
  ))
_sym_db.RegisterMessage(DeleteBookResponse)



_API = _descriptor.ServiceDescriptor(
  name='API',
  full_name='proto.API',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=638,
  serialized_end=1103,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateBook',
    full_name='proto.API.CreateBook',
    index=0,
    containing_service=None,
    input_type=_CREATEBOOKREQUEST,
    output_type=_CREATEBOOKRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\"\022/v1/api/CreateBook:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='GetBook',
    full_name='proto.API.GetBook',
    index=1,
    containing_service=None,
    input_type=_GETBOOKREQUEST,
    output_type=_GETBOOKRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\024\"\017/v1/api/GetBook:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateBook',
    full_name='proto.API.UpdateBook',
    index=2,
    containing_service=None,
    input_type=_UPDATEBOOKREQUEST,
    output_type=_UPDATEBOOKRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\"\022/v1/api/UpdateBook:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteBook',
    full_name='proto.API.DeleteBook',
    index=3,
    containing_service=None,
    input_type=_DELETEBOOKREQUEST,
    output_type=_DELETEBOOKRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\027\"\022/v1/api/DeleteBook:\001*')),
  ),
  _descriptor.MethodDescriptor(
    name='GetVersion',
    full_name='proto.API.GetVersion',
    index=4,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_VERSIONRESPONSE,
    options=_descriptor._ParseOptions(descriptor_pb2.MethodOptions(), _b('\202\323\344\223\002\024\022\022/v1/api/GetVersion')),
  ),
])
_sym_db.RegisterServiceDescriptor(_API)

DESCRIPTOR.services_by_name['API'] = _API

# @@protoc_insertion_point(module_scope)