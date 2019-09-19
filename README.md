# RabbitMQ CLI

## Tool to send messages in a easy way

### The CLI try to be smart

**Features**:

- It can save specific files in our storage and when you send the same queue name, we can use the same information.

- When we have files saved, we have the option to use this file but with different content, you can set new content dinamically.

- If you modified the content saved, you also can save again the new changes

- It can send many messages as you need.

### Commands with params

- **send**
  - --exchange or -e: Choose the exchange.
  - --queue or -q: Choose the queue name.
  - --file or -f: Choose the json file.
  - --save or -s: Save the json file or the new values that you changed.
  - --manually or -m: Type new values for the json file saved.
  - --counter or -c: Repeat # times.

- **listener**
  - --queue or -q: Choose the queue name.
  - --auto or -a: Auto ack messages

### Future features

- Listener ✓
- Listen RPC answer
- Share Database
- Exporse RPC queues as API
