# Configuration file for ipcontroller.

c = get_config()
c.HubFactory.ip = '*'
c.LocalControllerLauncher.controller_args = ['--log-to-file', '--log-level=20', "--ip='*'"]

c.TaskScheduler.scheme_name = 'leastload'
c.TaskScheduler.hwm = 2

#------------------------------------------------------------------------------
# IPControllerApp configuration
#------------------------------------------------------------------------------

# IPControllerApp will inherit config from: BaseParallelApplication,
# BaseIPythonApplication, Application

# The IPython profile to use.
# c.IPControllerApp.profile = u'default'

# import statements to be run at startup.  Necessary in some environments
# c.IPControllerApp.import_statements = []

# Whether to reuse existing json connection files. If False, connection files
# will be removed on a clean exit.
#c.IPControllerApp.reuse_files = True

# Set the log level by value or name.
# c.IPControllerApp.log_level = 30

# Set the working dir for the process.
# c.IPControllerApp.work_dir = u'/home/molu8455'

# ssh url for engines to use when connecting to the Controller processes. It
# should be of the form: [user@]server[:port]. The Controller's listening
# addresses must be accessible from the ssh server
# c.IPControllerApp.engine_ssh_server = u''

# The ZMQ URL of the iplogger to aggregate logging.
# c.IPControllerApp.log_url = ''

# JSON filename where engine connection info will be stored.
# c.IPControllerApp.engine_json_file = 'ipcontroller-engine.json'

# Whether to create profile dir if it doesn't exist.
# c.IPControllerApp.auto_create = True

# whether to log to a file
# c.IPControllerApp.log_to_file = False

# JSON filename where client connection info will be stored.
# c.IPControllerApp.client_json_file = 'ipcontroller-client.json'

# String id to add to runtime files, to prevent name collisions when using
# multiple clusters with a single profile simultaneously.
# 
# When set, files will be named like: 'ipcontroller-<cluster_id>-engine.json'
# 
# Since this is text inserted into filenames, typical recommendations apply:
# Simple character strings are ideal, and spaces are not recommended (but should
# generally work).
# c.IPControllerApp.cluster_id = ''

# The external IP or domain name of the Controller, used for disambiguating
# engine and client connections.
# c.IPControllerApp.location = u''

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.IPControllerApp.copy_config_files = False

# whether to cleanup old logfiles before starting
# c.IPControllerApp.clean_logs = False

# Use threads instead of processes for the schedulers
# c.IPControllerApp.use_threads = False

# The Logging format template
# c.IPControllerApp.log_format = '[%(name)s] %(message)s'

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.IPControllerApp.verbose_crash = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This options can also be specified through the environment
# variable IPYTHONDIR.
# c.IPControllerApp.ipython_dir = u'/home/molu8455/.ipython'

# ssh url for clients to use when connecting to the Controller processes. It
# should be of the form: [user@]server[:port]. The Controller's listening
# addresses must be accessible from the ssh server
# c.IPControllerApp.ssh_server = u''

# Whether to overwrite existing config files when copying
# c.IPControllerApp.overwrite = False

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
# 
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
# 
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = u''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
# 
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
# 
# Sessions support configurable serialiization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
# 
# Parameters ----------
# 
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
# 
#     The functions must accept at least valid JSON input, and output *bytes*.
# 
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# Username for the Session. Default is your system username.
# c.Session.username = 'molu8455'

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# The UUID identifying this session.
# c.Session.session = u''

# execution key, for extra authentication.
# c.Session.key = ''

# Debug output in the Session
# c.Session.debug = False

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# path to file containing execution key.
# c.Session.keyfile = ''

#------------------------------------------------------------------------------
# HubFactory configuration
#------------------------------------------------------------------------------

# The Configurable for setting up a Hub.

# HubFactory will inherit config from: RegistrationFactory

# Engine/Client Port pair for Control queue
# c.HubFactory.control = None

# 0MQ transport for monitor messages. [default : tcp]
# c.HubFactory.monitor_transport = 'tcp'

# IP on which to listen for client connections. [default: loopback]
# c.HubFactory.client_ip = '127.0.0.1'

# Engine/Client Port pair for Task queue
# c.HubFactory.task = None

# 0MQ transport for engine connections. [default: tcp]
# c.HubFactory.engine_transport = 'tcp'

# 0MQ transport for client connections. [default : tcp]
# c.HubFactory.client_transport = 'tcp'

# Monitor (SUB) port for queue traffic
# c.HubFactory.mon_port = 0

# The IP address for registration.  This is generally either '127.0.0.1' for
# loopback only or '*' for all interfaces. [default: '127.0.0.1']
# c.HubFactory.ip = '127.0.0.1'

# Engine/Client Port pair for MUX queue
# c.HubFactory.mux = None

# PUB port for sending engine status notifications
# c.HubFactory.notifier_port = 0

# The port on which the Hub listens for registration.
# c.HubFactory.regport = 0

# The 0MQ url used for registration. This sets transport, ip, and port in one
# variable. For example: url='tcp://127.0.0.1:12345' or url='epgm://*:90210'
# c.HubFactory.url = ''

# IP on which to listen for engine connections. [default: loopback]
# c.HubFactory.engine_ip = '127.0.0.1'

# Engine/Client Port pair for IOPub relay
# c.HubFactory.iopub = None

# DEALER/SUB Port pair for Engine heartbeats
# c.HubFactory.hb = None

# The class to use for the DB backend
# 
# Options include:
# 
# SQLiteDB: SQLite MongoDB : use MongoDB DictDB  : in-memory storage (fastest,
# but be mindful of memory growth of the Hub) NoDB    : disable database
# altogether (default)
# c.HubFactory.db_class = 'NoDB'

# IP on which to listen for monitor messages. [default: loopback]
# c.HubFactory.monitor_ip = '127.0.0.1'

# The 0MQ transport for communications.  This will likely be the default of
# 'tcp', but other values include 'ipc', 'epgm', 'inproc'.
# c.HubFactory.transport = 'tcp'



#------------------------------------------------------------------------------
# HeartMonitor configuration
#------------------------------------------------------------------------------

# A basic HeartMonitor class pingstream: a PUB stream pongstream: an ROUTER
# stream period: the period of the heartbeat in milliseconds

# The frequency at which the Hub pings the engines for heartbeats (in ms)
# c.HeartMonitor.period = 3000

#------------------------------------------------------------------------------
# SQLiteDB configuration
#------------------------------------------------------------------------------

# SQLite3 TaskRecord backend.

# The SQLite Table to use for storing tasks for this session. If unspecified, a
# new table will be created with the Hub's IDENT.  Specifying the table will
# result in tasks from previous sessions being available via Clients' db_query
# and get_result methods.
# c.SQLiteDB.table = ''

# The directory containing the sqlite task database.  The default is to use the
# cluster_dir location.
# c.SQLiteDB.location = ''

# The filename of the sqlite task database. [default: 'tasks.db']
# c.SQLiteDB.filename = 'tasks.db'