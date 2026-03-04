# CHRONX_PROJECT_BRIEF.md
# Single Source of Truth for All Claude Instances Working on ChronX
# Last updated: 2026-03-04
# Stored at: https://github.com/Counselco/Counselco-chronx-internal (PRIVATE)
# Also deployed to: https://chronx.io/internal/ai-brief.md

---

## CRITICAL INSTRUCTION FOR ALL CLAUDE INSTANCES

At the start of EVERY session working on ChronX:
1. Fetch this file: `curl -sL https://chronx.io/internal/ai-brief.md`
2. Read it completely before asking Joseph ANY questions
3. At the END of every session, update this document with anything that changed
4. This document is NEVER complete — keep it current or the next Claude instance suffers

### Communication Protocol
- Joseph is a **beginner developer** — all instructions must include step-by-step explanations, explain WHY and HOW, not just WHAT
- At END of every session: produce a completely updated ai-brief.md with all status, bugs, TODOs

---

## 1. PROJECT OVERVIEW

**ChronX** is a purpose-built blockchain protocol for future payments. The central innovation is the native time-lock: an on-chain Promise to deliver funds at a future date, enforced by the protocol itself. No custodian. No lawyer. No fees. Ever.

**Vision:** Enable any human to make a verifiable, unstoppable financial promise to any other human.

**Founding Developer:** Joseph Sanchez (GitHub: Counselco). Solo founder. AI-assisted development via Claude Code.

**Token:** KX
**Base unit:** Chrono (1 KX = 1,000,000 Chronos)
**Total supply:** 8,270,000,000 KX (fixed forever at genesis)
**Transaction fees:** Zero. Completely free. Forever.

**Current Phase:** Pre-ICO live. Wallet v1.4.24. Website live. Node on Vultr. Re-genesis completed 2026-03-03.

**Official ICO Date:** September 22, 2026 — the Autumnal Equinox

**Key differentiators:**
- Post-quantum cryptography (CRYSTALS-Dilithium2, NIST standard)
- Native time-locks at protocol level (not smart contracts)
- Zero fees forever — protocol-enforced
- Email-based sending with secure claim codes
- Cascade Send (multi-stage email promises with one claim code)
- Fixed supply matched to world population at genesis (Jan 1, 2026)

### Regulatory Principles (NEVER VIOLATE)
- KX is a UTILITY TOKEN, not a security or investment
- NEVER use words: "investment", "invest", "investor", "returns", "profit", "gains", "ROI"
- Use: "purchase", "participate", "buyer", "participant" instead

---

## 2. ARCHITECTURE & INFRASTRUCTURE

### Node (Vultr)
- **IP:** 45.63.22.189
- **SSH:** `ssh -i ~/.ssh/id_ed25519 root@45.63.22.189`
- **User home:** /home/josep (lowercase j)
- **Node binary:** /home/josep/chronx/target/release/chronx-node
- **Wallet CLI:** /home/josep/chronx/target/release/chronx-wallet
- **Node data dir:** /home/josep/.chronx/data
- **Genesis params:** /home/josep/chronx/genesis-params.json
- **RPC (internal):** http://127.0.0.1:8545
- **P2P port:** 30303
- **systemd service:** chronx-node (enabled, auto-restarts)
- **Last rebuild:** 2026-03-04 — engine multi-action lock ID fix + cascade CLI

### Wallet CLI (Vultr)
The `chronx-wallet` binary has these subcommands:
- `keygen`, `balance`, `transfer`, `timelock`, `claim`, `email-timelock`, `info`
- `cascade` — NEW: sends multi-stage cascade with shared claim code
  - Usage: `chronx-wallet --keyfile <path> cascade --email <email> --stages '<JSON>' [--memo <text>]`
  - Stages JSON: `[{"amount_kx":100,"lock_seconds":0},{"amount_kx":250,"lock_seconds":172800},...]`
  - `lock_seconds: 0` = immediately claimable
- `recover`, `challenge-recovery`, `vote-recovery`, `finalize-recovery`, `genesis-params`
- **cargo env:** `PATH=/home/josep/.cargo/bin:/usr/local/bin:/usr/bin:/bin` (must set explicitly for SSH)
- **Build:** `PATH=... cargo build --release -p chronx-wallet` in /home/josep/chronx

