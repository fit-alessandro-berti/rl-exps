from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the POWL model
colony_sourcing = Transition(label='Colony Sourcing')
hive_design = Transition(label='Hive Design')
site_survey = Transition(label='Site Survey')
installation_prep = Transition(label='Installation Prep')
hive_setup = Transition(label='Hive Setup')
sensor_install = Transition(label='Sensor Install')
health_monitor = Transition(label='Health Monitor')
pest_control = Transition(label='Pest Control')
honey_harvest = Transition(label='Honey Harvest')
wax_processing = Transition(label='Wax Processing')
product_packaging = Transition(label='Product Packaging')
order_dispatch = Transition(label='Order Dispatch')
workshop_setup = Transition(label='Workshop Setup')
community_outreach = Transition(label='Community Outreach')
regulation_check = Transition(label='Regulation Check')
data_analysis = Transition(label='Data Analysis')
maintenance_plan = Transition(label='Maintenance Plan')

# Define the POWL model structure
root = StrictPartialOrder(
    nodes=[
        colony_sourcing,
        hive_design,
        site_survey,
        installation_prep,
        hive_setup,
        sensor_install,
        health_monitor,
        pest_control,
        honey_harvest,
        wax_processing,
        product_packaging,
        order_dispatch,
        workshop_setup,
        community_outreach,
        regulation_check,
        data_analysis,
        maintenance_plan
    ],
    order=[
        (colony_sourcing, hive_design),
        (hive_design, site_survey),
        (site_survey, installation_prep),
        (installation_prep, hive_setup),
        (hive_setup, sensor_install),
        (sensor_install, health_monitor),
        (health_monitor, pest_control),
        (pest_control, honey_harvest),
        (honey_harvest, wax_processing),
        (wax_processing, product_packaging),
        (product_packaging, order_dispatch),
        (order_dispatch, workshop_setup),
        (workshop_setup, community_outreach),
        (community_outreach, regulation_check),
        (regulation_check, data_analysis),
        (data_analysis, maintenance_plan)
    ]
)

print(root)