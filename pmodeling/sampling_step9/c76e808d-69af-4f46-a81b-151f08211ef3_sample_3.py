import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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
skip_milk_sourcing = SilentTransition(label='Milk Sourcing')
skip_culture_selection = SilentTransition(label='Culture Selection')
skip_milk_testing = SilentTransition(label='Milk Testing')
skip_curd_formation = SilentTransition(label='Curd Formation')
skip_whey_separation = SilentTransition(label='Whey Separation')
skip_molding_cheese = SilentTransition(label='Molding Cheese')
skip_salting_process = SilentTransition(label='Salting Process')
skip_aging_setup = SilentTransition(label='Aging Setup')
skip_env_monitoring = SilentTransition(label='Env Monitoring')
skip_flavor_profiling = SilentTransition(label='Flavor Profiling')
skip_packaging_design = SilentTransition(label='Packaging Design')
skip_blockchain_entry = SilentTransition(label='Blockchain Entry')
skip_quality_audit = SilentTransition(label='Quality Audit')
skip_retail_sync = SilentTransition(label='Retail Sync')
skip_transport_prep = SilentTransition(label='Transport Prep')
skip_delivery_tracking = SilentTransition(label='Delivery Tracking')
skip_customer_feedback = SilentTransition(label='Customer Feedback')

# Define the choices
milk_sourcing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_sourcing, skip_milk_sourcing])
culture_selection_choice = OperatorPOWL(operator=Operator.XOR, children=[culture_selection, skip_culture_selection])
milk_testing_choice = OperatorPOWL(operator=Operator.XOR, children=[milk_testing, skip_milk_testing])
curd_formation_choice = OperatorPOWL(operator=Operator.XOR, children=[curd_formation, skip_curd_formation])
whey_separation_choice = OperatorPOWL(operator=Operator.XOR, children=[whey_separation, skip_whey_separation])
molding_cheese_choice = OperatorPOWL(operator=Operator.XOR, children=[molding_cheese, skip_molding_cheese])
salting_process_choice = OperatorPOWL(operator=Operator.XOR, children=[salting_process, skip_salting_process])
aging_setup_choice = OperatorPOWL(operator=Operator.XOR, children=[aging_setup, skip_aging_setup])
env_monitoring_choice = OperatorPOWL(operator=Operator.XOR, children=[env_monitoring, skip_env_monitoring])
flavor_profiling_choice = OperatorPOWL(operator=Operator.XOR, children=[flavor_profiling, skip_flavor_profiling])
packaging_design_choice = OperatorPOWL(operator=Operator.XOR, children=[packaging_design, skip_packaging_design])
blockchain_entry_choice = OperatorPOWL(operator=Operator.XOR, children=[blockchain_entry, skip_blockchain_entry])
quality_audit_choice = OperatorPOWL(operator=Operator.XOR, children=[quality_audit, skip_quality_audit])
retail_sync_choice = OperatorPOWL(operator=Operator.XOR, children=[retail_sync, skip_retail_sync])
transport_prep_choice = OperatorPOWL(operator=Operator.XOR, children=[transport_prep, skip_transport_prep])
delivery_tracking_choice = OperatorPOWL(operator=Operator.XOR, children=[delivery_tracking, skip_delivery_tracking])
customer_feedback_choice = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, skip_customer_feedback])

# Define the loop
loop = OperatorPOWL(operator=Operator.LOOP, children=[milk_sourcing_choice, culture_selection_choice, milk_testing_choice, curd_formation_choice, whey_separation_choice, molding_cheese_choice, salting_process_choice, aging_setup_choice, env_monitoring_choice, flavor_profiling_choice, packaging_design_choice, blockchain_entry_choice, quality_audit_choice, retail_sync_choice, transport_prep_choice, delivery_tracking_choice, customer_feedback_choice])

# Define the root
root = StrictPartialOrder(nodes=[loop])
root.order.add_edge(loop, loop)

print(root)