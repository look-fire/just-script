#!/usr/bin/python
# -*- coding: utf8 -*-
"""
usage demo for gerrit_rest_api package
"""

import os
import pprint
import sys
import gerrit_rest_api
from datetime import datetime
from gerrit_rest_api import (GerritHTTP, GerritConfig, GerritTasks,
     GerritProject, GerritGroup, GerritProjectAccess, GerritChange,
     ProjectInfo, GroupInfo, ChangeInfo)

# in case of pprint ascii parse error
reload(sys)
sys.setdefaultencoding('utf-8')

# requests TIMEOUT customization
gerrit_rest_api.TIMEOUT = 30

# WARNING: DO NOT HARD CODE username/passwd
#     YOU CAN GET THEM  FROM ENVIRONMENT VARIABLES
HTTP = GerritHTTP(os.environ['GERRITUSER'], os.environ['GERRITPASSWD'],
                  '192.168.10.48')

pprint = pprint.PrettyPrinter().pprint


def print_server_summary():
    summary = GerritConfig(HTTP).get_summary()

    task_summary = summary.task_summary
    mem_summary = summary.mem_summary
    thread_summary = summary.thread_summary

    pprint("task total: {}".format(task_summary.total))
    pprint("task running: {}".format(task_summary.running))
    pprint("task ready: {}".format(task_summary.ready))
    pprint("task sleeping: {}".format(task_summary.sleeping))

    pprint("mem total: {}".format(mem_summary.total))
    pprint("mem used: {}".format(mem_summary.used))
    pprint("mem free: {}".format(mem_summary.free))
    pprint("mem buffers: {}".format(mem_summary.buffers))
    pprint("mem max: {}".format(mem_summary.max_))
    pprint("mem open_files: {}".format(mem_summary.open_files))

    pprint("thread cpus: {}".format(thread_summary.cpus))
    pprint("thread threads: {}".format(thread_summary.threads))
    pprint("thread counts: {}".format(thread_summary.counts))


def print_server_tasks():
    tasks = GerritTasks(HTTP).get()

    for task in tasks:
        pprint("task id: {}".format(task.id_))
        pprint("task state: {}".format(task.state))
        pprint("task start_time: {}".format(task.start_time))
        pprint("task delay: {}".format(task.delay))
        pprint("task command: {}".format(task.command))
        pprint("task project_name: {}".format(task.project_name))
        utc_start_time = datetime.strptime(task.start_time,
                                           "%Y-%m-%d %H:%M:%S.%f000")
        utc_now = datetime.utcnow()
        pprint("utc_start_time: {} utc_now: {}".format(utc_start_time, utc_now))
        delta = utc_now - utc_start_time
        pprint("time delta: {}".format(delta))


