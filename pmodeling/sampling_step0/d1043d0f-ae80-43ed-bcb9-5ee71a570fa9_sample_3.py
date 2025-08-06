import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
activities = ['Site Survey', 'Env Analysis', 'Module Design', 'Seed Selection', 'Nutrient Mix', 'Climate Setup', 'LED Install', 'Sensor Deploy', 'Pest Control', 'Waste Recycle', 'Hydro Test', 'Staff Train', 'Yield Forecast', 'Market Plan', 'Data Review']

# Create the POWL model
root = StrictPartialOrder(nodes=activities)

# Define the partial order edges
root.order.add_edge('Site Survey', 'Env Analysis')
root.order.add_edge('Env Analysis', 'Module Design')
root.order.add_edge('Module Design', 'Seed Selection')
root.order.add_edge('Seed Selection', 'Nutrient Mix')
root.order.add_edge('Nutrient Mix', 'Climate Setup')
root.order.add_edge('Climate Setup', 'LED Install')
root.order.add_edge('LED Install', 'Sensor Deploy')
root.order.add_edge('Sensor Deploy', 'Pest Control')
root.order.add_edge('Pest Control', 'Waste Recycle')
root.order.add_edge('Waste Recycle', 'Hydro Test')
root.order.add_edge('Hydro Test', 'Staff Train')
root.order.add_edge('Staff Train', 'Yield Forecast')
root.order.add_edge('Yield Forecast', 'Market Plan')
root.order.add_edge('Market Plan', 'Data Review')

# Print the POWL model
print(root)