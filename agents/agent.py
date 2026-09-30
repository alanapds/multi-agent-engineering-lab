class EngineeringAgent:

    def __init__(self, name):
        self.name = name

    def respond(self, task):
        return f"{self.name} recebeu a tarefa: {task}"