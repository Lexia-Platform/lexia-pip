# Progressive Tracing API

## Overview

The Progressive Tracing API allows you to build a single trace entry incrementally over time, rather than creating multiple separate trace entries. This is perfect for loops, long-running processes, or any scenario where you want to show progressive updates in one collapsible trace block.

## API Methods

### `session.tracing_begin(message: str, visibility: str = "all")`
Start a progressive trace block.

**Parameters:**
- `message` (str): Initial message to start the trace with
- `visibility` (str): Who can see this trace - `"all"` or `"admin"` (default: `"all"`)

### `session.tracing_append(message: str)`
Append content to the current progressive trace block.

**Parameters:**
- `message` (str): Content to append to the progressive trace

**Note:** Must be called after `tracing_begin()`

### `session.tracing_end(message: str = None)`
Complete and send the progressive trace block.

**Parameters:**
- `message` (str, optional): Final message to append before sending

## Usage Example

### Basic Usage

```python
# Start progressive trace
session.tracing_begin("🔄 Processing items:", "all")

# Append progress as you go
for i, item in enumerate(items, 1):
    session.tracing_append(f"\n  • Item {i}/{len(items)}...")
    process(item)
    session.tracing_append(" ✓")

# Complete the trace
session.tracing_end("\n✅ All items processed!")
```

**Result:** One collapsible trace entry:
```
> 🔄 Processing items:
    • Item 1/5... ✓
    • Item 2/5... ✓
    • Item 3/5... ✓
    • Item 4/5... ✓
    • Item 5/5... ✓
  ✅ All items processed!
```

### Transcription Agent Example

```python
# Start progressive trace for chunk transcription
session.tracing_begin("🔄 Transcription progress:", "all")

# Process chunks
for chunk_index in range(total_chunks):
    # Transcribe chunk
    transcript = transcribe_chunk(chunk_index)
    
    # Append progress
    session.tracing_append(f"\n  • Chunk {chunk_index + 1}/{total_chunks}: ✓ {len(transcript)} chars")
    
    # Stream actual content (separate from trace)
    session.stream(f"{transcript} ")

# Complete the trace
session.tracing_end(f"\n✅ All {total_chunks} chunks transcribed!")
```

**Result:**
```
> 🔄 Transcription progress:
    • Chunk 1/10: ✓ 312 chars
    • Chunk 2/10: ✓ 298 chars
    • Chunk 3/10: ✓ 325 chars
    ...
    • Chunk 10/10: ✓ 289 chars
  ✅ All 10 chunks transcribed!
```

### Admin-Only Progressive Trace

```python
# Start admin-only trace
session.tracing_begin("🔍 Debug information:", "admin")

# Add debug info as you go
session.tracing_append("\n  - Memory usage: 45.2 MB")
session.tracing_append("\n  - CPU usage: 12.3%")
session.tracing_append("\n  - Active threads: 4")

# Complete
session.tracing_end("\n  - Status: Healthy ✓")
```

## Benefits

### Without Progressive Tracing (Multiple Traces)
```python
for i in range(10):
    session.tracing(f"Processing chunk {i+1}/10...", "all")
    # ... process ...
    session.tracing(f"Chunk {i+1} complete", "all")
```

**Result:** 20 separate trace entries (cluttered!)

### With Progressive Tracing (One Trace)
```python
session.tracing_begin("Processing chunks:", "all")
for i in range(10):
    session.tracing_append(f"\n  • Chunk {i+1}/10...")
    # ... process ...
    session.tracing_append(" ✓")
session.tracing_end("\n✅ Done!")
```

**Result:** 1 clean, organized trace entry!

## Implementation Details

### Internal Buffer

The `_Session` class maintains an internal buffer:
- `_progressive_trace_buffer`: Accumulates all appended messages
- `_progressive_trace_visibility`: Stores the visibility setting

### Flow

1. **tracing_begin()**: Initializes buffer with starting message
2. **tracing_append()**: Appends to buffer (can be called multiple times)
3. **tracing_end()**: Sends complete buffer as single trace entry

### Error Handling

- Calling `tracing_append()` without `tracing_begin()` logs a warning
- Calling `tracing_end()` without `tracing_begin()` logs a warning
- Invalid visibility values default to `"all"` with a warning

## Best Practices

### DO ✅

```python
# Clear structure
session.tracing_begin("Processing:", "all")
for item in items:
    session.tracing_append(f"\n  • {item}...")
    process(item)
    session.tracing_append(" ✓")
session.tracing_end("\n✅ Complete!")
```

### DON'T ❌

```python
# Don't forget to call tracing_begin
session.tracing_append("Something")  # Warning!

# Don't forget to call tracing_end
session.tracing_begin("Starting...")
session.tracing_append("stuff")
# Missing tracing_end() - buffer never sent!
```

## When to Use

### Use Progressive Tracing When:
- ✅ Processing items in a loop
- ✅ Long-running tasks with multiple steps
- ✅ Want to show detailed progress in one place
- ✅ Building a progress report incrementally

### Use Regular Tracing When:
- ✅ Single, standalone diagnostic message
- ✅ Different logical steps that should be separate
- ✅ Simple start/end markers

## Comparison

| Feature | `tracing()` | Progressive Tracing |
|---------|-------------|-------------------|
| Trace entries | One per call | One total |
| Use case | Single messages | Progressive updates |
| Buffer | No | Yes |
| Best for | Standalone logs | Loops, progress |

## Migration

### Before (Multiple Traces)
```python
for i in range(total):
    session.tracing(f"Processing {i+1}/{total}...", "all")
    work(i)
    session.tracing(f"Completed {i+1}/{total}", "all")
```

### After (Progressive Trace)
```python
session.tracing_begin(f"Processing {total} items:", "all")
for i in range(total):
    session.tracing_append(f"\n  • Item {i+1}/{total}...")
    work(i)
    session.tracing_append(" ✓")
session.tracing_end("\n✅ Complete!")
```

**Result:** Cleaner, more organized UI!

## Version

Added in Lexia SDK v1.2.9+

## See Also

- `session.tracing()` - Regular tracing for single messages
- `session.stream()` - Stream content to users
- `session.close()` - Complete the response

