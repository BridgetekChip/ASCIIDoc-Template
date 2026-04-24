# MCP Server Setup Guide

## What I've Configured

I've set up 4 MCP servers for your AsciiDoc datasheet project:

### Files Created/Modified:

1. **`.vscode/mcp.json`** - MCP server configurations
   - Defines how to connect to Filesystem, Shell, Git, and Docker servers

2. **`.vscode/copilot-instructions.md`** - Instructions for using MCP servers
   - Explains what each server does and when to use it

3. **`.devcontainer/Dockerfile`** - Updated to:
   - Fix the missing fonts directory error
   - Install Node.js v20 and npm (required for MCP servers)

## How to Use

### 1. **Rebuild the Dev Container**
```bash
# Reopen folder in Dev Container (VS Code command palette):
> Dev Containers: Reopen in Container
```

### 2. **Use Filesystem Server** 
Ask Claude to:
- "Browse the chapters directory and list all files"
- "Edit the themes/theme.yml file to..."
- "Read the datasheet.adoc file"

### 3. **Use Shell Server**
Ask Claude to:
- "Run ./build-zh-pdf.sh"
- "Execute: asciidoctor -r asciidoctor-diagram datasheet.adoc"
- "Install any missing gems"

### 4. **Use Git Server**
Ask Claude to:
- "Commit all changes with message: 'Update datasheet'"
- "Show git log for datasheet.adoc"
- "Create a new branch for documentation updates"

### 5. **Use Docker Server**
Ask Claude to:
- "Check the container status"
- "List running containers"
- "Manage the dev container"

## Example Workflow

1. **Edit documentation:** "Add a new chapter in chapters/ directory"
2. **Build output:** "Run the build script to generate PDF"
3. **Track changes:** "Commit these changes to git"

## Troubleshooting

### If MCP servers don't work:
1. Check that Node.js is installed: `node --version`
2. Ensure `@modelcontextprotocol` packages are available
3. Verify paths in `mcp.json` are correct

### If fonts still fail to build:
- Create an empty `fonts/` directory in the project root
- Or add some `.ttf` files to the `fonts/` directory

## Next Steps

- Start using Claude/Copilot Chat to work with your files via MCP servers
- Test by asking it to read a file or run a build command
- The servers will be automatically available when you work in the dev container
