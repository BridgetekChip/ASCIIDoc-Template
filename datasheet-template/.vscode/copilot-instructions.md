# MCP Server Instructions for AsciiDoc Datasheet Template

## Available MCP Servers

This workspace is configured with the following MCP servers:

### 1. **Filesystem Server**
- **Purpose:** Read and write files in the project directory
- **Use for:** 
  - Browsing `chapters/`, `images/`, `regs/`, and `themes/` directories
  - Editing `.adoc` files and YAML theme configurations
  - Managing project structure

### 2. **Shell Server**
- **Purpose:** Execute bash commands within the dev container
- **Use for:**
  - Running `./build-zh-pdf.sh` to build PDFs
  - Executing Asciidoctor commands
  - Installing dependencies with `apt-get` or `gem`
  - Running any build/compilation tasks

### 3. **Git Server**
- **Purpose:** Manage version control operations
- **Use for:**
  - Committing changes to `datasheet.adoc` and related files
  - Viewing git history and diffs
  - Creating branches for documentation updates
  - Tracking changes to themes and content

### 4. **Docker Server**
- **Purpose:** Manage the dev container lifecycle
- **Use for:**
  - Checking container status
  - Building and running the container
  - Managing dev container resources

## Project Context

- **Main Document:** `datasheet.adoc`
- **Build Script:** `./build-zh-pdf.sh` (for Chinese PDF generation)
- **Theme Files:** `themes/theme.yml`, `themes/theme-zh.yml`
- **Content Fragments:** `chapters/`, `regs/`, `images/`

## Workflow Examples

- **Edit documentation:** Use Filesystem server to modify `.adoc` files
- **Build output:** Use Shell server to run `asciidoctor` or `./build-zh-pdf.sh`
- **Commit changes:** Use Git server to track document versions
- **Manage container:** Use Docker server to handle dev environment
