import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
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

# Define the POWL model
root = StrictPartialOrder(
    nodes=[seed_select, germinate_seeds, transplant_seedlings, mix_nutrients, adjust_pH, monitor_climate, control_humidity, co2_regulation, detect_pests, deploy_biocontrols, schedule_harvest, automate_picking, package_produce, compost_waste, recycle_water, data_logging, system_maintenance],
    order={
        (seed_select, germinate_seeds): None,
        (germinate_seeds, transplant_seedlings): None,
        (transplant_seedlings, mix_nutrients): None,
        (mix_nutrients, adjust_pH): None,
        (adjust_pH, monitor_climate): None,
        (monitor_climate, control_humidity): None,
        (control_humidity, co2_regulation): None,
        (co2_regulation, detect_pests): None,
        (detect_pests, deploy_biocontrols): None,
        (deploy_biocontrols, schedule_harvest): None,
        (schedule_harvest, automate_picking): None,
        (automate_picking, package_produce): None,
        (package_produce, compost_waste): None,
        (compost_waste, recycle_water): None,
        (recycle_water, data_logging): None,
        (data_logging, system_maintenance): None
    }
)