import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
milk_sourcing = Transition(label='Milk Sourcing')
culture_selection = Transition(label='Culture Selection')
milk_testing = Transition(label='Milk Testing')
curd_formation = Transition(label='Curd Formation')
whey_separation = Transition(label='Whey Separation')
molding_cheese = Transition(label='Molding Cheese')
salting_process = Transition(label='Salting Process')
aging_setup = Transition(label='Aging Setup')
env_monitoring = Transition(label='Env Monitoring')
flavor_profiling = Transition(label='Flavor Profiling')
packaging_design = Transition(label='Packaging Design')
blockchain_entry = Transition(label='Blockchain Entry')
quality_audit = Transition(label='Quality Audit')
retail_sync = Transition(label='Retail Sync')
transport_prep = Transition(label='Transport Prep')
delivery_tracking = Transition(label='Delivery Tracking')
customer_feedback = Transition(label='Customer Feedback')

# Define the control-flow operators
xor = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, culture_selection])
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_testing, curd_formation])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, molding_cheese])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[salting_process, aging_setup])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[env_monitoring, flavor_profiling])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[packaging_design, blockchain_entry])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, retail_sync])
loop4 = OperatorPOWL(operator=Operator.LOOP, children=[transport_prep, delivery_tracking])
xor5 = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, customer_feedback])

# Define the partial order
root = StrictPartialOrder(nodes=[xor, loop, xor2, loop2, xor3, loop3, xor4, loop4, xor5])
root.order.add_edge(xor, loop)
root.order.add_edge(loop, xor2)
root.order.add_edge(xor2, loop2)
root.order.add_edge(loop2, xor3)
root.order.add_edge(xor3, loop3)
root.order.add_edge(loop3, xor4)
root.order.add_edge(xor4, loop4)
root.order.add_edge(loop4, xor5)

# Print the root
print(root)