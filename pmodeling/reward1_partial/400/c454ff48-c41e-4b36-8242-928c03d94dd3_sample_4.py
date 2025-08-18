from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

# Define the activities
site_assess = Transition(label='Site Assess')
permit_obtain = Transition(label='Permit Obtain')
soil_testing = Transition(label='Soil Testing')
crop_select = Transition(label='Crop Select')
irrigation_setup = Transition(label='Irrigation Setup')
drainage_install = Transition(label='Drainage Install')
energy_integrate = Transition(label='Energy Integrate')
staff_train = Transition(label='Staff Train')
pest_control = Transition(label='Pest Control')
logistics_plan = Transition(label='Logistics Plan')
supply_coordinate = Transition(label='Supply Coordinate')
distribution_map = Transition(label='Distribution Map')
community_engage = Transition(label='Community Engage')
monitoring_setup = Transition(label='Monitoring Setup')
yield_optimize = Transition(label='Yield Optimize')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        site_assess,
        permit_obtain,
        soil_testing,
        crop_select,
        irrigation_setup,
        drainage_install,
        energy_integrate,
        staff_train,
        pest_control,
        logistics_plan,
        supply_coordinate,
        distribution_map,
        community_engage,
        monitoring_setup,
        yield_optimize
    ],
    order=[
        (site_assess, permit_obtain),
        (permit_obtain, soil_testing),
        (soil_testing, crop_select),
        (crop_select, irrigation_setup),
        (irrigation_setup, drainage_install),
        (drainage_install, energy_integrate),
        (energy_integrate, staff_train),
        (staff_train, pest_control),
        (pest_control, logistics_plan),
        (logistics_plan, supply_coordinate),
        (supply_coordinate, distribution_map),
        (distribution_map, community_engage),
        (community_engage, monitoring_setup),
        (monitoring_setup, yield_optimize)
    ]
)