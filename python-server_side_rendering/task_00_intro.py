"""Function to generate invitations"""
import os

def generate_invitations(template, attendees):
    """Generate an invitataion based on the information given from the template"""

    if not isinstance(template, str):
        print("Error: Template must be a string")
        return
    if not isinstance(attendees, list) or not all(isinstance(attendees,dict) for attendees in attendees):
        print("Error: Attendees must be a list of dictionaries")
        return

    if not template.strip():
        print("Error: Template cannot be empty")
        return
    if not attendees:
        print("Error: No attendees provided")
        return

    for key, attendee in enumerate(attendees, start=1):
        filled = {
            "name": attendee.get("name", "N/A"),
            "event_title": attendee.get("event_title", "N/A"),
            "event_date": attendee.get("event_date", "N/A"),
            "event_location": attendee.get("event_location", "N/A"),
        }

        filename = f"output_{key}.txt"

        try:
            with open(filename, "w") as f:
                f.write(template.format(**filled))
            print(f"Generated {filename}")
        except KeyError as e:
            print(f"Error: Missing key {str(e)} in the template for attendee {key}")