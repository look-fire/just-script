#!/usr/bin/python
# -*- coding: utf8 -*-
"""
lib of http wrappers for gerrit rest api
check "gerrit_rest_api_demo.py" for usage reference
"""

import base64
import cStringIO
import json
import os
import urllib
import requests
from requests.auth import HTTPDigestAuth

# can be customized
TIMEOUT = 10


# GERRIT INFO CLASSES
class TaskSummaryInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-config.html#task-summary-info
    """
    def __init__(self, total=None, running=None, ready=None, sleeping=None):
        self.total = total
        self.running = running
        self.ready = ready
        self.sleeping = sleeping

    @classmethod
    def from_dict(cls, dict_):
        return cls(total=dict_.get('total', None),
                   running=dict_.get('running', None),
                   ready=dict_.get('ready', None),
                   sleeping=dict_.get('sleeping', None),)

    def __repr__(self):
        return '<TaskSummaryInfo()>'


class MemSummaryInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-config.html#mem-summary-info
    """
    def __init__(self, total, used, free, buffers, max_, open_files=None):
        self.total = total
        self.used = used
        self.free = free
        self.buffers = buffers
        self.max_ = max_
        self.open_files = open_files

    @classmethod
    def from_dict(cls, dict_):
        return cls(total=dict_.get('total', None),
                   used=dict_.get('used', None),
                   free=dict_.get('free', None),
                   buffers=dict_.get('buffers', None),
                   max_=dict_.get('max', None),
                   open_files=dict_.get('open_files', None),)

    def __repr__(self):
        return '<MemSummaryInfo()>'


class ThreadSummaryInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-config.html#thread-summary-info
    """
    def __init__(self, cpus, threads, counts):
        self.cpus = cpus
        self.threads = threads
        self.counts = counts

    @classmethod
    def from_dict(cls, dict_):
        return cls(cpus=dict_.get('cpus', None),
                   threads=dict_.get('threads', None),
                   counts=dict_.get('counts', None))

    def __repr__(self):
        return '<ThreadSummaryInfo()>'


class JvmSummaryInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-config.html#jvm-summary-info
    parsed output example:
        {u'jvm_summary': {u'current_working_directory': u'/home/xxx/review_site',
                          u'host': u'xxx',
                          u'os_arch': u'amd64',
                          u'os_name': u'Linux',
                          u'os_version': u'3.11.0-15-generic',
                          u'site': u'/home/xxx/review_site',
                          u'user': u'xxx',
                          u'vm_name': u'OpenJDK 64-Bit Server VM',
                          u'vm_vendor': u'Oracle Corporation',
                          u'vm_version': u'24.111-b01'},
         u'mem_summary': {u'buffers': u'10.00m',
                          u'free': u'2.91g',
                          u'max': u'6.97g',
                          u'open_files': 2,
                          u'total': u'4.16g',
                          u'used': u'1.24g'},
         u'task_summary': {u'running': 4, u'sleeping': 1, u'total': 5},
         u'thread_summary': {u'counts': {u'HTTP': {u'RUNNABLE': 3,
                                                   u'TIMED_WAITING': 8},
                                         u'Other': {u'RUNNABLE': 29,
                                                    u'TIMED_WAITING': 28,
                                                    u'WAITING': 44},
                                         u'ReceiveCommits': {u'WAITING': 32},
                                         u'SSH git-upload-pack': {u'RUNNABLE': 1,
                                                                  u'WAITING': 3},
                                         u'SSH-Interactive-Worker': {u'WAITING': 42},
                                         u'SshCommandStart': {u'WAITING': 2}},
                             u'cpus': 32,
                             u'threads': 192}}
    """
    def __init__(self, vm_vendor, vm_name, vm_version, os_name, os_version, os_arch,
                 user, current_working_directory, site, host=None):
        self.vm_vendor = vm_vendor
        self.vm_name = vm_name
        self.vm_version = vm_version
        self.os_name = os_name
        self.os_version = os_version
        self.os_arch = os_arch
        self.user = user
        self.current_working_directory = current_working_directory
        self.site = site
        self.host = host

    @classmethod
    def from_dict(cls, dict_):
        return cls(vm_vendor=dict_.get('vm_vendor', None),
                   vm_name=dict_.get('vm_name', None),
                   vm_version=dict_.get('vm_version', None),
                   os_name=dict_.get('os_name', None),
                   os_version=dict_.get('os_version', None),
                   os_arch=dict_.get('os_arch', None),
                   user=dict_.get('user', None),
                   current_working_directory=dict_.get('current_working_directory', None),
                   site=dict_.get('site', None),
                   host=dict_.get('host', None))

    def __repr__(self):
        return '<JvmSummaryInfo()>'


class SummaryInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-config.html#summary-info
    """
    def __init__(self, task_summary, mem_summary, thread_summary, jvm_summary=None):
        self.task_summary = task_summary
        self.mem_summary = mem_summary
        self.thread_summary = thread_summary
        self.jvm_summary = jvm_summary

    @classmethod
    def from_dict(cls, dict_):
        return cls(task_summary=TaskSummaryInfo.from_dict(dict_.get('task_summary', {})),
                   mem_summary=MemSummaryInfo.from_dict(dict_.get('mem_summary', {})),
                   thread_summary=ThreadSummaryInfo.from_dict(dict_.get('thread_summary', {})),
                   jvm_summary=JvmSummaryInfo.from_dict(dict_.get('jvm_summary', {})))

    def __repr__(self):
        return '<SummaryInfo()>'


class ProjectInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-projects.html#project-info
    parsed output example:
        {u'id': u'HIOSN%2Fvendor%2Ftecno%2Fpackages',
         u'name': u'HIOSN/vendor/tecno/packages',
         u'parent': u'All-Projects',
         u'state': u'ACTIVE'}
    """
    def __init__(self, name, id_=None, parent=None, description=None,
                 state=None, branches=None, web_links=None):
        self.id_ = id_
        self.name = name
        self.parent = parent
        self.description = description
        self.state = state
        self.branches = branches
        self.web_links = web_links

    @classmethod
    def from_dict(cls, dict_):
        return cls(id_=dict_.get('id', None),
                   name=dict_.get('name', None),
                   parent=dict_.get('parent', None),
                   description=dict_.get('description', None),
                   state=dict_.get('state', None),
                   branches=dict_.get('branches', None),
                   web_links=dict_.get('web_links', None))

    def __repr__(self):
        return repr({k:v for k, v in self.__dict__.iteritems() if v is not None})


class BranchInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-projects.html#branch-info
    parsed output example:
        {u'ref': u'refs/heads/master',
         u'revision': u'8fc7d10675a7f76642d1248bff5b5893c993b118'}
    """
    def __init__(self, ref, revision, can_delete=None, web_links=None):
        self.ref = ref
        self.revision = revision
        self.can_delete = can_delete
        self.web_links = web_links

    @classmethod
    def from_dict(cls, dict_):
        return cls(ref=dict_.get('ref', None),
                   revision=dict_.get('revision', None),
                   can_delete=dict_.get('can_delete', None),
                   web_links=dict_.get('web_links', None))

    def __repr__(self):
        return '<BranchInfo[ref:{0} revision:{1}]>'.format(self.ref, self.revision)


class TagInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-projects.html#tag-info
    parsed output example:
        {u'message': u'tag before change CXLite_H3713_HiOS2.0.0_N branch base to E31_H375_HiOS2.0.0_N_DEV.xml',
         u'object': u'f448fedb534efc74501306cedc287d229479794c',
         u'ref': u'refs/tags/CXLite_H3713_HiOS2.0.0_N_BEFORE_TAG_20161217',
         u'revision': u'3b9ad67ba003908ba1e6790488c909522cc9d960',
         u'tagger': {u'date': u'2016-12-17 08:15:44.000000000',
                     u'email': u'haobin.zhang@reallytek.com',
                     u'name': u'haobin.zhang',
                     u'tz': 480}}
    """
    def __init__(self, ref, revision, object_=None, message=None, tagger=None):
        self.ref = ref
        self.revision = revision
        self.object_ = object_
        self.message = message
        self.tagger = tagger

    @classmethod
    def from_dict(cls, dict_):
        return cls(ref=dict_.get('ref', None),
                   revision=dict_.get('revision', None),
                   object_=dict_.get('object', None),
                   message=dict_.get('message', None),
                   tagger=GitPersonInfo.from_dict(dict_.get('tagger', {})))

    def __repr__(self):
        return '<TagInfo[ref:{0} revision:{1}]>'.format(self.ref, self.revision)


class GitPersonInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#git-person-info
    """
    def __init__(self, name, email, date, tz):
        self.name = name
        self.email = email
        self.date = date
        self.tz = tz

    @classmethod
    def from_dict(cls, dict_):
        return cls(name=dict_.get('name', None),
                   email=dict_.get('email', None),
                   date=dict_.get('date', None),
                   tz=dict_.get('tz', None))

    def __repr__(self):
        return '<GitPersonInfo()>'


class CommitInfo(object):
    r"""
    http://192.168.10.48/Documentation/rest-api-changes.html#commit-info
    parsed output example:
        {u'author': {u'date': u'2016-12-09 06:40:35.000000000',
                     u'email': u'hui.zhang@reallytek.com',
                     u'name': u'hui.zhang',
                     u'tz': 480},
         u'commit': u'8b7a1b7752069c02b1f1099f9dfcef65989faa64',
         u'committer': {u'date': u'2016-12-09 06:55:17.000000000',
                        u'email': u'hui.zhang@reallytek.com',
                        u'name': u'Zhang Hui(\u5f20\u8f89)',
                        u'tz': 480},
         u'message': u'BUG ID:none\nDESCRIPTION:\u6dfb\u52a0TP\u6a21\u5757\u56fa\u4ef6\u4fe1\u606f\u8282\u70b9\n\nChange-Id: I23199bff36b3b7c157c01930ac2b237e5fee96a6\n',
         u'parents': [{u'commit': u'a547d50e849f93ba632cddecbe506c0ac6ca9758',
                       u'subject': u'BUG ID: none DESCRIPTION: \u6253\u5f00\u5c55\u9891\uff1b\u53d6\u6d88\u5c4f\u4e0b\u7535\uff0c\u8bbe\u7f6e\u8fdb\u5165\u6df1\u7761'}],
         u'subject': u'BUG ID:none DESCRIPTION:\u6dfb\u52a0TP\u6a21\u5757\u56fa\u4ef6\u4fe1\u606f\u8282\u70b9'}
    """
    def __init__(self, commit, parents, author, committer,
                 subject, message, web_links=None):
        self.commit = commit
        self.parents = parents
        self.author = author
        self.committer = committer
        self.subject = subject
        self.message = message
        self.web_links = web_links

    @classmethod
    def from_dict(cls, dict_):
        parents = []
        # 'parents of parents...' is limited, no infinite loop is possible
        for parent in dict_.get('parents', ()):
            parents.append(CommitInfo.from_dict(parent))
        return cls(commit=dict_.get('commit', None),
                   parents=parents,
                   author=GitPersonInfo.from_dict(dict_.get('author', {})),
                   committer=GitPersonInfo.from_dict(dict_.get('committer', {})),
                   subject=dict_.get('subject', None),
                   message=dict_.get('message', None),
                   web_links=dict_.get('web_links', None))

    def __repr__(self):
        return '<CommitInfo()>'


class TaskInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-config.html#task-info
    parsed output example:
        {u'command': u"git-upload-pack '/MT6755_N/prebuilts' (yongqi.li)",
         u'delay': -965957144,
         u'id': u'11ce6517',
         u'project_name': u'MT6755_N/prebuilts',
         u'start_time': u'2016-12-16 12:36:36.813000000',
         u'state': u'RUNNING'}
    """
    def __init__(self, id_, state, start_time, delay, command, project_name):
        self.id_ = id_
        self.state = state
        self.start_time = start_time # seems always UTC time
        self.delay = delay
        self.command = command
        # documentation of gerrit v2.12.5 indicates "remote_name" but actually returns "project_name"
        self.project_name = project_name

    @classmethod
    def from_dict(cls, dict_):
        return cls(id_=dict_.get('id', None),
                   state=dict_.get('state', None),
                   start_time=dict_.get('start_time', None),
                   delay=dict_.get('delay', None),
                   command=dict_.get('command', None),
                   project_name=dict_.get('project_name', None))

    def __repr__(self):
        return '<TaskInfo()>'


class RepositoryStatisticsInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-projects.html#repository-statistics-info
    parsed output example:
        {u'number_of_loose_objects': 5,
         u'number_of_loose_refs': 37,
         u'number_of_pack_files': 35,
         u'number_of_packed_objects': 434,
         u'number_of_packed_refs': 0,
         u'size_of_loose_objects': 489,
         u'size_of_packed_objects': 37007649}
    """
    def __init__(self, number_of_loose_objects, number_of_loose_refs,
                 number_of_pack_files, number_of_packed_objects,
                 number_of_packed_refs, size_of_loose_objects,
                 size_of_packed_objects):
        self.number_of_loose_objects = number_of_loose_objects
        self.number_of_loose_refs = number_of_loose_refs
        self.number_of_pack_files = number_of_pack_files
        self.number_of_packed_objects = number_of_packed_objects
        self.number_of_packed_refs = number_of_packed_refs
        self.size_of_loose_objects = size_of_loose_objects
        self.size_of_packed_objects = size_of_packed_objects

    @classmethod
    def from_dict(cls, dict_):
        return cls(number_of_loose_objects=dict_.get('number_of_loose_objects', None),
                   number_of_loose_refs=dict_.get('number_of_loose_refs', None),
                   number_of_pack_files=dict_.get('number_of_pack_files', None),
                   number_of_packed_objects=dict_.get('number_of_packed_objects', None),
                   number_of_packed_refs=dict_.get('number_of_packed_refs', None),
                   size_of_loose_objects=dict_.get('size_of_loose_objects', None),
                   size_of_packed_objects=dict_.get('size_of_packed_objects', None))

    def __repr__(self):
        return '<RepositoryStatisticsInfo()>'


class AccountInfo(object):
    r"""
    http://192.168.10.48/Documentation/rest-api-accounts.html#account-info
    parsed output example:
        {u'_account_id': 1000261,
         u'email': u'qijie.gao@reallytek.com',
         u'name': u'Gao Qijie(\u9ad8\u542f\u6770)',
         u'username': u'qijie.gao'}
    """
    def __init__(self, account_id, name, email, username):
        self.account_id = account_id
        self.name = name
        self.email = email
        self.username = username

    @classmethod
    def from_dict(cls, dict_):
        return cls(account_id=dict_.get('_account_id', None),
                   name=dict_.get('name', None),
                   email=dict_.get('email', None),
                   username=dict_.get('username', None))

    def __repr__(self):
        return '<AccountInfo()>'


class GroupInfo(object):
    r"""
    http://192.168.10.48/Documentation/rest-api-groups.html#group-info
    parsed output example:
        {u'group_id': 13,
         u'id': u'f1c47b4c9db35d15e8b7386054f7ef2f56bd63dd',
         u'includes': [],
         u'members': [{u'_account_id': 1000261,
                       u'email': u'qijie.gao@reallytek.com',
                       u'name': u'Gao Qijie(\u9ad8\u542f\u6770)',
                       u'username': u'qijie.gao'}],
         u'name': u'CX_H501_HiOS2.0.0_N_Merge',
         u'options': {},
         u'owner': u'Administrators',
         u'owner_id': u'50cdda658ea9c1dd1a639a1fe90a30cf7b24dda4',
         u'url': u'#/admin/groups/uuid-f1c47b4c9db35d15e8b7386054f7ef2f56bd63dd'}
    """
    def __init__(self, name, id_=None, options=None, url=None, description=None,
                 group_id=None, owner=None, owner_id=None, members=None, includes=None):
        self.id_ = id_
        self.name = name
        self.options = options
        self.url = url
        self.description = description
        self.group_id = group_id
        self.owner = owner
        self.owner_id = owner_id
        self.members = members
        self.includes = includes

    @classmethod
    def from_dict(cls, dict_):
        # avoid infinite loop
        if len(dict_) == 0:
            return cls(id_=None, name=None, options=None)

        members = []
        for member in dict_.get('members', ()):
            members.append(AccountInfo.from_dict(member))

        return cls(id_=dict_.get('id', None),
                   name=dict_.get('name', None),
                   options=dict_.get('options', None),
                   url=dict_.get('url', None),
                   description=dict_.get('description', None),
                   group_id=dict_.get('group_id', None),
                   owner=dict_.get('owner', None),
                   owner_id=dict_.get('owner_id', None),
                   members=members,
                   includes=GroupInfo.from_dict(dict_.get('includes', {})))

    def __repr__(self):
        return '<GroupInfo()>'


class GroupAuditEventInfo(object):
    r"""
    http://192.168.10.48/Documentation/rest-api-groups.html#group-audit-event-info
    parsed output example:
        {u'date': u'2016-12-16 07:51:12.276000000',
         u'member': {u'_account_id': 1000225,
                     u'email': u'rong.tang@reallytek.com',
                     u'name': u'Tang Rong(\u5510\u8363)',
                     u'username': u'rong.tang'},
         u'type': u'REMOVE_USER',
         u'user': {u'_account_id': 1000000,
                   u'email': u'scm@reallytek.com',
                   u'name': u'scm',
                   u'username': u'scm'}}
    """
    def __init__(self, member, type_, user, date):
        self.member = member
        self.type_ = type_
        self.user = user
        self.date = date

    @classmethod
    def from_dict(cls, dict_):
        type_ = dict_.get('type', None)
        if type_ == 'ADD_USER' or type_ == 'REMOVE_USER':
            member = AccountInfo.from_dict(dict_.get('member', {}))
        elif type_ == 'ADD_GROUP' or type_ == 'REMOVE_GROUP':
            member = GroupInfo.from_dict(dict_.get('member', {}))
        else:
            member = None
        user = AccountInfo.from_dict(dict_.get('user', {}))
        date = dict_.get('date', None)

        return cls(member, type_, user, date)

    def __repr__(self):
        return '<GroupAuditEventInfo()>'


class PermissionRuleInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-access.html#permission-info
    """
    def __init__(self, action, force, min_, max_):
        self.action = action
        self.force = force
        self.min_ = min_
        self.max_ = max_

    @classmethod
    def from_dict(cls, dict_):
        return cls(action=dict_.get('action', None),
                   force=dict_.get('force', None),
                   min_=dict_.get('min', None),
                   max_=dict_.get('max', None))

    def __repr__(self):
        return repr({k:v for k, v in self.__dict__.iteritems() if v is not None})


class ProjectAccessInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-access.html#project-access-info
    parsed output example:
        {'can_add': True,
         'can_upload': True,
         'config_visible': True,
         'inherits_from': {'id_': u'access_inherit_for_hios_developers', 'state': u'ACTIVE', 'name': u'access_inherit_for_hios_developers', 'parent': u'All-Projects'},
         'is_owner': True,
         'local': {u'refs/heads/HIOSN_DEV_N': {'permissions': {u'label-Code-Review': {u'exclusive': True,
                                                                                      u'label': u'Code-Review',
                                                                                      u'rules': {u'9fd17752eb952631ee0d4c35a59032fda211dc23': {'action': u'ALLOW', 'max_': 2, 'min_': -2}}},
                                                               u'submit': {u'exclusive': True,
                                                                           u'rules': {u'9fd17752eb952631ee0d4c35a59032fda211dc23': {'action': u'ALLOW'}}}}}},
         'owner_of': [u'refs/heads/HIOSN_DEV_N'],
         'revision': u'0ff2489eb9257deff9c2b2535eaa4acf032fc865'}
    """
    def __init__(self, revision, inherits_from, local, is_owner,
                 owner_of, can_upload, can_add, config_visible):
        self.revision = revision
        self.inherits_from = inherits_from
        self.local = local
        self.is_owner = is_owner
        self.owner_of = owner_of
        self.can_upload = can_upload
        self.can_add = can_add
        self.config_visible = config_visible

    @classmethod
    def from_dict(cls, dict_):
        local = {}
        for ref, access_section_info_dict in dict_.get('local', {}).iteritems():
            # _ is always 'permissions'
            permission = {}
            for _, permission_dict in access_section_info_dict.iteritems():
                # NOTICE: iterate only once
                permissions = {}
                for permission_name, permission_info_dict in permission_dict.iteritems():
                    permission_info = {}
                    for permission_info_k, permission_info_v in permission_info_dict.iteritems():
                        if permission_info_k == 'rules':
                            group_to_rule_info_map = {}
                            for group_uuid, permission_rule_info_dict in permission_info_v.iteritems():
                                permission_rule_info = PermissionRuleInfo.from_dict(permission_rule_info_dict)
                                group_to_rule_info_map[group_uuid] = permission_rule_info
                            permission_info[permission_info_k] = group_to_rule_info_map
                        else:
                            permission_info[permission_info_k] = permission_info_v
                    permissions[permission_name] = permission_info
                permission['permissions'] = permissions
            local[ref] = permission
        return cls(revision=dict_.get('revision', None),
                   inherits_from=ProjectInfo.from_dict(dict_.get('inherits_from', {})),
                   local=local,
                   is_owner=dict_.get('is_owner', None),
                   owner_of=dict_.get('owner_of', None),
                   can_upload=dict_.get('can_upload', None),
                   can_add=dict_.get('can_add', None),
                   config_visible=dict_.get('config_visible', None))

    def __repr__(self):
        return repr({k:v for k, v in self.__dict__.iteritems()})


class FetchInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#fetch-info
    """
    def __init__(self, url, ref, commands):
        self.url = url
        self.ref = ref
        self.commands = commands

    @classmethod
    def from_dict(cls, dict_):
        return cls(url=dict_.get('url', None),
                   ref=dict_.get('ref', None),
                   commands=dict_.get('commands', None))

    def __repr__(self):
        return '<FetchInfo()>'


class FileInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#file-info
    """
    def __init__(self, status, binary, old_path, lines_inserted,
                 lines_deleted, size_delta):
        self.status = status
        self.binary = binary
        self.old_path = old_path
        self.lines_inserted = lines_inserted
        self.lines_deleted = lines_deleted
        self.size_delta = size_delta

    @classmethod
    def from_dict(cls, dict_):
        return cls(status=dict_.get('status', None),
                   binary=dict_.get('binary', None),
                   old_path=dict_.get('old_path', None),
                   lines_inserted=dict_.get('lines_inserted', None),
                   lines_deleted=dict_.get('lines_deleted', None),
                   size_delta=dict_.get('size_delta', None))

    def __repr__(self):
        return '<FileInfo()>'


class ActionInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#action-info
    """
    def __init__(self, method, label, title, enabled):
        self.method = method
        self.label = label
        self.title = title
        self.enabled = enabled

    @classmethod
    def from_dict(cls, dict_):
        return cls(method=dict_.get('method', None),
                   label=dict_.get('label', None),
                   title=dict_.get('title', None),
                   enabled=dict_.get('enabled', None))

    def __repr__(self):
        return '<ActionInfo()>'


class RevisionInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#revision-info
    """
    def __init__(self, draft, number, created, uploader, ref, fetch, commit,
                 files, actions, reviewed, messageWithFooter, push_certificate):
        self.draft = draft
        self.number = number
        self.created = created
        self.uploader = uploader # AccountInfo
        self.ref = ref
        self.fetch = fetch # map(protocol name -> FetchInfo)
        self.commit = commit # CommitInfo
        self.files = files # map(file name -> FileInfo)
        self.actions = actions # map(view name -> ActionInfo)
        self.reviewed = reviewed
        self.messageWithFooter = messageWithFooter
        self.push_certificate = push_certificate # GPG related, ignore

    @classmethod
    def from_dict(cls, dict_):
        fetch = {}
        for protocol, fetchinfo in dict_.get('fetch', {}):
            fetch[protocol] = FetchInfo.from_dict(fetchinfo)
        files = {}
        for filename, fileinfo in dict_.get('files', {}):
            files[filename] = FileInfo.from_dict(fileinfo)
        actions = {}
        for viewname, actioninfo in dict_.get('actions', {}):
            actions[viewname] = ActionInfo.from_dict(actioninfo)

        return cls(draft=dict_.get('draft', None),
                   number=dict_.get('number', None),
                   created=dict_.get('created', None),
                   uploader=AccountInfo.from_dict(dict_.get('uploader', {})),
                   ref=dict_.get('ref', None),
                   fetch=fetch,
                   commit=CommitInfo.from_dict(dict_.get('commit', {})),
                   files=files,
                   actions=actions,
                   reviewed=dict_.get('reviewed', None),
                   messageWithFooter=dict_.get('messageWithFooter', None),
                   push_certificate=dict_.get('push_certificate', None))

    def __repr__(self):
        return '<RevisionInfo()>'


class ProblemInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#problem-info
    """
    def __init__(self, message, status, outcome):
        self.message = message
        self.status = status
        self.outcome = outcome

    @classmethod
    def from_dict(cls, dict_):
        return cls(message=dict_.get('message', None),
                   status=dict_.get('status', None),
                   outcome=dict_.get('outcome', None))

    def __repr__(self):
        return '<ProblemInfo()>'


class ApprovalInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#approval-info
    """
    def __init__(self, account_id, name, email, username, value, date):
        self.account_id = account_id
        self.name = name
        self.email = email
        self.username = username
        self.value = value
        self.date = date

    @classmethod
    def from_dict(cls, dict_):
        return cls(account_id=dict_.get('_account_id', None),
                   name=dict_.get('name', None),
                   email=dict_.get('email', None),
                   username=dict_.get('username', None),
                   value=dict_.get('value', None),
                   date=dict_.get('date', None))

    def __repr__(self):
        return '<ApprovalInfo()>'


class LabelInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#label-info
    """
    def __init__(self, optional, approved, rejected, recommended, disliked,
                 blocking, value, default_value, all_, values):
        self.optional = optional
        self.approved = approved
        self.rejected = rejected
        self.recommended = recommended
        self.disliked = disliked
        self.blocking = blocking
        self.value = value
        self.default_value = default_value
        self.all_ = all_ # list of ApprovalInfo
        self.values = values

    @classmethod
    def from_dict(cls, dict_):
        all_ = []
        for item in dict_.get('all', []):
            all_.append(ApprovalInfo.from_dict(item))

        return cls(optional=dict_.get('optional', None),
                   approved=AccountInfo.from_dict(dict_.get('approved', {})),
                   rejected=AccountInfo.from_dict(dict_.get('rejected', {})),
                   recommended=AccountInfo.from_dict(dict_.get('recommended', {})),
                   disliked=AccountInfo.from_dict(dict_.get('disliked', {})),
                   blocking=dict_.get('blocking', None),
                   value=dict_.get('value', None),
                   default_value=dict_.get('default_value', None),
                   all_=all_,
                   values=dict_.get('values', None))

    def __repr__(self):
        return '<LabelInfo()>'


class ChangeMessageInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#change-message-info
    """
    def __init__(self, id_, author, date, message, revision_number):
        self.id_ = id_
        self.author = author # AccountInfo
        self.date = date
        self.message = message
        self.revision_number = revision_number

    @classmethod
    def from_dict(cls, dict_):
        all_ = []
        for item in dict_.get('all', []):
            all_.append(ApprovalInfo.from_dict(item))

        return cls(id_=dict_.get('id', None),
                   author=AccountInfo.from_dict(dict_.get('author', {})),
                   date=dict_.get('date', {}),
                   message=dict_.get('message', {}),
                   revision_number=dict_.get('revision_number', {}))

    def __repr__(self):
        return '<ChangeMessageInfo()>'


class ChangeInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#change-info
    """
    def __init__(self, id_, project=None, branch=None, topic=None, change_id=None,
                 subject=None, status=None, created=None, updated=None, starred=None,
                 reviewed=None, mergeable=None, insertions=None, deletions=None,
                 number=None, owner=None, actions=None, labels=None,
                 permitted_labels=None, removable_reviewers=None, messages=None,
                 current_revision=None, revisions=None, more_changes=None,
                 problems=None, base_change=None):
        self.id_ = id_
        self.project = project
        self.branch = branch
        self.topic = topic
        self.change_id = change_id
        self.subject = subject
        self.status = status
        self.created = created
        self.updated = updated
        self.starred = starred
        self.reviewed = reviewed
        self.mergeable = mergeable
        self.insertions = insertions
        self.deletions = deletions
        self.number = number
        self.owner = owner  # AccountInfo
        self.actions = actions  # map (view name -> AccountInfo)
        self.labels = labels # map (label name -> LabelInfo)
        self.permitted_labels = permitted_labels # map (label name -> list)
        self.removable_reviewers = removable_reviewers # list of AccountInfo
        self.messages = messages # list of ChangeMessageInfo
        self.current_revision = current_revision
        self.revisions = revisions # map (commit id-> RevisionInfo)
        self.more_changes = more_changes
        self.problems = problems # list of ProblemInfo
        self.base_change = base_change

    @classmethod
    def from_dict(cls, dict_):
        actions = {}
        for viewname, actioninfo in dict_.get('actions', {}):
            actions[viewname] = ActionInfo.from_dict(actioninfo)

        return cls(id_=dict_.get('id', None),
                   project=dict_.get('project', None),
                   branch=dict_.get('branch', None),
                   topic=dict_.get('topic', None),
                   change_id=dict_.get('change_id', None),
                   subject=dict_.get('subject', None),
                   status=dict_.get('status', None),
                   created=dict_.get('created', None),
                   updated=dict_.get('updated', None),
                   starred=dict_.get('starred', None),
                   reviewed=dict_.get('reviewed', None),
                   mergeable=dict_.get('mergeable', None),
                   insertions=dict_.get('insertions', None),
                   deletions=dict_.get('deletions', None),
                   number=dict_.get('_number', None),
                   owner=AccountInfo.from_dict(dict_.get('owner', {})),
                   actions={viewname:ActionInfo.from_dict(actioninfo) for viewname, actioninfo in dict_.get('actions', {})},
                   labels={labelname:LabelInfo.from_dict(labelinfo) for labelname, labelinfo in dict_.get('labels', {}).iteritems()},
                   permitted_labels=dict_.get('permitted_labels', None),
                   removable_reviewers=[AccountInfo.from_dict(item) for item in dict_.get('removable_reviewers', [])],
                   messages=[ChangeMessageInfo.from_dict(item) for item in dict_.get('messages', [])],
                   current_revision=dict_.get('current_revision', None),
                   revisions={commitid:RevisionInfo.from_dict(revisioninfo) for commitid, revisioninfo in dict_.get('revisions', {})},
                   more_changes=dict_.get('_more_changes', None),
                   problems=[ProblemInfo.from_dict(item) for item in dict_.get('problems', [])],
                   base_change=dict_.get('base_change', None))

    def __repr__(self):
        return '<ChangeInfo()>'


class ReviewerInfo(object):
    """
    http://192.168.10.48/Documentation/rest-api-changes.html#reviewer-info
    """
    def __init__(self, account_id, name, email, username, approvals):
        self.account_id = account_id
        self.name = name
        self.email = email
        self.username = username
        self.approvals = approvals

    @classmethod
    def from_dict(cls, dict_):
        return cls(account_id=dict_.get('_account_id', None),
                   name=dict_.get('name', None),
                   email=dict_.get('email', None),
                   username=dict_.get('username', None),
                   approvals=dict_.get('approvals', None))

    def __repr__(self):
        return '<ReviewerInfo()>'


# MAIN CLASSES
class GerritHTTP(object):
    """
    Wrapper of http on which gerrit commands run.
    Can be reused since all internal states would be clear after re-run

    WARNING: DO NOT HARD CODE username/passwd, YOU CAN GET THEM  FROM ENVIRONMENT VARIABLES
    """
    def __init__(self, username, passwd, ip, port=80):
        self.ip = ip
        self.port = port
        self.auth = HTTPDigestAuth(username, passwd)

    # avoid inadvertent password leakage
    def __repr__(self):
        return 'GerritHTTP(ip={0}, port={1})'.format(self.ip, self.port)

    # avoid inadvertent password leakage
    __str__ = __repr__


class GerritConfig(object):
    def __init__(self, http):
        self.http = http

    def get_summary(self):
        r = requests.get('http://{0}:{1}/a/config/server/summary?jvm'.format(
                self.http.ip, self.http.port), auth=self.http.auth, timeout=TIMEOUT)
        if len(r.text) >= 4 and r.text[0:4] == ")]}'":
            return SummaryInfo.from_dict(json.loads(r.text[4:].encode('utf-8')))
        else:
            raise Exception("unexpected response: {0}".format(r.text))


class GerritTasks(object):
    def __init__(self, http):
        self.http = http

    def get(self):
        r = requests.get('http://{0}:{1}/a/config/server/tasks'.format(
                self.http.ip, self.http.port), auth=self.http.auth, timeout=TIMEOUT)
        if len(r.text) >= 4 and r.text[0:4] == ")]}'":
            task_infos = []
            for v in json.loads(r.text[4:].encode('utf-8')):
                task_infos.append(TaskInfo.from_dict(v))
            return task_infos
        else:
            raise Exception("unexpected response: {0}".format(r.text))


