from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions for each activity
site_assess = Transition(label='Site Assess')
zoning_check = Transition(label='Zoning Check')
design_farm = Transition(label='Design Farm')
procure_gear = Transition(label='Procure Gear')
install_systems = Transition(label='Install Systems')
setup_sensors = Transition(label='Setup Sensors')
select_crops = Transition(label='Select Crops')
prepare_seeds = Transition(label='Prepare Seeds')
mix_nutrients = Transition(label='Mix Nutrients')
monitor_growth = Transition(label='Monitor Growth')
adjust_climate = Transition(label='Adjust Climate')
robotic_harvest = Transition(label='Robotic Harvest')
grade_quality = Transition(label='Grade Quality')
pack_produce = Transition(label='Pack Produce')
manage_logistics = Transition(label='Manage Logistics')
market_products = Transition(label='Market Products')
recycle_waste = Transition(label='Recycle Waste')
audit_systems = Transition(label='Audit Systems')

# Define silent transitions
skip = SilentTransition()

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        site_assess,
        zoning_check,
        design_farm,
        procure_gear,
        install_systems,
        setup_sensors,
        select_crops,
        prepare_seeds,
        mix_nutrients,
        monitor_growth,
        adjust_climate,
        robotic_harvest,
        grade_quality,
        pack_produce,
        manage_logistics,
        market_products,
        recycle_waste,
        audit_systems
    ],
    order=[
        # Define the dependencies between activities
        (site_assess, zoning_check),
        (zoning_check, design_farm),
        (design_farm, procure_gear),
        (procure_gear, install_systems),
        (install_systems, setup_sensors),
        (setup_sensors, select_crops),
        (select_crops, prepare_seeds),
        (prepare_seeds, mix_nutrients),
        (mix_nutrients, monitor_growth),
        (monitor_growth, adjust_climate),
        (adjust_climate, robotic_harvest),
        (robotic_harvest, grade_quality),
        (grade_quality, pack_produce),
        (pack_produce, manage_logistics),
        (manage_logistics, market_products),
        (market_products, recycle_waste),
        (recycle_waste, audit_systems)
    ]
)