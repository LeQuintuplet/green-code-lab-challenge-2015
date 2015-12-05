from daemon import runner

class Program():
    def __init__(self):
        self.stdin_path = '/dev/null'
        self.stdout_path = '/dev/tty'
        self.stderr_path = '/dev/tty'
        self.pidfile_path =  '/tmp/foo.pid'
        self.pidfile_timeout = 5
    def run(self):
        # Main Code Here

prog = Program()
daemon_runner = runner.DaemonRunner(prog)
daemon_runner.do_action()