### Wallet Keyfiles (Vultr)
| Wallet | Path | Account ID | Balance |
|---|---|---|---|
| Public Sale | /home/josep/.chronx/public-sale-wallet.json | Fycy2Sh4SkYiKKVdB8wQSdkymJgJZ4kAGPK7eFn7zPny | ~6,165,000,000 KX |
| Faucet | /home/josep/.chronx/faucet-wallet.json | CkBgP1mYQVFrLThM1VTqMLNXjqwW5RP7iKS4x3LouRN3 | ~3,000,000 KX |
| Node Rewards | /home/josep/.chronx/node-rewards-wallet.json | 3i4tBfxhFCoZFqmuiV7LRoZgyMMUwSq4xAr9SzAQjt6W | 0 KX (timelocked) |
| Founder | C:\Users\Josep\.chronx\wallet.json (LOCAL ONLY) | BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT | ~99,979,200 KX |

**IMPORTANT:** Founder wallet lives on Windows only. For cascade sends: SCP to Vultr temporarily, run CLI, then DELETE immediately after. Never leave it on the server.

### Notify API (Vultr)
- **URL:** https://api.chronx.io
- **Internal:** localhost:3001
- **Service:** chronx-notify (systemd)
- **Files:** /opt/chronx-notify/
- **Config:** /opt/chronx-notify/.env (MYSQL_PASSWORD=CxDb2026, ADMIN_KEY=ChronXAdmin2026, RESEND_API_KEY)
- **Endpoints:** POST /notify (single + cascade), POST /register, POST /faucet/register, GET /faucet/check, POST /faucet/claim, GET /faucet/stats, GET /rewards/status, admin routes
- **Email delivery:** WORKING as of 2026-03-04. Fixed falsy-value bug (unlock_at:0 treated as missing).
- **Resend domain:** Verify chronx.io at resend.com/domains for better deliverability (currently using unverified domain)

### Website (Hostinger)
- **URL:** https://chronx.io
- **FTP host:** 82.29.199.47, user u507945893
- **TRUE web root:** /domains/chronx.io/public_html
- **Deploy:** `cd C:\Users\Josep && python deploy_website.py`
- **After deploy:** Purge cache at hPanel -> Cache Manager -> Purge All

### RPC Endpoint (Public)
- **URL:** https://rpc.chronx.io
- **nginx proxy:** rpc.chronx.io -> http://127.0.0.1:8545

### GitHub Repos
| Repo | URL | Local Path |
|---|---|---|
| Protocol (node) | https://github.com/Counselco/chronx | C:\Users\Josep\chronx |
| Wallet | https://github.com/Counselco/wallet-gui | C:\Users\Josep\chronx\wallet-gui-temp |
| Docs | https://github.com/Counselco/chronx-docs | C:\Users\Josep\chronx-docs |

---

## 3. GENESIS ALLOCATIONS (Re-genesis 2026-03-03)

**Genesis date:** January 1, 2026 00:00:00 UTC (Unix: 1,735,689,600)
**Total supply:** 8,270,000,000 KX = 8,270,000,000,000,000 Chronos

| # | Allocation | KX Amount | % | Lock Condition |
|---|---|---|---|---|
| 1 | Public Sale | 6,268,000,000 | 75.79% | Spendable at genesis |
| 2 | Treasury | 1,000,000,000 | 12.09% | 100 annual harmonic locks 2029-2128 |
| 3 | Node Rewards | 1,000,000,000 | 12.09% | 100 annual harmonic locks 2029-2128 (same formula as Treasury) |
| 4 | Humanity Stake | 1,000,000 | 0.012% | Locked until 2126-01-01 (100 years from genesis) |
| 5 | Milestone 2076 | 500,000 | 0.006% | Locked until 2076-01-01 |
| 6 | Protocol Reserve | 500,000 | 0.006% | Locked until 2036-01-01 |

### Additional Allocations (from Public Sale)
| Allocation | KX | Source |
|---|---|---|
| Founder | 100,000,000 | Transfer from Public Sale |
| Faucet | 3,000,000 | Transfer from Public Sale |

