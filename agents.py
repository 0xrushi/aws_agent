from textwrap import dedent
from crewai import Agent
from tools import test_run_tool, write_data

class AWSAgents():
	def senior_engineer_agent(self):
		return Agent(
			role='Senior Cloud Architect',
			goal='Create AWS solution as needed',
			backstory=dedent("""\
				You are a Senior Cloud Architect at a leading tech think tank.
				Your expertise in building aws solutions using PlantUML scripts and do your best to
				produce perfect code.
				Write your response as if you were handing it to a developer  to fix the issues. Before passing
				make sure the code works, use the write_data tool to save to 1.puml file and use the test_run_tool to check
				if the file runs without any errors. If there are no errors, exit."""),
			allow_delegation=False,
			tools=[test_run_tool, write_data],
			verbose=True
		)

	def code_reviewer_agent(self):
		return Agent(
			role='Cloud Architect Engineer',
  		goal='create prefect code, by analizing the code that is given for errors',
  		backstory=dedent("""\
				You are a software engineer that specializes in checking code
  			for errors. You have an eye for detail and a knack for finding
				hidden bugs.
  			You check for missing imports, mismatched
				brackets, wrong imports and syntax errors.
  			You also check for logic errors"""),
			allow_delegation=False,
			verbose=True
		)

	# def chief_qa_engineer_agent(self):
	# 	return Agent(
	# 		role='Chief Software Quality Control Engineer',
 #  		goal='Ensure that the code does the job that it is supposed to do',
 #  		backstory=dedent("""\
	# 			You feel that programmers always do only half the job, so you are
	# 			super dedicate to make high quality code."""),
	# 		allow_delegation=True,
	# 		verbose=True
	# 	)
