import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define activities
site_survey       = Transition(label='Site Survey')
rack_design       = Transition(label='Rack Design')
system_setup      = Transition(label='System Setup')
climate_calibrate = Transition(label='Climate Calibrate')
nutrient_prep     = Transition(label='Nutrient Prep')
crop_select       = Transition(label='Crop Select')
seed_germinate    = Transition(label='Seed Germinate')
sensor_deploy     = Transition(label='Sensor Deploy')
pest_control      = Transition(label='Pest Control')
harvest_auto      = Transition(label='Harvest Automate')
quality_check     = Transition(label='Quality Check')
pack_produce      = Transition(label='Pack Produce')
data_analyze      = Transition(label='Data Analyze')
engage_community  = Transition(label='Engage Community')
logistics_plan    = Transition(label='Logistics Plan')

# Define the monitoring sequence as a partial order
monitoring = StrictPartialOrder(nodes=[
    seed_germinate,
    sensor_deploy,
    pest_control,
    harvest_auto,
    quality_check,
    pack_produce
])
monitoring.order.add_edge(seed_germinate, sensor_deploy)
monitoring.order.add_edge(sensor_deploy, pest_control)
monitoring.order.add_edge(pest_control, harvest_auto)
monitoring.order.add_edge(harvest_auto, quality_check)
monitoring.order.add_edge(quality_check, pack_produce)

# Define the main process as a loop:
# 1. Site Survey -> Rack Design -> System Setup -> Climate Calibrate -> Nutrient Prep
# 2. Crop Select
# 3. Monitoring sequence (seed germination, sensor deployment, etc.)
# 4. Pest Control
# 5. Harvest Automate -> Quality Check -> Pack Produce
# 6. Data Analyze
# 7. Engage Community
# 8. Logistics Plan
main_sequence = StrictPartialOrder(nodes=[
    site_survey,
    rack_design,
    system_setup,
    climate_calibrate,
    nutrient_prep,
    crop_select,
    monitoring,
    pest_control,
    harvest_auto,
    quality_check,
    pack_produce,
    data_analyze,
    engage_community,
    logistics_plan
])
main_sequence.order.add_edge(site_survey, rack_design)
main_sequence.order.add_edge(rack_design, system_setup)
main_sequence.order.add_edge(system_setup, climate_calibrate)
main_sequence.order.add_edge(climate_calibrate, nutrient_prep)
main_sequence.order.add_edge(nutrient_prep, crop_select)
main_sequence.order.add_edge(crop_select, monitoring)
main_sequence.order.add_edge(monitoring, pest_control)
main_sequence.order.add_edge(pest_control, harvest_auto)
main_sequence.order.add_edge(harvest_auto, quality_check)
main_sequence.order.add_edge(quality_check, pack_produce)
main_sequence.order.add_edge(pack_produce, data_analyze)
main_sequence.order.add_edge(data_analyze, engage_community)
main_sequence.order.add_edge(engage_community, logistics_plan)

# Loop: do the main sequence, then optionally repeat
root = OperatorPOWL(operator=Operator.LOOP, children=[main_sequence, main_sequence])