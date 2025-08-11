from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions
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

# Define operators
xor_foraging = OperatorPOWL(operator=Operator.XOR, children=[forager_dispatch, SilentTransition()])
xor_inspection = OperatorPOWL(operator=Operator.XOR, children=[quality_inspection, SilentTransition()])
xor_forecast = OperatorPOWL(operator=Operator.XOR, children=[demand_forecast, SilentTransition()])
xor_reputation = OperatorPOWL(operator=Operator.XOR, children=[reputation_audit, SilentTransition()])

loop_authenticity = OperatorPOWL(operator=Operator.LOOP, children=[authenticity_check, xor_inspection])
loop_allocation = OperatorPOWL(operator=Operator.LOOP, children=[artisan_allocation, xor_foraging])
loop_forecast = OperatorPOWL(operator=Operator.LOOP, children=[price_adjustment, xor_forecast])
loop_reputation = OperatorPOWL(operator=Operator.LOOP, children=[compliance_review, xor_reputation])

xor_product = OperatorPOWL(operator=Operator.XOR, children=[logistics_planning, SilentTransition()])
xor_distributor = OperatorPOWL(operator=Operator.XOR, children=[distributor_sync, SilentTransition()])
xor_feedback = OperatorPOWL(operator=Operator.XOR, children=[customer_feedback, SilentTransition()])

xor_refinement = OperatorPOWL(operator=Operator.XOR, children=[product_refinement, SilentTransition()])

loop_seasonal = OperatorPOWL(operator=Operator.LOOP, children=[batch_scheduling, xor_seasonal])

xor_final = OperatorPOWL(operator=Operator.XOR, children=[xor_product, xor_distributor, xor_feedback, xor_refinement])

root = StrictPartialOrder(nodes=[loop_seasonal, xor_final])
root.order.add_edge(loop_seasonal, xor_final)

print(root)