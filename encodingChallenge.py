from pwn import *  # Install with: pip install pwntools
from Crypto.Util.number import bytes_to_long, long_to_bytes
import json
import base64
import codecs

# Establish a connection to the remote server
remote_conn = remote('socket.cryptohack.org', 13377, level='debug')

def receive_json():
    """Receive and decode a JSON object from the remote connection."""
    data = remote_conn.recvline().decode()
    return json.loads(data)

def send_json(payload):
    """Encode and send a JSON object to the remote connection."""
    remote_conn.sendline(json.dumps(payload).encode())

def decode_data(data_type, encoded_value):
    """Decode the received data based on its type."""
    if data_type == "base64":
        return base64.b64decode(encoded_value).decode()
    elif data_type == "rot13":
        return codecs.decode(encoded_value, 'rot_13')
    elif data_type == "bigint":
        hex_value = encoded_value.replace("0x", "")
        return bytes.fromhex(hex_value).decode()
    elif data_type == "utf-8":
        return "".join(chr(byte) for byte in encoded_value)
    elif data_type == "hex":
        return bytes.fromhex(encoded_value).decode('utf-8')
    else:
        raise ValueError(f"Unsupported data type: {data_type}")

# Process incoming messages
for _ in range(100):
    message = receive_json()

    data_type = message.get("type")
    encoded_value = message.get("encoded")

    print(f"Received type: {data_type}")
    print(f"Received encoded value: {encoded_value}")

    try:
        decoded_value = decode_data(data_type, encoded_value)
        send_json({"decoded": decoded_value})
    except Exception as e:
        print(f"Error decoding data: {e}")

# Ensure the final message is received
final_message = receive_json()
print(final_message)