class GerritProject(object):
    def __init__(self, http, project_info):
        """
        only 'name' field is mandatory for project_info
        """
        self.http = http
        self.project_info = project_info

    def __repr__(self):
        return '<GerritProject[{0} {1}]>'.format(self.http, self.project_info)

    @classmethod
    def list_(cls, http, branch=None, prefix=None, regex=None, substring=None):
        if sum([prefix is not None, regex is not None, substring is not None]) > 1:
            raise Exception("specify exactly one of p(prefix)/m(regex)/r(substring)")
        option = 'd'
        if branch is not None:
            option += '&b={0}'.format(branch)
        if prefix is not None:
            option += '&p={0}'.format(prefix)
        if regex is not None:
            option += '&r={0}'.format(regex)
        if substring is not None:
            option += '&m={0}'.format(substring)
        r = requests.get('http://{0}:{1}/a/projects/?{2}'.format(
                http.ip, http.port, option), auth=http.auth, timeout=TIMEOUT)
        if len(r.text) >= 4 and r.text[0:4] == ")]}'":
            projects = []
            for k, v in json.loads(r.text[4:].encode('utf-8')).iteritems():
                v['name'] = k
                projects.append(GerritProject(http, ProjectInfo.from_dict(v)))
            return projects
        else:
            raise Exception("unexpected response: {0}".format(r.text))

    def _get(self, url_tail=(), file_mode=False):
        """
        generic get method
        """
        name_encode_slash = self.project_info.name.replace('/', '%2F')
        url_tail_encode_slash = [item.replace('/', '%2F') for item in url_tail]
        if len(url_tail_encode_slash) > 0:
            r = requests.get('http://{0}:{1}/a/projects/{2}/{3}'.format(
                    self.http.ip, self.http.port, name_encode_slash,
                    '/'.join(url_tail_encode_slash)), auth=self.http.auth,
                    timeout=TIMEOUT)
        else:
            r = requests.get('http://{0}:{1}/a/projects/{2}'.format(
                    self.http.ip, self.http.port, name_encode_slash),
                    auth=self.http.auth, timeout=TIMEOUT)
        if file_mode:
            if r.text in [u'Not Found\n', u'Notfound\n', u'Notfound']:
                raise Exception("unexpected response: {0}".format(r.text))
            # type of 'str'
            return base64.b64decode(r.text)
        else:
            if len(r.text) >= 4 and r.text[0:4] == ")]}'":
                return json.loads(r.text[4:].encode('utf-8'))
            else:
                raise Exception("unexpected response: {0}".format(r.text))

    def get(self):
        """
        get more detail version of GerritProject('parent', 'state' etc.)
        """
        return GerritProject(self.http, ProjectInfo.from_dict(self._get()))

    def get_parent(self):
        """
        parsed output example:
            u'All-Projects'
        """
        return self._get(('parent',))

    def get_stats(self):
        return RepositoryStatisticsInfo.from_dict(self._get(('statistics.git',)))

    def get_branches(self):
        branches = []
        for v in self._get(('branches',)):
            branches.append(BranchInfo.from_dict(v))
        return branches

    def get_branch(self, branch):
        v = self._get(('branches', branch))
        return BranchInfo(ref=v.get('ref', None), revision=v.get('revision', None),
                               can_delete=v.get('can_delete', None))


    def get_branch_file_content(self, branch, file_):
        """
        returns file content with type 'str'
        """
        return self._get(('branches', branch, 'files', urllib.quote(file_), 'content'), file_mode=True)

    def get_children(self):
        projects = []
        for v in self._get(('children',)):
            projects.append(GerritProject(self.http, ProjectInfo.from_dict(v)))
        return projects

    def get_tags(self):
        tags = []
        for v in self._get(('tags',)):
            tags.append(TagInfo.from_dict(v))
        return tags

    def get_tag(self, tagname):
        return TagInfo.from_dict(self._get(('tags', tagname)))

    def get_commit(self, commitid):
        return CommitInfo.from_dict(self._get(('commits', commitid)))

    def get_commit_file_content(self, commitid, file_):
        """
        returns file content with type 'str'
        """
        return self._get(('commits', commitid, 'files', urllib.quote(file_), 'content'), file_mode=True)


