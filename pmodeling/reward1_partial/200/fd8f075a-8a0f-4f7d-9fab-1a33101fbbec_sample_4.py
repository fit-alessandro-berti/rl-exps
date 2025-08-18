from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

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

# Site Analysis and Permit Filing
site_analysis = OperatorPOWL(operator=Operator.XOR, children=[site_survey, permit_filing])

# Structural Adaptation
structure_adaptation = OperatorPOWL(operator=Operator.XOR, children=[structure_prep, system_install])

# Nutrient Solution Formulation
nutrient_mixing = OperatorPOWL(operator=Operator.XOR, children=[nutrient_mix, sensor_setup])

# Sensor Calibration and AI Calibration
sensor_calibration = OperatorPOWL(operator=Operator.XOR, children=[sensor_setup, ai_calibration])

# Seed Sourcing and Staff Training
seed_sourcing_training = OperatorPOWL(operator=Operator.XOR, children=[seed_sourcing, staff_training])

# Energy Connection and Water Cycle
energy_connection = OperatorPOWL(operator=Operator.XOR, children=[energy_connect, water_cycle])

# Growth Monitoring and Waste Audit
growth_monitoring = OperatorPOWL(operator=Operator.XOR, children=[growth_monitor, waste_audit])

# Community Engagement and Data Review
community_engagement = OperatorPOWL(operator=Operator.XOR, children=[community_meet, data_review])

# Yield Forecasting
yield_forecasting = OperatorPOWL(operator=Operator.XOR, children=[yield_forecast])

root = StrictPartialOrder(nodes=[site_analysis, structure_adaptation, nutrient_mixing, sensor_calibration, seed_sourcing_training, energy_connection, growth_monitoring, community_engagement, yield_forecasting])

root.order.add_edge(site_analysis, structure_adaptation)
root.order.add_edge(site_analysis, nutrient_mixing)
root.order.add_edge(nutrient_mixing, sensor_calibration)
root.order.add_edge(nutrient_mixing, seed_sourcing_training)
root.order.add_edge(structure_adaptation, energy_connection)
root.order.add_edge(structure_adaptation, growth_monitoring)
root.order.add_edge(growth_monitoring, community_engagement)
root.order.add_edge(community_engagement, yield_forecasting)