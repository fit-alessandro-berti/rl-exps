import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their exact names
activities = {
    'Data Capture': Transition(label='Data Capture'),
    'Quantum Calc': Transition(label='Quantum Calc'),
    'Demand Forecast': Transition(label='Demand Forecast'),
    'Inventory Check': Transition(label='Inventory Check'),
    'Route Update': Transition(label='Route Update'),
    'Shipment Plan': Transition(label='Shipment Plan'),
    'Supplier Sync': Transition(label='Supplier Sync'),
    'Contract Mod': Transition(label='Contract Mod'),
    'Blockchain Verify': Transition(label='Blockchain Verify'),
    'Risk Assess': Transition(label='Risk Assess'),
    'Scenario Sim': Transition(label='Scenario Sim'),
    'Feedback Loop': Transition(label='Feedback Loop'),
    'AI Adjust': Transition(label='AI Adjust'),
    'Waste Audit': Transition(label='Waste Audit'),
    'Report Generate': Transition(label='Report Generate'),
    'Stakeholder Alert': Transition(label='Stakeholder Alert'),
    'Compliance Review': Transition(label='Compliance Review')
}

# Create the StrictPartialOrder model
root = StrictPartialOrder(nodes=list(activities.values()))

# Add dependencies based on the process description
root.order.add_edge(activities['Data Capture'], activities['Quantum Calc'])
root.order.add_edge(activities['Quantum Calc'], activities['Demand Forecast'])
root.order.add_edge(activities['Data Capture'], activities['Inventory Check'])
root.order.add_edge(activities['Inventory Check'], activities['Route Update'])
root.order.add_edge(activities['Data Capture'], activities['Shipment Plan'])
root.order.add_edge(activities['Shipment Plan'], activities['Supplier Sync'])
root.order.add_edge(activities['Supplier Sync'], activities['Contract Mod'])
root.order.add_edge(activities['Blockchain Verify'], activities['Risk Assess'])
root.order.add_edge(activities['Risk Assess'], activities['Scenario Sim'])
root.order.add_edge(activities['Feedback Loop'], activities['AI Adjust'])
root.order.add_edge(activities['Waste Audit'], activities['Report Generate'])
root.order.add_edge(activities['Stakeholder Alert'], activities['Compliance Review'])

# Print the root model
print(root)