class GerritGroup(object):
    def __init__(self, http, group_info):
        """
        only 'name' field is mandatory for group_info
        """
        self.http = http
        self.group_info = group_info

    @classmethod
    def list_(cls, http, detail=False):
        if detail:
            options = '?o=INCLUDES&o=MEMBERS'
        else:
            options = ''

        r = requests.get('http://{0}:{1}/a/groups/{2}'.format(
                http.ip, http.port, options), auth=http.auth, timeout=TIMEOUT)
        if len(r.text) >= 4 and r.text[0:4] == ")]}'":
            groups = []
            for k, v in json.loads(r.text[4:].encode('utf-8')).iteritems():
                v['name'] = k
                groups.append(GerritGroup(http, GroupInfo.from_dict(v)))
            return groups
        else:
            raise Exception("unexpected response: {0}".format(r.text))

    def _get(self, url_tail=(), file_mode=False):
        """
        generic get method
        """
        name_encode_slash = self.group_info.name.replace('/', '%2F')
        url_tail_encode_slash = [item.replace('/', '%2F') for item in url_tail]
        if len(url_tail_encode_slash) > 0:
            r = requests.get('http://{0}:{1}/a/groups/{2}/{3}'.format(
                    self.http.ip, self.http.port, name_encode_slash,
                    '/'.join(url_tail_encode_slash)),
                    auth=self.http.auth, timeout=TIMEOUT)
        else:
            r = requests.get('http://{0}:{1}/a/groups/{2}'.format(
                    self.http.ip, self.http.port, name_encode_slash),
                    auth=self.http.auth, timeout=TIMEOUT)
        if file_mode:
            if r.text in [u'Not Found\n', u'Notfound\n', u'Notfound']:
                raise Exception("unexpected response: {0}".format(r.text))
            # type of 'str'
            return base64.b64decode(r.text)
        else:
            if len(r.text) >= 4 and r.text[0:4] == ")]}'":
                return json.loads(r.text[4:].encode('utf-8'))
            else:
                raise Exception("unexpected response: {0}".format(r.text))

    def get(self):
        """
        get more detail version of GerritGroup to fill group_info field
        """
        return GerritGroup(self.http, GroupInfo.from_dict(self._get()))

    def get_detail(self):
        """
        get more detail version of GerritGroup('members' 'includes' etc.)
        """
        return GerritGroup(self.http, GroupInfo.from_dict(self._get(('detail',))))

    def get_name(self):
        """
        id/name -> name
        parsed output example:
            u'CX_H501_HiOS2.0.0_N_Merge'
        """
        return self._get(('name',))

    def get_log_audit(self):
        infos = []
        for v in self._get(('log.audit',)):
            infos.append(GroupAuditEventInfo.from_dict(v))
        return infos

    def get_members(self):
        members = []
        for v in self._get(('members',)):
            members.append(AccountInfo.from_dict(v))
        return members

    def get_groups(self):
        """
        get included groups
        """
        groups = []
        for v in self._get(('groups',)):
            groups.append(GroupInfo.from_dict(v))
        return groups


class GerritProjectAccess(object):
    def __init__(self, http, project):
        self.http = http
        self.project = project

    def get(self):
        r = requests.get('http://{0}:{1}/a/access/?project={2}'.format(
                self.http.ip, self.http.port, self.project),
                auth=self.http.auth, timeout=TIMEOUT)
        if len(r.text) >= 4 and r.text[0:4] == ")]}'":
            return ProjectAccessInfo.from_dict(json.loads(r.text[4:].encode('utf-8'))[self.project])
        else:
            raise Exception("unexpected response: {0}".format(r.text))


class GerritChange(object):
    def __init__(self, http, change_info):
        """
        only 'id_' field is mandatory for change_info
        """
        self.http = http
        self.change_info = change_info

    def __repr__(self):
        return '<GerritChange({})>'.format(self.change_info)

    @classmethod
    def list_(cls, http, option):
        r = requests.get('http://{0}:{1}/a/changes/?q={2}'.format(
                http.ip, http.port, urllib.quote(option)),
                auth=http.auth, timeout=TIMEOUT)
        if len(r.text) >= 4 and r.text[0:4] == ")]}'":
            changes = []
            for item in json.loads(r.text[4:].encode('utf-8')):
                changes.append(GerritChange(http, ChangeInfo.from_dict(item)))
            return changes
        else:
            raise Exception("unexpected response: {0}".format(r.text))

    def _get(self, url_tail=(), file_mode=False):
        """
        generic get method
        """
        id_encode_slash = self.change_info.id_.replace('/', '%2F')
        url_tail_encode_slash = [item.replace('/', '%2F') for item in url_tail]
        if len(url_tail_encode_slash) > 0:
            r = requests.get('http://{0}:{1}/a/changes/{2}/{3}'.format(
                    self.http.ip, self.http.port, id_encode_slash, '/'.join(url_tail_encode_slash)),
                    auth=self.http.auth, timeout=TIMEOUT)
        else:
            r = requests.get('http://{0}:{1}/a/changes/{2}'.format(
                    self.http.ip, self.http.port, id_encode_slash),
                    auth=self.http.auth, timeout=TIMEOUT)
        if file_mode:
            if r.text in [u'Not Found\n', u'Notfound\n', u'Notfound']:
                raise Exception("unexpected response: {0}".format(r.text))
            # type of 'str'
            return base64.b64decode(r.text)
        else:
            if len(r.text) >= 4 and r.text[0:4] == ")]}'":
                return json.loads(r.text[4:].encode('utf-8'))
            else:
                raise Exception("unexpected response: {0}".format(r.text))

    def get(self):
        return GerritChange(self.http, ChangeInfo.from_dict(self._get()))

    def get_detail(self):
        return GerritChange(self.http, ChangeInfo.from_dict(self._get(('detail',))))

    def get_reviewers(self):
        return [ReviewerInfo.from_dict(item) for item in self._get(('reviewers',))]

    def get_reviewer(self, reviewer):
        # NOTICE: documentation of v2.12.5 returns dict but actually returns list
        result = self._get(('reviewers', reviewer))
        if isinstance(result, list):
            result = result[0]
        return ReviewerInfo.from_dict(result)

    def get_commit(self, revision):
        return CommitInfo.from_dict(self._get(('revisions', revision, 'commit')))

    def get_patch(self, revision):
        """
        returns file content with type 'str'
        """
        return self._get(('revisions', revision, 'patch'), file_mode=True)

    def get_files(self, revision):
        return {name:FileInfo.from_dict(fileinfo) for name, fileinfo in self._get(('revisions', revision, 'files')).iteritems()}

    def get_file_content(self, revision, file_):
        """
        returns file content with type 'str'
        """
        return self._get(('revisions', revision, 'files', urllib.quote(file_), 'content'), file_mode=True)


if __name__ == '__main__':
    pass
