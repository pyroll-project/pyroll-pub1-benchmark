from numpy import pi
from pyroll.core import BoxGroove, CircularOvalGroove, Oval3RadiiFlankedGroove, FalseRoundGroove, Oval3RadiiGroove, \
    Roll, Profile, RollPass, Transport

from pyroll.freiberg_flow_stress import FreibergFlowStressCoefficients

in_profile = Profile.box(
    height=160e-3,
    width=160e-3,
    corner_radius=3e-3,
    temperature=1100 + 273.15,
    strain=0,
    material="B10",
    freiberg_flow_stress_coefficients=FreibergFlowStressCoefficients(
        a=5.7547e-19 * 1e6,
        m1=-0.0110429,
        m2=0.36016,
        m3=-0.141903,
        m4=0.000949296,
        m5=-0.00146294,
        m6=0,
        m7=-0.0288221,
        m8=0.000258262,
        m9=8.48549,
        baseStrain=0.1,
        baseStrainRate=0.1
    ),
    density=7.5e3,
    thermal_capacity=690,
)

"""##########     ROll GAPS     ##########"""

roll_gap_1 = 15e-3
roll_gap_2 = 15e-3
roll_gap_3 = 12e-3
roll_gap_4 = 10e-3
roll_gap_5 = 10e-3
roll_gap_6 = 8e-3
roll_gap_7 = 8e-3
roll_gap_8 = 6e-3
roll_gap_9 = 7e-3
roll_gap_10 = 6e-3
roll_gap_11 = 5e-3
roll_gap_12 = 4e-3
roll_gap_13 = 5.5e-3
roll_gap_14 = 5e-3
roll_gap_15 = 4.5e-3
roll_gap_16 = 4.5e-3

"""##########     ROLL VELOCITIES     ##########"""

roll_velocity_1 = 0.261
roll_velocity_2 = 0.339
roll_velocity_3 = 0.448
roll_velocity_4 = 0.556
roll_velocity_5 = 0.768
roll_velocity_6 = 0.938
roll_velocity_7 = 1.238
roll_velocity_8 = 1.526
roll_velocity_9 = 2.06
roll_velocity_10 = 2.52
roll_velocity_11 = 3.45
roll_velocity_12 = 4.43
roll_velocity_13 = 5.72
roll_velocity_14 = 7.02
roll_velocity_15 = 8.98
roll_velocity_16 = 10.8

"""##########     ROLL TEMPERATURES    ##########"""

roll_temperature_1 = 20
roll_temperature_2 = 20
roll_temperature_3 = 20
roll_temperature_4 = 20
roll_temperature_5 = 20
roll_temperature_6 = 20
roll_temperature_7 = 20
roll_temperature_8 = 20
roll_temperature_9 = 20
roll_temperature_10 = 20
roll_temperature_11 = 20
roll_temperature_12 = 20
roll_temperature_13 = 20
roll_temperature_14 = 20
roll_temperature_15 = 20
roll_temperature_16 = 20

