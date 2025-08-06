import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

seed_select = Transition(label='Seed Select')
germinate_seeds = Transition(label='Germinate Seeds')
transplant_seedlings = Transition(label='Transplant Seedlings')
mix_nutrients = Transition(label='Mix Nutrients')
adjust_pH = Transition(label='Adjust pH')
monitor_climate = Transition(label='Monitor Climate')
control_humidity = Transition(label='Control Humidity')
co2_regulation = Transition(label='CO2 Regulation')
detect_pests = Transition(label='Detect Pests')
deploy_biocontrols = Transition(label='Deploy Biocontrols')
schedule_harvest = Transition(label='Schedule Harvest')
automate_picking = Transition(label='Automate Picking')
package_produce = Transition(label='Package Produce')
compost_waste = Transition(label='Compost Waste')
recycle_water = Transition(label='Recycle Water')
data_logging = Transition(label='Data Logging')
system_maintenance = Transition(label='System Maintenance')

skip = SilentTransition()

# Define loops and exclusive choices
mix_adjust = OperatorPOWL(operator=Operator.XOR, children=[mix_nutrients, adjust_pH])
climate_control = OperatorPOWL(operator=Operator.XOR, children=[control_humidity, co2_regulation])
pest_control = OperatorPOWL(operator=Operator.XOR, children=[detect_pests, deploy_biocontrols])
harvest_schedule = OperatorPOWL(operator=Operator.XOR, children=[schedule_harvest, automate_picking])
waste_compost = OperatorPOWL(operator=Operator.XOR, children=[compost_waste, recycle_water])

# Define the POWL model
root = StrictPartialOrder(nodes=[
    seed_select,
    germinate_seeds,
    transplant_seedlings,
    mix_adjust,
    climate_control,
    pest_control,
    harvest_schedule,
    waste_compost,
    data_logging,
    system_maintenance
])
root.order.add_edge(seed_select, germinate_seeds)
root.order.add_edge(germinate_seeds, transplant_seedlings)
root.order.add_edge(transplant_seedlings, mix_adjust)
root.order.add_edge(mix_adjust, climate_control)
root.order.add_edge(climate_control, pest_control)
root.order.add_edge(pest_control, harvest_schedule)
root.order.add_edge(harvest_schedule, waste_compost)
root.order.add_edge(waste_compost, data_logging)
root.order.add_edge(data_logging, system_maintenance)