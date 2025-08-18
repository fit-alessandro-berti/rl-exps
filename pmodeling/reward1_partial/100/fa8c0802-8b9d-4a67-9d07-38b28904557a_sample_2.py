import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities with their respective labels
activities = {
    'Data Aggregation': Transition(label='Data Aggregation'),
    'Anomaly Detect': Transition(label='Anomaly Detect'),
    'Risk Assess': Transition(label='Risk Assess'),
    'Demand Model': Transition(label='Demand Model'),
    'Stakeholder Sync': Transition(label='Stakeholder Sync'),
    'Auto Negotiate': Transition(label='Auto Negotiate'),
    'Inventory Optimize': Transition(label='Inventory Optimize'),
    'Contingency Plan': Transition(label='Contingency Plan'),
    'Resource Allocate': Transition(label='Resource Allocate'),
    'Sustainability Check': Transition(label='Sustainability Check'),
    'Compliance Verify': Transition(label='Compliance Verify'),
    'Impact Score': Transition(label='Impact Score'),
    'Distribution Plan': Transition(label='Distribution Plan'),
    'Feedback Loop': Transition(label='Feedback Loop'),
    'Performance Audit': Transition(label='Performance Audit'),
    'Schedule Execute': Transition(label='Schedule Execute')
}

# Create the POWL model structure
root = StrictPartialOrder(nodes=[activities['Data Aggregation'], activities['Anomaly Detect'], activities['Risk Assess'], activities['Demand Model'], activities['Stakeholder Sync'], activities['Auto Negotiate'], activities['Inventory Optimize'], activities['Contingency Plan'], activities['Resource Allocate'], activities['Sustainability Check'], activities['Compliance Verify'], activities['Impact Score'], activities['Distribution Plan'], activities['Feedback Loop'], activities['Performance Audit'], activities['Schedule Execute']])

# Define the control flow operators
root.order.add_edge(activities['Data Aggregation'], activities['Anomaly Detect'])
root.order.add_edge(activities['Anomaly Detect'], activities['Risk Assess'])
root.order.add_edge(activities['Risk Assess'], activities['Demand Model'])
root.order.add_edge(activities['Demand Model'], activities['Stakeholder Sync'])
root.order.add_edge(activities['Stakeholder Sync'], activities['Auto Negotiate'])
root.order.add_edge(activities['Auto Negotiate'], activities['Inventory Optimize'])
root.order.add_edge(activities['Inventory Optimize'], activities['Contingency Plan'])
root.order.add_edge(activities['Contingency Plan'], activities['Resource Allocate'])
root.order.add_edge(activities['Resource Allocate'], activities['Sustainability Check'])
root.order.add_edge(activities['Sustainability Check'], activities['Compliance Verify'])
root.order.add_edge(activities['Compliance Verify'], activities['Impact Score'])
root.order.add_edge(activities['Impact Score'], activities['Distribution Plan'])
root.order.add_edge(activities['Distribution Plan'], activities['Feedback Loop'])
root.order.add_edge(activities['Feedback Loop'], activities['Performance Audit'])
root.order.add_edge(activities['Performance Audit'], activities['Schedule Execute'])

# Print the final POWL model
print(root)