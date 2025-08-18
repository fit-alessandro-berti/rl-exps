from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_acquisition = Transition(label='Site Acquisition')
impact_assess = Transition(label='Impact Assess')
modular_setup = Transition(label='Modular Setup')
crop_planting = Transition(label='Crop Planting')
nutrient_control = Transition(label='Nutrient Control')
pest_control = Transition(label='Pest Control')
growth_monitor = Transition(label='Growth Monitor')
community_engage = Transition(label='Community Engage')
yield_forecast = Transition(label='Yield Forecast')
supply_coordinate = Transition(label='Supply Coordinate')
compliance_check = Transition(label='Compliance Check')
waste_recycle = Transition(label='Waste Recycle')
energy_optimize = Transition(label='Energy Optimize')
market_strategy = Transition(label='Market Strategy')
performance_review = Transition(label='Performance Review')

# Define silent transitions (if any)
skip = SilentTransition()

# Define loop nodes
loop_modular_setup = OperatorPOWL(operator=Operator.LOOP, children=[modular_setup])
loop_crop_planting = OperatorPOWL(operator=Operator.LOOP, children=[crop_planting])
loop_yield_forecast = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast])

# Define choice nodes
choice_pest_control = OperatorPOWL(operator=Operator.XOR, children=[pest_control, skip])
choice_supply_coordinate = OperatorPOWL(operator=Operator.XOR, children=[supply_coordinate, skip])
choice_compliance_check = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, skip])
choice_waste_recycle = OperatorPOWL(operator=Operator.XOR, children=[waste_recycle, skip])
choice_energy_optimize = OperatorPOWL(operator=Operator.XOR, children=[energy_optimize, skip])
choice_market_strategy = OperatorPOWL(operator=Operator.XOR, children=[market_strategy, skip])

# Define the root of the POWL model
root = StrictPartialOrder(nodes=[
    site_acquisition,
    impact_assess,
    modular_setup,
    loop_modular_setup,
    crop_planting,
    loop_crop_planting,
    nutrient_control,
    choice_pest_control,
    community_engage,
    yield_forecast,
    loop_yield_forecast,
    supply_coordinate,
    choice_supply_coordinate,
    compliance_check,
    choice_compliance_check,
    waste_recycle,
    choice_waste_recycle,
    energy_optimize,
    choice_energy_optimize,
    market_strategy,
    choice_market_strategy,
    performance_review
])

# Add dependencies between nodes
root.order.add_edge(site_acquisition, impact_assess)
root.order.add_edge(impact_assess, modular_setup)
root.order.add_edge(modular_setup, loop_modular_setup)
root.order.add_edge(loop_modular_setup, modular_setup)
root.order.add_edge(modular_setup, crop_planting)
root.order.add_edge(crop_planting, loop_crop_planting)
root.order.add_edge(loop_crop_planting, crop_planting)
root.order.add_edge(crop_planting, nutrient_control)
root.order.add_edge(nutrient_control, choice_pest_control)
root.order.add_edge(choice_pest_control, pest_control)
root.order.add_edge(choice_pest_control, skip)
root.order.add_edge(pest_control, community_engage)
root.order.add_edge(community_engage, yield_forecast)
root.order.add_edge(yield_forecast, loop_yield_forecast)
root.order.add_edge(loop_yield_forecast, yield_forecast)
root.order.add_edge(yield_forecast, supply_coordinate)
root.order.add_edge(supply_coordinate, choice_supply_coordinate)
root.order.add_edge(choice_supply_coordinate, supply_coordinate)
root.order.add_edge(supply_coordinate, compliance_check)
root.order.add_edge(compliance_check, choice_compliance_check)
root.order.add_edge(choice_compliance_check, compliance_check)
root.order.add_edge(compliance_check, waste_recycle)
root.order.add_edge(waste_recycle, choice_waste_recycle)
root.order.add_edge(choice_waste_recycle, waste_recycle)
root.order.add_edge(waste_recycle, energy_optimize)
root.order.add_edge(energy_optimize, choice_energy_optimize)
root.order.add_edge(choice_energy_optimize, energy_optimize)
root.order.add_edge(energy_optimize, market_strategy)
root.order.add_edge(market_strategy, choice_market_strategy)
root.order.add_edge(choice_market_strategy, market_strategy)
root.order.add_edge(market_strategy, performance_review)

# Print the root
print(root)