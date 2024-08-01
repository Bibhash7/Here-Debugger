from locust import task, User, constant
from src.here_debugger.debug import here_debugger

class LoadTestHereDebugger(User):

    @task
    def test_here_debugger_without_parameters(self):
        a = 2
        here_debugger("Here",a)
        b = [9]*1000
        here_debugger("here",b)
