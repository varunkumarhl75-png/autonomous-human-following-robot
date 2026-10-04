"""
Robot Decision and Environment Safety Module

This module converts human position, estimated distance,
and environment conditions into simulated robot commands.

The commands are simulation outputs only. No physical
robot hardware is controlled by this module.
"""


def analyze_environment(brightness, edge_ratio):
    """
    Classify the visual environment using simple image statistics.

    Parameters
    ----------
    brightness : float
        Mean grayscale brightness of the image.

    edge_ratio : float
        Ratio of edge pixels detected in the image.

    Returns
    -------
    str
        Environment category.
    """

    if brightness < 55:
        return "LOW LIGHT"

    elif brightness < 80 and edge_ratio < 0.03:
        return "DARK / UNCLEAR"

    else:
        return "NORMAL"


def get_robot_command(position, distance):
    """
    Generate a basic simulated robot command.

    Parameters
    ----------
    position : str
        Human position: LEFT, CENTER, or RIGHT.

    distance : str
        Estimated distance: NEAR, MEDIUM, or FAR.

    Returns
    -------
    str
        Simulated robot command.
    """

    if distance == "NEAR":
        return "STOP"

    if position == "LEFT":
        return "TURN LEFT"

    elif position == "RIGHT":
        return "TURN RIGHT"

    elif distance == "FAR":
        return "MOVE FORWARD"

    else:
        return "FOLLOW"


def apply_environment_safety(command, environment):
    """
    Modify the robot command according to environment conditions.

    Parameters
    ----------
    command : str
        Initial simulated robot command.

    environment : str
        Environment category.

    Returns
    -------
    str
        Safety-adjusted simulated command.
    """

    if environment == "DARK / UNCLEAR":
        return "STOP - ENVIRONMENT UNCLEAR"

    elif environment == "LOW LIGHT":

        if command == "MOVE FORWARD":
            return "MOVE FORWARD - CAUTIOUS"

        elif command == "FOLLOW":
            return "FOLLOW - CAUTIOUS"

    return command


def final_robot_decision(position, distance, environment):
    """
    Generate the final simulated robot command.

    The decision process first considers human position and
    estimated distance, then applies environment-aware safety.
    """

    command = get_robot_command(position, distance)

    final_command = apply_environment_safety(
        command,
        environment
    )

    return final_command


if __name__ == "__main__":

    test_cases = [
        ("CENTER", "MEDIUM", "NORMAL"),
        ("LEFT", "MEDIUM", "NORMAL"),
        ("RIGHT", "MEDIUM", "NORMAL"),
        ("CENTER", "FAR", "NORMAL"),
        ("CENTER", "FAR", "LOW LIGHT"),
        ("CENTER", "MEDIUM", "DARK / UNCLEAR"),
        ("CENTER", "NEAR", "NORMAL"),
    ]

    print("ROBOT DECISION MODULE TEST")
    print("-" * 55)

    for position, distance, environment in test_cases:

        command = final_robot_decision(
            position,
            distance,
            environment
        )

        print(
            f"{position:6} | "
            f"{distance:6} | "
            f"{environment:15} | "
            f"{command}"
        )