import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
from pm4py.algo.discovery.dfg import algorithm as dfg_discovery

# Define the activities
activities = ['Data Ingest', 'Status Check', 'Forecast Update', 'Risk Assess', 'Scenario Sim', 'Model Run', 'Option Select', 'Team Review', 'Plan Approve', 'Procure Adjust', 'Route Replan', 'Inventory Shift', 'Execute Updates', 'Monitor KPIs', 'Feedback Loop']

# Create the POWL model
root = StrictPartialOrder(nodes=activities)

# Define the dependencies between activities
root.order.add_edge('Data Ingest', 'Status Check')
root.order.add_edge('Data Ingest', 'Forecast Update')
root.order.add_edge('Status Check', 'Risk Assess')
root.order.add_edge('Forecast Update', 'Risk Assess')
root.order.add_edge('Risk Assess', 'Scenario Sim')
root.order.add_edge('Scenario Sim', 'Model Run')
root.order.add_edge('Model Run', 'Option Select')
root.order.add_edge('Option Select', 'Team Review')
root.order.add_edge('Team Review', 'Plan Approve')
root.order.add_edge('Plan Approve', 'Procure Adjust')
root.order.add_edge('Procure Adjust', 'Route Replan')
root.order.add_edge('Route Replan', 'Inventory Shift')
root.order.add_edge('Inventory Shift', 'Execute Updates')
root.order.add_edge('Execute Updates', 'Monitor KPIs')
root.order.add_edge('Monitor KPIs', 'Feedback Loop')

# Print the root
print(root)