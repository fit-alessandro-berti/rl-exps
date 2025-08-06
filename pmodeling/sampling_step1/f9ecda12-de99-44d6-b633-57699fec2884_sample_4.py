from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions (activities) with their names
activities = {
    'Concept Approve': Transition(label='Concept Approve'),
    'Budget Align': Transition(label='Budget Align'),
    'Design Review': Transition(label='Design Review'),
    'Structure Simulate': Transition(label='Structure Simulate'),
    'Material Procure': Transition(label='Material Procure'),
    'Vendor Select': Transition(label='Vendor Select'),
    'Permit Apply': Transition(label='Permit Apply'),
    'Safety Check': Transition(label='Safety Check'),
    'Site Prep': Transition(label='Site Prep'),
    'Logistics Plan': Transition(label='Logistics Plan'),
    'Fabricate Parts': Transition(label='Fabricate Parts'),
    'Assemble Onsite': Transition(label='Assemble Onsite'),
    'Quality Inspect': Transition(label='Quality Inspect'),
    'Weather Monitor': Transition(label='Weather Monitor'),
    'Public Unveil': Transition(label='Public Unveil'),
    'Maintenance Plan': Transition(label='Maintenance Plan'),
    'Stakeholder Meet': Transition(label='Stakeholder Meet')
}

# Define the POWL model
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the dependencies between activities
root.order.add_edge(activities['Concept Approve'], activities['Budget Align'])
root.order.add_edge(activities['Budget Align'], activities['Design Review'])
root.order.add_edge(activities['Design Review'], activities['Structure Simulate'])
root.order.add_edge(activities['Structure Simulate'], activities['Material Procure'])
root.order.add_edge(activities['Material Procure'], activities['Vendor Select'])
root.order.add_edge(activities['Vendor Select'], activities['Permit Apply'])
root.order.add_edge(activities['Permit Apply'], activities['Safety Check'])
root.order.add_edge(activities['Safety Check'], activities['Site Prep'])
root.order.add_edge(activities['Site Prep'], activities['Logistics Plan'])
root.order.add_edge(activities['Logistics Plan'], activities['Fabricate Parts'])
root.order.add_edge(activities['Fabricate Parts'], activities['Assemble Onsite'])
root.order.add_edge(activities['Assemble Onsite'], activities['Quality Inspect'])
root.order.add_edge(activities['Quality Inspect'], activities['Weather Monitor'])
root.order.add_edge(activities['Weather Monitor'], activities['Public Unveil'])
root.order.add_edge(activities['Public Unveil'], activities['Maintenance Plan'])
root.order.add_edge(activities['Maintenance Plan'], activities['Stakeholder Meet'])

# Print the root to verify the model
print(root)