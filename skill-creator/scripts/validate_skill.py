#!/usr/bin/env python3
"""
Skill Validation Script

Validates a skill directory for correctness and best practices.

Usage:
    python validate_skill.py <skill-directory>
    python validate_skill.py ./my-skill --strict
"""

import argparse
import os
import re
import sys
from pathlib import Path
from typing import List, Tuple, Optional


class ValidationResult:
    def __init__(self):
        self.errors: List[str] = []
        self.warnings: List[str] = []
        self.info: List[str] = []
    
    def add_error(self, msg: str):
        self.errors.append(f"❌ ERROR: {msg}")
    
    def add_warning(self, msg: str):
        self.warnings.append(f"⚠️  WARNING: {msg}")
    
    def add_info(self, msg: str):
        self.info.append(f"ℹ️  INFO: {msg}")
    
    def is_valid(self) -> bool:
        return len(self.errors) == 0
    
    def print_results(self):
        if self.errors:
            print("\nErrors (must fix):")
            for e in self.errors:
                print(f"  {e}")
        
        if self.warnings:
            print("\nWarnings (should fix):")
            for w in self.warnings:
                print(f"  {w}")
        
        if self.info:
            print("\nInfo:")
            for i in self.info:
                print(f"  {i}")
        
        print("\n" + "="*50)
        if self.is_valid():
            print("✅ VALIDATION PASSED")
            if self.warnings:
                print(f"   ({len(self.warnings)} warnings to consider)")
        else:
            print(f"❌ VALIDATION FAILED ({len(self.errors)} errors)")


def parse_frontmatter(content: str) -> Tuple[Optional[dict], str]:
    """Parse YAML frontmatter from markdown content."""
    if not content.startswith("---"):
        return None, content
    
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content
    
    frontmatter = {}
    for line in parts[1].strip().split("\n"):
        if ":" in line:
            key, value = line.split(":", 1)
            frontmatter[key.strip()] = value.strip()
    
    return frontmatter, parts[2]


