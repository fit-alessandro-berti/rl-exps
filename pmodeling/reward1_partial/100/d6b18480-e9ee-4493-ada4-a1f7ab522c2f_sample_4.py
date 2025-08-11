import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the transitions
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

# Define the POWL model
xor_blockchain = OperatorPOWL(operator=Operator.XOR, children=[blockchain_update, SilentTransition()])
xor_forecast = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, SilentTransition()])
xor_price = OperatorPOWL(operator=Operator.XOR, children=[price_adjustment, SilentTransition()])
xor_compliance = OperatorPOWL(operator=Operator.XOR, children=[compliance_review, SilentTransition()])
xor_logistics = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, SilentTransition()])
xor_distributor = OperatorPOWL(operator=Operator.XOR, children=[distributor_sync, SilentTransition()])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, SilentTransition()])
xor_refinement = OperatorPOWL(operator=Operator.XOR, children=[product_refinement, SilentTransition()])
xor_reputation = OperatorPOWL(operator=Operator.XOR, children=[reputation_audit, SilentTransition()])
xor_seasonal = OperatorPOWL(operator=Operator.XOR, children=[seasonal_review, SilentTransition()])

xor_authenticity = OperatorPOWL(operator=Operator.XOR, children=[authenticity_check, SilentTransition()])

xor_foraging = OperatorPOWL(operator=Operator.XOR, children=[forager_dispatch, SilentTransition()])

xor_artisan = OperatorPOWL(operator=Operator.XOR, children=[artisan_allocation, SilentTransition()])

xor_batch = OperatorPOWL(operator=Operator.XOR, children=[batch_scheduling, SilentTransition()])

xor_craft = OperatorPOWL(operator=Operator.XOR, children=[craft_assembly, SilentTransition()])

xor_inspection = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, SilentTransition()])

root = StrictPartialOrder(nodes=[
    xor_blockchain, xor_forecast, xor_price, xor_compliance, xor_logistics, xor_distributor, xor_feedback, xor_refinement, xor_reputation, xor_seasonal, xor_authenticity, xor_foraging, xor_artisan, xor_batch, xor_craft, xor_inspection])

root.order.add_edge(xor_blockchain, xor_forecast)
root.order.add_edge(xor_forecast, xor_price)
root.order.add_edge(xor_price, xor_compliance)
root.order.add_edge(xor_compliance, xor_logistics)
root.order.add_edge(xor_logistics, xor_distributor)
root.order.add_edge(xor_distributor, xor_feedback)
root.order.add_edge(xor_feedback, xor_refinement)
root.order.add_edge(xor_refinement, xor_reputation)
root.order.add_edge(xor_reputation, xor_seasonal)
root.order.add_edge(xor_seasonal, xor_authenticity)
root.order.add_edge(xor_authenticity, xor_foraging)
root.order.add_edge(xor_foraging, xor_artisan)
root.order.add_edge(xor_artisan, xor_batch)
root.order.add_edge(xor_batch, xor_craft)
root.order.add_edge(xor_craft, xor_inspection)
root.order.add_edge(xor_inspection, xor_blockchain)

# Print the root model
print(root)