from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition

# Define transitions (activities)
site_survey = Transition(label='Site Survey')
design_modules = Transition(label='Design Modules')
install_sensors = Transition(label='Install Sensors')
calibrate_climate = Transition(label='Calibrate Climate')
select_seeds = Transition(label='Select Seeds')
optimize_nutrients = Transition(label='Optimize Nutrients')
deploy_robots = Transition(label='Deploy Robots')
monitor_growth = Transition(label='Monitor Growth')
detect_pests = Transition(label='Detect Pests')
analyze_data = Transition(label='Analyze Data')
harvest_crops = Transition(label='Harvest Crops')
customize_pack = Transition(label='Customize Pack')
recycle_waste = Transition(label='Recycle Waste')
audit_energy = Transition(label='Audit Energy')
align_demand = Transition(label='Align Demand')

# Define the POWL model
root = StrictPartialOrder(
    nodes=[
        site_survey,
        design_modules,
        install_sensors,
        calibrate_climate,
        select_seeds,
        optimize_nutrients,
        deploy_robots,
        monitor_growth,
        detect_pests,
        analyze_data,
        harvest_crops,
        customize_pack,
        recycle_waste,
        audit_energy,
        align_demand
    ],
    order={
        site_survey: design_modules,
        design_modules: install_sensors,
        install_sensors: calibrate_climate,
        calibrate_climate: select_seeds,
        select_seeds: optimize_nutrients,
        optimize_nutrients: deploy_robots,
        deploy_robots: monitor_growth,
        monitor_growth: detect_pests,
        detect_pests: analyze_data,
        analyze_data: harvest_crops,
        harvest_crops: customize_pack,
        customize_pack: recycle_waste,
        recycle_waste: audit_energy,
        audit_energy: align_demand
    }
)