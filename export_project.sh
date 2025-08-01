#!/usr/bin/env bash
# export_project.sh
#
# Usage: Run this script in the root of your project directory:
#   bash export_project.sh
#
# This will generate two files:
#   1) directory_tree.txt — a complete listing of all directories and files
#   2) all_contents.txt  — the concatenated contents of every file, separated by clear markers

set -euo pipefail

# Identify script and output filenames
SCRIPT_NAME=$(basename "$0")
OUTPUT_TREE="directory_tree.txt"
OUTPUT_CONTENTS="all_contents.txt"

# Generate directory and file tree, excluding this script, output files, and .git directory
if command -v tree >/dev/null 2>&1; then
  tree -a \
    -I "$SCRIPT_NAME" \
    -I "$OUTPUT_TREE" \
    -I "$OUTPUT_CONTENTS" \
    -I ".git" . | sed 's|^\./||' > "$OUTPUT_TREE"
else
  find . -print \
    | grep -Ev "^(?:\./?\.git(?:/.*)?|\./?$SCRIPT_NAME|\./?$OUTPUT_TREE|\./?$OUTPUT_CONTENTS)" \
    | sed 's|^\./||' > "$OUTPUT_TREE"
fi

# Concatenate all file contents with separators, excluding this script, output files, and .git directory contents
: > "$OUTPUT_CONTENTS"
find . -type f \
  ! -path "./.git/*" \
  ! -name "$SCRIPT_NAME" \
  ! -name "$OUTPUT_TREE" \
  ! -name "$OUTPUT_CONTENTS" \
  -print \
  | sed 's|^\./||' \
  | while IFS= read -r file; do
    echo -e "\n===== FILE: $file =====\n" >> "$OUTPUT_CONTENTS"
    cat "$file" >> "$OUTPUT_CONTENTS"
done

echo "Generated $OUTPUT_TREE and $OUTPUT_CONTENTS, excluding $SCRIPT_NAME and .git directory contents."
