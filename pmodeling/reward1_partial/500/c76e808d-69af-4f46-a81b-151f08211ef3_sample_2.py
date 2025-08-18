import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL nodes
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

# Define the POWL operators
xor1 = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, env_monitoring])
xor2 = OperatorPOWL(operator=Operator.XOR, children=[salting_process, packaging_design])
xor3 = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, transport_prep])
xor4 = OperatorPOWL(operator=Operator.XOR, children=[delivery_tracking, customer_feedback])
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, xor3])
loop2 = OperatorPOWL(operator=Operator.LOOP, children=[flavor_profiling, xor4])
loop3 = OperatorPOWL(operator=Operator.LOOP, children=[blockchain_entry, quality_audit])

# Define the POWL partial order
root = StrictPartialOrder(nodes=[milk_sourcing, culture_selection, xor1, xor2, loop1, loop2, loop3, xor3, xor4])
root.order.add_edge(milk_sourcing, culture_selection)
root.order.add_edge(culture_selection, xor1)
root.order.add_edge(xor1, xor2)
root.order.add_edge(xor2, loop1)
root.order.add_edge(loop1, loop2)
root.order.add_edge(loop2, loop3)
root.order.add_edge(loop3, xor3)
root.order.add_edge(xor3, xor4)
root.order.add_edge(xor4, loop1)