# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gogo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ngogo.proto\x12\tgogoproto\x1a google/protobuf/descriptor.proto:;\n\x13goproto_enum_prefix\x12\x1c.google.protobuf.EnumOptions\x18\xb1\xe4\x03 \x01(\x08:=\n\x15goproto_enum_stringer\x12\x1c.google.protobuf.EnumOptions\x18\xc5\xe4\x03 \x01(\x08:5\n\renum_stringer\x12\x1c.google.protobuf.EnumOptions\x18\xc6\xe4\x03 \x01(\x08:7\n\x0f\x65num_customname\x12\x1c.google.protobuf.EnumOptions\x18\xc7\xe4\x03 \x01(\t:0\n\x08\x65numdecl\x12\x1c.google.protobuf.EnumOptions\x18\xc8\xe4\x03 \x01(\x08:A\n\x14\x65numvalue_customname\x12!.google.protobuf.EnumValueOptions\x18\xd1\x83\x04 \x01(\t:;\n\x13goproto_getters_all\x12\x1c.google.protobuf.FileOptions\x18\x99\xec\x03 \x01(\x08:?\n\x17goproto_enum_prefix_all\x12\x1c.google.protobuf.FileOptions\x18\x9a\xec\x03 \x01(\x08:<\n\x14goproto_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\x9b\xec\x03 \x01(\x08:9\n\x11verbose_equal_all\x12\x1c.google.protobuf.FileOptions\x18\x9c\xec\x03 \x01(\x08:0\n\x08\x66\x61\x63\x65_all\x12\x1c.google.protobuf.FileOptions\x18\x9d\xec\x03 \x01(\x08:4\n\x0cgostring_all\x12\x1c.google.protobuf.FileOptions\x18\x9e\xec\x03 \x01(\x08:4\n\x0cpopulate_all\x12\x1c.google.protobuf.FileOptions\x18\x9f\xec\x03 \x01(\x08:4\n\x0cstringer_all\x12\x1c.google.protobuf.FileOptions\x18\xa0\xec\x03 \x01(\x08:3\n\x0bonlyone_all\x12\x1c.google.protobuf.FileOptions\x18\xa1\xec\x03 \x01(\x08:1\n\tequal_all\x12\x1c.google.protobuf.FileOptions\x18\xa5\xec\x03 \x01(\x08:7\n\x0f\x64\x65scription_all\x12\x1c.google.protobuf.FileOptions\x18\xa6\xec\x03 \x01(\x08:3\n\x0btestgen_all\x12\x1c.google.protobuf.FileOptions\x18\xa7\xec\x03 \x01(\x08:4\n\x0c\x62\x65nchgen_all\x12\x1c.google.protobuf.FileOptions\x18\xa8\xec\x03 \x01(\x08:5\n\rmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xa9\xec\x03 \x01(\x08:7\n\x0funmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xaa\xec\x03 \x01(\x08:<\n\x14stable_marshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xab\xec\x03 \x01(\x08:1\n\tsizer_all\x12\x1c.google.protobuf.FileOptions\x18\xac\xec\x03 \x01(\x08:A\n\x19goproto_enum_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\xad\xec\x03 \x01(\x08:9\n\x11\x65num_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\xae\xec\x03 \x01(\x08:<\n\x14unsafe_marshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xaf\xec\x03 \x01(\x08:>\n\x16unsafe_unmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xb0\xec\x03 \x01(\x08:B\n\x1agoproto_extensions_map_all\x12\x1c.google.protobuf.FileOptions\x18\xb1\xec\x03 \x01(\x08:@\n\x18goproto_unrecognized_all\x12\x1c.google.protobuf.FileOptions\x18\xb2\xec\x03 \x01(\x08:8\n\x10gogoproto_import\x12\x1c.google.protobuf.FileOptions\x18\xb3\xec\x03 \x01(\x08:6\n\x0eprotosizer_all\x12\x1c.google.protobuf.FileOptions\x18\xb4\xec\x03 \x01(\x08:3\n\x0b\x63ompare_all\x12\x1c.google.protobuf.FileOptions\x18\xb5\xec\x03 \x01(\x08:4\n\x0ctypedecl_all\x12\x1c.google.protobuf.FileOptions\x18\xb6\xec\x03 \x01(\x08:4\n\x0c\x65numdecl_all\x12\x1c.google.protobuf.FileOptions\x18\xb7\xec\x03 \x01(\x08:<\n\x14goproto_registration\x12\x1c.google.protobuf.FileOptions\x18\xb8\xec\x03 \x01(\x08:7\n\x0fmessagename_all\x12\x1c.google.protobuf.FileOptions\x18\xb9\xec\x03 \x01(\x08:=\n\x15goproto_sizecache_all\x12\x1c.google.protobuf.FileOptions\x18\xba\xec\x03 \x01(\x08:;\n\x13goproto_unkeyed_all\x12\x1c.google.protobuf.FileOptions\x18\xbb\xec\x03 \x01(\x08::\n\x0fgoproto_getters\x12\x1f.google.protobuf.MessageOptions\x18\x81\xf4\x03 \x01(\x08:;\n\x10goproto_stringer\x12\x1f.google.protobuf.MessageOptions\x18\x83\xf4\x03 \x01(\x08:8\n\rverbose_equal\x12\x1f.google.protobuf.MessageOptions\x18\x84\xf4\x03 \x01(\x08:/\n\x04\x66\x61\x63\x65\x12\x1f.google.protobuf.MessageOptions\x18\x85\xf4\x03 \x01(\x08:3\n\x08gostring\x12\x1f.google.protobuf.MessageOptions\x18\x86\xf4\x03 \x01(\x08:3\n\x08populate\x12\x1f.google.protobuf.MessageOptions\x18\x87\xf4\x03 \x01(\x08:3\n\x08stringer\x12\x1f.google.protobuf.MessageOptions\x18\xc0\x8b\x04 \x01(\x08:2\n\x07onlyone\x12\x1f.google.protobuf.MessageOptions\x18\x89\xf4\x03 \x01(\x08:0\n\x05\x65qual\x12\x1f.google.protobuf.MessageOptions\x18\x8d\xf4\x03 \x01(\x08:6\n\x0b\x64\x65scription\x12\x1f.google.protobuf.MessageOptions\x18\x8e\xf4\x03 \x01(\x08:2\n\x07testgen\x12\x1f.google.protobuf.MessageOptions\x18\x8f\xf4\x03 \x01(\x08:3\n\x08\x62\x65nchgen\x12\x1f.google.protobuf.MessageOptions\x18\x90\xf4\x03 \x01(\x08:4\n\tmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x91\xf4\x03 \x01(\x08:6\n\x0bunmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x92\xf4\x03 \x01(\x08:;\n\x10stable_marshaler\x12\x1f.google.protobuf.MessageOptions\x18\x93\xf4\x03 \x01(\x08:0\n\x05sizer\x12\x1f.google.protobuf.MessageOptions\x18\x94\xf4\x03 \x01(\x08:;\n\x10unsafe_marshaler\x12\x1f.google.protobuf.MessageOptions\x18\x97\xf4\x03 \x01(\x08:=\n\x12unsafe_unmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x98\xf4\x03 \x01(\x08:A\n\x16goproto_extensions_map\x12\x1f.google.protobuf.MessageOptions\x18\x99\xf4\x03 \x01(\x08:?\n\x14goproto_unrecognized\x12\x1f.google.protobuf.MessageOptions\x18\x9a\xf4\x03 \x01(\x08:5\n\nprotosizer\x12\x1f.google.protobuf.MessageOptions\x18\x9c\xf4\x03 \x01(\x08:2\n\x07\x63ompare\x12\x1f.google.protobuf.MessageOptions\x18\x9d\xf4\x03 \x01(\x08:3\n\x08typedecl\x12\x1f.google.protobuf.MessageOptions\x18\x9e\xf4\x03 \x01(\x08:6\n\x0bmessagename\x12\x1f.google.protobuf.MessageOptions\x18\xa1\xf4\x03 \x01(\x08:<\n\x11goproto_sizecache\x12\x1f.google.protobuf.MessageOptions\x18\xa2\xf4\x03 \x01(\x08::\n\x0fgoproto_unkeyed\x12\x1f.google.protobuf.MessageOptions\x18\xa3\xf4\x03 \x01(\x08:1\n\x08nullable\x12\x1d.google.protobuf.FieldOptions\x18\xe9\xfb\x03 \x01(\x08:.\n\x05\x65mbed\x12\x1d.google.protobuf.FieldOptions\x18\xea\xfb\x03 \x01(\x08:3\n\ncustomtype\x12\x1d.google.protobuf.FieldOptions\x18\xeb\xfb\x03 \x01(\t:3\n\ncustomname\x12\x1d.google.protobuf.FieldOptions\x18\xec\xfb\x03 \x01(\t:0\n\x07jsontag\x12\x1d.google.protobuf.FieldOptions\x18\xed\xfb\x03 \x01(\t:1\n\x08moretags\x12\x1d.google.protobuf.FieldOptions\x18\xee\xfb\x03 \x01(\t:1\n\x08\x63\x61sttype\x12\x1d.google.protobuf.FieldOptions\x18\xef\xfb\x03 \x01(\t:0\n\x07\x63\x61stkey\x12\x1d.google.protobuf.FieldOptions\x18\xf0\xfb\x03 \x01(\t:2\n\tcastvalue\x12\x1d.google.protobuf.FieldOptions\x18\xf1\xfb\x03 \x01(\t:0\n\x07stdtime\x12\x1d.google.protobuf.FieldOptions\x18\xf2\xfb\x03 \x01(\x08:4\n\x0bstdduration\x12\x1d.google.protobuf.FieldOptions\x18\xf3\xfb\x03 \x01(\x08:3\n\nwktpointer\x12\x1d.google.protobuf.FieldOptions\x18\xf4\xfb\x03 \x01(\x08:5\n\x0c\x63\x61strepeated\x12\x1d.google.protobuf.FieldOptions\x18\xf5\xfb\x03 \x01(\tBH\n\x13\x63om.google.protobufB\nGoGoProtosZ%github.com/cosmos/gogoproto/gogoproto')


