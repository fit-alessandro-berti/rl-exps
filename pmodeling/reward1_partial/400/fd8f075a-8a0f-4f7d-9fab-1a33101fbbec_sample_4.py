import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
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

# Define control-flow operators
permit_filing_to_structure = OperatorPOWL(operator=Operator.XOR, children=[permit_filing, structure_prep])
structure_to_install = OperatorPOWL(operator=Operator.XOR, children=[structure_prep, system_install])
install_to_mix = OperatorPOWL(operator=Operator.XOR, children=[system_install, nutrient_mix])
mix_to_setup = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, sensor_setup])
setup_to_calibrate = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, ai_calibration])
calibrate_to_source = OperatorPOWL(operator=Operator.XOR, children=[ai_calibration, seed_sourcing])
source_to_train = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, staff_training])
train_to_connect = OperatorPOWL(operator=Operator.XOR, children=[staff_training, energy_connect])
connect_to_cycle = OperatorPOWL(operator=Operator.XOR, children=[energy_connect, water_cycle])
cycle_to_monitor = OperatorPOWL(operator=Operator.XOR, children=[water_cycle, growth_monitor])
monitor_to_audit = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, waste_audit])
audit_to_meet = OperatorPOWL(operator=Operator.XOR, children=[waste_audit, community_meet])
meet_to_review = OperatorPOWL(operator=Operator.XOR, children=[community_meet, data_review])
review_to_forecast = OperatorPOWL(operator=Operator.XOR, children=[data_review, yield_forecast])

# Define partial order
root = StrictPartialOrder(nodes=[
    permit_filing,
    structure_prep,
    system_install,
    nutrient_mix,
    sensor_setup,
    ai_calibration,
    seed_sourcing,
    staff_training,
    energy_connect,
    water_cycle,
    growth_monitor,
    waste_audit,
    community_meet,
    data_review,
    yield_forecast
])
root.order.add_edge(permit_filing, structure_prep)
root.order.add_edge(structure_prep, system_install)
root.order.add_edge(system_install, nutrient_mix)
root.order.add_edge(nutrient_mix, sensor_setup)
root.order.add_edge(sensor_setup, ai_calibration)
root.order.add_edge(ai_calibration, seed_sourcing)
root.order.add_edge(seed_sourcing, staff_training)
root.order.add_edge(staff_training, energy_connect)
root.order.add_edge(energy_connect, water_cycle)
root.order.add_edge(water_cycle, growth_monitor)
root.order.add_edge(growth_monitor, waste_audit)
root.order.add_edge(waste_audit, community_meet)
root.order.add_edge(community_meet, data_review)
root.order.add_edge(data_review, yield_forecast)