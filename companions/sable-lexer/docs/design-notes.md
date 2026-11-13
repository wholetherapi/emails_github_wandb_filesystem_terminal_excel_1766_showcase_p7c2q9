# Sable Lexer - design notes

## Goal

Provide a single-pass lexer that can be used both by the browser editor and by the
build-time validator.

## Open questions

- Handling nested interpolation expressions
- Error recovery strategy for unterminated strings
- Streaming API shape

No implementation has been committed yet.
