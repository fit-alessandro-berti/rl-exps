import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey       = Transition(label='Site Survey')
system_design     = Transition(label='System Design')
module_build      = Transition(label='Module Build')
nutrient_mix      = Transition(label='Nutrient Mix')
seed_selection    = Transition(label='Seed Selection')
planting_plan     = Transition(label='Planting Plan')
irrigation_setup  = Transition(label='Irrigation Setup')
climate_control   = Transition(label='Climate Control')
lighting_adjust   = Transition(label='Lighting Adjust')
pest_monitor      = Transition(label='Pest Monitor')
waste_cycle       = Transition(label='Waste Cycle')
data_capture      = Transition(label='Data Capture')
yield_forecast    = Transition(label='Yield Forecast')
regulation_check  = Transition(label='Regulation Check')
community_meet    = Transition(label='Community Meet')
harvest_prep      = Transition(label='Harvest Prep')
market_link       = Transition(label='Market Link')

# Loop for continuous data capture and yield forecasting
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_capture, yield_forecast])

# Build the partial order
root = StrictPartialOrder(nodes=[
    site_survey,
    system_design,
    module_build,
    nutrient_mix,
    seed_selection,
    planting_plan,
    irrigation_setup,
    climate_control,
    lighting_adjust,
    pest_monitor,
    waste_cycle,
    loop_data,
    regulation_check,
    community_meet,
    harvest_prep,
    market_link
])

# Define the control-flow dependencies
root.order.add_edge(site_survey, system_design)
root.order.add_edge(system_design, module_build)
root.order.add_edge(module_build, nutrient_mix)
root.order.add_edge(module_build, seed_selection)
root.order.add_edge(nutrient_mix, planting_plan)
root.order.add_edge(seed_selection, planting_plan)
root.order.add_edge(planting_plan, irrigation_setup)
root.order.add_edge(planting_plan, climate_control)
root.order.add_edge(planting_plan, lighting_adjust)
root.order.add_edge(irrigation_setup, pest_monitor)
root.order.add_edge(climate_control, pest_monitor)
root.order.add_edge(lighting_adjust, pest_monitor)
root.order.add_edge(pest_monitor, waste_cycle)
root.order.add_edge(waste_cycle, loop_data)
root.order.add_edge(loop_data, regulation_check)
root.order.add_edge(loop_data, community_meet)
root.order.add_edge(regulation_check, harvest_prep)
root.order.add_edge(community_meet, harvest_prep)
root.order.add_edge(harvest_prep, market_link)

print(root)