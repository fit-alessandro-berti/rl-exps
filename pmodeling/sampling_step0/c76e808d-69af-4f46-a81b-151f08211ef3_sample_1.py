from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions for each activity
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

# Define the silent transitions
skip = SilentTransition()

# Define the exclusive choice between culture selection and milk sourcing
culture_or_milk = OperatorPOWL(operator=Operator.XOR, children=[culture_selection, milk_sourcing])

# Define the loop for aging setup and environmental monitoring
aging_loop = OperatorPOWL(operator=Operator.LOOP, children=[aging_setup, env_monitoring])

# Define the exclusive choice between packaging design and blockchain entry
packaging_or_blockchain = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, blockchain_entry])

# Define the exclusive choice between quality audit and retail sync
audit_or_sync = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, retail_sync])

# Define the exclusive choice between transport prep and delivery tracking
transport_or_delivery = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, delivery_tracking])

# Define the exclusive choice between customer feedback and end
feedback_or_end = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip])

# Define the root POWL model
root = StrictPartialOrder(nodes=[milk_sourcing, culture_or_milk, curd_formation, whey_separation, molding_cheese, salting_process, aging_loop, flavor_profiling, packaging_or_blockchain, audit_or_sync, transport_or_delivery, feedback_or_end])
root.order.add_edge(milk_sourcing, culture_or_milk)
root.order.add_edge(culture_or_milk, curd_formation)
root.order.add_edge(curd_formation, whey_separation)
root.order.add_edge(whey_separation, molding_cheese)
root.order.add_edge(molding_cheese, salting_process)
root.order.add_edge(salting_process, aging_loop)
root.order.add_edge(aging_loop, flavor_profiling)
root.order.add_edge(flavor_profiling, packaging_or_blockchain)
root.order.add_edge(packaging_or_blockchain, audit_or_sync)
root.order.add_edge(audit_or_sync, transport_or_delivery)
root.order.add_edge(transport_or_delivery, feedback_or_end)
root.order.add_edge(feedback_or_end, customer_feedback)
root.order.add_edge(customer_feedback, skip)