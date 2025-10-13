# Error Flow Diagram

## When `lexia.send_error()` is Called

```
┌─────────────────────────────────────────────────────────────┐
│                   lexia.send_error()                         │
│                                                              │
│  Parameters:                                                 │
│  - data: Request context                                     │
│  - error_message: Error description                          │
│  - trace: Optional stack trace                               │
│  - exception: Optional exception object                      │
└─────────────────────────────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │    STEP 1: Stream Error to Frontend   │
        │                                        │
        │  via Centrifugo (prod) or             │
        │  DevStreamClient (dev)                │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  STEP 2: Persist Error to Backend     │
        │                                        │
        │  POST {data.url}                       │
        │  {                                     │
        │    uuid, conversation_id,              │
        │    content, status: "FAILED"           │
        │  }                                     │
        └───────────────────────────────────────┘
                            │
                            ▼
        ┌───────────────────────────────────────┐
        │  STEP 3: Log Error (NEW!)             │
        │                                        │
        │  POST {base_url}/api/internal/v1/logs │
        │  {                                     │
        │    message,                            │
        │    trace,                              │
        │    level: "error",                     │
        │    where: "lexia-sdk",                 │
        │    additional: {metadata}              │
        │  }                                     │
        └───────────────────────────────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │   Complete!  │
                    └──────────────┘
```

## Error Logging Details

### Stack Trace Extraction Priority

```
1. trace parameter provided?
   ├── YES → Use it
   └── NO → Check next
       
2. exception parameter provided?
   ├── YES → Extract from exception.__traceback__
   └── NO → Check next
       
3. Current exception context available?
   ├── YES → Use traceback.format_exc()
   └── NO → No trace (empty string)
```

### URL Construction

```
data.url = "https://api.example.com/api/v1/responses"
                    ↓
            Parse URL
                    ↓
base_url = "https://api.example.com"
                    ↓
log_url = "https://api.example.com/api/internal/v1/logs"
```

## Usage Patterns

### Pattern 1: With Exception (Recommended)

```python
try:
    result = process_data()
except Exception as e:
    lexia.send_error(data, f"Processing failed: {e}", exception=e)
    #                                                  ^^^^^^^^^^^^
    #                                   Automatically extracts full stack trace
```

**Flow:**
1. ✅ Error streamed to frontend: "Processing failed: ..."
2. ✅ Error persisted to backend with FAILED status
3. ✅ Error logged with full stack trace to /api/internal/v1/logs

---

### Pattern 2: With Custom Trace

```python
import traceback

try:
    result = process_data()
except Exception as e:
    trace = traceback.format_exc()
    custom_trace = f"Custom context:\n{trace}"
    lexia.send_error(data, str(e), trace=custom_trace)
```

**Flow:**
1. ✅ Error streamed to frontend
2. ✅ Error persisted to backend
3. ✅ Error logged with custom trace format

---

### Pattern 3: Simple Error (No Trace)

```python
if not api_key:
    lexia.send_error(data, "API key not configured")
```

**Flow:**
1. ✅ Error streamed to frontend
2. ✅ Error persisted to backend
3. ✅ Error logged without trace (message only)

---

## Backend Processing

### Laravel Controller

```php
POST /api/internal/v1/logs

Request Body:
{
    "message": "Error occurred",
    "trace": "Traceback (most recent call last)...",
    "level": "error",
    "where": "lexia-sdk",
    "additional": {
        "uuid": "...",
        "conversation_id": "...",
        "thread_id": "...",
        "channel": "..."
    }
}

↓

LogController::store()
    ├── Validate request
    ├── Extract log data
    ├── Log::error($message, $logData)
    └── Return success
```

### Validation Rules

| Field | Rules |
|-------|-------|
| message | required, string, max:1000 |
| trace | sometimes, nullable, string, max:5000 |
| level | sometimes, nullable, in:error,warning,info,critical |
| additional | sometimes, nullable, array |
| where | sometimes, nullable |

## Error Handling

All steps are wrapped in try-catch blocks:

```
Step 1 (Streaming) fails?
    ├── Log error, continue to Step 2
    
Step 2 (Persistence) fails?
    ├── Log error, continue to Step 3
    
Step 3 (Logging) fails?
    ├── Log error, but don't crash
    └── Error flow completes
```

**Result:** Even if logging fails, the main error is still streamed and persisted!

## Benefits

✅ **Resilient**: Failures in logging don't break error reporting

✅ **Comprehensive**: Captures message, trace, and metadata

✅ **Flexible**: Works with or without traces

✅ **Automatic**: Extracts traces from exceptions automatically

✅ **Compatible**: No breaking changes to existing code



