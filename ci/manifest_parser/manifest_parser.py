#!/usr/bin/python
#Transsion Top Secret

import os
import sys
import xml.etree.ElementTree as ET
from urlparse import urlparse


class Project(object):
    def __init__(self, name, path, remote, revision, upstream):
        self.name = name
        self.path = path
        self.remote = remote
        self.revision = revision
        self.upstream = upstream

    def __repr__(self):
        return "<project name:{} path:{} remote:{} revision:{} upstream:{}>".format(self.name, self.path, self.remote, self.revision, self.upstream)


class Remote(object):
    def __init__(self, name, fetch, review):
        self.name = name
        self.fetch = fetch
        self.review = review
        self.fetch_ip = urlparse(self.fetch).hostname
        self.review_ip = urlparse(self.review).hostname

    def __repr__(self):
        return "<remote name:{} fetch:{} review:{} fetch_ip:{} review_ip:{}>".format(self.name, self.fetch, self.review, self.fetch_ip, self.review_ip)


class Manifest(object):
    def __init__(self, fileobject):
        tree = ET.parse(fileobject)

        self.root = tree.getroot()
        self.remotes = []
        self.default_remote = None
        self.default_revision = None
        self.projects = []

        self._init_remotes()
        self._init_default_remote()
        self._init_default_revision()
        self._init_projects()

    def _init_remotes(self):
        for remote in self.root.findall('remote'):
            self.remotes.append(Remote(remote.get('name', None), remote.get('fetch', None), remote.get('review', None)))

    def _init_default_remote(self):
        default = self.root.find('default')
        if default is not None:
            self.default_remote = self._find_remote(default.get('remote'))

    def _find_remote(self, remote_name):
         for remote in self.remotes:
             if remote_name == remote.name:
                 return remote
         return None

    def _init_default_revision(self):
        default = self.root.find('default')
        if default is not None:
            self.default_revision = default.get('revision', None)

    def _init_projects(self):
        for project in self.root.findall('project'):
            name = project.get('name')
            path = project.get('path')
            remote = None
            remote_name = project.get('remote')
            revision = project.get('revision')
            upstream = project.get('upstream')

            if path is None:
                path = name
            if remote_name is None:
                remote = self.default_remote
            else:
                remote = self._find_remote(remote_name)
            if revision is None:
                revision = self.default_revision
            self.projects.append(Project(name, path, remote, revision, upstream))


def test():
    manifest = Manifest(sys.argv[1])
    print "remotes: %s " % manifest.remotes
    print "default_remote: %s" % manifest.default_remote
    print "default_revision: %s" % manifest.default_revision
    for project in manifest.projects:
        print "projects: %s" % project


if __name__ == '__main__':
    test()
