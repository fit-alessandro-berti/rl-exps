import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Collection Survey': Transition(label='Collection Survey'),
    'Provenance Check': Transition(label='Provenance Check'),
    'Legal Review': Transition(label='Legal Review'),
    'Scientific Test': Transition(label='Scientific Test'),
    'Material Analysis': Transition(label='Material Analysis'),
    'Ownership Audit': Transition(label='Ownership Audit'),
    'Ethical Screening': Transition(label='Ethical Screening'),
    'Condition Report': Transition(label='Condition Report'),
    'Expert Consultation': Transition(label='Expert Consultation'),
    'Transport Planning': Transition(label='Transport Planning'),
    'Secure Packing': Transition(label='Secure Packing'),
    'Customs Clearance': Transition(label='Customs Clearance'),
    'Insurance Setup': Transition(label='Insurance Setup'),
    'Exhibit Preparation': Transition(label='Exhibit Preparation'),
    'Final Approval': Transition(label='Final Approval')
}

# Define the partial order model
root = StrictPartialOrder(nodes=[
    activities['Collection Survey'],
    activities['Provenance Check'],
    activities['Legal Review'],
    activities['Scientific Test'],
    activities['Material Analysis'],
    activities['Ownership Audit'],
    activities['Ethical Screening'],
    activities['Condition Report'],
    activities['Expert Consultation'],
    activities['Transport Planning'],
    activities['Secure Packing'],
    activities['Customs Clearance'],
    activities['Insurance Setup'],
    activities['Exhibit Preparation'],
    activities['Final Approval']
])

# Define the dependencies between activities
root.order.add_edge(activities['Collection Survey'], activities['Provenance Check'])
root.order.add_edge(activities['Provenance Check'], activities['Legal Review'])
root.order.add_edge(activities['Legal Review'], activities['Scientific Test'])
root.order.add_edge(activities['Scientific Test'], activities['Material Analysis'])
root.order.add_edge(activities['Material Analysis'], activities['Ownership Audit'])
root.order.add_edge(activities['Ownership Audit'], activities['Ethical Screening'])
root.order.add_edge(activities['Ethical Screening'], activities['Condition Report'])
root.order.add_edge(activities['Condition Report'], activities['Expert Consultation'])
root.order.add_edge(activities['Expert Consultation'], activities['Transport Planning'])
root.order.add_edge(activities['Transport Planning'], activities['Secure Packing'])
root.order.add_edge(activities['Secure Packing'], activities['Customs Clearance'])
root.order.add_edge(activities['Customs Clearance'], activities['Insurance Setup'])
root.order.add_edge(activities['Insurance Setup'], activities['Exhibit Preparation'])
root.order.add_edge(activities['Exhibit Preparation'], activities['Final Approval'])

# Print the root model
print(root)