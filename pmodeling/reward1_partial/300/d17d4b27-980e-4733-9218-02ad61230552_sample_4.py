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

# Define connections
site_analysis_to_zoning = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, zoning_review])
zoning_to_modular = OperatorPOWL(operator=Operator.XOR, children=[zoning_review, modular_design])
modular_to_climate = OperatorPOWL(operator=Operator.XOR, children=[modular_design, climate_setup])
climate_to_nutrient = OperatorPOWL(operator=Operator.XOR, children=[climate_setup, nutrient_mix])
nutrient_to_seed = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, seed_selection])
seed_to_ai = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, ai_monitoring])
ai_to_lighting = OperatorPOWL(operator=Operator.XOR, children=[ai_monitoring, lighting_control])
lighting_to_energy = OperatorPOWL(operator=Operator.XOR, children=[lighting_control, energy_audit])
energy_to_water = OperatorPOWL(operator=Operator.XOR, children=[energy_audit, water_reclaim])
water_to_waste = OperatorPOWL(operator=Operator.XOR, children=[water_reclaim, waste_sorting])
waste_to_community = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, community_meet])
community_to_staff = OperatorPOWL(operator=Operator.XOR, children=[community_meet, staff_training])
staff_to_yield = OperatorPOWL(operator=Operator.XOR, children=[staff_training, yield_forecast])
yield_to_market = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, market_sync])
market_to_supply = OperatorPOWL(operator=Operator.XOR, children=[market_sync, supply_chain])

# Define root node with all activities
root = StrictPartialOrder(nodes=[
    site_analysis_to_zoning,
    zoning_to_modular,
    modular_to_climate,
    climate_to_nutrient,
    nutrient_to_seed,
    seed_to_ai,
    ai_to_lighting,
    lighting_to_energy,
    energy_to_water,
    water_to_waste,
    waste_to_community,
    community_to_staff,
    staff_to_yield,
    yield_to_market,
    market_to_supply
])

# Add dependencies
root.order.add_edge(site_analysis_to_zoning, zoning_to_modular)
root.order.add_edge(zoning_to_modular, modular_to_climate)
root.order.add_edge(modular_to_climate, climate_to_nutrient)
root.order.add_edge(climate_to_nutrient, nutrient_to_seed)
root.order.add_edge(nutrient_to_seed, seed_to_ai)
root.order.add_edge(seed_to_ai, ai_to_lighting)
root.order.add_edge(ai_to_lighting, lighting_to_energy)
root.order.add_edge(lighting_to_energy, energy_to_water)
root.order.add_edge(energy_to_water, water_to_waste)
root.order.add_edge(water_to_waste, waste_to_community)
root.order.add_edge(waste_to_community, community_to_staff)
root.order.add_edge(community_to_staff, staff_to_yield)
root.order.add_edge(staff_to_yield, yield_to_market)
root.order.add_edge(yield_to_market, market_to_supply)

print(root)