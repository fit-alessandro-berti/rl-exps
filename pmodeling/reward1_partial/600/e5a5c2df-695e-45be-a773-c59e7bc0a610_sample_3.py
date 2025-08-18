from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
root = StrictPartialOrder(nodes=[
    Transition(label='Alert Trigger'),
    Transition(label='Initial Assess'),
    Transition(label='Stakeholder Notify'),
    Transition(label='Resource Check'),
    Transition(label='Risk Analyze'),
    Transition(label='Command Setup'),
    Transition(label='Deploy Teams'),
    Transition(label='Data Collect'),
    Transition(label='Situation Update'),
    Transition(label='Priority Adjust'),
    Transition(label='External Liaison'),
    Transition(label='Supply Dispatch'),
    Transition(label='Media Brief'),
    Transition(label='Impact Review'),
    Transition(label='Recovery Plan'),
    Transition(label='Process Audit')
])

# Add the dependencies between activities
root.order.add_edge(Transition(label='Alert Trigger'), Transition(label='Initial Assess'))
root.order.add_edge(Transition(label='Alert Trigger'), Transition(label='Stakeholder Notify'))
root.order.add_edge(Transition(label='Initial Assess'), Transition(label='Resource Check'))
root.order.add_edge(Transition(label='Resource Check'), Transition(label='Risk Analyze'))
root.order.add_edge(Transition(label='Risk Analyze'), Transition(label='Command Setup'))
root.order.add_edge(Transition(label='Command Setup'), Transition(label='Deploy Teams'))
root.order.add_edge(Transition(label='Deploy Teams'), Transition(label='Data Collect'))
root.order.add_edge(Transition(label='Data Collect'), Transition(label='Situation Update'))
root.order.add_edge(Transition(label='Situation Update'), Transition(label='Priority Adjust'))
root.order.add_edge(Transition(label='Priority Adjust'), Transition(label='External Liaison'))
root.order.add_edge(Transition(label='External Liaison'), Transition(label='Supply Dispatch'))
root.order.add_edge(Transition(label='Supply Dispatch'), Transition(label='Media Brief'))
root.order.add_edge(Transition(label='Media Brief'), Transition(label='Impact Review'))
root.order.add_edge(Transition(label='Impact Review'), Transition(label='Recovery Plan'))
root.order.add_edge(Transition(label='Recovery Plan'), Transition(label='Process Audit'))

# Print the final model
print(root)