sequence = [
    RollPass(
        label="Stand 1",
        roll=Roll(
            groove=BoxGroove(
                usable_width=185.29e-3,
                depth=52e-3,
                ground_width=157.62e-3,
                r1=15e-3,
                r2=18e-3
            ),
            nominal_radius=635e-3 / 2,
        ),
        velocity=roll_velocity_1,
        gap=roll_gap_1,
    ),
    Transport(duration=1.5 / roll_velocity_1, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 2",
        roll=Roll(
            groove=BoxGroove(
                usable_width=138.435e-3,
                depth=55.5e-3,
                ground_width=108.693e-3,
                r1=22e-3,
                r2=20e-3
            ),
            nominal_radius=635e-3 / 2,
        ),
        velocity=roll_velocity_2,
        gap=roll_gap_2,
    ),
    Transport(duration=1.5 / roll_velocity_2, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 3",
        roll=Roll(
            groove=Oval3RadiiFlankedGroove(
                depth=41.1e-3,
                r1=6e-3,
                r2=23.5e-3,
                r3=183e-3,
                flank_angle=(90 - 17) * pi / 180,
                usable_width=148.5e-3
            ),
            nominal_radius=635e-3 / 2,
        ),
        velocity=roll_velocity_3,
        gap=roll_gap_3
    ),
    Transport(duration=1.5 / roll_velocity_3, cooling_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 4",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=50e-3,
                r1=8e-3,
                r2=55e-3,
                flank_angle=(90 - 25) * pi / 180
            ),
            nominal_radius=635e-3 / 2,
        ),
        velocity=roll_velocity_4,
        gap=roll_gap_4

    ),
    Transport(duration=1.5 / roll_velocity_4, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 5",
        roll=Roll(
            groove=Oval3RadiiGroove(
                depth=28.5e-3,
                r1=10e-3,
                r2=30e-3,
                r3=170e-3,
                usable_width=124.618e-3
            ),
            nominal_radius=530e-3 / 2,
        ),
        velocity=roll_velocity_5,
        gap=roll_gap_5
    ),
    Transport(duration=1.5 / roll_velocity_5, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 6",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=39e-3,
                r1=6e-3,
                r2=42.5e-3,
                flank_angle=(90 - 25) * pi / 180
            ),
            nominal_radius=530e-3 / 2,
        ),
        velocity=roll_velocity_6,
        gap=roll_gap_6
    ),
    Transport(duration=2 / roll_velocity_6, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 7",
        roll=Roll(
            groove=Oval3RadiiGroove(
                depth=24.5e-3,
                r1=8e-3,
                r2=34e-3,
                r3=81.5e-3,
                usable_width=97.3375e-3
            ),
            nominal_radius=530e-3 / 2,
        ),
        velocity=roll_velocity_7,
        gap=roll_gap_7,
    ),
    Transport(duration=2 / roll_velocity_7, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 8",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=30e-3,
                r1=6e-3,
                r2=33e-3,
                flank_angle=(90 - 25) * pi / 180
            ),
            nominal_radius=530e-3 / 2,
        ),
        velocity=roll_velocity_8,
        gap=roll_gap_8,

    ),
    Transport(duration=6 / roll_velocity_8, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 9",
        roll=Roll(
            groove=CircularOvalGroove(
                depth=17.5e-3,
                r1=7e-3,
                r2=60e-3
            ),
            nominal_radius=450e-3 / 2,
        ),
        velocity=roll_velocity_9,
        gap=roll_gap_9
    ),
    Transport(duration=3 / roll_velocity_9, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 10",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=22.75e-3,
                r1=4.5e-3,
                r2=25.75e-3,
                flank_angle=(90 - 25) * pi / 180
            ),
            nominal_radius=450e-3 / 2,
        ),
        velocity=roll_velocity_10,
        gap=roll_gap_10
    ),
    Transport(duration=3 / roll_velocity_10, convection_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 11",
        roll=Roll(
            groove=Oval3RadiiGroove(
                depth=12e-3,
                r1=5e-3,
                r2=8.8e-3,
                r3=71e-3,
                usable_width=69.03e-3
            ),
            nominal_radius=450e-3 / 2,
        ),
        velocity=roll_velocity_11,
        gap=roll_gap_11
    ),
    Transport(duration=3 / roll_velocity_11, cooling_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 12",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=17.25e-3,
                r1=3.5e-3,
                r2=19.25e-3,
                flank_angle=(90 - 30.01) * pi / 180
            ),
            nominal_radius=450e-3 / 2,
        ),
        velocity=roll_velocity_12,
        gap=roll_gap_12
    ),
    Transport(duration=3 / roll_velocity_12, cooling_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 13",
        roll=Roll(
            groove=CircularOvalGroove(
                depth=9.5e-3,
                r1=5e-3,
                r2=40e-3
            ),
            nominal_radius=360e-3 / 2,
        ),
        velocity=roll_velocity_13,
        gap=roll_gap_13
    ),
    Transport(duration=4.2 / roll_velocity_13, cooling_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 14",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=13e-3,
                r1=2.5e-3,
                r2=14.9e-3,
                flank_angle=(90 - 30.01) * pi / 180
            ),
            nominal_radius=360e-3 / 2,
        ),
        velocity=roll_velocity_14,
        gap=roll_gap_14,
    ),
    Transport(duration=4.2 / roll_velocity_14, cooling_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 15",
        roll=Roll(
            groove=CircularOvalGroove(
                depth=7.5e-3,
                r1=4e-3,
                r2=31e-3
            ),
            nominal_radius=360e-3 / 2,
        ),
        velocity=roll_velocity_15,
        gap=roll_gap_15,
    ),
    Transport(duration=4.2 / roll_velocity_15, cooling_heat_transfer_coefficient=30),
    RollPass(
        label="Stand 16",
        roll=Roll(
            groove=FalseRoundGroove(
                depth=10.25e-3,
                r1=2.5e-3,
                r2=12e-3,
                flank_angle=(90 - 29.99) * pi / 180
            ),
            nominal_radius=360e-3 / 2,
        ),
        velocity=roll_velocity_16,
        gap=roll_gap_16,
    )
]
