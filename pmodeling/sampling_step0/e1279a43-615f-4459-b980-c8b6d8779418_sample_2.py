import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

site_analysis_loop = OperatorPOWL(operator=Operator.LOOP, children=[site_analysis, infrastructure_setup])
seed_selection_loop = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection, nutrient_mix])
planting_cycle_loop = OperatorPOWL(operator=Operator.LOOP, children=[planting_cycle, climate_adjust, growth_monitor, pest_control, harvesting_mode, quality_check, packaging_phase])
cold_storage_loop = OperatorPOWL(operator=Operator.LOOP, children=[cold_storage, order_dispatch])
waste_recycling_loop = OperatorPOWL(operator=Operator.LOOP, children=[waste_recycling, system_maintain])

root = StrictPartialOrder(nodes=[site_analysis_loop, seed_selection_loop, planting_cycle_loop, cold_storage_loop, waste_recycling_loop])
root.order.add_edge(site_analysis_loop, seed_selection_loop)
root.order.add_edge(seed_selection_loop, planting_cycle_loop)
root.order.add_edge(planting_cycle_loop, cold_storage_loop)
root.order.add_edge(cold_storage_loop, waste_recycling_loop)