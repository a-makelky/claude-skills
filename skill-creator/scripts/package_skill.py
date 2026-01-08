#!/usr/bin/env python3
"""
Skill Packaging Script

Packages a skill directory into a properly structured ZIP file for distribution.

Usage:
    python package_skill.py <skill-directory>
    python package_skill.py ./my-skill --output my-skill.zip
"""

import argparse
import os
import sys
import zipfile
from pathlib import Path
from datetime import datetime


def get_skill_name(skill_path: Path) -> str:
    """Extract skill name from SKILL.md frontmatter."""
    skill_md = None
    for f in skill_path.iterdir():
        if f.name.lower() == "skill.md":
            skill_md = f
            break
    
    if not skill_md:
        return skill_path.name
    
    content = skill_md.read_text()
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 2:
            for line in parts[1].split("\n"):
                if line.startswith("name:"):
                    return line.split(":", 1)[1].strip()
    
    return skill_path.name


def should_include(file_path: Path, skill_path: Path) -> bool:
    """Determine if a file should be included in the package."""
    relative = file_path.relative_to(skill_path)
    
    # Skip hidden files and directories
    for part in relative.parts:
        if part.startswith("."):
            return False
    
    # Skip common unwanted files
    skip_patterns = [
        "__pycache__",
        "*.pyc",
        "*.pyo",
        ".DS_Store",
        "Thumbs.db",
        ".git",
        ".gitignore",
        "node_modules",
        "*.egg-info",
        ".env",
        ".venv",
        "venv",
    ]
    
    for pattern in skip_patterns:
        if pattern.startswith("*"):
            if file_path.suffix == pattern[1:]:
                return False
        elif pattern in str(relative):
            return False
    
    return True


def package_skill(skill_path: Path, output_path: Path = None, verbose: bool = False) -> Path:
    """Package a skill directory into a ZIP file."""
    
    # Validate skill directory
    if not skill_path.exists():
        print(f"Error: Directory not found: {skill_path}")
        sys.exit(1)
    
    if not skill_path.is_dir():
        print(f"Error: Not a directory: {skill_path}")
        sys.exit(1)
    
    # Check for SKILL.md
    has_skill_md = any(f.name.lower() == "skill.md" for f in skill_path.iterdir())
    if not has_skill_md:
        print("Error: No SKILL.md found in directory")
        sys.exit(1)
    
    # Get skill name for ZIP
    skill_name = skill_path.name.lower().replace(" ", "-").replace("_", "-")
    
    # Determine output path
    if output_path is None:
        output_path = skill_path.parent / f"{skill_name}.zip"
    
    # Ensure output has .zip extension
    if not str(output_path).endswith(".zip"):
        output_path = Path(str(output_path) + ".zip")
    
    # Collect files
    files_to_include = []
    for file_path in skill_path.rglob("*"):
        if file_path.is_file() and should_include(file_path, skill_path):
            files_to_include.append(file_path)
    
    if not files_to_include:
        print("Error: No files to package")
        sys.exit(1)
    
    # Create ZIP
    print(f"Packaging skill: {skill_name}")
    print(f"Output: {output_path}")
    print("-" * 40)
    
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(files_to_include):
            relative = file_path.relative_to(skill_path)
            # Create proper archive path: skill-name/path/to/file
            archive_path = f"{skill_name}/{relative}"
            
            if verbose:
                print(f"  Adding: {archive_path}")
            
            zf.write(file_path, archive_path)
    
    # Summary
    print("-" * 40)
    print(f"✅ Packaged {len(files_to_include)} files")
    
    # Verify structure
    with zipfile.ZipFile(output_path, "r") as zf:
        names = zf.namelist()
        
        # Check for correct structure
        has_root_folder = all(n.startswith(f"{skill_name}/") for n in names)
        has_skill_md = any("skill.md" in n.lower() for n in names)
        
        if not has_root_folder:
            print("⚠️  Warning: Files not under root folder")
        if not has_skill_md:
            print("⚠️  Warning: SKILL.md not found in archive")
    
    # File size
    size_bytes = output_path.stat().st_size
    if size_bytes < 1024:
        size_str = f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        size_str = f"{size_bytes / 1024:.1f} KB"
    else:
        size_str = f"{size_bytes / (1024 * 1024):.1f} MB"
    
    print(f"📦 Package size: {size_str}")
    print(f"\nTo install:")
    print(f"  1. Open Claude Desktop")
    print(f"  2. Go to Settings > Capabilities")
    print(f"  3. Upload: {output_path.name}")
    
    return output_path


def list_contents(zip_path: Path):
    """List contents of a skill ZIP file."""
    if not zip_path.exists():
        print(f"Error: File not found: {zip_path}")
        sys.exit(1)
    
    print(f"Contents of: {zip_path.name}")
    print("-" * 40)
    
    with zipfile.ZipFile(zip_path, "r") as zf:
        for info in zf.infolist():
            size = info.file_size
            if size < 1024:
                size_str = f"{size:>6} B"
            else:
                size_str = f"{size/1024:>5.1f} KB"
            
            print(f"  {size_str}  {info.filename}")
    
    print("-" * 40)
    print(f"Total: {len(zf.namelist())} files")


def main():
    parser = argparse.ArgumentParser(
        description="Package a Claude skill for distribution",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python package_skill.py ./my-skill
  python package_skill.py ./my-skill --output ~/Desktop/my-skill.zip
  python package_skill.py ./my-skill.zip --list

Correct ZIP structure:
  my-skill.zip
  └── my-skill/
      ├── SKILL.md
      ├── scripts/
      ├── references/
      └── templates/
        """
    )
    parser.add_argument(
        "path",
        help="Path to skill directory (or ZIP file with --list)"
    )
    parser.add_argument(
        "--output", "-o",
        help="Output ZIP file path (default: <skill-name>.zip)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Show files being added"
    )
    parser.add_argument(
        "--list", "-l",
        action="store_true",
        help="List contents of existing ZIP file"
    )
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if args.list:
        if not str(path).endswith(".zip"):
            path = Path(str(path) + ".zip")
        list_contents(path)
    else:
        output = Path(args.output) if args.output else None
        package_skill(path, output, args.verbose)


if __name__ == "__main__":
    main()