def print_projects():
    projects = GerritProject.list_(HTTP)
    project = projects[0]

    pprint("project info: {}".format(project.project_info))
    pprint("project : {}".format(project.get()))
    pprint("project parent: {}".format(project.get_parent()))

    stats = project.get_stats()
    pprint("number_of_loose_objects: {}".format(stats.number_of_loose_objects))
    pprint("number_of_loose_refs: {}".format(stats.number_of_loose_refs))
    pprint("number_of_pack_files: {}".format(stats.number_of_pack_files))
    pprint("number_of_packed_objects: {}".format(
           stats.number_of_packed_objects))
    pprint("number_of_packed_refs: {}".format(stats.number_of_packed_refs))
    pprint("size_of_loose_objects: {}".format(stats.size_of_loose_objects))
    pprint("size_of_packed_objects: {}".format(stats.size_of_packed_objects))

    for branch in project.get_branches():
        pprint("branch ref: {}".format(branch.ref))
        pprint("branch revision: {}".format(branch.revision))
        pprint("branch can_delete: {}".format(branch.can_delete))
        pprint("branch web_links: {}".format(branch.web_links))

    pprint("branch: {}".format(project.get_branch('refs/meta/config')))
    pprint("branch file: {}".format(project.get_branch_file_content(
                                    'refs/meta/config', 'project.config')))

    allproject = GerritProject(HTTP, ProjectInfo('All-Projects'))
    pprint("children: {}".format(allproject.get_children()))

    tag = project.get_tags()[0]
    pprint("tag ref: {}".format(tag.ref))
    pprint("tag revision: {}".format(tag.revision))
    pprint("tag object: {}".format(tag.object_))
    pprint("tag message: {}".format(tag.message))
    pprint("tag tagger: {}".format(tag.tagger))
    pprint("tag tagger name: {}".format(tag.tagger.name))
    pprint("tag tagger email: {}".format(tag.tagger.email))
    pprint("tag tagger date: {}".format(tag.tagger.date))
    pprint("tag tagger tz: {}".format(tag.tagger.tz))

    tag = project.get_tag(
              'refs/tags/CXLite_H3713_HiOS2.0.0_N_BEFORE_TAG_20161217')
    pprint("tag message: {}".format(tag.message))

    commit = project.get_commit('1b54b56ea5746c2bc1c15617b7fc263890db77b9')
    pprint("commit: {}".format(commit.commit))
    pprint("commit parents: {}".format(commit.parents))
    pprint("commit author: {}".format(commit.author))

    pprint(project.get_commit_file_content(
               '1b54b56ea5746c2bc1c15617b7fc263890db77b9', 'tools/Android.mk'))


def print_groups():
    groups = GerritGroup.list_(HTTP)
    group = groups[1]
    info = group.group_info
    print info.name
    pprint("group id: {}".format(info.id_))
    pprint("group name: {}".format(info.name))
    pprint("group options: {}".format(info.options))
    pprint("group url: {}".format(info.url))
    pprint("group description: {}".format(info.description))
    pprint("group group_id: {}".format(info.group_id))
    pprint("group owner: {}".format(info.owner))
    pprint("group owner_id: {}".format(info.owner_id))
    pprint("group members: {}".format(info.members))

    group = GerritGroup(HTTP, GroupInfo('codereview')).get()
    pprint(group.group_info.id_)
    member = group.get_detail().group_info.members[0]
    pprint("member id:{} name:{} email:{} username:{}".format(
           member.account_id, member.name, member.email, member.username))
    pprint(group.get_name())
    auditinfo = group.get_log_audit()[0]
    pprint("audit date:{} type:{} user:{} member:{}".format(
           auditinfo.date, auditinfo.type_, auditinfo.user.username,
           auditinfo.member.username))
    member = group.get_members()[0]
    pprint("member id:{} name:{} email:{} username:{}".format(
           member.account_id, member.name, member.email, member.username))
    for included_group in group.get_groups():
        pprint(included_group.get_name())


def print_project_access():
    project_access_info = GerritProjectAccess(HTTP, 'All-Projects').get()
    pprint("project_access can_add:{}".format(project_access_info.can_add))
    pprint("project_access can_upload:{}".format(
           project_access_info.can_upload))
    pprint("project_access config_visible:{}".format(
           project_access_info.config_visible))
    pprint("project_access inherits_from:{}".format(
           project_access_info.inherits_from.name))
    pprint("project_access is_owner:{}".format(project_access_info.is_owner))
    pprint("project_access owner_of:{}".format(project_access_info.owner_of))
    pprint("project_access revision:{}".format(project_access_info.revision))
    local = project_access_info.local
    for ref, access_section_info_dict in local.iteritems():
        pprint("project_access local ref:{}".format(ref))
        permission_dict = access_section_info_dict['permissions']
        for permission_name, permission_info_dict in permission_dict.iteritems():
            pprint("project_access local   permission_name:{}".format(permission_name))
            for permission_info_k, permission_info_v in permission_info_dict.iteritems():
                if permission_info_k == 'rules':
                    for group_uuid, permission_rule_info in permission_info_v.iteritems():
                        pprint("project_access local     group_uuid:{}".format(group_uuid))
                        pprint("project_access local     permission_rule_info:{}".format(permission_rule_info))


