# Architecture

## Boundary

This server is a read-only knowledge service. It never imports Orion Ark,
connects to a device, or executes any documented API. Ark classes and methods
are indexed records, not dynamically registered MCP tools.

## Data flow

1. `orion/ark.py` crawls the Sphinx site into a complete Markdown snapshot.
2. `build-index` validates `manifest.json` before accepting the snapshot.
3. The parser extracts documented classes, enums, functions, and methods.
4. The builder writes documents, interfaces, provenance, and FTS5 indexes to a
   temporary SQLite database, checks it, and atomically replaces the active DB.
5. MCP tools query the immutable database. Concrete text resources expose the
   103 full documents; exact API records are returned by `get_ark_interface`
   without advertising more than 1,800 resources to every client.

## Recommendation safety

Recommendation uses reviewed scenario definitions plus indexed API evidence.
It applies action-intent gates so destructive or unrelated calls such as
`erase`, `format`, or `record_video` are not introduced unless the goal asks
for them. Sphinx aliases are collapsed for recommendation output, while exact
search intentionally retains aliases.

Every recommendation includes a source URL, snapshot version, confidence, and
an explicit notice that parameters and hardware compatibility must be checked
before performing device operations.

## Trust and deployment

The source corpus contains internal URLs and operational information. Keep the
database and server on approved internal systems. `stdio` is the preferred
local transport. The HTTP transport binds to loopback by default and does not
implement identity itself; place it behind an authenticated internal gateway
before allowing remote access.