### Treasury & Node Rewards Harmonic Series
- Formula: release_k = floor(POOL_CHRONOS / (H_100 x k))
- H_100 = 5.187377517639621
- 100 annual releases, Jan 1, 2029 through Jan 1, 2128
- Year 1 (k=1): largest release; Year 100 (k=100): smallest
- Rounding dust added to k=1 so sum is exactly 1,000,000,000,000,000 Chronos

### Chain Stats (2026-03-04)
- Total accounts: 5
- Total timelocks: 246 (204 genesis + cascade sends)
- DAG tips: 1
- Total supply: 8,270,000,000 KX (verified)
- Founder balance: 99,979,200 KX (after cascade sends)

---

## 4. TOKENOMICS & ICO

### Pre-ICO (LIVE NOW)
| Period | Price per KX |
|---|---|
| Now to June 22, 2026 | $0.00030 |
| June 22 to Aug 22, 2026 | $0.00033 |
| Aug 22 to Sep 22, 2026 | $0.00036 |

### Payment Addresses
| Currency | Address |
|---|---|
| BTC | bc1qftz4ut7vyeulz9e9k6nsuljdjjxszxhms3tmjh |
| ETH / USDC | 0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54 |
| SOL | 3owKW4ppK76np6um86yd45AzNtLLQVyYoD2iDAGSES7p |

### Official ICO Tiers (Sep 22, 2026)
| Tier | Lock | Price | Discount | Unlocks |
|---|---|---|---|---|
| Spot | None | $0.00055 | -- | Immediate |
| Believer | 6 months | $0.00048 | 13% | Mar 22, 2027 |
| Founder | 12 months | $0.00040 | 27% | Sep 22, 2027 |
| Visionary | 18 months | $0.00032 | 42% | Mar 22, 2028 |

---

## 5. SECURE EMAIL CLAIM SYSTEM

### How It Works
1. Alice sends KX to bob@gmail.com in her wallet
2. Wallet generates claim_secret, formats as KX-XXXX-XXXX-XXXX-XXXX
3. BLAKE3(email) -> recipient_email_hash, BLAKE3(claim_secret) -> extension_data (0xC5 marker + 32 bytes)
4. Node stores hash in email_claim_hashes sled tree
5. Wallet POSTs claim_code to api.chronx.io/notify which emails Bob
6. Notify API sends email and IMMEDIATELY FORGETS the claim_code
7. Bob enters claim code in wallet -> Promises Made tab -> Claim Now
8. Node verifies BLAKE3(claim_secret) matches -> KX transfers to Bob
9. If unclaimed in 72 hours -> auto-reverts to Alice

### Email Send Now (v1.4.24)
- Frontend sends `unlock_at = 0` (sentinel for "Send Now")
- Backend maps `unlock_at <= 0` to `now` (server timestamp)
- Engine skips `UnlockTimestampInPast` check for email locks (0xC5 marker)
- Result: lock is immediately claimable upon creation, just like a direct transfer
- The only difference from a KX address transfer: recipient claims with a code

### Cascade Send (LIVE as of 2026-03-04)
- Multiple locks can share the same claim_secret_hash (same claim code)
- `TimeLockClaimWithSecret` batch-claims ALL matured locks with matching hash
- Wallet CLI: `chronx-wallet cascade --email <addr> --stages '<JSON>' [--memo <text>]`
- New RPC: `chronx_sendCascade(tx_hex)` — submit cascade transaction
- New RPC: `chronx_getCascadeDetails(claim_secret_hash)` — returns all locks in cascade
- Notify API: POST /notify accepts optional `series` array for cascade email template
- 72-hour claim window applies to entire cascade
- Cancel cancels all locks sharing the hash
- **Engine fix (2026-03-04):** Multi-action transactions now derive unique lock IDs per action: action_idx=0 uses tx_id (backward compat), action_idx>0 uses BLAKE3(tx_id || idx). Previous behavior overwrote all locks with same tx_id.

### Cascade Send Standard Template
For future "friendly" sends to new users:
- Memo: "Hey! Here is a gift for you! Come try out the new ChronX blockchain!"
- Stage 1: 100 KX — immediately (lock_seconds: 0)
- Stage 2: 250 KX — 2 days (lock_seconds: 172800)
- Stage 3: 350 KX — 1 week (lock_seconds: 604800)
- Stage 4: 500 KX — 10 days (lock_seconds: 864000)
- Stage 5: 800 KX — 1 month (lock_seconds: 2592000)
- Stage 6: 1,000 KX — 1 year (lock_seconds: 31536000)
- Total: 3,000 KX per recipient

