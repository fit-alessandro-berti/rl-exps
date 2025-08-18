import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Brand Audit': Transition(label='Brand Audit'),
    'Equity Review': Transition(label='Equity Review'),
    'Market Analysis': Transition(label='Market Analysis'),
    'Legal Clearance': Transition(label='Legal Clearance'),
    'Trademark Check': Transition(label='Trademark Check'),
    'Portfolio Merge': Transition(label='Portfolio Merge'),
    'Customer Sync': Transition(label='Customer Sync'),
    'Cultural Align': Transition(label='Cultural Align'),
    'Internal Brief': Transition(label='Internal Brief'),
    'Campaign Design': Transition(label='Campaign Design'),
    'Resource Plan': Transition(label='Resource Plan'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet'),
    'Launch Prep': Transition(label='Launch Prep'),
    'Feedback Loop': Transition(label='Feedback Loop'),
    'Performance Track': Transition(label='Performance Track')
}

# Define the process steps
root = StrictPartialOrder(nodes=[
    activities['Brand Audit'],
    activities['Equity Review'],
    activities['Market Analysis'],
    activities['Legal Clearance'],
    activities['Trademark Check'],
    activities['Portfolio Merge'],
    activities['Customer Sync'],
    activities['Cultural Align'],
    activities['Internal Brief'],
    activities['Campaign Design'],
    activities['Resource Plan'],
    activities['Stakeholder Meet'],
    activities['Launch Prep'],
    activities['Feedback Loop'],
    activities['Performance Track']
])

# Define the partial order
root.order.add_edge(activities['Brand Audit'], activities['Equity Review'])
root.order.add_edge(activities['Equity Review'], activities['Market Analysis'])
root.order.add_edge(activities['Market Analysis'], activities['Legal Clearance'])
root.order.add_edge(activities['Legal Clearance'], activities['Trademark Check'])
root.order.add_edge(activities['Trademark Check'], activities['Portfolio Merge'])
root.order.add_edge(activities['Portfolio Merge'], activities['Customer Sync'])
root.order.add_edge(activities['Customer Sync'], activities['Cultural Align'])
root.order.add_edge(activities['Cultural Align'], activities['Internal Brief'])
root.order.add_edge(activities['Internal Brief'], activities['Campaign Design'])
root.order.add_edge(activities['Campaign Design'], activities['Resource Plan'])
root.order.add_edge(activities['Resource Plan'], activities['Stakeholder Meet'])
root.order.add_edge(activities['Stakeholder Meet'], activities['Launch Prep'])
root.order.add_edge(activities['Launch Prep'], activities['Feedback Loop'])
root.order.add_edge(activities['Feedback Loop'], activities['Performance Track'])

# Print the root
print(root)