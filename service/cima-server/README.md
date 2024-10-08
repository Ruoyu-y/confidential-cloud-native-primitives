# CIMA Service

This service will provide CC event log/CC measurement/CC report by [Evidence API](https://github.com/cc-api/evidence-api) for remote attestation service to verify the integrity and confidentiality of the trusted computing environment and required software environment.

## Start Service

Run the command:

```
sudo ./cima_server
[2024-02-22T07:18:29Z INFO  cima_server] [cima-server]: set sock file permissions: /run/cima/uds/cima-server.sock
[2024-02-22T07:18:29Z INFO  cima_server] [cima-server]: staring the service...
[2024-02-22T07:18:29Z INFO  cima_server::agent] The system has been measured as the policy defined.
[2024-02-22T07:19:03Z INFO  cima_server::agent] Loaded ... event logs.
```

## Query Information

1. Query the CC report

Run the command:

```
grpcurl -authority "dummy"  -plaintext -d '{ "container_id": "29134314a2...", "user_data": "MTIzNDU2NzgxMjM0NTY3ODEyMzQ1Njc4MTIzNDU2NzgxMjM0NTY3ODEyMzQ1Njc4", "nonce":"IXUKoBO1UM3c1wopN4sY" }'  -unix /run/cima/uds/cima-server.sock cima_server_pb.cima.GetCcReport
```

The output looks like this:

```
{
  "ccType": 1,
  "ccReport": "..."
}
```

2. Query the CC measurement

Run the command:

```
grpcurl -authority "dummy"  -plaintext -d '{ "container_id": "29134314a2...", "index": 0, "algo_id": 12}'  -unix /run/cima/uds/cima-server.sock cima_server_pb.cima.GetCcMeasurement
```

The output looks like:

```
{
  "measurement": {
    "algoId": 12,
    "hash": "..."
  }
}
```

3. Query the eventlog

Run the command:

```
grpcurl -authority "dummy"  -plaintext -d '{"container_id": "29134314a2...", "start": 0, "count": 3}'  -unix /run/cima/uds/cima-server.sock cima_server_pb.cima.GetCcEventlog
```

The output looks like:

```
{
  "eventLogs": [
    {
      "eventType": 3,
      "digests": [
        {
          "algoId": 4,
          "hash": "..."
        }
      ],
      "eventSize": 33,
      "event": "..."
    },
    {
      "eventType": 2147483659,
      "digests": [
        {
          "algoId": 12,
          "hash": "..."
        }
      ],
      "eventSize": 42,
      "event": "..."
    },
    {
      "eventType": 2147483658,
      "digests": [
        {
          "algoId": 12,
          "hash": "..."
        }
      ],
      "eventSize": 58,
      "event": "..."
    }
  ]
}
```