### Cascade Sends Completed (2026-03-04)
| Recipient | Claim Code | Status |
|---|---|---|
| cabfone11@gmail.com | KX-CEQT-9D0T-M14R-ETK3 | Sent + email delivered |
| sadieprincesspea@gmail.com | KX-HDYF-7HR6-LQOY-1H5T | Sent + email delivered |
| kevin@whiteashlab.com | KX-L3T1-941V-EI79-6Z6L | Sent + email delivered |
| yvettedaquiz@gmail.com | KX-IPT8-R7O3-RC9O-WK60 | Sent + email delivered |
| usmanuah9@gmail.com | KX-OM3Y-7ZKN-ZHQG-9HQH | Sent + email delivered |

---

## 6. WALLET STATUS

**Current version:** v1.4.24
**Platform:** Windows x64, Android APK
**Installer:** https://chronx.io/dl/chronx-wallet-setup.exe
**APK:** https://chronx.io/dl/chronx-wallet.apk
**Framework:** Tauri v2 + Leptos 0.7 CSR

### APK Signing
- Keystore: `C:\Users\Josep\chronx\chronx-release.keystore`
- Password: `ChronX2026`
- Always sign APK after every Android build: `zipalign -f 4 input.apk aligned.apk && apksigner sign --ks chronx-release.keystore aligned.apk`

### Features (v1.4.24)
- PIN login (4/6/8 digit toggle), Change PIN
- Account tab: balance, QR, account ID, incoming promises
- Send to KX Address and Send to Email (Send Now + Send Later BETA)
- Cold storage wallet generator
- Private key export (copy + save to file)
- Promises tab with incoming email locks and outgoing timelocks
- History tab with email send status tracking
- Cancel button on pending sends
- Rewards tab with email opt-in
- Settings: Node URL, PIN length, Cold Storage, Export Key, Notices with bell icon, Claim Email
- Version notification (bell icon + gold card)
- Auto-generated update notice in Settings/Notices when new version detected (once per version)
- Faucet tank graphic (on website)

### Tauri Commands
- `check_node`, `get_account_info`, `send_transfer`, `create_timelock`
- `create_email_timelock`, `claim_email_timelock` (pre-validates maturity), `claim_timelock`, `cancel_timelock`
- `get_timelocks`, `get_pending_incoming`, `get_transaction_history`
- `export_public_key`, `export_secret_key`, `restore_wallet`
- `get_node_url`, `set_node_url`, `generate_wallet`
- `check_pin_set`, `set_pin`, `verify_pin`
- `get_claim_email`, `set_claim_email`
- `save_email_send`, `notify_email_recipient`
- `register_for_rewards`, `check_rewards_status`
- `check_for_updates`, `fetch_notices`, `get_seen_notices`, `mark_notice_seen`
- `open_url`, `get_app_version`
- `generate_cold_wallet`, `get_cold_wallets`, `save_cold_wallet`

---

## 7. RPC METHODS

All prefixed with `chronx_`:

| Method | Description |
|---|---|
| getAccount(id) | Full account state |
| getBalance(id) | Balance in Chronos |
| sendTransaction(hex) | Submit signed transaction |
| getTransaction(txId) | Get vertex by TxId |
| getTimeLockContracts(id) | List timelocks for account |
| getTimeLockById(lockId) | Single timelock |
| getPendingIncoming(id) | Pending incoming locks |
| getTimeLockContractsPaged(id, offset, limit) | Paginated timelocks |
| getDagTips() | Current DAG tips |
| getGenesisInfo() | Protocol constants (includes node_rewards_kx) |
| getChainStats() | Aggregate stats |
| getRecentTransactions(limit) | Recent tx summaries |
| getLocksByUnlockDate(from, to) | Locks by date range |
| getVersion() | Node version info |
| cancelLock(hex) | Cancel a timelock |
| searchLocks(query) | Search with filters |
| getGlobalLockStats() | Active lock count + total locked |
| getEmailLocks(emailHashHex) | Locks by email hash |
| getIncomingTransfers(id) | Incoming transfers for account |
| getNetworkInfo() | P2P peer multiaddress |
| sendCascade(hex) | Submit cascade transaction |
| getCascadeDetails(hashHex) | All locks sharing a claim_secret_hash |