def print_changes():
    changes = GerritChange.list_(HTTP,
        "status:merged project:MT6755_N/external branch:CX_H501_HiOS2.0.0_N message:{P18}")
    for change in changes:
        info = change.change_info
        pprint("change change_id: {}".format(info.change_id))

    change = GerritChange(HTTP, ChangeInfo('I0d596962b2d614ac3e3fb21e0b81d1e36b155015'))
    info = change.get().change_info
    pprint("change subject: {}".format(info.subject))

    changes = GerritChange.list_(HTTP, "label:Code-Review+1")
    change = changes[-1]
    info = change.change_info
    pprint("change more_changes: {}".format(info.more_changes)) # True
    info = change.get().change_info
    pprint("change subject: {}".format(info.subject))
    pprint("change more_changes: {}".format(info.more_changes)) # False

    info = change.get_detail().change_info
    pprint("change more_changes: {}".format(info.more_changes))
    pprint("change change_id: {}".format(info.change_id))
    pprint("change id_: {}".format(info.id_))
    pprint("change project: {}".format(info.project))
    pprint("change branch: {}".format(info.branch))
    pprint("change topic: {}".format(info.topic))
    pprint("change change_id: {}".format(info.change_id))
    pprint("change subject: {}".format(info.subject))
    pprint("change status: {}".format(info.status))
    pprint("change created: {}".format(info.created))
    pprint("change updated: {}".format(info.updated))
    pprint("change starred: {}".format(info.starred))
    pprint("change reviewed: {}".format(info.reviewed))
    pprint("change mergeable: {}".format(info.mergeable))
    pprint("change insertions: {}".format(info.insertions))
    pprint("change deletions: {}".format(info.deletions))
    pprint("change number: {}".format(info.number))
    pprint("change owner: {}".format(info.owner.username))
    pprint("change info.actions: {}".format(info.actions))
    for labelname, lableinfo in info.labels.iteritems():
        pprint("change   labelname: {}".format(labelname))
        pprint("change   lableinfo approved: {}".format(
               lableinfo.approved.username))
        pprint("change   lableinfo all: {}".format(lableinfo.all_[0].__dict__))
    pprint("change permitted_labels: {}".format(info.permitted_labels))
    pprint("change removable_reviewers: {}".format(info.removable_reviewers))
    for message in info.messages:
        pprint("change    message: {} {} {}".format(
               message.date, message.message, message.author.username))
    pprint("change info.current_revision: {}".format(info.current_revision))
    pprint("change revisions: {}".format(info.revisions))
    pprint("change more_changes: {}".format(info.more_changes))
    pprint("change problems: {}".format(info.problems))
    pprint("change base_change: {}".format(info.base_change))

    for reviewer in change.get_reviewers():
        pprint("reviewer username:{} approvals:{}".format(
               reviewer.username, reviewer.approvals))
        pprint("reviewer approvals:{}".format(
               change.get_reviewer(reviewer.username).approvals))

    commit = change.get_commit('1')
    pprint("change commit 1 commit: {}".format(commit.commit))
    pprint("change commit 1 parents: {}".format(commit.parents[0].commit))
    pprint("change commit 1 author: {}".format(commit.author.name))
    pprint("change commit 1 committer: {}".format(commit.committer.name))
    pprint("change commit 1 subject: {}".format(commit.subject))
    pprint("change commit 1 message: {}".format(commit.message))
    pprint("change commit 1 web_links: {}".format(commit.web_links))

    patch = change.get_patch('1')
    pprint("change commit 1 patch: {}".format(patch))

    files = change.get_files('1')
    filename = files.keys()[0]
    fileinfo = files[filename]
    pprint("change commit 1 file name: {}".format(filename))
    pprint("change commit 1 file size delta: {}".format(fileinfo.size_delta))
    pprint("change commit 1 file content: {}".format(
           change.get_file_content('1', filename)[0:10]))


if __name__ == '__main__':
    print_server_summary()
    print_server_tasks()
    print_projects()
    print_groups()
    print_project_access()
    print_changes()
