import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
site_survey = Transition(label='Site Survey')
permit_filing = Transition(label='Permit Filing')
structure_prep = Transition(label='Structure Prep')
system_install = Transition(label='System Install')
nutrient_mix = Transition(label='Nutrient Mix')
sensor_setup = Transition(label='Sensor Setup')
ai_calibration = Transition(label='AI Calibration')
seed_sourcing = Transition(label='Seed Sourcing')
staff_training = Transition(label='Staff Training')
energy_connect = Transition(label='Energy Connect')
water_cycle = Transition(label='Water Cycle')
growth_monitor = Transition(label='Growth Monitor')
waste_audit = Transition(label='Waste Audit')
community_meet = Transition(label='Community Meet')
data_review = Transition(label='Data Review')
yield_forecast = Transition(label='Yield Forecast')

skip = SilentTransition()

# Define the loops and XOR
structure_loop = OperatorPOWL(operator=Operator.LOOP, children=[structure_prep, system_install])
permit_loop = OperatorPOWL(operator=Operator.LOOP, children=[permit_filing, site_survey])
sensor_loop = OperatorPOWL(operator=Operator.LOOP, children=[sensor_setup, ai_calibration])
water_loop = OperatorPOWL(operator=Operator.LOOP, children=[water_cycle, waste_audit])
staff_loop = OperatorPOWL(operator=Operator.LOOP, children=[staff_training, seed_sourcing])
energy_loop = OperatorPOWL(operator=Operator.LOOP, children=[energy_connect, community_meet])
growth_loop = OperatorPOWL(operator=Operator.LOOP, children=[growth_monitor, data_review])
yield_loop = OperatorPOWL(operator=Operator.LOOP, children=[yield_forecast, community_meet])

# Define the partial order
root = StrictPartialOrder(nodes=[structure_loop, permit_loop, sensor_loop, water_loop, staff_loop, energy_loop, growth_loop, yield_loop])
root.order.add_edge(structure_loop, permit_loop)
root.order.add_edge(permit_loop, sensor_loop)
root.order.add_edge(sensor_loop, water_loop)
root.order.add_edge(water_loop, staff_loop)
root.order.add_edge(staff_loop, energy_loop)
root.order.add_edge(energy_loop, growth_loop)
root.order.add_edge(growth_loop, yield_loop)
root.order.add_edge(yield_loop, community_meet)

# Print the POWL model
print(root)