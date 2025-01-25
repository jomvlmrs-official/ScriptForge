# Minecraft Bedrock Edition block schema
scriptforge_schema = {
    "type": "object",
    "properties": {
        "block_identifier": {"type": "string"},
        "states": {"type": "object"},
    },
    "required": ["block_identifier", "states"]
}