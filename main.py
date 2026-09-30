from agents.agent import EngineeringAgent


agent = EngineeringAgent("Engineering Agent")

task = input("Digite uma tarefa: ")

response = agent.respond(task)

print()
print(response)
