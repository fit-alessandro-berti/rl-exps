import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
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

# Define silent transitions
skip = SilentTransition()

# Define partial order nodes
site_infrastructure = OperatorPOWL(operator=Operator.PO, children=[site_analysis, infrastructure_setup])
seed_nutrient = OperatorPOWL(operator=Operator.PO, children=[seed_selection, nutrient_mix])
plant_climate = OperatorPOWL(operator=Operator.PO, children=[planting_cycle, climate_adjust])
growth_monitor_control = OperatorPOWL(operator=Operator.PO, children=[growth_monitor, pest_control])
harvest_quality = OperatorPOWL(operator=Operator.PO, children=[harvesting_mode, quality_check])
packaging_cold = OperatorPOWL(operator=Operator.PO, children=[packaging_phase, cold_storage])
dispatch_recycle = OperatorPOWL(operator=Operator.PO, children=[order_dispatch, waste_recycling])
maintain = OperatorPOWL(operator=Operator.PO, children=[system_maintain])

# Define exclusive choice nodes
site_infrastructure_seed_nutrient = OperatorPOWL(operator=Operator.XOR, children=[site_infrastructure, seed_nutrient])
plant_climate_growth_monitor_control = OperatorPOWL(operator=Operator.XOR, children=[plant_climate, growth_monitor_control])
harvest_quality_packaging_cold = OperatorPOWL(operator=Operator.XOR, children=[harvest_quality, packaging_cold])
dispatch_recycle_maintain = OperatorPOWL(operator=Operator.XOR, children=[dispatch_recycle, maintain])

# Define the root node
root = StrictPartialOrder(nodes=[site_infrastructure_seed_nutrient, plant_climate_growth_monitor_control, harvesting_quality_packaging_cold, dispatch_recycle_maintain])
root.order.add_edge(site_infrastructure_seed_nutrient, plant_climate_growth_monitor_control)
root.order.add_edge(plant_climate_growth_monitor_control, harvesting_quality_packaging_cold)
root.order.add_edge(harvesting_quality_packaging_cold, dispatch_recycle_maintain)