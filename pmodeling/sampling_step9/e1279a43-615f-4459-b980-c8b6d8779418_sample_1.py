import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model for the urban vertical farming process
site_analysis = Transition(label='Site Analysis')
infrastructure_setup = Transition(label='Infrastructure Setup')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_cycle = Transition(label='Planting Cycle')
climate_adjust = Transition(label='Climate Adjust')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
harvesting_mode = Transition(label='Harvesting Mode')
quality_check = Transition(label='Quality Check')
packaging_phase = Transition(label='Packaging Phase')
cold_storage = Transition(label='Cold Storage')
order_dispatch = Transition(label='Order Dispatch')
waste_recycling = Transition(label='Waste Recycling')
system_maintain = Transition(label='System Maintain')

skip = SilentTransition()

# Define the process tree structure
site_analysis_infrastructure = OperatorPOWL(operator=Operator.XOR, children=[site_analysis, infrastructure_setup])
seed_nutrient_mix = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])
planting_climate = OperatorPOWL(operator=Operator.XOR, children=[planting_cycle, climate_adjust])
growth_monitor_pest = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])
harvest_quality = OperatorPOWL(operator=Operator.XOR, children=[harvesting_mode, quality_check])
packaging_cold = OperatorPOWL(operator=Operator.XOR, children=[packaging_phase, cold_storage])
order_dispatch_waste = OperatorPOWL(operator=Operator.XOR, children=[order_dispatch, waste_recycling])
system_maintain = OperatorPOWL(operator=Operator.XOR, children=[system_maintain])

# Define the loop nodes
loop1 = OperatorPOWL(operator=Operator.LOOP, children=[seed_nutrient_mix, planting_climate, growth_monitor_pest, harvesting_mode, packaging_cold, order_dispatch_waste, system_maintain])

root = StrictPartialOrder(nodes=[site_analysis_infrastructure, loop1])
root.order.add_edge(site_analysis_infrastructure, loop1)

# Save the final result in the variable 'root'
print(root)