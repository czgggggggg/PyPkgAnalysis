import bupt.src.util.MetadataUtil
from bupt.src.util.MetadataUtil import *

metadataUtil = MetadataUtil("test")

json_content = metadataUtil.get_metadata("numpy")
print(json_content)

author_info = metadataUtil.get_author("numpy")
print(author_info)
author_info = metadataUtil.get_author("django")
print(author_info)
author_info = metadataUtil.get_author("panda")
print(author_info)

version_date = metadataUtil.get_versions("numpy")
print(version_date)