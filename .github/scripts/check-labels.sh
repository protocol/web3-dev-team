#!/bin/bash
#
# This script checks the local label table (ISSUE_LABELS.md) against canonical label file in the
# protocol/.github repo.

set -euo pipefail
set -x

# The canonical source of labels.
CANONICAl_LABELS="https://raw.githubusercontent.com/protocol/.github/master/ISSUE_LABELS.json"

# Matches labels in label tables. Assumes table rows have the form:
# | `label name` | Some description... | ...`#hexcolor`... |
LABEL_REGEXP='s/|.*`\([^`]*\)`.*| *\([^|]*[^ |]\) *|.*`\(#[a-f0-9]*\)`.*|/\1\t\3\t\2/p'

# Reads a label markdown file on stdin and prints a JSON version on stdout.
parse_labels() {
    while IFS=$'\t' read -r label color description; do
        jq -n \
           --arg name "$label" \
           --arg color "${color##\#}" \
           --arg description "$description" \
           '{"name": $name, "color": $color, "description": $description}'
    done < <(sed -ne "$LABEL_REGEXP" - ) |
        jq 'select(.name | startswith("area/") == false)' | # area labels are not synced.
        jq -s 'sort_by(.name)' # sort into a canonical order for comparison.
}

# Extract labels.
parse_labels < ISSUE_LABELS.md > ISSUE_LABELS.json

# Download canonical labels.
curl "$CANONICAl_LABELS" |
    jq 'del(.aliases)|sort_by(.name)' > CANONICAL_LABELS.json

# Compare.
if ! diff -u CANONICAL_LABELS.json ISSUE_LABELS.json; then
    echo "Please update the labels defined at https://github.com/protocol/.github/blob/master/ISSUE_LABELS.json."
    exit 1
fi

