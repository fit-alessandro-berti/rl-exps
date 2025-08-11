import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define silent activities
skip = SilentTransition()

# Define loops and XORs
climate_loop = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, lighting_control])
audit_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_audit, water_reclaim])
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, market_sync])
supply_chain_loop = OperatorPOWL(operator=Operator.LOOP, children=[supply_chain, yield_forecast])

# Define XORs
seed_xor = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, skip])
community_xor = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[site_analysis, zoning_review, modular_design, climate_loop, audit_loop, staff_loop, seed_xor, community_xor, supply_chain_loop])
root.order.add_edge(site_analysis, zoning_review)
root.order.add_edge(site_analysis, modular_design)
root.order.add_edge(zoning_review, modular_design)
root.order.add_edge(modular_design, climate_loop)
root.order.add_edge(modular_design, audit_loop)
root.order.add_edge(modular_design, seed_xor)
root.order.add_edge(modular_design, community_xor)
root.order.add_edge(modular_design, supply_chain_loop)
root.order.add_edge(climate_loop, audit_loop)
root.order.add_edge(climate_loop, supply_chain_loop)
root.order.add_edge(audit_loop, supply_chain_loop)
root.order.add_edge(seed_xor, community_xor)
root.order.add_edge(seed_xor, supply_chain_loop)
root.order.add_edge(community_xor, supply_chain_loop)

# Print the root of the POWL model
print(root)