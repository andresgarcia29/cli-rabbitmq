# RabbitMQ CLI

## How it works?

### The CLI try to be smart.

**features**:

- It can save specific files in our storage and when you send the same queue name, we can use this file.

- When we have files saved, we have the option to use this file but with different content, you can set new content dinamically.

- It can send many messages as you need.

### Commands with params

- **connect**
  - --url or -u: Url to connect with RabbitMq

- **send**
  - --exchange or -e: Choose the exchange.
  - --queue or -q: Choose the queue name.
  - --file or -f: Choose the json file.
  - --save or -s: Save the json file.
  - --manually or -m: Write manually.
  - --counter or -c: Repeat # times.
