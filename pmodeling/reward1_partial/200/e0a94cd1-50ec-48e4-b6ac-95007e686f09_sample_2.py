from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = {
    'Data Ingestion': Transition(label='Data Ingestion'),
    'Quantum Setup': Transition(label='Quantum Setup'),
    'Route Optimize': Transition(label='Route Optimize'),
    'Demand Forecast': Transition(label='Demand Forecast'),
    'Scenario Simulate': Transition(label='Scenario Simulate'),
    'Risk Assess': Transition(label='Risk Assess'),
    'Anomaly Detect': Transition(label='Anomaly Detect'),
    'Supplier Sync': Transition(label='Supplier Sync'),
    'Quantum Communicate': Transition(label='Quantum Communicate'),
    'Inventory Adjust': Transition(label='Inventory Adjust'),
    'Procurement Plan': Transition(label='Procurement Plan'),
    'Performance Track': Transition(label='Performance Track'),
    'Feedback Loop': Transition(label='Feedback Loop'),
    'Decision Automate': Transition(label='Decision Automate'),
    'Cost Analyze': Transition(label='Cost Analyze'),
    'Network Adapt': Transition(label='Network Adapt')
}

# Define the relationships between activities
root = StrictPartialOrder(nodes=list(activities.values()))

# Define the edges (dependencies) between activities
root.order.add_edge(activities['Data Ingestion'], activities['Quantum Setup'])
root.order.add_edge(activities['Quantum Setup'], activities['Route Optimize'])
root.order.add_edge(activities['Quantum Setup'], activities['Demand Forecast'])
root.order.add_edge(activities['Route Optimize'], activities['Scenario Simulate'])
root.order.add_edge(activities['Demand Forecast'], activities['Scenario Simulate'])
root.order.add_edge(activities['Scenario Simulate'], activities['Risk Assess'])
root.order.add_edge(activities['Scenario Simulate'], activities['Anomaly Detect'])
root.order.add_edge(activities['Scenario Simulate'], activities['Supplier Sync'])
root.order.add_edge(activities['Scenario Simulate'], activities['Quantum Communicate'])
root.order.add_edge(activities['Scenario Simulate'], activities['Inventory Adjust'])
root.order.add_edge(activities['Scenario Simulate'], activities['Procurement Plan'])
root.order.add_edge(activities['Scenario Simulate'], activities['Performance Track'])
root.order.add_edge(activities['Risk Assess'], activities['Feedback Loop'])
root.order.add_edge(activities['Anomaly Detect'], activities['Feedback Loop'])
root.order.add_edge(activities['Supplier Sync'], activities['Feedback Loop'])
root.order.add_edge(activities['Quantum Communicate'], activities['Feedback Loop'])
root.order.add_edge(activities['Inventory Adjust'], activities['Feedback Loop'])
root.order.add_edge(activities['Procurement Plan'], activities['Feedback Loop'])
root.order.add_edge(activities['Performance Track'], activities['Feedback Loop'])
root.order.add_edge(activities['Feedback Loop'], activities['Decision Automate'])
root.order.add_edge(activities['Decision Automate'], activities['Cost Analyze'])
root.order.add_edge(activities['Cost Analyze'], activities['Network Adapt'])

# Return the root POWL model
return root