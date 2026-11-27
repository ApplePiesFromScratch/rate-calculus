# Using the method in any AI chat

1. Open a new chat with any assistant.
2. Paste the whole of `CHAT_START.md` as your first message.
3. Ask your question. The assistant should answer with moves shown, refusals named, tiers, and a report card at the end.
4. When it writes code, run it yourself (Python 3, with this repo's `ratecalc` if you have it) and paste back the lines it asks for.
5. If an answer breaks a rule (an independent variable, a refusal turned into infinity, a claim with no tier), quote the rule number back to it.

The chat cannot run anything on your machine. Your run outranks its arithmetic.
