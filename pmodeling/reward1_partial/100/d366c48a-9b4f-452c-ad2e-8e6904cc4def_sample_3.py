import pm4py
from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define transitions for each activity
site_survey = Transition(label='Site Survey')
climate_scan = Transition(label='Climate Scan')
module_setup = Transition(label='Module Setup')
crop_choice = Transition(label='Crop Choice')
nutrient_feed = Transition(label='Nutrient Feed')
pest_control = Transition(label='Pest Control')
energy_audit = Transition(label='Energy Audit')
waste_cycle = Transition(label='Waste Cycle')
growth_track = Transition(label='Growth Track')
demand_plan = Transition(label='Demand Plan')
community_link = Transition(label='Community Link')
regulation_check = Transition(label='Regulation Check')
supply_sync = Transition(label='Supply Sync')
system_upgrade = Transition(label='System Upgrade')
data_backup = Transition(label='Data Backup')

# Define silent transitions
skip = SilentTransition()

# Define nodes and edges for the partial order
root = StrictPartialOrder(
    nodes=[
        site_survey,
        climate_scan,
        module_setup,
        crop_choice,
        nutrient_feed,
        pest_control,
        energy_audit,
        waste_cycle,
        growth_track,
        demand_plan,
        community_link,
        regulation_check,
        supply_sync,
        system_upgrade,
        data_backup
    ],
    order=[
        (site_survey, climate_scan),
        (climate_scan, module_setup),
        (module_setup, crop_choice),
        (crop_choice, nutrient_feed),
        (nutrient_feed, pest_control),
        (pest_control, energy_audit),
        (energy_audit, waste_cycle),
        (waste_cycle, growth_track),
        (growth_track, demand_plan),
        (demand_plan, community_link),
        (community_link, regulation_check),
        (regulation_check, supply_sync),
        (supply_sync, system_upgrade),
        (system_upgrade, data_backup)
    ]
)

print(root)