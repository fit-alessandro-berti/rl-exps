import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_analysis = Transition(label='Site Analysis')
zoning_review = Transition(label='Zoning Review')
modular_design = Transition(label='Modular Design')
climate_setup = Transition(label='Climate Setup')
nutrient_mix = Transition(label='Nutrient Mix')
seed_selection = Transition(label='Seed Selection')
ai_monitoring = Transition(label='AI Monitoring')
lighting_control = Transition(label='Lighting Control')
energy_audit = Transition(label='Energy Audit')
water_reclaim = Transition(label='Water Reclaim')
waste_sorting = Transition(label='Waste Sorting')
community_meet = Transition(label='Community Meet')
staff_training = Transition(label='Staff Training')
yield_forecast = Transition(label='Yield Forecast')
market_sync = Transition(label='Market Sync')
supply_chain = Transition(label='Supply Chain')

# Define silent transitions for loop nodes
skip = SilentTransition()

# Define loop nodes
site_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, zoning_review])
design_loop = OperatorPOWL(operator=Operator.LOOP, children=[modular_design, climate_setup])
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_reclaim, waste_sorting])

# Define exclusive choice nodes
exclusive_choice = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, ai_monitoring])

# Define the root model
root = StrictPartialOrder(nodes=[site_loop, design_loop, water_loop, exclusive_choice, yield_forecast, market_sync, supply_chain])
root.order.add_edge(site_loop, design_loop)
root.order.add_edge(design_loop, water_loop)
root.order.add_edge(water_loop, exclusive_choice)
root.order.add_edge(exclusive_choice, yield_forecast)
root.order.add_edge(yield_forecast, market_sync)
root.order.add_edge(market_sync, supply_chain)

# Print the root model
print(root)