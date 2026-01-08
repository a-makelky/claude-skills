#!/usr/bin/env python3
"""
Validate LinkedIn hook formatting rules.

Usage:
    python validate_hook.py "Line 1 text" "Line 2 text" ["Line 3 text"]
    
Or pipe multiline input:
    echo -e "Line 1\nLine 2" | python validate_hook.py
"""

import sys

# Character limits per line
LIMITS = {
    1: 62,
    2: 62,
    3: 50
}

def validate_line(line_num, text):
    """Validate a single line against character limits."""
    limit = LIMITS.get(line_num, 62)
    char_count = len(text.strip())
    
    return {
        "line": line_num,
        "text": text.strip(),
        "chars": char_count,
        "limit": limit,
        "valid": char_count <= limit,
        "overflow": max(0, char_count - limit)
    }

def validate_hook(lines):
    """Validate complete hook against all formatting rules."""
    results = {
        "lines": [],
        "all_valid": True,
        "issues": []
    }
    
    # Filter empty lines for text validation
    text_lines = [l for l in lines if l.strip()]
    
    # Rule: Maximum 2 text lines (plus 1 empty for spacing)
    if len(text_lines) > 2:
        results["issues"].append("Too many text lines: {} (max 2)".format(len(text_lines)))
        results["all_valid"] = False
    
    # Validate each text line
    for i, line in enumerate(text_lines, 1):
        line_result = validate_line(i, line)
        results["lines"].append(line_result)
        
        if not line_result["valid"]:
            results["all_valid"] = False
            results["issues"].append(
                "Line {} exceeds limit: {}/{} chars (overflow: {})".format(
                    i, line_result["chars"], line_result["limit"], line_result["overflow"]
                )
            )
    
    return results

def format_output(results):
    """Format validation results for display."""
    output = []
    output.append("=" * 50)
    output.append("LINKEDIN HOOK VALIDATION")
    output.append("=" * 50)
    
    for line_result in results["lines"]:
        status = "PASS" if line_result["valid"] else "FAIL"
        output.append(
            "\nLine {}: {} ({}/{} chars)".format(
                line_result["line"], status, line_result["chars"], line_result["limit"]
            )
        )
        output.append('  "{}"'.format(line_result["text"]))
    
    output.append("\n" + "-" * 50)
    
    if results["all_valid"]:
        output.append("RESULT: HOOK PASSES ALL CHECKS")
    else:
        output.append("RESULT: HOOK HAS ISSUES:")
        for issue in results["issues"]:
            output.append("   - {}".format(issue))
    
    output.append("=" * 50)
    return "\n".join(output)

def main():
    # Get input from args or stdin
    if len(sys.argv) > 1:
        lines = sys.argv[1:]
    elif not sys.stdin.isatty():
        lines = sys.stdin.read().strip().split("\n")
    else:
        print('Usage: python validate_hook.py "Line 1" "Line 2" ["Line 3"]')
        print('Or:    echo -e "Line 1\\nLine 2" | python validate_hook.py')
        sys.exit(1)
    
    results = validate_hook(lines)
    print(format_output(results))
    
    # Exit with error code if validation failed
    sys.exit(0 if results["all_valid"] else 1)

if __name__ == "__main__":
    main()