GOPROTO_ENUM_PREFIX_FIELD_NUMBER = 62001
goproto_enum_prefix = DESCRIPTOR.extensions_by_name['goproto_enum_prefix']
GOPROTO_ENUM_STRINGER_FIELD_NUMBER = 62021
goproto_enum_stringer = DESCRIPTOR.extensions_by_name['goproto_enum_stringer']
ENUM_STRINGER_FIELD_NUMBER = 62022
enum_stringer = DESCRIPTOR.extensions_by_name['enum_stringer']
ENUM_CUSTOMNAME_FIELD_NUMBER = 62023
enum_customname = DESCRIPTOR.extensions_by_name['enum_customname']
ENUMDECL_FIELD_NUMBER = 62024
enumdecl = DESCRIPTOR.extensions_by_name['enumdecl']
ENUMVALUE_CUSTOMNAME_FIELD_NUMBER = 66001
enumvalue_customname = DESCRIPTOR.extensions_by_name['enumvalue_customname']
GOPROTO_GETTERS_ALL_FIELD_NUMBER = 63001
goproto_getters_all = DESCRIPTOR.extensions_by_name['goproto_getters_all']
GOPROTO_ENUM_PREFIX_ALL_FIELD_NUMBER = 63002
goproto_enum_prefix_all = DESCRIPTOR.extensions_by_name['goproto_enum_prefix_all']
GOPROTO_STRINGER_ALL_FIELD_NUMBER = 63003
goproto_stringer_all = DESCRIPTOR.extensions_by_name['goproto_stringer_all']
VERBOSE_EQUAL_ALL_FIELD_NUMBER = 63004
verbose_equal_all = DESCRIPTOR.extensions_by_name['verbose_equal_all']
FACE_ALL_FIELD_NUMBER = 63005
face_all = DESCRIPTOR.extensions_by_name['face_all']
GOSTRING_ALL_FIELD_NUMBER = 63006
gostring_all = DESCRIPTOR.extensions_by_name['gostring_all']
POPULATE_ALL_FIELD_NUMBER = 63007
populate_all = DESCRIPTOR.extensions_by_name['populate_all']
STRINGER_ALL_FIELD_NUMBER = 63008
stringer_all = DESCRIPTOR.extensions_by_name['stringer_all']
ONLYONE_ALL_FIELD_NUMBER = 63009
onlyone_all = DESCRIPTOR.extensions_by_name['onlyone_all']
EQUAL_ALL_FIELD_NUMBER = 63013
equal_all = DESCRIPTOR.extensions_by_name['equal_all']
DESCRIPTION_ALL_FIELD_NUMBER = 63014
description_all = DESCRIPTOR.extensions_by_name['description_all']
TESTGEN_ALL_FIELD_NUMBER = 63015
testgen_all = DESCRIPTOR.extensions_by_name['testgen_all']
BENCHGEN_ALL_FIELD_NUMBER = 63016
benchgen_all = DESCRIPTOR.extensions_by_name['benchgen_all']
MARSHALER_ALL_FIELD_NUMBER = 63017
marshaler_all = DESCRIPTOR.extensions_by_name['marshaler_all']
UNMARSHALER_ALL_FIELD_NUMBER = 63018
unmarshaler_all = DESCRIPTOR.extensions_by_name['unmarshaler_all']
STABLE_MARSHALER_ALL_FIELD_NUMBER = 63019
stable_marshaler_all = DESCRIPTOR.extensions_by_name['stable_marshaler_all']
SIZER_ALL_FIELD_NUMBER = 63020
sizer_all = DESCRIPTOR.extensions_by_name['sizer_all']
GOPROTO_ENUM_STRINGER_ALL_FIELD_NUMBER = 63021
goproto_enum_stringer_all = DESCRIPTOR.extensions_by_name['goproto_enum_stringer_all']
ENUM_STRINGER_ALL_FIELD_NUMBER = 63022
enum_stringer_all = DESCRIPTOR.extensions_by_name['enum_stringer_all']
UNSAFE_MARSHALER_ALL_FIELD_NUMBER = 63023
unsafe_marshaler_all = DESCRIPTOR.extensions_by_name['unsafe_marshaler_all']
UNSAFE_UNMARSHALER_ALL_FIELD_NUMBER = 63024
unsafe_unmarshaler_all = DESCRIPTOR.extensions_by_name['unsafe_unmarshaler_all']
GOPROTO_EXTENSIONS_MAP_ALL_FIELD_NUMBER = 63025
goproto_extensions_map_all = DESCRIPTOR.extensions_by_name['goproto_extensions_map_all']
GOPROTO_UNRECOGNIZED_ALL_FIELD_NUMBER = 63026
goproto_unrecognized_all = DESCRIPTOR.extensions_by_name['goproto_unrecognized_all']
GOGOPROTO_IMPORT_FIELD_NUMBER = 63027
gogoproto_import = DESCRIPTOR.extensions_by_name['gogoproto_import']
PROTOSIZER_ALL_FIELD_NUMBER = 63028
protosizer_all = DESCRIPTOR.extensions_by_name['protosizer_all']
COMPARE_ALL_FIELD_NUMBER = 63029
compare_all = DESCRIPTOR.extensions_by_name['compare_all']
TYPEDECL_ALL_FIELD_NUMBER = 63030
typedecl_all = DESCRIPTOR.extensions_by_name['typedecl_all']
ENUMDECL_ALL_FIELD_NUMBER = 63031
enumdecl_all = DESCRIPTOR.extensions_by_name['enumdecl_all']
GOPROTO_REGISTRATION_FIELD_NUMBER = 63032
goproto_registration = DESCRIPTOR.extensions_by_name['goproto_registration']
MESSAGENAME_ALL_FIELD_NUMBER = 63033
messagename_all = DESCRIPTOR.extensions_by_name['messagename_all']
GOPROTO_SIZECACHE_ALL_FIELD_NUMBER = 63034
goproto_sizecache_all = DESCRIPTOR.extensions_by_name['goproto_sizecache_all']
GOPROTO_UNKEYED_ALL_FIELD_NUMBER = 63035
goproto_unkeyed_all = DESCRIPTOR.extensions_by_name['goproto_unkeyed_all']
GOPROTO_GETTERS_FIELD_NUMBER = 64001
goproto_getters = DESCRIPTOR.extensions_by_name['goproto_getters']
GOPROTO_STRINGER_FIELD_NUMBER = 64003
goproto_stringer = DESCRIPTOR.extensions_by_name['goproto_stringer']
VERBOSE_EQUAL_FIELD_NUMBER = 64004
verbose_equal = DESCRIPTOR.extensions_by_name['verbose_equal']
FACE_FIELD_NUMBER = 64005
face = DESCRIPTOR.extensions_by_name['face']
GOSTRING_FIELD_NUMBER = 64006
gostring = DESCRIPTOR.extensions_by_name['gostring']
POPULATE_FIELD_NUMBER = 64007
populate = DESCRIPTOR.extensions_by_name['populate']
STRINGER_FIELD_NUMBER = 67008
stringer = DESCRIPTOR.extensions_by_name['stringer']
ONLYONE_FIELD_NUMBER = 64009
onlyone = DESCRIPTOR.extensions_by_name['onlyone']
EQUAL_FIELD_NUMBER = 64013
equal = DESCRIPTOR.extensions_by_name['equal']
DESCRIPTION_FIELD_NUMBER = 64014
description = DESCRIPTOR.extensions_by_name['description']
TESTGEN_FIELD_NUMBER = 64015
testgen = DESCRIPTOR.extensions_by_name['testgen']
BENCHGEN_FIELD_NUMBER = 64016
benchgen = DESCRIPTOR.extensions_by_name['benchgen']
MARSHALER_FIELD_NUMBER = 64017
marshaler = DESCRIPTOR.extensions_by_name['marshaler']
UNMARSHALER_FIELD_NUMBER = 64018
unmarshaler = DESCRIPTOR.extensions_by_name['unmarshaler']
STABLE_MARSHALER_FIELD_NUMBER = 64019
stable_marshaler = DESCRIPTOR.extensions_by_name['stable_marshaler']
SIZER_FIELD_NUMBER = 64020
sizer = DESCRIPTOR.extensions_by_name['sizer']
UNSAFE_MARSHALER_FIELD_NUMBER = 64023
unsafe_marshaler = DESCRIPTOR.extensions_by_name['unsafe_marshaler']
UNSAFE_UNMARSHALER_FIELD_NUMBER = 64024
unsafe_unmarshaler = DESCRIPTOR.extensions_by_name['unsafe_unmarshaler']
GOPROTO_EXTENSIONS_MAP_FIELD_NUMBER = 64025
goproto_extensions_map = DESCRIPTOR.extensions_by_name['goproto_extensions_map']
GOPROTO_UNRECOGNIZED_FIELD_NUMBER = 64026
goproto_unrecognized = DESCRIPTOR.extensions_by_name['goproto_unrecognized']
PROTOSIZER_FIELD_NUMBER = 64028
protosizer = DESCRIPTOR.extensions_by_name['protosizer']
COMPARE_FIELD_NUMBER = 64029
compare = DESCRIPTOR.extensions_by_name['compare']
TYPEDECL_FIELD_NUMBER = 64030
typedecl = DESCRIPTOR.extensions_by_name['typedecl']
MESSAGENAME_FIELD_NUMBER = 64033
messagename = DESCRIPTOR.extensions_by_name['messagename']
GOPROTO_SIZECACHE_FIELD_NUMBER = 64034
goproto_sizecache = DESCRIPTOR.extensions_by_name['goproto_sizecache']
GOPROTO_UNKEYED_FIELD_NUMBER = 64035
goproto_unkeyed = DESCRIPTOR.extensions_by_name['goproto_unkeyed']
NULLABLE_FIELD_NUMBER = 65001
nullable = DESCRIPTOR.extensions_by_name['nullable']
EMBED_FIELD_NUMBER = 65002
embed = DESCRIPTOR.extensions_by_name['embed']
CUSTOMTYPE_FIELD_NUMBER = 65003
customtype = DESCRIPTOR.extensions_by_name['customtype']
CUSTOMNAME_FIELD_NUMBER = 65004
customname = DESCRIPTOR.extensions_by_name['customname']
JSONTAG_FIELD_NUMBER = 65005
jsontag = DESCRIPTOR.extensions_by_name['jsontag']
MORETAGS_FIELD_NUMBER = 65006
moretags = DESCRIPTOR.extensions_by_name['moretags']
CASTTYPE_FIELD_NUMBER = 65007
casttype = DESCRIPTOR.extensions_by_name['casttype']
CASTKEY_FIELD_NUMBER = 65008
castkey = DESCRIPTOR.extensions_by_name['castkey']
CASTVALUE_FIELD_NUMBER = 65009
castvalue = DESCRIPTOR.extensions_by_name['castvalue']
STDTIME_FIELD_NUMBER = 65010
stdtime = DESCRIPTOR.extensions_by_name['stdtime']
STDDURATION_FIELD_NUMBER = 65011
stdduration = DESCRIPTOR.extensions_by_name['stdduration']
WKTPOINTER_FIELD_NUMBER = 65012
wktpointer = DESCRIPTOR.extensions_by_name['wktpointer']
CASTREPEATED_FIELD_NUMBER = 65013
castrepeated = DESCRIPTOR.extensions_by_name['castrepeated']

