Overview:
The File Inventory Reporter is a local python uttility that safely scans a folder and creates an inventory of the files it contains. Instead of modifying files, the program generates a report that helps users understand what is stored, identify unusually small or large files, and prepare for future cleanup or organization.

This project was creates as the first step in learning business automation and safe file-management workflows. It emphasizes understanding data before taking action.

Problem it solves:
Over time, computers accumulate thousands of files spread across many folders. It becomes difficult to know what files exist, which files consume the most storage, which files may be duplicates or unusually small, and where storage is being used.

Many cleanup tools immidiately rename, move, or delete files. This project intentioanlly avoids those actions and instead provides visibility so users can make informed decisions before changing anything.

Who could use it:
This tool could be useful for individuals organizing personal files, small businesses managing shared folders, IT or operations staff performing storage reviews, anyone preparing for a larger file cleanup or migration, and future automation workflows that require file inventories.

What folders it scans:
Version 1.0 scans a user-selected folder and all of its subfolders recursively. The intiial development version will use a dedicated sample_files folder containing harmless test files. It is intentionally designed to avoid scanning important system directories while the project is being developed.

Information it records:
For every file discovered, the program records file name, full extension, full file path, parent folder, file size (bytes), file size (megabytes), last modified date and time, and review category (for example: normal, very small, large)

Future versions may also include duplicate detection, file hashes, file age, storage summaries, and customizable reporting.

What is must never do:
Safety is the highest priority. Version 1.0 will never delete files, rename files, move files, modify files contents, change folder structures, access cloud accounts, or scan protected system folders without permission. The program is designed to be read-only during development.

Output:
The program generates a CSV report containing one row for each file that was scanned. Examples include file name, extension, full path, parent folder, size (bytes), size (MB), moified date, review category. The report allows users to sort, filter, and analyze their files using spreadsheet software such as Excel.

Future improvements:
Planned future enhancements include duplicate file detection, file hash comparison, storage usage summaries, configurable size thresholds, interactice filters, optional dry-run cleanup recommendations, export to excel dashboards, integration into larger autmoation workflows using python and n8n.

Skills demonstrated:
This project demonstrates business process analysis, workflow design, safe automation practices, python file handling, data collection, CSV generation, error handling, documentation, and thinking through user requirements before implementation.