def validate_skill(skill_path: Path, strict: bool = False) -> ValidationResult:
    """Validate a skill directory."""
    result = ValidationResult()
    
    # Check directory exists
    if not skill_path.exists():
        result.add_error(f"Directory does not exist: {skill_path}")
        return result
    
    if not skill_path.is_dir():
        result.add_error(f"Path is not a directory: {skill_path}")
        return result
    
    # Check SKILL.md exists (case-insensitive)
    skill_md = None
    for f in skill_path.iterdir():
        if f.name.lower() == "skill.md":
            skill_md = f
            break
    
    if not skill_md:
        result.add_error("Missing SKILL.md file (required)")
        return result
    
    result.add_info(f"Found: {skill_md.name}")
    
    # Read and parse SKILL.md
    try:
        content = skill_md.read_text()
    except Exception as e:
        result.add_error(f"Cannot read SKILL.md: {e}")
        return result
    
    # Parse frontmatter
    frontmatter, markdown = parse_frontmatter(content)
    
    if not frontmatter:
        result.add_error("Missing YAML frontmatter (must start with ---)")
        return result
    
    # Validate required fields
    if "name" not in frontmatter:
        result.add_error("Missing required field: name")
    else:
        name = frontmatter["name"]
        if len(name) > 64:
            result.add_error(f"name exceeds 64 characters ({len(name)} chars)")
        elif len(name) < 3:
            result.add_warning("name is very short (less than 3 characters)")
        else:
            result.add_info(f"name: {name} ({len(name)} chars)")
    
    if "description" not in frontmatter:
        result.add_error("Missing required field: description")
    else:
        desc = frontmatter["description"]
        if len(desc) > 200:
            result.add_error(f"description exceeds 200 characters ({len(desc)} chars)")
        elif len(desc) < 20:
            result.add_warning("description is very short (less than 20 characters)")
        else:
            result.add_info(f"description: {len(desc)} chars")
        
        # Check description quality
        if desc.startswith("[") or "TODO" in desc.upper():
            result.add_warning("description appears to be a placeholder")
        
        if not any(word in desc.lower() for word in ["when", "use", "for", "to"]):
            result.add_warning("description should explain WHEN to use the skill")
    
    # Validate optional fields
    if "allowed-tools" in frontmatter:
        tools = frontmatter["allowed-tools"]
        result.add_info(f"allowed-tools: {tools}")
        
        # Check for overly broad permissions
        if tools.strip('"') == "Bash" or tools.strip('"') == "*":
            result.add_warning("allowed-tools is very broad - consider scoping")
    
    if "dependencies" in frontmatter:
        result.add_info(f"dependencies: {frontmatter['dependencies']}")
    
    if "model" in frontmatter:
        result.add_info(f"model: {frontmatter['model']}")
    
    # Validate markdown body
    if len(markdown.strip()) < 100:
        result.add_warning("SKILL.md body is very short (less than 100 characters)")
    
    word_count = len(markdown.split())
    if word_count > 5000:
        result.add_warning(f"SKILL.md body is very long ({word_count} words). Consider using references/")
    else:
        result.add_info(f"Body: ~{word_count} words")
    
    # Split by code blocks to avoid matching examples in subsequent checks
    non_code_sections = re.split(r'```[\s\S]*?```', markdown)
    
    # Check for hardcoded paths (excluding code blocks and examples)
    hardcoded_patterns = [
        r"/home/\w+/",
        r"/Users/\w+/",
        r"C:\\Users\\",
        r"/root/"
    ]
    # Only check non-code sections
    for section in non_code_sections:
        for pattern in hardcoded_patterns:
            if re.search(pattern, section):
                result.add_error(f"Found hardcoded path matching {pattern}. Use {{baseDir}} instead.")
    
    # Check for {baseDir} usage
    if "scripts/" in markdown or "references/" in markdown or "templates/" in markdown:
        if "{baseDir}" not in markdown:
            result.add_warning("References to scripts/references/templates/ should use {baseDir}")
    
    # Check directory structure
    subdirs = {d.name for d in skill_path.iterdir() if d.is_dir()}
    
    expected_dirs = {"scripts", "references", "templates"}
    for dir_name in expected_dirs:
        dir_path = skill_path / dir_name
        if dir_path.exists():
            file_count = len([f for f in dir_path.iterdir() if f.is_file() and not f.name.startswith(".")])
            result.add_info(f"{dir_name}/: {file_count} files")
        elif strict:
            result.add_warning(f"Missing optional directory: {dir_name}/")
    
    # Check for referenced files (excluding code blocks and examples)
    for section in non_code_sections:
        file_refs = re.findall(r'\{baseDir\}/(\S+)', section)
        for ref in file_refs:
            ref_clean = ref.rstrip('`').rstrip("'").rstrip('"')
            # Skip if it looks like an example/placeholder
            if any(x in ref_clean.lower() for x in ['example', 'your_', '<', '>', '*']):
                continue
            ref_path = skill_path / ref_clean
            if not ref_path.exists():
                result.add_warning(f"Referenced file not found: {ref_clean}")
    
    # Check scripts for executability
    scripts_dir = skill_path / "scripts"
    if scripts_dir.exists():
        for script in scripts_dir.glob("*.py"):
            try:
                script_content = script.read_text()
                if "if __name__" not in script_content:
                    result.add_warning(f"{script.name}: Missing if __name__ == '__main__' guard")
                if "argparse" not in script_content and "sys.argv" not in script_content:
                    result.add_info(f"{script.name}: No argument parsing detected")
            except:
                pass
    
    return result


def main():
    parser = argparse.ArgumentParser(
        description="Validate a Claude skill directory",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python validate_skill.py ./my-skill
  python validate_skill.py ./my-skill --strict
        """
    )
    parser.add_argument(
        "skill_path",
        help="Path to the skill directory"
    )
    parser.add_argument(
        "--strict", "-s",
        action="store_true",
        help="Enable strict validation (more warnings)"
    )
    
    args = parser.parse_args()
    
    skill_path = Path(args.skill_path)
    
    print(f"Validating skill: {skill_path}")
    print("="*50)
    
    result = validate_skill(skill_path, args.strict)
    result.print_results()
    
    sys.exit(0 if result.is_valid() else 1)


if __name__ == "__main__":
    main()
