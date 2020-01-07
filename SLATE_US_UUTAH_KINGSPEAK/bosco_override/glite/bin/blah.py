"""Common functions for BLAH python scripts"""

import os
from ConfigParser import RawConfigParser
# TODO: io.StringIO is preferred in Python3 since it handles unicode-encoded files
from StringIO import StringIO

class BlahConfigParser(RawConfigParser, object):

    def __init__(self, path='/etc/blah.config', defaults=None):
        path = '%s/etc/blah.config' % (os.environ['GLITE_LOCATION'])
        # RawConfigParser requires ini-style [section headers] but since
        # blah.config is also used as a shell script we need to fake one
        self.header = 'blahp'
        with open(path) as f:
            config = f.read()
        vfile = StringIO('[%s]\n%s' % (self.header, config))

        super(BlahConfigParser, self).__init__(defaults=defaults)
        # TODO: readfp() is replaced by read_file() in Python 3.2+
        self.readfp(vfile)

    def items(self):
        return super(BlahConfigParser, self).items(self.header)

    def get(self, option):
        # ConfigParser happily includes quotes in value strings, which we
        # happily allow in /etc/blah.config. This causes failures when joining
        # paths, for example.
        return super(BlahConfigParser, self).get(self.header, option).strip('"\'')

    def set(self, option, value):
        return super(BlahConfigParser, self).set(self.header, option, value)

    def has_option(self, option):
        return super(BlahConfigParser, self).has_option(self.header, option)
