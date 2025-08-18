import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define the transitions
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

# Define the operators
# Exclusive choice: Site Survey -> Modular Design
exclusive_choice_1 = OperatorPOWL(operator=Operator.XOR, children=[site_survey, modular_design])

# Exclusive choice: Modular Design -> System Build
exclusive_choice_2 = OperatorPOWL(operator=Operator.XOR, children=[modular_design, system_build])

# Exclusive choice: System Build -> Env Control
exclusive_choice_3 = OperatorPOWL(operator=Operator.XOR, children=[system_build, env_control])

# Exclusive choice: Env Control -> Seed Selection
exclusive_choice_4 = OperatorPOWL(operator=Operator.XOR, children=[env_control, seed_selection])

# Exclusive choice: Seed Selection -> Nutrient Mix
exclusive_choice_5 = OperatorPOWL(operator=Operator.XOR, children=[seed_selection, nutrient_mix])

# Exclusive choice: Nutrient Mix -> Planting Setup
exclusive_choice_6 = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, planting_setup])

# Exclusive choice: Planting Setup -> Growth Monitor
exclusive_choice_7 = OperatorPOWL(operator=Operator.XOR, children=[planting_setup, growth_monitor])

# Exclusive choice: Growth Monitor -> Pest Control
exclusive_choice_8 = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, pest_control])

# Exclusive choice: Pest Control -> Water Cycle
exclusive_choice_9 = OperatorPOWL(operator=Operator.XOR, children=[pest_control, water_cycle])

# Exclusive choice: Water Cycle -> Data Capture
exclusive_choice_10 = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, data_capture])

# Exclusive choice: Data Capture -> Yield Forecast
exclusive_choice_11 = OperatorPOWL(operator=Operator.XOR, children=[data_capture, yield_forecast])

# Exclusive choice: Yield Forecast -> Waste Reuse
exclusive_choice_12 = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast, waste_reuse])

# Exclusive choice: Waste Reuse -> Stakeholder Meet
exclusive_choice_13 = OperatorPOWL(operator=Operator.XOR, children=[waste_reuse, stakeholder_meet])

# Exclusive choice: Stakeholder Meet -> Compliance Check
exclusive_choice_14 = OperatorPOWL(operator=Operator.XOR, children=[stakeholder_meet, compliance_check])

# Exclusive choice: Compliance Check -> Supply Sync
exclusive_choice_15 = OperatorPOWL(operator=Operator.XOR, children=[compliance_check, supply_sync])

# Define the root POWL model
root = StrictPartialOrder(nodes=[
    site_survey,
    modular_design,
    system_build,
    env_control,
    seed_selection,
    nutrient_mix,
    planting_setup,
    growth_monitor,
    pest_control,
    water_cycle,
    data_capture,
    yield_forecast,
    waste_reuse,
    stakeholder_meet,
    compliance_check,
    supply_sync
])

# Define the order
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, env_control)
root.order.add_edge(env_control, seed_selection)
root.order.add_edge(seed_selection, nutrient_mix)
root.order.add_edge(nutrient_mix, planting_setup)
root.order.add_edge(planting_setup, growth_monitor)
root.order.add_edge(growth_monitor, pest_control)
root.order.add_edge(pest_control, water_cycle)
root.order.add_edge(water_cycle, data_capture)
root.order.add_edge(data_capture, yield_forecast)
root.order.add_edge(yield_forecast, waste_reuse)
root.order.add_edge(waste_reuse, stakeholder_meet)
root.order.add_edge(stakeholder_meet, compliance_check)
root.order.add_edge(compliance_check, supply_sync)

print(root)