if _descriptor._USE_C_DESCRIPTORS == False:
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(goproto_enum_prefix)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(goproto_enum_stringer)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_stringer)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_customname)
  google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enumdecl)
  google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enumvalue_customname)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_getters_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_enum_prefix_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_stringer_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(verbose_equal_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(face_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(gostring_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(populate_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(stringer_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(onlyone_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(equal_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(description_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(testgen_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(benchgen_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(marshaler_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unmarshaler_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(stable_marshaler_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(sizer_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_enum_stringer_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(enum_stringer_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unsafe_marshaler_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unsafe_unmarshaler_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_extensions_map_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_unrecognized_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(gogoproto_import)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(protosizer_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(compare_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(typedecl_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(enumdecl_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_registration)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(messagename_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_sizecache_all)
  google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_unkeyed_all)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_getters)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_stringer)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(verbose_equal)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(face)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(gostring)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(populate)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(stringer)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(onlyone)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(equal)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(description)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(testgen)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(benchgen)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(marshaler)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unmarshaler)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(stable_marshaler)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(sizer)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unsafe_marshaler)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unsafe_unmarshaler)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_extensions_map)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_unrecognized)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(protosizer)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(compare)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(typedecl)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(messagename)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_sizecache)
  google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_unkeyed)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nullable)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(embed)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(customtype)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(customname)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(jsontag)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(moretags)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(casttype)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castkey)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castvalue)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stdtime)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stdduration)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(wktpointer)
  google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castrepeated)

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\023com.google.protobufB\nGoGoProtosZ%github.com/cosmos/gogoproto/gogoproto'
# @@protoc_insertion_point(module_scope)
