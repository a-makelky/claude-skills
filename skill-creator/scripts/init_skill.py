#!/usr/bin/env python3
"""
Skill Initialization Script

Creates a properly structured skill directory with template files.

Usage:
    python init_skill.py <skill-name> --path <output-directory>
    python init_skill.py my-skill --path ./skills
"""

import argparse
import os
import sys
from pathlib import Path
from datetime import datetime

SKILL_MD_TEMPLATE = '''---
name: {name}
description: {description}
---

# {title}

Brief description of what this skill does.

## Overview

Explain the purpose and value of this skill. When should Claude use it?

## Prerequisites

List any required:
- Tools (Read, Write, Bash, etc.)
- Files or context
- Dependencies

## Instructions

### Step 1: [First Action]

Describe the first step with imperative language.

### Step 2: [Next Action]

Continue with clear, actionable instructions.

### Step 3: [Final Action]

Complete the workflow.

## Output Format

Describe how results should be structured and presented.

## Error Handling

Explain what to do when:
- Required files are missing
- Validation fails
- Unexpected errors occur

## Examples

### Example 1: Basic Usage

**Input:**
```
[Example input here]
```

**Expected Output:**
```
[Example output here]
```

## Resources

- Scripts: `{{baseDir}}/scripts/`
- References: `{{baseDir}}/references/`
- Templates: `{{baseDir}}/templates/`
'''

README_TEMPLATE = '''# {title}

{description}

## Installation

1. Download or clone this skill directory
2. Upload the ZIP to Claude Desktop via Settings > Capabilities
3. Enable the skill

## Usage

[Describe how to trigger this skill with example prompts]

## Structure

```
{name}/
├── SKILL.md           # Main skill definition
├── scripts/           # Executable scripts
│   └── example.py     # Example script
├── references/        # Reference documentation
│   └── README.md      # This file
└── templates/         # Template files
    └── example.txt    # Example template
```

## Development

To modify this skill:
1. Edit SKILL.md to change instructions
2. Add scripts to scripts/ for automation
3. Add reference docs to references/
4. Add templates to templates/

## License

[Specify license]
'''

EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example Script

This is a placeholder script. Replace with your actual implementation.

Usage:
    python example.py --input <file> --output <file>
"""

import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(description="Example script")
    parser.add_argument("--input", "-i", required=True, help="Input file path")
    parser.add_argument("--output", "-o", required=True, help="Output file path")
    args = parser.parse_args()

    try:
        # Read input
        with open(args.input, "r") as f:
            data = f.read()

        # Process (replace with actual logic)
        result = {"status": "success", "input_length": len(data)}

        # Write output
        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)

        print(f"Successfully processed {args.input}")
        print(f"Output written to {args.output}")

    except FileNotFoundError as e:
        print(f"Error: File not found - {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
'''

EXAMPLE_TEMPLATE = '''<!-- Example Template -->
<!DOCTYPE html>
<html>
<head>
    <title>{{TITLE}}</title>
</head>
<body>
    <h1>{{HEADING}}</h1>
    <p>{{CONTENT}}</p>
    <footer>Generated on {{DATE}}</footer>
</body>
</html>
'''


def create_skill(name: str, output_path: str, description: str = "") -> Path:
    """Create a new skill directory with template files."""
    
    # Validate name
    if len(name) > 64:
        print(f"Error: Skill name must be 64 characters or less (got {len(name)})")
        sys.exit(1)
    
    # Clean name for directory
    dir_name = name.lower().replace(" ", "-").replace("_", "-")
    
    # Create paths
    base_path = Path(output_path) / dir_name
    scripts_path = base_path / "scripts"
    references_path = base_path / "references"
    templates_path = base_path / "templates"
    
    # Check if exists
    if base_path.exists():
        print(f"Error: Directory already exists: {base_path}")
        sys.exit(1)
    
    # Create directories
    base_path.mkdir(parents=True)
    scripts_path.mkdir()
    references_path.mkdir()
    templates_path.mkdir()
    
    # Generate title from name
    title = name.replace("-", " ").replace("_", " ").title()
    
    # Default description if not provided
    if not description:
        description = f"[Describe what {title} does and when to use it - max 200 chars]"
    
    # Write SKILL.md
    skill_content = SKILL_MD_TEMPLATE.format(
        name=name,
        title=title,
        description=description
    )
    (base_path / "SKILL.md").write_text(skill_content)
    
    # Write README
    readme_content = README_TEMPLATE.format(
        name=dir_name,
        title=title,
        description=description
    )
    (references_path / "README.md").write_text(readme_content)
    
    # Write example script
    (scripts_path / "example.py").write_text(EXAMPLE_SCRIPT)
    os.chmod(scripts_path / "example.py", 0o755)
    
    # Write example template
    (templates_path / "example.html").write_text(EXAMPLE_TEMPLATE)
    
    # Write .gitkeep files
    (scripts_path / ".gitkeep").touch()
    (references_path / ".gitkeep").touch()
    (templates_path / ".gitkeep").touch()
    
    print(f"✅ Created skill: {base_path}")
    print(f"")
    print(f"Structure:")
    print(f"  {dir_name}/")
    print(f"  ├── SKILL.md              # Edit this file to define your skill")
    print(f"  ├── scripts/")
    print(f"  │   └── example.py        # Add your scripts here")
    print(f"  ├── references/")
    print(f"  │   └── README.md         # Add reference docs here")
    print(f"  └── templates/")
    print(f"      └── example.html      # Add templates here")
    print(f"")
    print(f"Next steps:")
    print(f"  1. Edit {base_path}/SKILL.md to define your skill")
    print(f"  2. Add scripts to {scripts_path}/")
    print(f"  3. Validate with: python validate_skill.py {base_path}")
    print(f"  4. Package with: python package_skill.py {base_path}")
    
    return base_path


def main():
    parser = argparse.ArgumentParser(
        description="Initialize a new Claude skill directory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python init_skill.py my-skill --path ./skills
  python init_skill.py "Code Reviewer" --path . --description "Review code for best practices"
        """
    )
    parser.add_argument(
        "name",
        help="Name of the skill (max 64 characters)"
    )
    parser.add_argument(
        "--path", "-p",
        default=".",
        help="Directory to create the skill in (default: current directory)"
    )
    parser.add_argument(
        "--description", "-d",
        default="",
        help="Description of the skill (max 200 characters)"
    )
    
    args = parser.parse_args()
    
    # Validate description length
    if args.description and len(args.description) > 200:
        print(f"Error: Description must be 200 characters or less (got {len(args.description)})")
        sys.exit(1)
    
    create_skill(args.name, args.path, args.description)


if __name__ == "__main__":
    main()
