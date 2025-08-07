import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define atomic activities
site_survey      = Transition(label='Site Survey')
modular_design   = Transition(label='Modular Design')
system_build     = Transition(label='System Build')
env_control      = Transition(label='Env Control')
seed_selection   = Transition(label='Seed Selection')
nutrient_mix     = Transition(label='Nutrient Mix')
planting_setup   = Transition(label='Planting Setup')
growth_monitor   = Transition(label='Growth Monitor')
pest_control     = Transition(label='Pest Control')
water_cycle      = Transition(label='Water Cycle')
data_capture     = Transition(label='Data Capture')
yield_forecast   = Transition(label='Yield Forecast')
waste_reuse      = Transition(label='Waste Reuse')
stakeholder_meet = Transition(label='Stakeholder Meet')
compliance_check = Transition(label='Compliance Check')
supply_sync      = Transition(label='Supply Sync')

# Define the calibration sub-process: Env Control -> Nutrient Mix -> Planting Setup
calibration = StrictPartialOrder(nodes=[env_control, nutrient_mix, planting_setup])
calibration.order.add_edge(env_control, nutrient_mix)
calibration.order.add_edge(nutrient_mix, planting_setup)

# Define the monitoring sub-process: Growth Monitor -> Pest Control -> Water Cycle -> Data Capture
monitoring = StrictPartialOrder(nodes=[growth_monitor, pest_control, water_cycle, data_capture])
monitoring.order.add_edge(growth_monitor, pest_control)
monitoring.order.add_edge(pest_control, water_cycle)
monitoring.order.add_edge(water_cycle, data_capture)

# Define the reporting & compliance loop:
# Body: Yield Forecast -> Waste Reuse -> Stakeholder Meet -> Compliance Check -> Supply Sync
body = StrictPartialOrder(nodes=[yield_forecast, waste_reuse, stakeholder_meet, compliance_check, supply_sync])
body.order.add_edge(yield_forecast, waste_reuse)
body.order.add_edge(waste_reuse, stakeholder_meet)
body.order.add_edge(stakeholder_meet, compliance_check)
body.order.add_edge(compliance_check, supply_sync)

# Loop operator: execute body, then optionally repeat
reporting_loop = OperatorPOWL(operator=Operator.LOOP, children=[body, body])

# Assemble the overall process
root = StrictPartialOrder(nodes=[
    site_survey,
    modular_design,
    system_build,
    calibration,
    monitoring,
    reporting_loop
])

# Add dependencies
root.order.add_edge(site_survey, modular_design)
root.order.add_edge(modular_design, system_build)
root.order.add_edge(system_build, calibration)
root.order.add_edge(calibration, monitoring)
root.order.add_edge(monitoring, reporting_loop)