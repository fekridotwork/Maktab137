#!/bin/bash

LOG_DIR="/var/log"

BACKUP_DIR="/var/log/backup"

ARCHIVE_DIR="/var/log/archive"

REPORT="/var/log/logmaster/report.txt"

mkdir -p "$BACKUP_DIR"
mkdir -p "$ARCHIVE_DIR"

cp $LOG_DIR/*.log "$BACKUP_DIR/$(date +%F)_backup.log"

find $LOG_DIR -name "*.log" -mtime +7 -exec mv {} "$ARCHIVE_DIR" \;

python3 logmaster.py scan --file "$LOG_DIR/syslog" --errors --count > "$REPORT"

USAGE=$(df -h / | tail -1 | awk '{print $5}' | sed 's/%//')
if [ "$USAGE" -gt 90 ]; then
  echo "WARNING: Low disk space"
fi
