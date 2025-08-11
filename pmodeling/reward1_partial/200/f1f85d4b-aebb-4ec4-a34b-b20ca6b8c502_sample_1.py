import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = {
    'Initial Review': Transition(label='Initial Review'),
    'Provenance Check': Transition(label='Provenance Check'),
    'Material Testing': Transition(label='Material Testing'),
    'Expert Survey': Transition(label='Expert Survey'),
    'Digital Scan': Transition(label='Digital Scan'),
    'Condition Report': Transition(label='Condition Report'),
    'Legal Review': Transition(label='Legal Review'),
    'Risk Analysis': Transition(label='Risk Analysis'),
    'Seller Negotiation': Transition(label='Seller Negotiation'),
    'Documentation': Transition(label='Documentation'),
    'Archival Entry': Transition(label='Archival Entry'),
    'Committee Review': Transition(label='Committee Review'),
    'Final Approval': Transition(label='Final Approval'),
    'Acquisition Setup': Transition(label='Acquisition Setup'),
    'Exhibit Planning': Transition(label='Exhibit Planning')
}

# Define silent transitions
skip = SilentTransition()

# Define workflow structure
root = StrictPartialOrder()

# Add activities to the root
root.nodes.extend(list(activities.values()))

# Define dependencies between activities
root.order.add_edge(activities['Initial Review'], activities['Provenance Check'])
root.order.add_edge(activities['Provenance Check'], activities['Material Testing'])
root.order.add_edge(activities['Material Testing'], activities['Expert Survey'])
root.order.add_edge(activities['Expert Survey'], activities['Digital Scan'])
root.order.add_edge(activities['Digital Scan'], activities['Condition Report'])
root.order.add_edge(activities['Condition Report'], activities['Legal Review'])
root.order.add_edge(activities['Legal Review'], activities['Risk Analysis'])
root.order.add_edge(activities['Risk Analysis'], activities['Seller Negotiation'])
root.order.add_edge(activities['Seller Negotiation'], activities['Documentation'])
root.order.add_edge(activities['Documentation'], activities['Archival Entry'])
root.order.add_edge(activities['Archival Entry'], activities['Committee Review'])
root.order.add_edge(activities['Committee Review'], activities['Final Approval'])
root.order.add_edge(activities['Final Approval'], activities['Acquisition Setup'])
root.order.add_edge(activities['Acquisition Setup'], activities['Exhibit Planning'])

# Return the root node
print(root)