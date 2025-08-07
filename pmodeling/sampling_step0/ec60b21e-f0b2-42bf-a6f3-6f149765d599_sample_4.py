import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator
site_survey = Transition(label='Site Survey')
modular_design = Transition(label='Modular Design')
system_build = Transition(label='System Build')
env_control = Transition(label='Env Control')
seed_selection = Transition(label='Seed Selection')
nutrient_mix = Transition(label='Nutrient Mix')
planting_setup = Transition(label='Planting Setup')
growth_monitor = Transition(label='Growth Monitor')
pest_control = Transition(label='Pest Control')
water_cycle = Transition(label='Water Cycle')
data_capture = Transition(label='Data Capture')
yield_forecast = Transition(label='Yield Forecast')
waste_reuse = Transition(label='Waste Reuse')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')
supply_sync = Transition(label='Supply Sync')
skip = SilentTransition()
loop_site = OperatorPOWL(operator=Operator.LOOP, children=[site_survey])
loop_env = OperatorPOWL(operator=Operator.LOOP, children=[env_control])
loop_seed = OperatorPOWL(operator=Operator.LOOP, children=[seed_selection])
loop_nutrient = OperatorPOWL(operator=Operator.LOOP, children=[nutrient_mix])
loop_plant = OperatorPOWL(operator=Operator.LOOP, children=[planting_setup])
loop_monitor = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor])
loop_control = OperatorPOWL(operator=Operator.LOOP, children=[pest_control])
loop_water = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle])
loop_data = OperatorPOWL(operator=Operator.LOOP, children=[data_capture])
loop_forecast = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast])
loop_reuse = OperatorPOWL(operator=Operator.LOOP, children=[waste_reuse])
loop_meet = OperatorPOWL(operator=Operator.LOOP, children=[stakeholder_meet])
loop_check = OperatorPOWL(operator=Operator.LOOP, children=[compliance_check])
loop_sync = OperatorPOWL(operator=Operator.LOOP, children=[supply_sync])
xor_supply = OperatorPOWL(operator=Operator.XOR, children=[supply_sync, skip])
root = StrictPartialOrder(nodes=[
    loop_site,
    loop_env,
    loop_seed,
    loop_nutrient,
    loop_plant,
    loop_monitor,
    loop_control,
    loop_water,
    loop_data,
    loop_forecast,
    loop_reuse,
    loop_meet,
    loop_check,
    loop_sync,
    xor_supply
])
root.order.add_edge(loop_site, loop_env)
root.order.add_edge(loop_env, loop_seed)
root.order.add_edge(loop_seed, loop_nutrient)
root.order.add_edge(loop_nutrient, loop_plant)
root.order.add_edge(loop_plant, loop_monitor)
root.order.add_edge(loop_monitor, loop_control)
root.order.add_edge(loop_control, loop_water)
root.order.add_edge(loop_water, loop_data)
root.order.add_edge(loop_data, loop_forecast)
root.order.add_edge(loop_forecast, loop_reuse)
root.order.add_edge(loop_reuse, loop_meet)
root.order.add_edge(loop_meet, loop_check)
root.order.add_edge(loop_check, loop_sync)
root.order.add_edge(loop_sync, xor_supply)