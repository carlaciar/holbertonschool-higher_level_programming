"""Module containing python script for sending invitations"""

def generate_invitations(template, attendees):
    """Function for generating invitations"""

    # 1. Type validation
    if not isinstance(template, str):
        print("Invalid input: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Invalid input: attendees must be a list of dictionaries.")
        return

    # 2. Empty checks
    if template == "":
        print("Template is empty, no output files generated.")
        return

    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # 3. Generate invitations
    for index, attendee in enumerate(attendees, start=1):
        invitation = template

        for key in ["name", "event_title", "event_date", "event_location"]:
            placeholder = "{" + key + "}"
            value = attendee.get(key) or "N/A"
            invitation = invitation.replace(placeholder, value)

        # 4. Always create / overwrite output files
        with open(f"output_{index}.txt", "w") as f:
            f.write(invitation)
