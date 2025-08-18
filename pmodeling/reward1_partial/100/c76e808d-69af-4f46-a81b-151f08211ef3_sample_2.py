import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

Milk_Sourcing = Transition(label='Milk Sourcing')
Culture_Selection = Transition(label='Culture Selection')
Milk_Testing = Transition(label='Milk Testing')
Curd_Formation = Transition(label='Curd Formation')
Whey_Separation = Transition(label='Whey Separation')
Molding_Cheese = Transition(label='Molding Cheese')
Salting_Process = Transition(label='Salting Process')
Aging_Setup = Transition(label='Aging Setup')
Env_Monitoring = Transition(label='Env Monitoring')
Flavor_Profiling = Transition(label='Flavor Profiling')
Packaging_Design = Transition(label='Packaging Design')
Blockchain_Entry = Transition(label='Blockchain Entry')
Quality_Audit = Transition(label='Quality Audit')
Retail_Sync = Transition(label='Retail Sync')
Transport_Prep = Transition(label='Transport Prep')
Delivery_Tracking = Transition(label='Delivery Tracking')
Customer_Feedback = Transition(label='Customer Feedback')

skip = SilentTransition()

# Milk Sourcing -> Culture Selection
milk_sourcing_to_culture_selection = OperatorPOWL(operator=Operator.SEQUENCE, children=[Milk_Sourcing, Culture_Selection])

# Milk Testing -> Curd Formation
milk_testing_to_curd_formation = OperatorPOWL(operator=Operator.SEQUENCE, children=[Milk_Testing, Curd_Formation])

# Curd Formation -> Whey Separation
curd_formation_to_whey_separation = OperatorPOWL(operator=Operator.SEQUENCE, children=[Curd_Formation, Whey_Separation])

# Whey Separation -> Molding Cheese
whey_separation_to_molding_cheese = OperatorPOWL(operator=Operator.SEQUENCE, children=[Whey_Separation, Molding_Cheese])

# Molding Cheese -> Salting Process
molding_cheese_to_salting_process = OperatorPOWL(operator=Operator.SEQUENCE, children=[Molding_Cheese, Salting_Process])

# Salting Process -> Aging Setup
salting_process_to_aging_setup = OperatorPOWL(operator=Operator.SEQUENCE, children=[Salting_Process, Aging_Setup])

# Aging Setup -> Env Monitoring
aging_setup_to_env_monitoring = OperatorPOWL(operator=Operator.SEQUENCE, children=[Aging_Setup, Env_Monitoring])

# Env Monitoring -> Flavor Profiling
env_monitoring_to_flavor_profiling = OperatorPOWL(operator=Operator.SEQUENCE, children=[Env_Monitoring, Flavor_Profiling])

# Flavor Profiling -> Packaging Design
flavor_profiling_to_packaging_design = OperatorPOWL(operator=Operator.SEQUENCE, children=[Flavor_Profiling, Packaging_Design])

# Packaging Design -> Blockchain Entry
packaging_design_to_blockchain_entry = OperatorPOWL(operator=Operator.SEQUENCE, children=[Packaging_Design, Blockchain_Entry])

# Blockchain Entry -> Quality Audit
blockchain_entry_to_quality_audit = OperatorPOWL(operator=Operator.SEQUENCE, children=[Blockchain_Entry, Quality_Audit])

# Quality Audit -> Retail Sync
quality_audit_to_retail_sync = OperatorPOWL(operator=Operator.SEQUENCE, children=[Quality_Audit, Retail_Sync])

# Retail Sync -> Transport Prep
retail_sync_to_transport_prep = OperatorPOWL(operator=Operator.SEQUENCE, children=[Retail_Sync, Transport_Prep])

# Transport Prep -> Delivery Tracking
transport_prep_to_delivery_tracking = OperatorPOWL(operator=Operator.SEQUENCE, children=[Transport_Prep, Delivery_Tracking])

# Delivery Tracking -> Customer Feedback
delivery_tracking_to_customer_feedback = OperatorPOWL(operator=Operator.SEQUENCE, children=[Delivery_Tracking, Customer_Feedback])

# Root model
root = StrictPartialOrder(nodes=[milk_sourcing_to_culture_selection, milk_testing_to_curd_formation, whey_separation_to_molding_cheese, molding_cheese_to_salting_process, salting_process_to_aging_setup, aging_setup_to_env_monitoring, env_monitoring_to_flavor_profiling, flavor_profiling_to_packaging_design, packaging_design_to_blockchain_entry, blockchain_entry_to_quality_audit, quality_audit_to_retail_sync, retail_sync_to_transport_prep, transport_prep_to_delivery_tracking, delivery_tracking_to_customer_feedback])