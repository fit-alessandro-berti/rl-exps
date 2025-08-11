import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
material_sourcing = Transition(label='Material Sourcing')
forager_dispatch = Transition(label='Forager Dispatch')
authenticity_check = Transition(label='Authenticity Check')
batch_scheduling = Transition(label='Batch Scheduling')
artisan_allocation = Transition(label='Artisan Allocation')
craft_assembly = Transition(label='Craft Assembly')
quality_inspection = Transition(label='Quality Inspection')
blockchain_update = Transition(label='Blockchain Update')
demand_forecast = Transition(label='Demand Forecast')
price_adjustment = Transition(label='Price Adjustment')
compliance_review = Transition(label='Compliance Review')
logistics_planning = Transition(label='Logistics Planning')
distributor_sync = Transition(label='Distributor Sync')
customer_feedback = Transition(label='Customer Feedback')
product_refinement = Transition(label='Product Refinement')
reputation_audit = Transition(label='Reputation Audit')
seasonal_review = Transition(label='Seasonal Review')

# Define silent transitions
skip = SilentTransition()

# Define loops and choices
# Material Sourcing -> Forager Dispatch -> Authenticity Check -> Batch Scheduling
material_sourcing_dispatch = OperatorPOWL(operator=Operator.XOR, children=[material_sourcing, forager_dispatch])
forager_dispatch_authenticity = OperatorPOWL(operator=Operator.XOR, children=[forager_dispatch, authenticity_check])
authenticity_check_batch = OperatorPOWL(operator=Operator.XOR, children=[authenticity_check, batch_scheduling])
loop_material_sourcing = StrictPartialOrder(nodes=[material_sourcing_dispatch, forager_dispatch_authenticity, authenticity_check_batch])
loop_material_sourcing.order.add_edge(material_sourcing_dispatch, forager_dispatch_authenticity)
loop_material_sourcing.order.add_edge(forager_dispatch_authenticity, authenticity_check_batch)
loop_material_sourcing.order.add_edge(authenticity_check_batch, material_sourcing_dispatch)

# Craft Assembly -> Quality Inspection -> Blockchain Update -> Demand Forecast
craft_assembly_inspection = OperatorPOWL(operator=Operator.XOR, children=[craft_assembly, quality_inspection])
quality_inspection_blockchain = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, blockchain_update])
blockchain_update_demand = OperatorPOWL(operator=Operator.XOR, children=[blockchain_update, demand_forecast])
loop_craft_assembly = StrictPartialOrder(nodes=[craft_assembly_inspection, quality_inspection_blockchain, blockchain_update_demand])
loop_craft_assembly.order.add_edge(craft_assembly_inspection, quality_inspection_blockchain)
loop_craft_assembly.order.add_edge(quality_inspection_blockchain, blockchain_update_demand)
loop_craft_assembly.order.add_edge(blockchain_update_demand, craft_assembly_inspection)

# Price Adjustment -> Compliance Review -> Logistics Planning -> Distributor Sync
price_adjustment_compliance = OperatorPOWL(operator=Operator.XOR, children=[price_adjustment, compliance_review])
compliance_review_logistics = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, logistics_planning])
logistics_planning_distributor = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, distributor_sync])
loop_price_adjustment = StrictPartialOrder(nodes=[price_adjustment_compliance, compliance_review_logistics, logistics_planning_distributor])
loop_price_adjustment.order.add_edge(price_adjustment_compliance, compliance_review_logistics)
loop_price_adjustment.order.add_edge(compliance_review_logistics, logistics_planning_distributor)
loop_price_adjustment.order.add_edge(logistics_planning_distributor, price_adjustment_compliance)

# Customer Feedback -> Product Refinement -> Reputation Audit -> Seasonal Review
customer_feedback_refinement = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, product_refinement])
product_refinement_audit = OperatorPOWL(operator=Operator.XOR, children=[product_refinement, reputation_audit])
reputation_audit_seasonal = OperatorPOWL(operator=Operator.XOR, children=[reputation_audit, seasonal_review])
loop_customer_feedback = StrictPartialOrder(nodes=[customer_feedback_refinement, product_refinement_audit, reputation_audit_seasonal])
loop_customer_feedback.order.add_edge(customer_feedback_refinement, product_refinement_audit)
loop_customer_feedback.order.add_edge(product_refinement_audit, reputation_audit_seasonal)
loop_customer_feedback.order.add_edge(reputation_audit_seasonal, customer_feedback_refinement)

# Final root node combining all loops
root = StrictPartialOrder(nodes=[loop_material_sourcing, loop_craft_assembly, loop_price_adjustment, loop_customer_feedback])
root.order.add_edge(loop_material_sourcing, loop_craft_assembly)
root.order.add_edge(loop_craft_assembly, loop_price_adjustment)
root.order.add_edge(loop_price_adjustment, loop_customer_feedback)
root.order.add_edge(loop_customer_feedback, loop_material_sourcing)