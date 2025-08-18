from pm4py.objects.powl.obj import StrictPartialOrder, OperatorPOWL, Transition, SilentTransition
from pm4py.objects.process_tree.obj import Operator

root = StrictPartialOrder(
    nodes=[
        Transition(label='Site Assess'),
        Transition(label='Zoning Check'),
        Transition(label='Design Farm'),
        Transition(label='Procure Gear'),
        Transition(label='Install Systems'),
        Transition(label='Setup Sensors'),
        Transition(label='Select Crops'),
        Transition(label='Prepare Seeds'),
        Transition(label='Mix Nutrients'),
        Transition(label='Monitor Growth'),
        Transition(label='Adjust Climate'),
        Transition(label='Robotic Harvest'),
        Transition(label='Grade Quality'),
        Transition(label='Pack Produce'),
        Transition(label='Manage Logistics'),
        Transition(label='Market Products'),
        Transition(label='Recycle Waste'),
        Transition(label='Audit Systems'),
    ],
    order=[
        ('Site Assess', 'Zoning Check'),
        ('Zoning Check', 'Design Farm'),
        ('Design Farm', 'Procure Gear'),
        ('Procure Gear', 'Install Systems'),
        ('Install Systems', 'Setup Sensors'),
        ('Setup Sensors', 'Select Crops'),
        ('Select Crops', 'Prepare Seeds'),
        ('Prepare Seeds', 'Mix Nutrients'),
        ('Mix Nutrients', 'Monitor Growth'),
        ('Monitor Growth', 'Adjust Climate'),
        ('Adjust Climate', 'Robotic Harvest'),
        ('Robotic Harvest', 'Grade Quality'),
        ('Grade Quality', 'Pack Produce'),
        ('Pack Produce', 'Manage Logistics'),
        ('Manage Logistics', 'Market Products'),
        ('Market Products', 'Recycle Waste'),
        ('Recycle Waste', 'Audit Systems')
    ]
)