import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
activities = ['Site Analysis', 'Impact Review', 'Modular Design', 'System Integration',
              'Climate Setup', 'Nutrient Mix', 'Light Config', 'Staff Training',
              'Pest Monitor', 'Drone Deploy', 'Health Scan', 'Data Logging',
              'Supply Sync', 'Maintenance Plan', 'Waste Manage']

# Create transitions for each activity
transitions = [Transition(label=activity) for activity in activities]

# Define exclusive choice for pest monitoring and drone deployment
pest_monitor = transitions[8]
drone_deploy = transitions[9]
pest_drone_choice = OperatorPOWL(operator=Operator.XOR, children=[pest_monitor, drone_deploy])

# Define loop for data logging and maintenance plan
data_logging = transitions[10]
maintenance_plan = transitions[12]
data_logging_maintenance_loop = OperatorPOWL(operator=Operator.LOOP, children=[data_logging, maintenance_plan])

# Define partial order with all nodes
root = StrictPartialOrder(nodes=transitions + [pest_drone_choice, data_logging_maintenance_loop])
root.order.add_edge(transitions[0], transitions[1])
root.order.add_edge(transitions[1], transitions[2])
root.order.add_edge(transitions[2], transitions[3])
root.order.add_edge(transitions[3], transitions[4])
root.order.add_edge(transitions[4], transitions[5])
root.order.add_edge(transitions[5], transitions[6])
root.order.add_edge(transitions[6], transitions[7])
root.order.add_edge(transitions[7], pest_drone_choice)
root.order.add_edge(pest_drone_choice, data_logging_maintenance_loop)
root.order.add_edge(data_logging_maintenance_loop, data_logging)
root.order.add_edge(data_logging, maintenance_plan)
root.order.add_edge(maintenance_plan, data_logging_maintenance_loop)
root.order.add_edge(transitions[8], data_logging_maintenance_loop)
root.order.add_edge(transitions[9], data_logging_maintenance_loop)
root.order.add_edge(transitions[10], data_logging_maintenance_loop)
root.order.add_edge(transitions[11], data_logging_maintenance_loop)
root.order.add_edge(transitions[12], data_logging_maintenance_loop)