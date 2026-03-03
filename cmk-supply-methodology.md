# ChronX (KX) — Supply Methodology

## Total Supply

**8,270,000,000 KX** (eight billion, two hundred seventy million)

The total supply was fixed at genesis (January 1, 2026) and matched to the estimated world population on that date. No new KX can ever be created. There is no inflation mechanism.

## Smallest Unit

1 KX = 1,000,000 Chronos (the smallest indivisible unit).

## Genesis Allocation

| Category | Amount (KX) | % of Supply | Unlock Schedule |
|----------|-------------|-------------|-----------------|
| Public Sale | 7,168,000,000 | 86.68% | Available immediately for Pre-ICO and ICO distribution |
| Founder Allocation | 100,000,000 | 1.21% | Available at genesis |
| Treasury Harmonic | 100 accounts x 10,000,000 | 12.09% | Time-locked, released on harmonic schedule |
| Humanity Stake | 1,000,000 | 0.012% | Time-locked until January 1, 2127 (101 years) |
| Milestone 2076 | 1,000,000 | 0.012% | Time-locked until 2076 |
| Protocol Reserve | Variable | Remaining | Time-locked, protocol-governed |

## Circulating Supply Calculation

```
Circulating Supply = Total Supply - Total KX Locked in Time-Lock Contracts
```

The circulating supply is verifiable on-chain in real-time via the JSON-RPC method:

```
POST https://rpc.chronx.io
{
  "jsonrpc": "2.0",
  "method": "chronx_getGlobalLockStats",
  "params": [],
  "id": 1
}
```

**Response:**
```json
{
  "active_lock_count": 123,
  "total_locked_chronos": "1002000122470582",
  "total_locked_kx": "1002000122"
}
```

**Formula:**
```
Circulating Supply (KX) = 8,270,000,000 - total_locked_kx
```

## Supply API Endpoints

| Endpoint | Method | Returns |
|----------|--------|---------|
| `chronx_getGlobalLockStats` | POST (JSON-RPC) | Active lock count, total locked (Chronos + KX) |
| `chronx_getSupplyInfo` | POST (JSON-RPC) | Supply breakdown |
| `chronx_getBalance` | POST (JSON-RPC) | Balance for a specific address |

**RPC URL:** `https://rpc.chronx.io`

## Key Properties

- **No inflation**: Total supply is permanently fixed at 8,270,000,000 KX
- **No burning**: KX is never destroyed
- **No minting**: No new KX can be created after genesis
- **Zero fees**: No transaction fees, no gas costs. The amount sent equals the amount received.
- **Time-lock mechanism**: KX can be locked until a future date (up to a century). Locked KX is excluded from circulating supply.

## Verification

All supply data is fully transparent and verifiable on-chain:
- **Block Explorer**: https://chronx.io/explorer.html
- **RPC Endpoint**: https://rpc.chronx.io
- **Source Code**: https://github.com/Counselco/chronx

## Contact

- **Website**: https://chronx.io
- **Support**: https://chronx.io/support.html
- **GitHub**: https://github.com/Counselco/chronx
