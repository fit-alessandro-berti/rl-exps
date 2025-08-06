import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions
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

# Define transitions
skip = SilentTransition()

# Define loop and choice nodes
loop_site_analysis = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, zoning_review])
choice_modular_design = OperatorPOWL(operator=Operator.XOR, children=[modular_design, skip])
loop_climate_setup = OperatorPOWL(operator=Operator.LOOP, children=[climate_setup, energy_audit])
choice_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, skip])
choice_ai_monitoring = OperatorPOWL(operator=Operator.XOR, children=[ai_monitoring, skip])
choice_lighting_control = OperatorPOWL(operator=Operator.XOR, children=[lighting_control, skip])
choice_water_reclaim = OperatorPOWL(operator=Operator.XOR, children=[water_reclaim, skip])
choice_waste_sorting = OperatorPOWL(operator=Operator.XOR, children=[waste_sorting, skip])
choice_community_meet = OperatorPOWL(operator=Operator.XOR, children=[community_meet, skip])
choice_staff_training = OperatorPOWL(operator=Operator.XOR, children=[staff_training, skip])
choice_yield_forecast = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, skip])
choice_market_sync = OperatorPOWL(operator=Operator.XOR, children=[market_sync, skip])
choice_supply_chain = OperatorPOWL(operator=Operator.XOR, children=[supply_chain, skip])

# Define root node
root = StrictPartialOrder(nodes=[loop_site_analysis, choice_modular_design, loop_climate_setup, choice_nutrient_mix, choice_ai_monitoring, choice_lighting_control, choice_water_reclaim, choice_waste_sorting, choice_community_meet, choice_staff_training, choice_yield_forecast, choice_market_sync, choice_supply_chain])
root.order.add_edge(loop_site_analysis, choice_modular_design)
root.order.add_edge(choice_modular_design, loop_climate_setup)
root.order.add_edge(loop_climate_setup, choice_nutrient_mix)
root.order.add_edge(choice_nutrient_mix, choice_ai_monitoring)
root.order.add_edge(choice_ai_monitoring, choice_lighting_control)
root.order.add_edge(choice_lighting_control, choice_water_reclaim)
root.order.add_edge(choice_water_reclaim, choice_waste_sorting)
root.order.add_edge(choice_waste_sorting, choice_community_meet)
root.order.add_edge(choice_community_meet, choice_staff_training)
root.order.add_edge(choice_staff_training, choice_yield_forecast)
root.order.add_edge(choice_yield_forecast, choice_market_sync)
root.order.add_edge(choice_market_sync, choice_supply_chain)