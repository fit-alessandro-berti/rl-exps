import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the silent transition
skip = SilentTransition()

# Define the partial order for site survey and modular design
site_modular = OperatorPOWL(operator=Operator.XOR, children=[site_survey, modular_design])

# Define the partial order for system build and env control
build_env = OperatorPOWL(operator=Operator.XOR, children=[system_build, env_control])

# Define the partial order for seed selection and nutrient mix
seed_nutrient = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])

# Define the partial order for planting setup and growth monitor
plant_growth = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, growth_monitor])

# Define the partial order for pest control and water cycle
pest_water = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_cycle])

# Define the partial order for data capture and yield forecast
data_yield = OperatorPOWL(operator=Operator.XOR, children=[data_capture, yield_forecast])

# Define the partial order for waste reuse and stakeholder meet
waste_stake = OperatorPOWL(operator=Operator.XOR, children=[waste_reuse, stakeholder_meet])

# Define the partial order for compliance check and supply sync
compliance_supply = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, supply_sync])

# Define the final partial order
root = StrictPartialOrder(nodes=[site_modular, build_env, seed_nutrient, plant_growth, pest_water, data_yield, waste_stake, compliance_supply])
root.order.add_edge(site_modular, build_env)
root.order.add_edge(build_env, seed_nutrient)
root.order.add_edge(seed_nutrient, plant_growth)
root.order.add_edge(plant_growth, pest_water)
root.order.add_edge(pest_water, data_yield)
root.order.add_edge(data_yield, waste_stake)
root.order.add_edge(waste_stake, compliance_supply)

print(root)