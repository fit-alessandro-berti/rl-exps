import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Alert Verify': Transition(label='Alert Verify'),
    'Impact Assess': Transition(label='Impact Assess'),
    'Team Assemble': Transition(label='Team Assemble'),
    'Resource Allocate': Transition(label='Resource Allocate'),
    'Stakeholder Notify': Transition(label='Stakeholder Notify'),
    'Legal Review': Transition(label='Legal Review'),
    'Media Brief': Transition(label='Media Brief'),
    'Response Deploy': Transition(label='Response Deploy'),
    'Situation Monitor': Transition(label='Situation Monitor'),
    'Data Collect': Transition(label='Data Collect'),
    'Risk Mitigate': Transition(label='Risk Mitigate'),
    'Recovery Plan': Transition(label='Recovery Plan'),
    'External Consult': Transition(label='External Consult'),
    'Status Update': Transition(label='Status Update'),
    'Post Review': Transition(label='Post Review')
}

# Define the POWL model
root = StrictPartialOrder(nodes=[
    activities['Alert Verify'],
    activities['Impact Assess'],
    activities['Team Assemble'],
    activities['Resource Allocate'],
    activities['Stakeholder Notify'],
    activities['Legal Review'],
    activities['Media Brief'],
    activities['Response Deploy'],
    activities['Situation Monitor'],
    activities['Data Collect'],
    activities['Risk Mitigate'],
    activities['Recovery Plan'],
    activities['External Consult'],
    activities['Status Update'],
    activities['Post Review']
])

# Define the dependencies
root.order.add_edge(activities['Alert Verify'], activities['Impact Assess'])
root.order.add_edge(activities['Alert Verify'], activities['Team Assemble'])
root.order.add_edge(activities['Impact Assess'], activities['Resource Allocate'])
root.order.add_edge(activities['Impact Assess'], activities['Stakeholder Notify'])
root.order.add_edge(activities['Team Assemble'], activities['Resource Allocate'])
root.order.add_edge(activities['Team Assemble'], activities['Stakeholder Notify'])
root.order.add_edge(activities['Resource Allocate'], activities['Legal Review'])
root.order.add_edge(activities['Resource Allocate'], activities['Media Brief'])
root.order.add_edge(activities['Resource Allocate'], activities['Response Deploy'])
root.order.add_edge(activities['Stakeholder Notify'], activities['Legal Review'])
root.order.add_edge(activities['Stakeholder Notify'], activities['Media Brief'])
root.order.add_edge(activities['Stakeholder Notify'], activities['Response Deploy'])
root.order.add_edge(activities['Legal Review'], activities['Situation Monitor'])
root.order.add_edge(activities['Legal Review'], activities['Data Collect'])
root.order.add_edge(activities['Legal Review'], activities['Risk Mitigate'])
root.order.add_edge(activities['Legal Review'], activities['Recovery Plan'])
root.order.add_edge(activities['Legal Review'], activities['External Consult'])
root.order.add_edge(activities['Legal Review'], activities['Status Update'])
root.order.add_edge(activities['Legal Review'], activities['Post Review'])
root.order.add_edge(activities['Media Brief'], activities['Situation Monitor'])
root.order.add_edge(activities['Media Brief'], activities['Data Collect'])
root.order.add_edge(activities['Media Brief'], activities['Risk Mitigate'])
root.order.add_edge(activities['Media Brief'], activities['Recovery Plan'])
root.order.add_edge(activities['Media Brief'], activities['External Consult'])
root.order.add_edge(activities['Media Brief'], activities['Status Update'])
root.order.add_edge(activities['Media Brief'], activities['Post Review'])
root.order.add_edge(activities['Response Deploy'], activities['Situation Monitor'])
root.order.add_edge(activities['Response Deploy'], activities['Data Collect'])
root.order.add_edge(activities['Response Deploy'], activities['Risk Mitigate'])
root.order.add_edge(activities['Response Deploy'], activities['Recovery Plan'])
root.order.add_edge(activities['Response Deploy'], activities['External Consult'])
root.order.add_edge(activities['Response Deploy'], activities['Status Update'])
root.order.add_edge(activities['Response Deploy'], activities['Post Review'])
root.order.add_edge(activities['Situation Monitor'], activities['Data Collect'])
root.order.add_edge(activities['Situation Monitor'], activities['Risk Mitigate'])
root.order.add_edge(activities['Situation Monitor'], activities['Recovery Plan'])
root.order.add_edge(activities['Situation Monitor'], activities['External Consult'])
root.order.add_edge(activities['Situation Monitor'], activities['Status Update'])
root.order.add_edge(activities['Situation Monitor'], activities['Post Review'])
root.order.add_edge(activities['Data Collect'], activities['Risk Mitigate'])
root.order.add_edge(activities['Data Collect'], activities['Recovery Plan'])
root.order.add_edge(activities['Data Collect'], activities['External Consult'])
root.order.add_edge(activities['Data Collect'], activities['Status Update'])
root.order.add_edge(activities['Data Collect'], activities['Post Review'])
root.order.add_edge(activities['Risk Mitigate'], activities['Recovery Plan'])
root.order.add_edge(activities['Risk Mitigate'], activities['External Consult'])
root.order.add_edge(activities['Risk Mitigate'], activities['Status Update'])
root.order.add_edge(activities['Risk Mitigate'], activities['Post Review'])
root.order.add_edge(activities['Recovery Plan'], activities['External Consult'])
root.order.add_edge(activities['Recovery Plan'], activities['Status Update'])
root.order.add_edge(activities['Recovery Plan'], activities['Post Review'])
root.order.add_edge(activities['External Consult'], activities['Status Update'])
root.order.add_edge(activities['External Consult'], activities['Post Review'])
root.order.add_edge(activities['Status Update'], activities['Post Review'])