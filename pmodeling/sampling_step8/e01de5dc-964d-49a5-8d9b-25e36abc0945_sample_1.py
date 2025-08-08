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

# Define the partial order model
root = StrictPartialOrder(
    nodes=[seed_select, germinate_seeds, transplant_seedlings, mix_nutrients, adjust_pH, monitor_climate,
           control_humidity, co2_regulation, detect_pests, deploy_biocontrols, schedule_harvest, automate_picking,
           package_produce, compost_waste, recycle_water, data_logging, system_maintenance],
    order=[
        (seed_select, germinate_seeds),
        (germinate_seeds, transplant_seedlings),
        (transplant_seedlings, mix_nutrients),
        (mix_nutrients, adjust_pH),
        (adjust_pH, monitor_climate),
        (monitor_climate, control_humidity),
        (control_humidity, co2_regulation),
        (co2_regulation, detect_pests),
        (detect_pests, deploy_biocontrols),
        (deploy_biocontrols, schedule_harvest),
        (schedule_harvest, automate_picking),
        (automate_picking, package_produce),
        (package_produce, compost_waste),
        (compost_waste, recycle_water),
        (recycle_water, data_logging),
        (data_logging, system_maintenance)
    ]
)

print(root)