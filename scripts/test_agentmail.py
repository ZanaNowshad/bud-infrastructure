"""Test AgentMail SDK connection and set up BUd email."""
import os

from agentmail import AgentMail

client = AgentMail()

# List inboxes
print("=== Inboxes ===")
inboxes = client.inboxes.list()
for i in inboxes.inboxes:
    print(f"  ID: {i.inbox_id}")
    print(f"  Display: {i.display_name}")
    print()

# Send a test email to ourselves
print("=== Sending test email ===")
send = client.inboxes.messages.send(
    inbox_id="muhamed-6323@agentmail.to",
    to="muhamed-6323@agentmail.to",
    subject="BUd is online!",
    text="Hello! This is BUd, your autonomous agent. The email system is working.",
)
print(f"  Message sent: {send.message_id}")

# List messages
print("\n=== Messages ===")
msgs = client.inboxes.messages.list(inbox_id="muhamed-6323@agentmail.to")
for m in msgs.messages:
    print(f"  Subject: {m.subject}")
    print(f"  From: {m.from_}")
    print(f"  Preview: {m.preview}")
    print()
