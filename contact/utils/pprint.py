

def pprint_contact_as_text(contact):
    """
    Pretty-print the given contact as text on the screen.
    """
    print("=" * 80)
    print(f"Contact Type: {contact.__module__}.{contact.__class__.__name__}")
    print("=" * 80)
    header_width = 20
    for entry in contact.read():
        for k in sorted(entry.all_fields()):
            print(f"{k:<{header_width}} {entry.get_value(k)}")
        print("-" * 80)


def pprint_contact_as_markdown(contact, file_path):
    """
    Pretty-print the given contact as a markdown file, displayable in any
    markdown viewer.
    """

    stream = (
        "# Contact list\n"
        "\n"
        f"## Contact Type: "
        f"`{contact.__module__}.{contact.__class__.__name__}`\n"
        "\n"
        "-----\n"
        "\n"
    )

    for entry in contact.read():
        for k in sorted(entry.all_fields()):
            stream += f"- **{k}**: {entry.get_value(k)}\n"
        stream += "\n"
        stream += "-----\n"
        stream += "\n"

    with open(file_path, "w") as f:
        f.write(stream)