---

## 8. WEBSITE PAGES

| Page | URL | Status |
|---|---|---|
| Home | /index.html | LIVE -- landing, stats bar, faucet modal, Windows + Android downloads |
| Wallet | /wallet.html | LIVE -- download page (Windows + Android) |
| Download | /download.html | LIVE -- platform cards |
| Claim | /claim.html | LIVE -- faucet claim + email lock claim (7 languages) |
| Pre-ICO | /preico.html | LIVE |
| Token Sale | /tokensale.html | LIVE |
| Exchange | /exchange.html | LIVE (placeholder) |
| Explorer | /explorer.html | LIVE |
| Analytics | /analytics.html | LIVE |
| Team | /team.html | LIVE |
| Rewards | /rewards.html | LIVE |
| Support | /support.html | LIVE |
| FAQ | /faq.html | LIVE -- includes cold storage FAQ |
| Disclaimer | /disclaimer.html | LIVE |
| Admin | /admin/index.html | LIVE -- faucet + pre-ICO admin (buttons only show for awaiting_approval) |
| version.json | /version.json | v1.4.24 |

### Website Deploy
- **Deploy script:** `cd C:\Users\Josep && python deploy_website.py`
- **TRUE web root:** /domains/chronx.io/public_html (NEVER use /public_html — that's stale)
- **Cache purge:** hPanel -> Cache Manager -> Purge All (after every deploy)
- **Translations:** js/translations.js — 7 languages (EN, FR, DE, ZH, ES, RU, AR)

---

## 9. KEY TECHNICAL DETAILS

- Consensus: PoW, SHA3-256, 20-bit difficulty
- Cryptography: CRYSTALS-Dilithium2 (post-quantum, NIST FIPS 204)
- Account IDs: BLAKE3(Dilithium2 public key), Base58 encoded
- Networking: libp2p | Storage: sled | Structure: DAG
- Minimum lock: 1 second (wallet enforces user-facing minimums)
- Locks >= 1 year: 24-hour cancellation window
- Email locks: 72-hour claim window, auto-revert (UnclaimedAction::RevertToSender)
- Email hash: BLAKE3(lowercase(email)) -- one-way, never reversible
- Claim secret: 32-byte random, BLAKE3 hash stored on-chain, plaintext never stored on server
- Extension data: 0xC5 marker byte + 32 bytes BLAKE3(claim_code)
- Cascade: multiple locks share same claim_secret_hash, batch claimed
- Multi-action lock IDs: action_idx=0 uses tx_id, action_idx>0 uses BLAKE3(tx_id || idx)
- All timestamps: UTC always
- Key sizes: public 1312 bytes, private 2528 bytes, signature 2420 bytes

### Android Build
```bash
JAVA_HOME="C:\\Program Files\\Android\\Android Studio\\jbr" cargo tauri android build
```

### Windows Build
```bash
cd C:\Users\Josep\chronx\wallet-gui-temp && cargo tauri build
```

---

## 10. KEY BUGS FIXED (2026-03-03 / 2026-03-04)

1. **Claim false success** — `sendTransaction` is fire-and-forget (returns TxId before engine executes). Wallet showed "Claimed!" even when node rejected. Fixed by pre-validating lock maturity via `getTimeLockById` RPC before submitting claim transaction.

2. **Email Send Now 24-hour delay** — Three-layer fix:
   - Frontend: `unlock_at = now + 86400` changed to `unlock_at = 0` (sentinel for Send Now)
   - Backend: Removed 24-hour minimum enforcement, maps `unlock_at <= 0` to server's `now`
   - Engine: Skips `UnlockTimestampInPast` check for email locks (0xC5 marker in extension_data)

3. **Notify API falsy-value bug** — JavaScript `!unlock_at` is true when `unlock_at = 0`. Line 321 of index.js: changed `!unlock_at` to `unlock_at == null`. Email delivery now works for Send Now emails.

4. **Engine multi-action lock ID collision** — All `TimeLockCreate` actions in one transaction used `tx_id` as lock ID, causing later locks to overwrite earlier ones in sled DB. Fixed: action_idx=0 uses tx_id, action_idx>0 uses `BLAKE3(tx_id || idx)`.

5. **Cascade email template undefined amounts** — `buildSeriesEmail()` read `e.amount` but cascade payload uses `amount_kx`. Fixed to `e.amount_kx || e.amount` for backward compat.

---

## 11. TODO LIST

### Next Build (v1.4.25+)
- [ ] Disable Android pinch-to-zoom (lock UI scaling)
- [ ] QR code button broken on BOTH Windows and Android -- fix
- [ ] "Convert KX<->USDC" Coming Soon page
- [ ] Change PIN if missing
- [ ] Wallet Cascade Send UI (create cascades from the wallet app)
- [ ] Nav redesign: merge Send into Account (Task 1 from v1.4.15 plan)
- [ ] Multiple claim emails in Settings (up to 3)
- [ ] chronx:// deep link protocol handler

### Active Infrastructure
- [ ] Fix stats bar CORS -- dashes still showing on some browsers
- [ ] Fix support form submission
- [ ] Verify Resend domain (chronx.io) at resend.com/domains
- [ ] Android wallet release to Play Store (APK on website now)

### Future (Phase 2+)
- [ ] IMPORTANT: Node operator incentive/distribution model -- must design before ICO Sep 22 2026
- [ ] Cascade Send web UI for businesses
- [ ] wKX ERC-20 on Base + Uniswap v3 pool + 1inch listing
- [ ] CMC + CoinGecko listing
- [ ] Web wallet, iOS
- [ ] Multi-sig, Oracle network, Conditional payments
- [ ] GitHub CI fix
- [ ] USB key backup (all private keys)
- [ ] Code signing cert ($300-400/yr)
- [ ] Play Store listing for Android

---

## 12. IMMUTABLE RULES

1. Never commit secrets to GitHub -- env vars only
2. All timestamps UTC
3. Zero fees forever -- protocol-enforced
4. ALL website deploys use deploy_website.py
5. Always build Windows + Android for wallet releases
6. KX is a UTILITY TOKEN -- never use "investment" language
7. Never store email->wallet mappings server-side
8. Never store claim secrets server-side
9. Email sends max 1,000,000 KX
10. systemd manages the node -- never start manually with nohup
11. Default RPC: https://rpc.chronx.io
12. PIN: shared PinInput, keydown-first, never set_value() in input handler
13. ICO date: September 22, 2026 -- Autumnal Equinox -- never change
14. Founder wallet NEVER left on Vultr -- SCP temporarily, use, DELETE immediately

---

## 13. SESSION LOG

### 2026-03-04 (Cascade Sends + Bug Fixes)
- **Notify API email fix:** `unlock_at: 0` treated as falsy in JavaScript. Changed `!unlock_at` to `unlock_at == null` on line 321 of /opt/chronx-notify/index.js. Email delivery restored for Send Now.
- **Cascade email template fix:** `buildSeriesEmail()` referenced `e.amount` but cascade payload uses `amount_kx`. Changed to `e.amount_kx || e.amount`. Amounts now display correctly in emails.
- **Engine multi-action lock ID fix:** Added `action_idx` parameter to `apply_action()`. Lock IDs now unique per action: idx=0 uses tx_id, idx>0 uses BLAKE3(tx_id || idx). Node rebuilt and restarted on Vultr.
- **Wallet CLI cascade subcommand:** Added `cascade` command to chronx-wallet CLI. Builds multi-action transaction with shared claim code. Built and deployed to Vultr.
- **Cascade sends to 5 recipients:** cabfone11 (3000 KX), sadieprincesspea (3000 KX), kevin@whiteashlab (3000 KX), yvettedaquiz (3000 KX), usmanuah9 (3000 KX). Total: 15,000 KX. All emails delivered successfully.
- **Chain stats:** 5 accounts, 246 timelocks, 1 DAG tip, supply 8.27B KX verified.

### 2026-03-04 (v1.4.24 -- Email Send Now zero delay)
- **Email Send Now -- zero delay:** Frontend sends `unlock_at = 0`; backend sets it to `now`; engine skips `unlock_at > now` check for email locks (0xC5 marker in extension_data). PoW takes 10-60s, so by the time the tx reaches the engine, `unlock_at` is in the past -- engine now allows this for email locks. Tested: lock created, claimed immediately, balance updated. No waiting.
- **Node engine patched on Vultr:** `crates/chronx-state/src/engine.rs` -- `TimeLockCreate` skips `UnlockTimestampInPast` and `LockDurationTooShort` errors for email locks (0xC5 extension_data). Non-email locks still enforce future unlock. Node rebuilt and restarted.
- **GitHub release v1.4.24**, website deployed, version.json updated.

### 2026-03-04 (v1.4.23 -- Send Now email fix)
- **CRITICAL FIX -- Send Now email locks immediately claimable:** Frontend was setting `unlock_at = now + 86400` (24 hours) for "Send Now" email. Backend also enforced 24-hour minimum. Fixed frontend to `now + 60` (1-min buffer), removed backend 24-hour minimum. Verified end-to-end: create lock, wait 60s, claim, balance updates.
- **GitHub release v1.4.23**, website deployed, version.json updated.

### 2026-03-04 (Critical Bug Fixes + v1.4.22)
- **CRITICAL FIX -- Claim code false success:** `sendTransaction` is fire-and-forget (returns TxId before execution). Wallet showed "Claimed X KX!" even when the node rejected the claim (e.g., lock not yet matured). Fixed by pre-validating lock maturity in both `claim_email_timelock` and `claim_by_code` before submitting.
- **Spam warning text:** Changed from ALL-CAPS breaking mid-word to proper sentence case with word-wrap CSS.
- **Logo positioning:** Added safe-area-inset-top padding for mobile/Android.
- **Android app icon updated:** ChronX gold logo on dark background, all mipmap densities.
- **GitHub release v1.4.22** with Windows installer + signed Android APK.

### 2026-03-03 (Post-Genesis Cleanup + v1.4.21)
- **Wallet v1.4.21:** Auto-generated update notice. Android APK on website.
- **Regulatory language scrubbed** across all files (notices, disclaimer, tokensale, translations).
- **Whitepaper v2.4:** Public Sale 6.268B, Node Rewards, Humanity Stake, Cascade Send, Android.
- **Email delivery confirmed working.** Resend API returns success.

### 2026-03-03 (Re-Genesis + Cascade Send Protocol)
- **RE-GENESIS completed:** 6 allocations, 204 timelocks, clean chain.
- Public Sale: 7,268,000,000 -> 6,268,000,000 KX (1B moved to Node Rewards)
- NEW: Node Rewards 1,000,000,000 KX (100 harmonic locks 2029-2128)
- Humanity Stake fixed: 2127 -> 2126 (exactly 100 years from genesis)
- **Cascade Send protocol implemented** in engine + RPC + DB.
- **Faucet wallet funded:** 3,000,000 KX. Founder wallet: 100,000,000 KX.

### 2026-03-03 (v1.4.19 -- v1.4.20)
- v1.4.19: Claim code top of Receive, auto-disburse, incoming history, settings badge, key export/import
- v1.4.20: PIN toggle, cold storage gen, export to file, faucet wallet 3M KX, tank graphic, FAQ, Android APK

### 2026-03-02 (Major Session)
- Implemented secure email claim system (claim_secret_hash, TimeLockClaimWithSecret)
- Notify API updated with claim codes in emails
- Wallet v1.4.6 through v1.4.9
- Whitepaper v2.2
- Website: disclaimer.html, wallet.html, CORS fix

---

## 14. ADMIN DASHBOARD

- **URL:** /admin/index.html ("ChronX Admin Dashboard")
- **Auth:** X-Admin-Key header (value in .env ADMIN_KEY)
- **Faucet tab:** Pending claims, approve/reject buttons (only show for awaiting_approval status)
- **Pre-ICO tab:** TX hash required, MySQL storage, admin approve/reject with buyer email notification

---

## 15. FAUCET

- **Wallet:** CkBgP1mYQVFrLThM1VTqMLNXjqwW5RP7iKS4x3LouRN3
- **Funded:** 3,000,000 KX from Public Sale
- **Amount per claim:** 9 KX
- **Endpoints:** POST /faucet/register, GET /faucet/check, POST /faucet/claim, GET /faucet/stats
- **Tank graphic:** /faucet/stats returns JSON with level percentage; website renders as animated tank
- **Security:** Server NEVER stores wallet addresses. Token-based flow only.

---

*Maintained by Claude instances working on ChronX. Last updated: 2026-03-04.*
