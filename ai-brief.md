# CHRONX_PROJECT_BRIEF.md
# Single Source of Truth for All Claude Instances Working on ChronX
# Last updated: 2026-03-23
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

## ✅ GENESIS 10 FINAL (2026-03-22)

**Genesis version: 10.0** — Full re-genesis with code cleanup. All nodes synced: Vultr + Windows + Mac Mini.

**Chain state:** 14 vertices, 20 accounts, 8,270,000,000 KX total supply confirmed. Fresh chain from clean genesis.

**Pre-genesis snapshot:** `/home/josep/pre-genesis-10-final-snapshot-v3.json` — every wallet balance verified to exact chronos before wipe.

**4 Protocol Bonds established at Genesis 10 (10M KX each):**
- MISAI Bond: `2EY2u8iLXW6KXM6zH2PYcB98WDBzBU7DK4d2PsLL422v`
- Verifas Bond: `CNUuEt3kQNAeQtSP9Y9muyCMujxFWq2AfsTecjHvCYtD`
- HedgeKX Bond: `64PXAwjapumXadK4e5Zk7f8zAxhaKwJifSJLHHiRsDKb`
- XChan Bond: `68Y97pWzwT8r5kEfozAjhZd6b4bhrKVmJUr84NAfz129` (NEW — keyfile `/home/josep/.chronx/xchan-bond-wallet.json`)

**Genesis 10 code changes (13 sub-phases):**
- 1A: Stale relay .env fixed (`9Vjh83mQHBEf5aMgz4emA3FaFygacDodWWLKeS31hp6m`)
- 1B: Loan storage standardized to JSON only (bincode removed, 5 handlers converted)
- 1C: 3 unspawned sweeps now running (genesis8_expiry, sign_of_life, promise_chain_anchors)
- 1D: All sweep intervals from genesis-params.json (zero hardcoded Duration::from_secs)
- 1E: Genesis naming purge (zero Genesis 7/8/9 references)
- 1F: Field renames — `extension_data`→`lock_marker`, `lock_convert_to`→`convert_to_suggestion`, `recipient_email_hash`→`email_recipient_hash` (129 renames)
- 1G: RPC renames — `getLocks`, `getLockById`, `getLocksPaged`, `getLockStats`, `getEmailStats`, `submitCascade`
- 1H: `memo_encrypted: bool` + `memo_public: bool` on Transfer + TimeLockCreate; engine rules for verified identity
- 1I: Persistent rate limiting (tx 10/wallet/min, loan 100/wallet/day, sled-backed, survives restart)
- 1J: Badge tier architecture (`issuer_tier` column in MySQL `wallet_badges`)
- 1K: Zero unwrap() in production code
- 1L: Zero TODO/FIXME/HACK comments
- 1M: PAY_AS delivery engine (`pay_as_amount: Option<f64>` on TimeLockCreate + Transfer, oracle scaffold in sweep)

**Build:** Zero errors, zero warnings. Git commit `b1883c1` pushed to main.

**Wallet v2.5.24:** Built and deployed to chronx.io. RPC methods renamed. Android AABs NOT yet built.

**Wallet export:** 12 wallet files in `C:\Users\Josep\OneDrive\Desktop\ChronX Vital\Genesis-10-Final-Wallets\` + USB backup.

**Relay actual address:** `9Vjh83mQHBEf5aMgz4emA3FaFygacDodWWLKeS31hp6m` (from keyfile, NOT the stale `8Nodc3F2...` in old MEMORY.md)

**Public Sale keyfile:** `/home/josep/genesis9/keyfiles/public-sale-wallet.json` on Vultr. Address: `B3NZbGxzkNMXgvR6NqvCJGN2UUuiyBMHxXRYs7xRdXg5`. Windows stale copy renamed to `-STALE-OLD-GENESIS.json`.

**Recent updates (2026-03-23 session 3 — Genesis 10 Reboot):**
- GENESIS 10 REBOOT COMPLETE. Chain wiped and re-populated cleanly.
- 13 vertices, 19 accounts, 8,270,000,000 KX supply confirmed.
- All user balances restored: Usman 1M, Michelle 100, Joseph Mobile 14,825, cabfone1999 8,630, iikrudiat20 25, cabfone1999-faucet 25.
- iikrudiat20 fix: original transfer failed (account not auto-created on fresh chain). Re-sent from Faucet (tx bfa216ca). Now 25 KX confirmed.
- Protocol wallets funded: Founder 188M, Faucet 3M, MISAI/Verifas/XChan bonds 10M each, Relay 10, wKX Bridge 884.
- Wallet key export: 14 files in Genesis-10-Reboot-Wallets/ on Desktop. USB backup pending.
- AABs ready on Desktop: chronx-internal-v2.5.28.aab (versionCode 2005028), chronx-production-v2.5.28.aab (versionCode 3005028). NOT uploaded to Play Store yet.
- Vultr + Windows nodes synced (13 vertices). Mac Mini needs manual sync.
- Notify API: GET /wallet/lookup-email/:email and /wallet/label/:address live.
- Whitepaper v6.4 additions committed to chronx-docs (commit 2f97268).
- MEMO ENCRYPTION: memo_encrypted_by_default=true, memo_public_by_default=false in genesis-params.

**TOMORROW FIRST TASKS:**
1. Joseph's 3 transactions (first on clean chain)
2. Memo encryption UI: Desktop Send tab — add "Make this memo public" checkbox below memo input. Unchecked by default, resets after every send. When checked: gold warning "This memo will be permanently visible to everyone on the blockchain. It cannot be deleted." Sets memo_encrypted=false, memo_public=true. When unchecked: memo_encrypted=true, memo_public=false. Mobile: no checkbox, always encrypted, no exception.
3. Loan sweep DAG vertex fix (currently only updates sled, no history)
4. AAB upload to Play Store (internal track first)
5. Mac Mini sync

**Previous updates (2026-03-22 session 2):**
- WALLET v2.5.28: Terms/Exit buttons wired, loan history fixes (LoanReceived + LoanPayment entries), Accept spinner, amount overflow fix. AABs: internal 2005028, production 3005028.
- LOAN DISBURSAL FIX: LoanAcceptance engine handler now correctly transfers principal. First confirmed working loan: Jodey/Fixed 10,000 KX (engine auto-disbursed on acceptance).
- LOAN FLAG SYSTEM: 28 flags, signing authority enforced at engine. All credit publishing OFF by default. Governance-gated.
- PRIVACY STUBS: PrivacySend + PrivacySendHigh in transaction.rs. Both return FeatureNotActive. genesis params: privacy_send_enabled: false, privacy_send_high_enabled: false.
- JURISDICTION LAYER: WalletConfig has jurisdiction field. Enforcement off. Data NEVER goes on-chain. Wallet-local only.
- NOTIFY API: GET /wallet/lookup-email/:email live. Queries verified_emails table. Returns wallet address for registered users. GET /wallet/label/:address also live.
- WHITEPAPER v6.4: additions.txt in chronx-docs. .docx incorporation pending next session.
- EXPLORER: Badge colors fixed (uses badge.color), Amount column added, Type column with 16 colored pill labels.

**Open bugs (carry forward):**
- Loan sweep not writing DAG vertices (balance correct, no history entries)
- Mobile history missing LoanReceived and LoanPayment entries
- Amount overflow on mobile history
- Loans tab needs auto-refresh without re-login

**Next session priorities:**
1. PAY_AS $100 USD loan — pay_as_enabled: true, pay_as_max_usd: 100.0 confirmed in genesis-params. XChan oracle. 1-month renewable.
2. AABs: internal 2005028, production 3005028. Upload internal to Play Console after Joseph reviews .exe.
3. Fix loan sweep to write DAG vertices (LoanPayment transactions)
4. cpnx.com admin v2 deploy ✅ DONE 2026-03-23

---

## ✅ CPNX ADMIN v2.2 — PUBLIC FORM + APPLICATIONS (2026-03-24)

**CPNX wallet:** `5g4Fcn8A9BigH8vvyNvVvTGksC6PVWTsQnvT8adRGfFp`
**CPNX keyfile:** `C:\Users\Josep\chronx\cpnx-wallet.json`
**NEVER leave keyfile on Vultr. SCP, use, delete.**

**Landing page:** https://cpnx.com — hero + bordered gold bond pill (visible) + partner badge + public forms
**Admin panel:** https://cpnx.com/admin.html — partner badge embedded
**Deploy:** `cd C:\Users\Josep && python deploy_cpnx.py`
**FTP:** u507945893.cpnx.com @ 82.29.199.47 (same password as other sites)
**Local folder:** `C:\Users\Josep\cpnx-website\`
**Bond wallet:** `5g4Fcn8A9BigH8vvyNvVvTGksC6PVWTsQnvT8adRGfFp` — 1M KX bonded, explorer-verifiable
**Partner badge:** `chronx.io/js/partner-badge.js` embedded on both index.html and admin.html
**Admin login:** Joseph changed password manually — not a bug, working as intended
**Badge Catalog fix (2026-03-24):** Null-safe `escapeHtml`/`escapeAttr` — `String()` coercion for numeric IDs. Catalog table reads `default_expiry_days` + `available_to_children` from API. Null guard on `.map()`.
**Public form (2026-03-24):** "Request a Badge" now opens web modal form (no longer opens email client). "Verify a Badge" opens wallet lookup form (no longer redirects to explorer). Public endpoints: `POST /cpnx/public/request-badge`, `GET /cpnx/public/verify/:address`. Confirmation email sent to applicant on submit. Admin notification email sent to yo@chronx.io. Applications tab in admin now shows submissions with approve/reject workflow + email notifications. `cpnx_applications` table created.
**Founder identity updated (2026-03-23):** "ChronX Founder" → "Founding Team" (voluntary revocation + re-issue via CPNX wallet)
- Revoke TX: `e9449ff53f943d9fb14ae1796e1985d710e2b68e2068a9d7c5c86c1040207fa5`
- Re-issue TX: `418ec17c328b73bfdeb884b720259e667b8c7718d0b9a1a849c6f72412892525`
- CPNX keyfile confirmed deleted from Vultr after use

### Badge System
- `wallet_badges` table now has `expires_at`, `badge_label`, `issued_by_child`, `child_account_id` columns
- Expired badges auto-filtered from public API response (`/wallet/badges/:address`)
- Default expiry: 90 days. Permanent badges: `expires_at = NULL`

### Badge Catalog
- 20 seeded badge types in `cpnx_badge_catalog` table
- Tiers: identity, partner, gaming, custom
- `available_to_children` flag for child account access control

### Child Accounts
- `cpnx_child_accounts` table live — B2B badge issuers
- `cpnx_child_badge_types` for per-account badge permissions
- API key auth for child badge issuance
- Quota enforcement + blackout checking

### CPNX Admin API Endpoints (all live)
```
GET  /cpnx/badge-catalog                        (public, no auth)
GET  /cpnx/admin/badges                          (admin auth)
POST /cpnx/admin/issue-badge                     (admin auth)
DELETE /cpnx/admin/badges/:id                    (admin auth)
GET  /cpnx/admin/wallet/:address                 (admin auth)
POST /cpnx/admin/verify-identity                 (admin auth)
POST /cpnx/admin/revoke-identity                 (admin auth)
GET  /cpnx/admin/child-accounts                  (admin auth)
POST /cpnx/admin/child-accounts                  (admin auth)
GET  /cpnx/admin/child-accounts/:id/badge-types  (admin auth)
POST /cpnx/admin/child-accounts/:id/badge-types  (admin auth)
PATCH /cpnx/admin/child-accounts/:id/status      (admin auth)
POST /cpnx/admin/badge-catalog                   (admin auth)
PUT  /cpnx/admin/badge-catalog/:id               (admin auth)
POST /cpnx/child/issue-badge                     (API key auth via X-Api-Key)
GET  /cpnx/child/my-badge-types                  (API key auth via X-Api-Key)
DELETE /cpnx/admin/child-accounts/:id             (admin auth)
DELETE /cpnx/admin/child-accounts/:id/badge-types/:typeId (admin auth)
POST /cpnx/public/request-badge                  (public, no auth)
GET  /cpnx/public/verify/:address                (public, no auth)
GET  /cpnx/admin/applications                    (admin auth)
PATCH /cpnx/admin/applications/:id/approve       (admin auth)
PATCH /cpnx/admin/applications/:id/reject        (admin auth)
```

### Admin Panel Nav (v2.2)
Dashboard | Active Badges | Issue Badge | Verify Wallet | Revoke | Child Accounts | Badge Catalog | Applications | Settings

### Issue Badge (admin)
Free-form badge type entry, color picker, emoji, live preview pill.
Collapsible "Browse badge ideas" catalog reference for inspiration.
Admin has no restrictions on badge types. Expiration default 90 days.

### Child Accounts
Admin creates child accounts with generated credentials.
Admin assigns specific badge types + quotas per child.
Child authenticates via API key. Quota enforced server-side.
Admin can delete child accounts (type DELETE to confirm).
Admin can manage badge types per child (add/remove).

### Settings
Change password form (calls POST /admin/change-password).
API key reveal/hide (10s auto-hide). No regeneration yet.

### Revoke
Badge revocation: instant MySQL delete via admin panel.
Identity revocation: radio buttons with descriptions for each type.
Fraud/impersonation triggers configurable badge blackout period.
CLI command shown in styled code block with Copy button.

### Database Tables Added
- `cpnx_child_accounts` — B2B child account management
- `cpnx_child_badge_types` — per-child badge permissions
- `cpnx_badge_catalog` — 20 seeded badge types
- `cpnx_verifications` — identity verification audit log
- `badge_blackouts` — fraud/impersonation badge blackouts
- `cpnx_applications` — public badge/verification requests (name, wallet, type, email, status, admin_notes, rejection_reason)

### Attestation Requirement
Identity verification requires mandatory checkbox: "I confirm I have independently verified..."
CPNX accepts sole legal responsibility. ChronX has no involvement in individual decisions.

### Revocation Types (on-chain)
- `fraud` / `impersonation` → badge blackout enforced (configurable years)
- `disambiguation` / `voluntary` / `administrative` → no blackout, clean record

### Verification Workflow
For now: admin logs verification, receives CLI command to run manually with CPNX keyfile.
Future: automated signing via HSM.

### CORS
Added to ALLOWED_ORIGINS: cpnx.com, www.cpnx.com, admin.cpnx.com, xchan.io, misai.io, kxgo.io (+ www variants)

### Server Files
- `/opt/chronx-notify/cpnx-routes.js` — all CPNX endpoints (loaded by index.js)
- `/opt/chronx-notify/index.js` — CORS updated, badge expiry filter added, cpnx-routes required

### OPEN ITEMS
1. Self-to-self loan test (install v2.5.33 .exe)
2. Android AAB build after biometric confirmed on device
3. Mobile Buy/Sell KX widget UI
4. Whitepaper push approval
5. PAY_AS test loan USD denomination
6. HedgeKX seeding (Joseph funds USDC reserve)
7. ~~EXECUTOR_WITHDRAW_DELAY = 86400~~ **DONE** (set 2026-03-24)
8. Mac Mini node sync
9. Operating agreements pre-ICO — **LEGAL DEPENDENCY: accreditation flow needs securities lawyer**
10. Foundation legal structure pre-ICO

---

## GOVERNANCE DIRECTIVES SYSTEM (v1.1 — 2026-03-24)

**Machine-readable:** https://chronx.io/governance-directives.json (v1.1)
**Human-readable:** https://chronx.io/governance.html — fully rebuilt (2026-03-24)
**Live API:** https://api.chronx.io/governance/params (public, no auth)

All 5 Essential Protocol Partners read this single JSON file for their current limits, bond info, and operating mode. Update one file → all partner sites update automatically.

### Governance Page Architecture (rebuilt 2026-03-24)
Three sections showing complete governance picture:
1. **Immutable Constants** — supply, fees, axiom counts, fee ceiling. Source: `/governance/params` API. Cannot change ever.
2. **Governed Parameters** — live values from `genesis-params.json`. Shows floor, ceiling, current value, purpose. Source: `/governance/params` API. Foundation vote required.
3. **EPP Directives** — per-partner limits, yellow notices, bond amounts, review dates. Source: `governance-directives.json`. Foundation governance vote.

### Governance Params API
`GET /governance/params` — returns immutable constants (5) + governed parameters (7+) from genesis-params.json. Public, no auth. Added to `/opt/chronx-notify/index.js`.

**Current Directives:**
| Partner | Bond | Limit | Status | Next Review |
|---------|------|-------|--------|-------------|
| CPNX | 1M KX | No limit | active | -- |
| Verifas | 10M KX | No limit | active | -- |
| XChan | 10M KX | $250/tx ($10K accredited) | active | Q1 2027 |
| HedgeKX | 10M KX | $250/hedge | building | Q1 2027 |
| MISAI | 10M KX | 80K KX, invite only | gate_restricted | Q4 2026 |

**v1.1 additions:** bond_wallet, bond_kx, bond_instrument_pending, tagline, operating_mode, principal_trading fields, spread floor/ceiling, accredited limits, auto-escalation flags.

**Governance notices live on:**
- chronx.io/ico.html — below XChan buy box
- xchan.io — below hero badges + operating mode indicator
- hedgekx.io — below CTA buttons
- All 5 sites: partner-bond.js displays live bond balance

## PARTNER BOND DISPLAY (2026-03-24)

**Shared script:** `https://chronx.io/js/partner-bond.js`
Each partner site loads this script and calls `initPartnerBond({...})` with their bond wallet address. Displays live bond balance fetched from ChronX RPC, with fallback to known amount if API unavailable. Positioned prominently (below hero, trust centerpiece — not a small badge).

**XChan operating mode indicator:** Shows current mode (principal trading vs Uniswap routing) with spread % and governance link.

**Bond Instrument loans:** Pending — wallet CLI does not have `loan-offer` subcommand. Joseph will issue via desktop wallet GUI. BLAKE2b placeholder hashes computed:
- XChan: `09e977a1aab1...`
- HedgeKX: `3c7ea3cb1e90...`
- CPNX: `8eb3e607a5bd...`
- Verifas: `f82daad65075...`
- MISAI: `9eb20c27eb9d...`

## ICO ACCREDITATION SYSTEM (2026-03-24)

**Database:** `ico_accreditations` table in MySQL (chronx DB on Vultr)
**Endpoints:**
- `POST /ico/accreditation/submit` — public, submits declaration
- `GET /ico/accreditation/limit/:wallet` — public, returns max_transaction_usd (250 or 10000)
- `GET /ico/accreditation/status/:wallet` — public, returns pending/approved/rejected/not_submitted
- `GET /admin/ico/accreditations` — admin, lists all applications
- `PATCH /admin/ico/accreditations/:id/approve` — admin, approves + sends email
- `PATCH /admin/ico/accreditations/:id/reject` — admin, rejects

**Flow:** Submit form on chronx.io/ico.html → confirmation email → Joseph reviews in admin panel → approve → applicant gets $10,000 limit on XChan.

**XChan enforcement:** Execute endpoint checks accreditation limit via `http://127.0.0.1:3001/ico/accreditation/limit/:wallet` before processing. Default: $250. Accredited: $10,000.

**LEGAL NOTE:** Accreditation is self-certification only. Securities lawyer must review before ICO launch. This is a declaration system, not verification.

## ICO ACCREDITED INVESTOR REGISTRY (2026-03-24)

**ICO page tabs:** "Public Sale" (default) + "Accredited Registry"
- Public Sale tab: existing content + accreditation declaration form
- Registry tab: public table of approved accredited investors with live wallet balances

**Registry columns:** Wallet (truncated) | Country | Approved date | KX Balance (live) | USD Value | Status
**Status indicators:** Green = holding, Yellow = reduced >10%, Red = near zero
**Balance source:** `chronx_getAccountInfo` RPC per wallet, price from `/api/xchan/price`
**Privacy:** Wallet addresses voluntarily disclosed by investors — balances are public blockchain data

## ADMIN OPERATIONS TAB (2026-03-24)

**URL:** chronx.io/admin.html → Operations tab

**Section 1 — Partner Health Cards:**
All 5 partners in a grid. Each shows: name, tagline, bond balance (live from RPC), status indicator. XChan card includes reserve health bar (color-coded: green >50%, yellow 20-50%, red <20%) and daily volume.

**Section 2 — ICO Accreditation Queue:**
Stats: Total / Pending / Approved / Rejected. Table with full details (name, country, wallet, email, US resident, KX balance, submitted date, status). Approve/Reject buttons per row.

**Section 3 — XChan Activity:**
Daily summary cards (buy volume, sell volume, spread income, trade count). Recent trades table (last 20).

## XCHAN SPREAD TIERS (2026-03-24)

**Two-tier spread system live:**
| Transaction | Spread | Registration |
|-------------|--------|-------------|
| Buy KX (any amount) | 2% | No |
| Sell KX ≤ 80,000 KX/day | 2% | No |
| Sell KX > 80,000 KX/day | 10% | Accredited required |

**Key design:** Buys are ALWAYS 2% regardless of size — we are in an ICO and want buyers. Sells have tiered spreads based on daily KX volume per wallet.

**Spread schedule (targets, subject to governance vote):**
- Launch: retail 2% / accredited sell 10%
- 2027-Q2: retail 2% / accredited sell 7%
- 2028-Q1: retail 2% / accredited sell 5%
- Maturity: route to Uniswap

**Daily KX sell volume tracker:** In-memory map per wallet, resets at midnight UTC. When a sell exceeds 80K KX/day, XChan returns a structured error with options (retail remaining KX at 2% or register for accredited at 10%).

**Trade logging:** `xchan_trades` MySQL table logs every execution. Endpoints:
- `GET /api/xchan/trades/recent` — public, last 20 trades (no wallet addresses)
- `GET /api/xchan/trades/summary/today` — buy/sell volume, spread income, trade count

## XCHAN COMPLETE RESERVE PICTURE (forensic audit 2026-03-24)

### All Wallet Addresses and Current Balances

**Base (Ethereum L2) wallets:**
| Wallet | ETH | USDC | wKX | Role |
|--------|-----|------|-----|------|
| `0x569EAea5F00B1f554790778d14934817bc00e733` | 0.00296 ($6.39) | $22.28 | 0 | Bridge signer, authorized wKX minter |
| `0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54` | 0.00853 | $2.50 | 8,192.7 | wKX contract owner (Joseph's LP wallet) |

**ChronX wallets:**
| Wallet | KX | Role |
|--------|-----|------|
| `FGSemyJdkCU85D4qQNWFd158J44MANAHTAF5Qx974WRR` | 884 | Bridge deposit address (ChronX side) |
| `68Y97pWzwT8r5kEfozAjhZd6b4bhrKVmJUr84NAfz129` | 10,000,000 | XChan Bond (intact) |
| `BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT` | 186,950,000 | Founder wallet |

**wKX ERC-20 contract (`0xD21176ad...`):**
- Owner: `0xF5fD...` (Joseph's LP wallet — can call `setBridge()`)
- Authorized minter: `0x569E...` (bridge wallet — can call `mint()`)
- Total supply: **21,464 wKX** still exists on Base
- totalKXLocked: 21,464 (contract self-reported)
- Joseph's LP wallet holds: 8,192.7 wKX
- Remaining ~13,271 wKX: in Uniswap pool and/or buyer wallets

### Pre-Genesis 10 Swap History (from bridge DB)

All swaps occurred March 11-14, 2026 — BEFORE Genesis 10 (March 22).

**21 total deposits detected:**
| Status | Count | Total KX | What happened |
|--------|-------|----------|---------------|
| swapped | 13 | 881 KX | wKX minted + USDC sent to seller |
| minted | 3 | 203 KX | wKX minted but no USDC sent |
| no_base_addr | 5 | 4,420 KX | KX received, no Base address registered |

**4 unique depositors:**
- `BCwHsG...` (Founder) — 9 deposits, 722 KX total
- `7Tiy3y...` — 6 deposits, 59 KX total
- `7xbB5n...` — 1 deposit, 300 KX
- `B3NZbG...` — 5 deposits, 4,420 KX (all "no_base_addr", post-Genesis 10)

**4 registered KX→Base address mappings** in bridge DB.

### What Genesis 10 Changed for XChan

Genesis 10 (March 22) reset the ChronX chain completely. This means:
1. **Pre-Genesis KX balances no longer exist** — all wallets were re-created with new allocations
2. **The bridge wallet got 884 KX** in the new genesis (from a transfer by B3NZbG...)
3. **Base was NOT reset** — wKX still exists on Base, Uniswap pool untouched
4. **wKX is now unbacked** — the 21,464 wKX on Base was backed by pre-Genesis KX deposits that no longer exist on the ChronX chain
5. **The bridge can still mint new wKX** — minting authority unchanged

### XChan Operational Status Post-Genesis 10

| Capability | Status | Detail |
|-----------|--------|--------|
| Receive KX from sellers | ✅ Works | Bridge polls `FGSemyJ...` for incoming transfers |
| Convert KX to wKX | ✅ Works | Bridge wallet is authorized minter |
| Send USDC to sellers | ✅ Works | $52.28 USDC in reserve (after pool seed) |
| Receive USDC from buyers | ✅ Works | Buyers send to `0x569E...` |
| Send wKX to buyers | ✅ Works | Bridge can mint wKX on demand |
| Uniswap pool | ✅ Live | $10 USDC + wKX at $0.00319/KX, liquidity active |

## UNISWAP POOL SEEDED (2026-03-24)

**Pool:** `0x23503b2947B07000279C0ac281ec61dBeb95b36D` (wKX/USDC, 1% fee, Base)
**Status:** LIVE with liquidity. Price feed active.

**Seeding transactions:**
1. Mint 3,135 wKX to bridge: `0x9df5e9efb8c4ba9e93fdafaa0370427cbbe170a4ae39eeea26f502854b3defea`
2. USDC approve: `0x1cf0cba0c996ba08a8fc0938490ddcd6fb21c845a52ced1fdd0cc2466b8c043f`
3. wKX approve: `0xd36e1f8916fa8dac39d541d491d0291d98a3a3292c1f73abd42742f026110a3a`
4. Add liquidity: `0xbb6d31124b12995a97aa586a7d17e72f78cb0d45b6abe8a69bb1cca77baf9bb8`

**Pool state after seeding:**
- Price: $0.003190 per wKX (matches ICO price)
- Pool USDC: $10.00
- Pool wKX: ~0.03 (most goes to concentrated position math)
- Liquidity: 564,778,005,311

**CoinMarketCap readiness:** Pool has liquidity, Uniswap V3 price feed active on Base. wKX/USDC pair discoverable by aggregators.

**Bridge wallet after seeding:**
- USDC: $52.28 (down from $62.28)
- wKX: ~3,135 (leftover from mint, not all consumed by pool)
- KX (ChronX side): 1,000,884

### What Still Needs to Happen

1. **Joseph funds more USDC** — send USDC on Base to `0x569EAea5F00B1f554790778d14934817bc00e733` ($500+ recommended)
2. **Burn pre-Genesis wKX** — Joseph burns 1,000,784 wKX from Coinbase (`0x2e78...`) to dead address
3. **CoinMarketCap listing** — submit wKX token for listing with pool as price source

## WHITEPAPER v6.8 (2026-03-24)

**Published:** `https://github.com/Counselco/chronx-docs` (commit `5db1ec1`)
**Local:** `C:\Users\Josep\chronx-docs\chronx-whitepaper-v6.8.docx`
**Desktop:** `C:\Users\Josep\OneDrive\Desktop\chronx-whitepaper-v6.8.docx` + `.pdf`

**Changes from v6.7:**
- Added Section D.9: Node Economics and Long-Term Sustainability
  - 2B KX (24.2% of supply) reserved for nodes + treasury 2029-2128
  - H_100 harmonic release schedule explained
  - Hardware requirements documented (modest: 4 cores, 8GB, 500GB SSD)
  - First annual release ~$2.8M USD at ICO price
  - Comparison to Bitcoin node economics
  - Foundation Treasury role across 100 years
  - Plain English sustainability case
- Version v6.7 → v6.8 (all locations)

**Previous v6.7 changes:**
- Section 1: 3-sentence plain English opening
- Section 4: five EPPs, Bond Instrument explanation
- Section 4.5: CPNX promoted to EPP
- Section 5.2: Bond Instrument definition (100yr, 0%, lender-exit only)
- Section 8 tokenomics table: CPNX Bond row (1,000,000 KX)
- Section C.2: Governance Directives reference
- ICO access: $250 via XChan (was $100)

## XCHAN INTERNAL RESERVE MODEL (2026-03-24)

**Execute endpoint functional** against internal reserve. Key architecture:
- Sell KX: user sends KX to bridge → bridge mints wKX → sends USDC from reserve (spread per tier)
- Buy KX: user sends USDC to bridge → bridge holds USDC → sends KX via CLI transfer
- Governance cap: $250/tx, $250/day per address (accredited: $10K)
- Reserve endpoint: `GET /api/xchan/reserves`
- Signer wallet: `BRIDGE_ETH_PRIVATE_KEY` from .env

**What Joseph needs to fund:** USDC on Base to `0x569EAea5F00B1f554790778d14934817bc00e733`. Current: $22.28. Recommend $500-1000.

## XCHAN GENESIS 10 RESTART (2026-03-24)

### KX Transfer Completed
1M KX transferred from Founder wallet to bridge wallet.
- TX: `014191c28a04162ed5d182b68f5080421032419daf95e28030f876760b40d3ee`
- Bridge wallet balance: **1,000,884 KX** (buy-side reserve)
- Founder wallet balance: 185,950,000 KX (reduced from 186,950,000)

### Auto-Mint Issue
The bridge auto-minted 1,000,000 wKX to `0x2e7825b5...` (Founder's registered Base address) before the reserve exclusion was added. Bridge code now excludes Founder, XChan Bond, and Public Sale wallets from auto-minting.

### wKX Burn Required — Current Distribution (1,021,464 wKX total)
| Holder | wKX | Joseph controls? |
|--------|-----|-----------------|
| `0x2e7825b5...` (Founder's Base addr) | 1,000,784 | Yes (MetaMask) |
| `0xF5fD6Da9...` (LP wallet) | 8,192.7 | Yes (MetaMask) |
| V4 Pool Manager | 12,187.3 | Yes (remove liquidity first) |
| `0x5a228855...` (external buyer) | 300 | **No** — cannot burn |
| **TOTAL** | **1,021,464** | 1,021,164 burnable |

### Joseph's Manual Burn Steps (MetaMask/Trust Wallet)

**Step 1 — Remove V4 pool liquidity:**
- Go to app.uniswap.org, connect LP wallet (`0xF5fD...`)
- Pool → Your Positions → find wKX/USDC position
- Remove 100% → confirm transaction
- ~12,187 wKX + some USDC return to LP wallet

**Step 2 — Burn from LP wallet:**
- In MetaMask, send ALL wKX from `0xF5fD...` to dead address:
  `0x000000000000000000000000000000000000dEaD`
- Token: wKX (`0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677`)
- Amount: MAX (all wKX in LP wallet)

**Step 3 — Burn from Founder's Base wallet:**
- Switch to `0x2e78...` in MetaMask
- Send ALL wKX to dead address: `0x000000000000000000000000000000000000dEaD`
- Amount: MAX (~1,000,784 wKX)

**Step 4 — Verify:**
- Check wKX total supply on BaseScan:
  `https://basescan.org/token/0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677`
- Supply should drop to ~300 (the external buyer's unburnable wKX)

### Cannot Burn
300 wKX held by `0x5a22885580617bde5dccb48f468f31476b8d33f5` — this is an external buyer from pre-Genesis 10. Joseph cannot burn tokens he doesn't own. This wKX is unbacked and effectively worthless since the underlying KX was wiped in Genesis 10.

### Stuck Pre-Genesis 10 Deposits
5 deposits from `B3NZbG...` (Public Sale wallet) marked `genesis_reset` in bridge DB. Total: 4,420 KX (wiped in Genesis 10). **Goodwill policy:** if any pre-Genesis depositor contacts Joseph, refund from faucet at yo@chronx.io.

### Bridge Reserve Exclusion (new)
Bridge daemon now excludes these wallets from auto-minting:
- Founder wallet (`BCwHsG...`)
- XChan Bond (`68Y97p...`)
- Public Sale (`B3NZbG...`)
- Old Public Sale (`5TBvi...`)
Future reserve deposits from these wallets park KX without triggering wKX minting.

**XChan long-term vision:**
- Stage 1 (now): Joseph as sole liquidity provider via internal reserve
- Stage 2 (post-ICO): Uniswap pool deepens naturally with trading volume
- Stage 3 (mature): XChan routes to best available price (reserve vs pool)
- Foundation controls USDC reserve sweep cadence

**ICO Buy KX flow:**
chronx.io/ico.html → accreditation form (name, country, wallet, email, self-cert) → submit → Joseph reviews → approved wallets get $10K limit on XChan. Non-accredited users → "Buy KX on XChan →" button → xchan.io with $250 governance cap.

**LEGAL DEPENDENCY — ACCREDITATION:**
Current system is self-certification only. Securities lawyer MUST review before ICO launch (Sep 22 2026). $250 default is based on Reg CF/Reg A+ thresholds as interim conservative limit. Cross-border attorney engagement is a pre-ICO requirement.

---

## PARTNER READINESS ASSESSMENT (corrected 2026-03-24)

### CPNX: ✅ 100% Ready
All features functional. Bond on-chain (10M KX). Identity verified. Web request form live. Admin panel complete with applications workflow.

### XCHAN: ⚠️ ~30% Ready
- **Quote endpoint:** working ✅ ($0.003077/KX from Uniswap V4 pool slot0, 15s cache)
- **Execute endpoints:** wired to placeholder, not real Uniswap ❌. Both return `"pending_execution"`. No Router configured. No signer wallet.
- **wKX Bridge:** healthy ✅ (defensive try/catch + email lock filter added 2026-03-24, running clean)
- **Daily cap:** $500/direction. Volume tracking in-memory (resets on restart).
- **Bond:** 10M KX on-chain at `68Y97pWzwT8r5kEfozAjhZd6b4bhrKVmJUr84NAfz129`.
- **To make functional:** Wire Uniswap V3 Router swap calls, fund signer wallet, seed pool liquidity, end-to-end test.
- **Estimated:** 2-3 sessions.

### MISAI: ⚠️ ~35% Ready

#### TYPE M LOCK — FULLY IMPLEMENTED ✅
Confirmed across 8 files in the Vultr codebase (2026-03-24 audit).

**What TYPE M is:** TYPE M is NOT a separate transaction type. It is a standard `TimeLockCreate` with these fields set:
- `lock_type: Some("M")` — tags the lock as AI-managed
- `agent_managed: Some(true)` — boolean flag
- `investable_fraction: Some(f64)` — e.g. 0.80 (80% of locked KX available for AI trading)
- `lock_metadata: Some("[184-char hex]")` — encrypted claim secret for MISAI:
  ephemeral_x25519_pubkey(32B) || nonce(12B) || ciphertext(32B) || tag(16B)
- `grantor_axiom_consent_hash` — BLAKE3 hash of combined promise + trading axioms
- `risk_level: Option<u32>` — 1-100 from wallet slider
- `investment_exclusions: Option<String>` — comma-separated exclusion list
- `grantor_intent: Option<String>` — free text (max MISAI_LOAN_PACKAGE_MAX_INTENT_CHARS)
- `backup_executors: Option<Vec<DilithiumPublicKey>>` — up to 3 backup AI executors
- `executor_threshold: Option<u8>` — minimum executor agreement threshold

**Key implementation locations:**
| File | What | Lines |
|------|------|-------|
| `transaction.rs` | TimeLockCreate fields (lock_type, agent_managed, investable_fraction, etc.) | 436-500 |
| `transaction.rs` | `ExecutorWithdraw` action (lock_id, destination, executor_pubkey) | 715-721 |
| `transaction.rs` | `AgentRegister`, `AgentCodeUpdate`, `AgentLoanRequest` actions | 674-699 |
| `engine.rs` | ExecutorWithdraw handler (validation, rate limit 3/24h, PendingExecutor) | 1414-1513 |
| `engine.rs` | `sweep_executor_withdrawals` finalization sweep | 2983-3042 |
| `account.rs` | `PendingExecutor` / `ExecutorWithdrawn` lock statuses | 303-308 |
| `db.rs` | 5 sled trees: agent_loans, agent_custody_records, axiom_consents, executor_withdrawals + full CRUD | 345-1299 |
| `error.rs` | `NotTypeMlock`, `ExecutorPubkeyMismatch`, `ExecutorWalletMismatch`, `LockMetadataNull`, `ExecutorWithdrawRateLimited` | 242-256 |
| `api.rs` | `getInvestablePromises`, `getGenesis8Constants`, `getMisaiPubkey` RPC | 220-227 |
| `types.rs` | `RpcAgentRecord`, `RpcAgentLoanRecord`, `RpcInvestablePromise` | 341-410 |
| `constants.rs` | `MISAI_MIN_INVESTMENT_WINDOW_DAYS=90`, `AI_LOCK_MAX_BACKUP_EXECUTORS=3` | 196, 293 |
| `main.rs` (CLI) | `executor-withdraw` subcommand | — |

**Dormant (needs governance flag flip):** `AgentRegister`, `AgentCodeUpdate`, `AgentLoanRequest` — scaffold complete, returns `FeatureNotActive`.

**SEARCHING FOR TYPE M IN CODE — NOTE FOR ALL CC INSTANCES:**
Do NOT search for "TypeM" or "AiManaged" — these strings do not exist.
DO search for: `agent_managed`, `lock_type`, `lock_metadata`, `ExecutorWithdraw`, `investable_fraction`

#### Other MISAI Status
- **EXECUTOR_WITHDRAW_DELAY:** ✅ SET to 86400 seconds (24 hours). Confirmed in both `genesis-params.json` and `/opt/misai/.env` (2026-03-24).
- **MISAI X25519 keypair:** `/opt/chronx-notify/.env` (for lock_metadata encryption)
- **API running:** `misai-api` service, 2+ weeks uptime. Market data flowing (9 assets, 30s poll).
- **AI engine:** stopped making decisions ❌ (last decision: 2026-03-07, 17 days ago). Service polls prices but generates no new decisions.
- **Executor wallet:** empty ❌ (`64PXAwjapumXadK4e5Zk7f8zAxhaKwJifSJLHHiRsDKb` = 0 KX)
- **Bond:** 10M KX on-chain at `2EY2u8iLXW6KXM6zH2PYcB98WDBzBU7DK4d2PsLL422v`.

#### MISAI Front Page — Redesigned (2026-03-24)
Three live status indicators on landing page (above existing comic):
1. **Engine running** — green/yellow + heartbeat time
2. **Type M discovery** — green/yellow + mandate count
3. **AI execution** — yellow = governance gate active
All fetch from `/misai/api/status` every 30 seconds. Comic (10 panels) preserved below.

#### MISAI New Pages (2026-03-24)
- `/status.html` — live engine log (auto-refreshes 10s), engine/mandate/decision summary cards
- `/mandates.html` — discovered Type M locks + registered agents table, governance notice
- `/decisions.html` — complete AI decision ledger with stats, every decision permanently on ChronX DAG

#### MISAI New API Endpoints (2026-03-24)
- `GET /misai/api/status` — engine heartbeat, mandate counts, last decision age, gate status
- `GET /misai/api/log` — last 100 lines from engine.log or journalctl fallback
- `GET /misai/api/mandates` — combined list from misai_mandates + agents tables
- `GET /misai/api/decisions` — merged decision ledger from decisions + misai_batch_decisions

#### MISAI Batch Decision Architecture
- **Batch A:** Aggressive/Long (risk >66, >10yr horizon)
- **Batch B:** Moderate/Medium (risk 34-66, 5-10yr)
- **Batch C:** Conservative/Short (risk <34, <5yr)
- ONE AI decision per batch per cycle. All mandates get identical decision, proportional execution by size.
- Fee: 0.4 KX per mandate per decision. Fee source: proceeds only, never principal. Accrues as debt if returns insufficient.

#### MISAI SQLite Tables (added 2026-03-24)
- `misai_mandates` — discovered Type M locks (lock_id, size_kx, risk_level, batch_id, status, accrued_fees_kx)
- `misai_batch_decisions` — batch AI decision ledger
- `misai_batch_mandate_link` — decision/mandate mapping with kx_affected + fee_kx

#### MISAI Heartbeat
Engine writes `/opt/misai/heartbeat.txt` each cycle. Status API checks file age (<2min = running). Engine log: `/opt/misai/logs/engine.log`.

#### MISAI Backend Notes
- Uses SQLite (`better-sqlite3`, synchronous) NOT MySQL. DB: `/opt/misai/misai.db`
- Port 4040, proxied via nginx at `api.chronx.io/misai/*`
- Index.js: 1170 lines. Engine.js: 707 lines. Market.js: 141 lines.
- Claude (Anthropic SDK) for AI decisions. Demo mode (simulated USD) and real mode (on-chain KX).

#### MISAI Engine Restart (2026-03-24)
**Root cause of March 7 stoppage:** All 3 agents had time-limited trade sessions that expired. Agent "Super Computer" and "Best Available Option" had 24h sessions; engine set them to `status='paused'` and the cron skipped them. No auto-restart mechanism existed.
**Fix applied:** All agents reactivated (status='active', trade_end_at=NULL). Heartbeat + file logging added to engine.js.
**BLOCKER:** Anthropic API key (`sk-ant-api03-h8UG7...`) is **invalid/revoked** — returns 401. Decisions will resume immediately once a valid key is set in `/opt/misai/.env` and service restarted.
**Action needed:** Replace `ANTHROPIC_API_KEY` in `/opt/misai/.env` with a valid Claude API key, then `systemctl restart misai-api`.

#### MISAI Remaining Work (1-2 sessions)
1. Replace Anthropic API key in .env (current key revoked)
2. Fund executor wallet with KX for first demo trade
3. Wire MISAI cron to detect new TYPE M locks on-chain and auto-submit ExecutorWithdraw
4. Test end-to-end: lock → detect → withdraw → convert via XChan → trade → return at maturity
5. Wire batch decision loop into engine.js (architecture defined, SQLite tables created)

### HEDGEKX: ⚠️ ~55% Ready (up from 5%)
- **Backend API LIVE** ✅ on Vultr port 4044, systemd service `hedgekx-api`.
- **MySQL tables:** `hedgekx_hedges`, `hedgekx_reserves` created in `chronx` database.
- **Endpoints:** `/hedgekx/quote`, `/hedgekx/purchase`, `/hedgekx/status/:id`, `/hedgekx/reserves`.
- **Governance enforcement:** API fetches directives from `governance-directives.json` every 5 min. Enforces currency restriction, daily cap, duration limit, partial fill logic.
- **Website updated** ✅ — No more "Q4 2026" placeholders. Live calculator with quote API. Governance notices displayed from JSON.
- **Phase 1 constraints:** Overnight only, $250 max, USDC only, 1.5% premium, Joseph as sole LP.
- **Settlement:** Auto-settles expired hedges every 60s. If KX drops, logs payout for manual USDC processing.
- **Joseph seeding initial USDC liquidity** ✅ (confirmed).
- **Remaining:** Seed USDC into reserve, test end-to-end purchase flow, wallet integration for premium payment.

#### HedgeKX Phase 1 Architecture
- Duration: overnight only (until midnight UTC)
- Max hedge: $250 per transaction
- Max daily: $250 total
- Premium: 1.5% of notional (governance parameter)
- Liquidity: Joseph's USDC (sole provider)
- Settlement: automatic at midnight UTC
- If KX drops: HedgeKX pays difference from USDC reserves
- Revenue: premium income accumulates in reserves
- Partial fill: offered when capacity partially available

#### HedgeKX Governance Directives (live)
Three yellow notices in `governance-directives.json`:
1. `CURRENCY_RESTRICTION`: USDC only. Others require governance vote.
2. `DAILY_CAP`: $250/day, subject to capacity. Resets midnight UTC.
3. `DURATION_RESTRICTION`: 1-day max. Revolving loans: rejected or partially filled if capacity insufficient at renewal.

API enforces governance at runtime:
- Loads directives on startup + every 5 min
- Currency check, cap check, duration check before quote
- Partial fill offered when cap nearly reached
- All governance notices returned in API response
- Website displays notices from JSON (live)

#### HedgeKX API Endpoints (live on api.chronx.io)
- `GET /hedgekx/quote?notional_usd=X&currency=USDC` — governance-checked quote
- `POST /hedgekx/purchase` — create hedge `{chronx_wallet, notional_usd}`
- `GET /hedgekx/status/:id` — hedge status + current exposure
- `GET /hedgekx/reserves` — public reserve status + governance notices

#### HedgeKX Roadmap
- Phase 1: Overnight, $250, USDC only (NOW)
- Phase 2: Up to 7 days, $1,000 cap (when reserves > $2,000)
- Phase 3: Open liquidity providers, longer durations, more currencies

### VERIFAS: 🔲 Protocol ~70% / Legal 0%
- **Bond confirmed:** 10M KX on-chain at `CNUuEt3kQNAeQtSP9Y9muyCMujxFWq2AfsTecjHvCYtD`.
- **Identity verified on-chain:** "Verifas Bond", permanent, gold badge.
- **Executor eligibility window:** needs config (1 session).
- **Legal:** Swiss nonprofit charter needed — start immediately (8-12 weeks).
- **To complete protocol:** 1 session for eligibility config.

### BUILD PRIORITY ORDER
1. **XCHAN** (2-3 sessions) — closest to working, direct revenue path
2. **MISAI** (2-3 sessions) — TYPE M protocol layer is done, needs engine restart + wiring
3. **VERIFAS** (1 session) — low code effort, legal runs in parallel
4. **HEDGEKX** (3-4 sessions) — largest build, ship as beta closer to ICO

### ⚠️ CRITICAL NOTE FOR ALL FUTURE CC INSTANCES

The partner readiness assessment from 2026-03-24 contained a critical error — it declared TYPE M "NOT IMPLEMENTED" after searching for wrong string literals ("TypeM", "AiManaged"). This was false. TYPE M has been implemented since March 2026 across 8 source files, tested functional, and was only missed because the previous CC searched for assumed names instead of actual field names.

**Before declaring any feature unimplemented, ALWAYS:**
1. Search Vultr source directly (`/home/josep/chronx/crates/`)
2. Search for actual field names, not assumed names (e.g. `agent_managed` not `TypeM`)
3. Check the Action enum in `transaction.rs` for action tags
4. Read the full historical ai-brief session logs
5. Cross-check with Joseph before writing "NOT IMPLEMENTED" to ai-brief

**TYPE M search terms that WORK:** `agent_managed`, `lock_type`, `lock_metadata`, `ExecutorWithdraw`, `investable_fraction`, `PendingExecutor`
**TYPE M search terms that DO NOT WORK:** `TypeM`, `AiManaged`, `type_m`, `AI_Lock`

### TWO-MACHINE SETUP (never omit)
- **CC-Win** = Windows PC (primary build/deploy)
- **CC-Mac** = Mac Mini M1 (iOS + Claudie)
- Always separate labeled blocks. Never combine.
- Joseph is a beginner. Plain English throughout.

---

## ✅ GENESIS 9 COMPLETE (2026-03-18) [SUPERSEDED BY GENESIS 10]

**Genesis version: 9.0** — Node v9.0.0 deployed. No re-genesis — binary-only upgrade from Genesis 8.

**Chain state:** SUPERSEDED. Genesis 10 replaced this chain on 2026-03-22.

**All 10 payment types (live, zero fees, immutable):**
- TYPE S — Standard Promise (TimeLockCreate)
- TYPE M — AI-Managed Promise (agent_managed + MISAI)
- TYPE I — Invoice (recipient-gated payment request)
- TYPE C — Credit Authorization (pre-authorized variable draws)
- TYPE Y — Interest Bearing Deposit (principal + interest obligation)
- TYPE V — Conditional Validity (attestor-released payment, M-of-N)
- TYPE L — Ledger Entry (bonded agents only, Promise Chain anchors)
- TYPE G — Wallet Group (CreateGroup, AddGroupMember, RemoveGroupMember, DissolveGroup, TransferGroupOwnership)
- TYPE P — Payment Request (on-chain, dormant — no wallet UI yet)
- TYPE T — Transfer (basic KX send)

**Genesis 9 new features:**
- Wallet Groups (TYPE_G): 5 new Action variants — CreateGroup, AddGroupMember, RemoveGroupMember, DissolveGroup, TransferGroupOwnership
- AuthorizedSet: Lock claim authorization by wallet list or group ID
- succession_group, backup_executors, executor_threshold fields on TimeLockCreate
- Humanity Stake pool infrastructure
- Node auto-update system: checks chronx.io/version.json every 24h, desktop notification with one-click update (Windows)

**Previous Genesis 8 features (all still live):**

**AI Agent Axioms:** 6 axioms (replaces 4 AI Trading Axioms). Encoded at genesis, immutable.
- I: Mandate, II: Transparency, III: Risk, IV: Separation, V: Coordination, VI: The Law
- Combined hash: `af1349b9f5f9a1a6a0404dea36dcc9499bcb25c9adc112b7cc9a93cae41f3262`

**Sign of Life:** Live. Annual interval (365 days), 90-day grace period. Guardian defaults to grantor.

**Promise Chains:** Infrastructure live. Daily anchor hashes on main chain.

**Wallet:** v2.2.2 (Windows + Android). 18 new Tauri commands for Genesis 8 types. CONVERT_TO suggestion field added.
- v2.2.2 new features: Identity checkmarks, KXGO badges, Commitments section (see below)
- v2.2.2 new Tauri commands: `get_verified_identity`, `get_wallet_badges`, `get_commitments`, `cancel_commitment`
- Current Android versionCodes: internal 2002002, production 3002002
- Next Android versionCodes: internal 2002003, production 3002003

**CONVERT_TO field:** Added to TimeLockCreate (suggestion only, max 50 chars). Stored in separate `lock_convert_to` sled tree for backward compatibility with existing bincode data. No protocol behavior — KX always releases as KX.

**Identity Verification (Genesis 8 patch 1):**
- IdentityVerified and IdentityRevoked TYPE L variants: live
- chronx_getVerifiedIdentity RPC: live (returns latest identity or null)
- chronx_getIdentityHistory RPC: live (returns full audit trail)
- identity_index secondary sled tree: live
- Test: Founder wallet verified as "ChronX Founder" / "FOUNDER" / gold (#D4A84B)
- Logic: latest entry wins — verify/revoke/re-verify cycle tested and working

**Identity in Wallet v2.2.2:**
- Wallet UI: gold ✓ checkmark + display_name for verified wallets (Promises tab, History tab)
- Falls back to truncated address for unverified wallets
- `identity_or_short()` helper with HashMap cache per panel
- `get_verified_identity` Tauri command (fetches from avatar meta API)
- KXGO badges: server-side registry in wallet_badges MySQL table (separate from on-chain identity)
- Block explorer checkmark display: future
- Corporate verification intake process via Verifas or bonded verifier: future

**Whitepaper:** v4.5 on GitHub (Counselco/chronx-docs)

**Node:** v9.0.0 — Linux x64 binary at chronx.io/dl/chronx-node-linux-x64.tar.gz. Auto-update system live (checks chronx.io/version.json every 24h).

**Founder balance:** ~187,700,000 KX (188M minus resent promises)

**Key wallets (Genesis 8):**
- Founder: BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT
- Public Sale: B3NZbGxzkNMXgvR6NqvCJGN2UUuiyBMHxXRYs7xRdXg5
- Faucet: 455fV35X3viK8je1hWoUrMaxzj8iUsZr3a3hvM8GH31T (3M KX)
- MISAI Bond: AG15CUEyMQcbBTf1stvrT52RJ1URxV2bRLFoPUgrh4C5 (10M KX)
- Verifas Bond: ERt5ZuYU3WMLEpZQtRxzftApRi5pSr7vcW3WaDV4y5LK (10M KX)
- Relay: 8Nodc3F2HwUjPMLaFfTJ6WKuSvjEa4fTeopLUK52y5EE (10 KX)

**Notify API (Genesis 8 + v2.2.2):** 10 Genesis 8 endpoints (8 internal + 2 admin) + 2 wallet v2.2.2 endpoints. Sign of Life, Guardian Transition, Verifas Pre-notify, TYPE V Attestor, TYPE I Invoice, TYPE Y Deposit matured/defaulted.
- **v2.2.2 endpoints (live on Vultr):**
  - `GET /wallet/badges/:wallet_address` — returns badge list from wallet_badges MySQL table (public, no auth, Cache-Control 300s)
  - `POST /wallet/commitment-cancel` — stores TYPE V cancellation request in commitment_cancellations table, notifies attestor
- **New MySQL tables (chronx database on Vultr):**
  - `wallet_badges` — wallet_address, badge_type, badge_color, issued_by, issued_at
  - `commitment_cancellations` — wallet_address, commitment_id, commitment_type, reason, requested_at

**⚠ TODO — Node auto-update notification:** Windows node software does not have an auto-update notification system. Node operators running old binaries will not automatically know about Genesis 8. This MUST be addressed before ICO (September 22, 2026) so node operators stay in sync. Options: (1) version check on startup against chronx.io/version.json, (2) P2P protocol version negotiation, (3) email notification to registered node operators.

**⚠ TODO — Remaining promise resends:** Some long-term promises from the pre-wipe snapshot may still need resending. Check genesis8-pre-wipe-report.txt on Vultr. The 250K to usmanuah9 and 50K to cabfone11 have been resent.

---

## ✅ COMPLETED v1.4.56 BUILD (2026-03-07)

All three pending items shipped in v1.4.56:

1. **[DONE] Promises tab — "Promises Coming To Me" section** with gold header, incoming delayed sends visible
2. **[DONE] History tab — gold "SCHEDULED" badge** for outgoing delayed sends with future unlock dates
3. **[DONE] Sender identity in Promise emails** — wallet now sends sender_email + sender_wallet in /notify payload

**Build outputs (v1.4.89 — 2026-03-13):**
- Windows: `chronx-wallet-setup.exe` (v1.4.89) deployed to chronx.io/dl/
- Android: v1.4.89 APK deployed to chronx.io/dl/ChronX_Android_v1.4.89.apk
- Android internal: `chronx-wallet-1.4.89-internal-1004089.aab` — ready for Play Console Internal Testing
- Android production: `chronx-wallet-1.4.89-production-2004089.aab` — on Desktop, ready for Google Play submission
- Next build MUST use versionCode 1004090 / 2004090

**v1.4.89 changes:**
- **XChan Convert: saved address chips** — replaced single saved address + "Save for next time" checkbox with clickable chip system. Up to 5 saved addresses shown as gold-bordered chips above the red warning. Click chip to fill address field, click × to delete. Nickname+Save row appears when valid address entered and < 5 saved. Enter key in nickname field also saves. Backend: new `base_addresses` field in WalletConfig (Vec of `{address, nickname}`), new commands `get_base_addresses`, `add_base_address`, `delete_base_address`. Auto-migrates legacy single `base_address` on first load.

**v1.4.88 changes:**
- **XChan Convert: red warning above Base address input** — always-visible red bold text: "Please enter ONLY a receiving USDC address on the Base network. Sending to any other address risks permanent loss of funds."

**wkx-bridge fixes (2026-03-13):**
- **eth_getLogs block range fix**: `pollUnwraps()` now chunks in 8-block ranges (was 2000) with 500ms delay between chunks. Alchemy free tier allows max 10 blocks per `eth_getLogs`. Initial backfill reduced from 1000 to 50 blocks. No more `UNWRAP POLL ERROR` spam.
- **Deposit 4 completed** (10 KX, was 'minted'): USDC sent to 0x2e7825b5e3ac7627594db18f246da3f5c431ac0a — $0.030462, tx 0x72779e3bf03cb9aa2895102ef1343f22c6ecbdd2e0cd1270118c00520534c61a. Status: swapped.
- **Deposit 5 completed** (10 KX, was 'no_base_addr'): Base address 0x2e7825b5e3ac7627594db18f246da3f5c431ac0a registered + minted (tx 0x6ecdd0a3e19e0c7bba53fdf368c38df445d75d00d8b86364021b9aa6cd6e5704) + USDC sent ($0.030462, tx 0xbb21c06b1b7841bd12da4c4aa62a9c38206eea278787118c988111f7e76b6b5f). Status: swapped.
- Updated BASE_RPCS in `/opt/wkx-bridge/index.js` — Alchemy primary, mainnet.base.org secondary, publicnode tertiary, llamarpc fallback.
- Previously: Manually completed stuck 3 KX conversion (deposit 802452ff...) — $0.009139 USDC, tx 0xca17d71e...c1331.

**v1.4.87 changes:**
- **"Promise" badge for outgoing email locks** — History tab now shows "Promise" instead of "Pending" for outgoing email sends that are submitted but not yet delivered. Change is in frontend display mapping only (`lib.rs` line 6062): when backend returns `"Pending Claim"` status, badge text renders as `"Promise"` instead of `"Pending"`.

**v1.4.86 changes (server-side fix):**
- **chronx-notify: Fix auto-delivery for verified email recipients** — the early `claim_registrations` INSERT in POST /notify was setting `status='delivered'` for ALL sends, preventing the 5-minute auto-delivery cron from processing them. Fixed: now checks `verified_emails` table; verified recipients get `status='registered'` with correct recipient wallet address; unverified get `status='pending_claim'`. The cron picks up `registered` rows where `unlock_at <= now` and auto-delivers via relay wallet.
- **Delivered stuck 33 KX + 2 KX** — email locks to josephrsanchez@gmail.com had `status='delivered'` but NULL `delivered_at`. Reset to `registered`, cron auto-delivered both within 30 seconds.

**v1.4.85 changes:**
- **Node: wallet-to-wallet auto-delivery sweep** — new `sweep_matured_wallet_locks()` runs every 60s, auto-delivers matured non-email locks (credits recipient, sets status Claimed). Email locks (0xC5 marker) still require claim code.
- **Wallet UI: removed "Claim Now" from wallet-to-wallet locks** — matured wallet locks show "Arriving shortly..." (sweep handles delivery). Email locks show "Enter claim code to receive".
- **Promises tab filter**: only shows locks where status=Pending AND unlock_at > now+60s (instant/completed sends no longer appear)
- **Save-contact banner**: replaced text input + single button with two-button card (gold Save Contact / red Cancel), no text input, auto-dismiss after 10 seconds
- **XChan conversion fix**: `convert_kx_to_usdc` now includes sender's KX address in POST to `/xchan/convert`; server-side endpoint extracts `kx_address` from body for registration
- chronx-notify restarted with /xchan/convert fix

**v1.4.84 changes:**
- Fixed XCHAN_BRIDGE_WALLET constant (was faucet wallet, now correct wKX bridge wallet FGSem...)
- wallet.html: APK button updated, sideload installation steps added (collapsible)
- version.json: android_download_url direct APK link
- All 8 translations updated (wdl_sideload_* keys added)
- wkx-bridge daemon: Fixed Base RPC ordering (mainnet.base.org demoted to fallback, llamarpc/publicnode primary)
- chronx-notify: Added GET /xchan/check-address and POST /xchan/convert endpoints

**Also completed earlier:**
- Re-genesis v5.0: Founder/MISAI/Verifas as genesis-level allocations, AI Trading Axioms metadata, Public Sale 6,093M
- Homepage rewrite: new hero ("A Promise the Blockchain Keeps"), 10-panel comic embed (panel 10 = "Try It Yourself" faucet CTA), "What Makes ChronX Different" section, Protocol Promise paragraph
- MISAI.io reframe: "The AI That Keeps Promises" (removed arena/leaderboard)
- Pre-ICO invite-only (removed payment addresses from homepage)
- Whitepaper v3.4: v5.0 tokenomics, AI Trading Axioms appendix, Foundation section, claim-on-maturity model, executor model
- governance.html: Dedicated page for ChronX Protocol Foundation + AI Trading Axioms + Genesis vs Governance table
- Governance nav link added to all 17 HTML pages with i18n (7 languages)
- tokensale.html + preico.html: Updated Public Sale allocation to 6,093,000,000 KX

---

## 1. PROJECT OVERVIEW

**ChronX** is a purpose-built blockchain protocol for future payments. The central innovation is the native time-lock: an on-chain Promise to deliver funds at a future date, enforced by the protocol itself. No custodian. No lawyer. No fees. Ever.

**Vision:** Enable any human to make a verifiable, unstoppable financial promise to any other human.

**Founding Developer:** Joseph Sanchez (GitHub: Counselco). Solo founder. AI-assisted development via Claude Code.

**Token:** KX
**Base unit:** Chrono (1 KX = 1,000,000 Chronos)
**Total supply:** 8,270,000,000 KX (fixed forever at genesis)
**Transaction fees:** Zero. Completely free. Forever.

**Current Phase:** Pre-ICO (invite-only). Wallet v2.2.2 (Windows + Android). Live on Google Play. Website live with 10-panel comic explainer + governance page. Node on Vultr (v9.0.0 — Genesis 9). Genesis 8 re-genesis completed 2026-03-08, Genesis 9 binary upgrade 2026-03-18. Verifas.io live. MISAI.io reframed as bonded AI executor. Whitepaper v5.0 published. Governance page with AI Agent Axioms live. KXGO.io gaming platform live (Castle Wars + Battle for the Realm).

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

## 1A. PROTOCOL DELIVERY MODEL (canonical — do not contradict)

### Claim-on-Maturity
- All time-locked transfers use claim-on-maturity: KX waits on DAG, beneficiary claims with one tap
- KX never moves automatically; sits indefinitely at zero cost until claimed
- Most promises: Mary claims herself, 100% delivered, no third party involved

### Executor Eligibility (90-day window)
- After 90 days unclaimed post-maturity: lock status flips to executor_eligible
- Any bonded executor (10M KX bond) may attempt delivery
- Open race model: no exclusivity window; first to deliver wins the fee
- Fee deducted atomically from claim at delivery time — trustless, protocol-enforced
- Bob sets NOTHING about executor fees — protocol handles it

### Executor Fee Cap
- Genesis-level ceiling: 7% of delivered amount (IMMUTABLE, can only be lowered)
- Foundation may reduce effective cap via governance; can never raise above 7%
- Market competes fee downward on valuable promises

### ChronX Protocol Foundation
- Governs: executor eligibility window, fee cap (<=7%), bond requirements, executor model
- Cannot govern: total supply, timelock enforcement, zero fees, 7% ceiling, strategy code immutability
- Legal structure: nonprofit foundation (details before ICO Sep 22 2026)
- Public copy: "ChronX Protocol Foundation"

### What is Genesis vs Governance
| Parameter | Level | Mutable? |
|---|---|---|
| Total supply (8,270,000,000 KX) | Genesis | Never |
| Timelock enforcement | Genesis | Never |
| Zero protocol fees | Genesis | Never |
| Max executor fee ceiling (7%) | Genesis | Never (lower only) |
| Strategy code immutability | Genesis | Never |
| Executor eligibility window (90 days) | Foundation Governance | Yes |
| Executor model (race vs staked) | Foundation Governance | Yes |
| Effective fee cap (<=7%) | Foundation Governance | Yes, downward only |
| Bond size requirements | Foundation Governance | Yes |
| AI Agent Axioms (6 axioms) | Genesis 8 | Never |

---

## 1B. AXIOMS (canonical — encoded at genesis, immutable)

Two axiom sets are encoded at genesis. They cannot be altered by any person, governance body, or software update.

### Promise Axioms (4 axioms)
1. **Intent Is the Master** — The grantor's intent is the master. Once a promise is made and the cancellation window closes, it is irrevocable. No person, institution, or governance body can recall it.
2. **Funds Are Never Lost** — Promised funds are never lost. A promise unclaimed by its intended beneficiary within 90 days of maturity is held by the Verified Delivery Protocol. A promise unclaimed for 100 years beyond maturity is transferred to the Humanity Stake, governed for the benefit of all.
3. **The Protocol Enforces Delivery** — No custodian, no lawyer, no intermediary is required for a promise between a sender and a reachable recipient. The blockchain is the contract.
4. **The Law** — All promises and their fulfillment remain subject to the laws of applicable jurisdictions.

### AI Agent Axioms (6 axioms — Genesis 8, replaces AI Trading Axioms)
1. **Mandate** — The grantor's intent, once encoded, is carried forward by autonomous software. Algorithms may evolve. The intent does not. An autonomous agent has no authority beyond that mandate, including any credit, attestation, or draw authority the grantor explicitly encoded.
2. **Transparency** — An AI agent must commit to a permanent public record before acting. Every decision is publicly verifiable. There are no private actions.
3. **Risk** — The grantor acknowledges, and the AI agent affirms, that AI management of any investment tranche may result in gains or losses up to and including total loss.
4. **Separation** — The agent that decides does not hold funds. The agent that holds does not decide.
5. **Coordination** — An agent is not the only actor. Before acting, an agent must account for the aggregate effect of similarly situated agents acting on similar instructions.
6. **The Law** — All agent actions, mandates, and their fulfillment remain subject to the laws of applicable jurisdictions.

**Storage:** `ai_agent_axioms` key in genesis-params.json. `trading_axioms` key retained for backward compatibility (deprecated).
**Retrieval:** RPC `chronx_getPromiseAxioms` → `{promise_axioms, trading_axioms, combined_axiom_hash}`.
**Website:** governance.html displays both axiom sets.

---

## 2. ARCHITECTURE & INFRASTRUCTURE

### Node (Vultr)
- **IP:** 45.63.22.189
- **SSH (Windows):** `ssh -i ~/.ssh/id_ed25519 root@45.63.22.189`
- **SSH (Mac Mini):** `ssh -i ~/.ssh/minty_sync root@45.63.22.189`
- **User home:** /home/josep (lowercase j)
- **Node binary:** /home/josep/chronx/target/release/chronx-node
- **Wallet CLI:** /home/josep/chronx/target/release/chronx-wallet
- **Node data dir:** /home/josep/.chronx/data
- **Genesis params:** /home/josep/chronx/genesis-params.json
- **RPC (internal):** http://127.0.0.1:8545
- **P2P port:** 30303
- **Permanent P2P peer ID:** 12D3KooWMsFQDZhqAFnkcj1XjPrjjVFwsQ6UqgvffvA6HFt6MfFU
- **Identity file:** /home/josep/.chronx/p2p-identity.key (protobuf-encoded Ed25519 keypair, persists across restarts)
- **systemd service:** chronx-node (enabled, auto-restarts, uses --identity-file)
- **Last rebuild:** 2026-03-05 — v3.5: Auto-create accounts for TimeLockClaimWithSecret (new user claim fix), memo character validation (reject control chars), per-wallet rate limiting (10 tx/60s), getIncomingTransfers now returns email claim receipts for claimers. Previous: v3.4: RevertToSender sweep, ReclaimExpiredLock, Reverted status, persistent P2P identity, getNetworkInfo, getEmailLockStats

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
| Public Sale | /home/josep/.chronx/public-sale-wallet.json | Fycy2Sh4SkYiKKVdB8wQSdkymJgJZ4kAGPK7eFn7zPny | ~6,082,000,000 KX |
| Faucet | /home/josep/.chronx/faucet-wallet.json | CkBgP1mYQVFrLThM1VTqMLNXjqwW5RP7iKS4x3LouRN3 | ~3,000,000 KX |
| Node Rewards | /home/josep/.chronx/node-rewards-wallet.json | 3i4tBfxhFCoZFqmuiV7LRoZgyMMUwSq4xAr9SzAQjt6W | 0 KX (timelocked) |
| Founder | C:\Users\Josep\.chronx\wallet.json (LOCAL ONLY) | BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT | ~155,000,000 KX |
| MISAI Bond | C:\Users\Josep\chronx\misai-wallet.json (LOCAL ONLY) | 3b4J81S9A8tmh1nt8cLMZC4FUsqasYJA9a2xgax1A9eU | 10,000,000 KX |
| Verifas Bond | C:\Users\Josep\chronx\verifas-wallet.json (LOCAL ONLY) | 9ozs5P48ENM2uJKyNfsTJfGm7uM5a1K4taToxARoot7i | 10,000,000 KX |
| Relay | /home/josep/.chronx/relay-wallet.json | 8Nodc3F2HwUjPMLaFfTJ6WKuSvjEa4fTeopLUK52y5EE | ~10 KX |
| wKX Bridge | /home/josep/.chronx/wkx-bridge-wallet.json | FGSemyJdkCU85D4qQNWFd158J44MANAHTAF5Qx974WRR | 0 KX |

**IMPORTANT:** Founder wallet + bond wallets live on Windows only. Bond wallet keyfiles were generated on Vultr, backed up locally, then shredded from the server. Never leave private keys on Vultr.

### Notify API (Vultr)
- **URL:** https://api.chronx.io
- **Internal:** localhost:3001
- **Service:** chronx-notify (systemd)
- **Files:** /opt/chronx-notify/
- **Config:** /opt/chronx-notify/.env (MYSQL_PASSWORD=CxDb2026, ADMIN_KEY=ChronXAdmin2026, RESEND_API_KEY)
- **Endpoints:** POST /notify (single + cascade; sends verified/promise/claim email based on recipient status and unlock time; accepts optional `sender_email` and `sender_wallet`), POST /register, POST /faucet/register, GET /faucet/check, POST /faucet/claim (rate limited: 10/IP/hr), GET /faucet/stats, GET /rewards/status, POST /verify-email, POST /verify-email/confirm (persists to verified_emails table), POST /claim/register (pre-register wallet for auto-delivery), GET /claim/status/:code (check registration status), admin routes. Three email variants based on recipient+timing: (1) Verified recipient + immediate unlock → relay auto-delivers + 'KX is in your wallet' email. (2) Any recipient + future unlock → immediate 'You've Been Made a Promise' email sent at send time (no claim code), PLUS auto-delivery or claim code email on unlock date. (3) Unverified + immediate → claim code email as before. Promise email subject: 'You just received a Promise of X KX 🔒'. Delivery confirmation email subject: 'A Promise made to you on [original send date] just delivered ✅' — references original send date from claim_registrations.created_at. Sender identity: 3-tier fallback — sender_email (from notify payload) > ....last6 of sender_wallet > 'Someone'. sender_display stored in claim_registrations table.
- **Auto-delivery system (added 2026-03-06):** Recipients register wallet via POST /claim/register (validates claim code against on-chain locks via RPC). Cron runs every 5 min, checks `claim_registrations` table for matured locks, delivers via relay wallet (claim-by-code + transfer). Series locks re-register for next unlock. MySQL table: `claim_registrations` (claim_code UNIQUE, wallet_address, email, memo, sender_display, amount_kx, unlock_at, is_series, status, delivered_at, tx_hash, error_msg).
- **PENDING REBUILD — sender identity in notify payload (commands.rs fix applied, not yet built):** notify_email_recipient command now loads sender_wallet from keypair (account_id.to_b58()) and sender_email from WalletConfig claim email. Both fields included in /notify POST payload. Until wallet is rebuilt, existing versions send without sender fields and 'Someone' fallback is used.
- **blake3 v2.1.4:** npm package for BLAKE3 hashing (matches Rust-side claim code hashing for getCascadeDetails RPC).
- **Public endpoints (added 2026-03-04):** POST /exchange-notify (stores email + source in MySQL notify_signups table, no auth)
- **Notices endpoints (added 2026-03-04):** GET /notices (public, version-filtered), POST /notices/:id/seen, POST /notices/:id/dismissed, GET /admin/notices, POST /admin/notices, PATCH /admin/notices/:id, DELETE /admin/notices/:id
- **Notices data:** /home/josep/notices.json (JSON file, not MySQL). Each notice: id, type (urgent/message), title, body, active, dismissible, expires_at, min_version, max_version, created_by, seen_count, dismissed_count
- **Auth endpoints (added 2026-03-04):** POST /admin/login, POST /admin/logout, GET /admin/verify, POST /admin/change-password, GET /admin/login-history
- **Admin endpoints:** GET /admin/faucet/pending, POST /admin/faucet/approve, POST /admin/faucet/reject, GET /admin/preico/pending, POST /admin/preico/approve, POST /admin/preico/reject, GET /admin/registry, GET /admin/transactions, GET /admin/downloads, GET /admin/network-health, GET /admin/token-economy, GET /admin/alerts, GET /admin/signups, POST /admin/support/resolve, GET /admin/reminders, POST /admin/reminders, PATCH /admin/reminders/:id, DELETE /admin/reminders/:id, GET /admin/notices, POST /admin/notices, PATCH /admin/notices/:id, DELETE /admin/notices/:id
- **Admin auth:** Bearer token (from POST /admin/login) or legacy X-Admin-Key header. Users: /home/josep/admin-users.json. Sessions: /home/josep/admin-sessions.json. Audit: /home/josep/admin-audit.log.
- **Email delivery:** WORKING as of 2026-03-04. Fixed falsy-value bug (unlock_at:0 treated as missing).
- **Resend domain:** Verify chronx.io at resend.com/domains for better deliverability (currently using unverified domain)

### Website (Hostinger)
- **URL:** https://chronx.io
- **FTP host:** 82.29.199.47, user u507945893
- **TRUE web root:** /domains/chronx.io/public_html
- **Deploy:** `cd C:\Users\Josep && python deploy_website.py`
- **After deploy:** Purge cache at hPanel -> Cache Manager -> Purge All

### XCHAN Website (Hostinger)
- **URL:** https://xchan.io
- **FTP host:** 82.29.199.47, user u507945893.xchan.io
- **Web root:** /public_html (FTP default CWD — unlike chronx.io, no /domains/ prefix needed)
- **Deploy:** `cd C:\Users\Josep && python deploy_xchan.py`
- **Local folder:** C:\Users\Josep\xchan-website\
- **Description:** Non-custodial exchange interface with live wKX/USDC swap on Base. Independent from ChronX.
- **Swap UI (2026-03-11):** Connect Wallet (EIP-1193), Base network check, wKX/USDC swap via Uniswap v3 SwapRouter (`0x2626664c2603336E57B271c5C0b26F421741e481`), live quotes via Quoter (`0x3d4e44Eb1374240CE5F1B871ab261CD16335B76a`), 1% pool fee, 0.5% slippage tolerance. Wallet registration form (KX address + Base address) POSTs to `https://api.chronx.io/api/xchan/register`. Unwrap wKX section calls `unwrap()` on wKX contract.
- **XChan API:** systemd service `xchan-api` on Vultr, port 4042. Source: `/opt/wkx-bridge/xchan-api.js`. Shares `bridge.db` with bridge daemon. Endpoints: `POST /api/xchan/register`, `GET /api/xchan/price` (live from Uniswap v3 Quoter, 60s cache), `GET /api/xchan/lookup/:kx_addr`, `GET /api/xchan/status`. nginx route on `api.chronx.io/api/xchan/*`.

### MISAI Website (Hostinger)
- **URL:** https://misai.io
- **FTP host:** 82.29.199.47, user u507945893.misai.io
- **Web root:** /public_html (FTP default CWD — same as xchan.io)
- **Deploy:** `cd C:\Users\Josep && python deploy_misai.py`
- **Local folder:** C:\Users\Josep\misai-website\
- **Description:** AI Trading Arena — beta-only platform. KX is compute fuel, trading is simulated USD. Independent from ChronX.
- **Pages:** index.html (newbie-friendly landing: hero, 3-step how-it-works, typing demo, brokerage cards, KX explainer, beta gate), arena.html (agent deploy form + compute fuel calculator), my-agent.html (personal agent dashboard: status bar, decision feed, connect wallet, trading mode toggle), arena-live.html (leaderboard + trade feed + price ticker, post-login only), admin.html (admin dashboard + platform revenue)

### MISAI Beta API (Vultr)
- **Location:** /opt/misai/index.js
- **Port:** 4040 (bound to 127.0.0.1)
- **Systemd:** `systemctl restart misai-api`
- **Database:** /opt/misai/misai.db (SQLite — tables: beta_signups, admin_log, agents, positions, decisions, price_history, platform_revenue). Agents table has `encrypted_private_key` (AES-256-GCM encrypted wallet key) and `mode` ('simulated' or 'real'). Decisions table has `tx_hash` for on-chain KX transfers.
- **Nginx:** Proxied at `https://api.chronx.io/misai/*` (location /misai/ in api.chronx.io config)
- **Auth:** Reuses /home/josep/admin-users.json and /home/joseph/admin-sessions.json (same as ChronX admin)
- **Env file:** /opt/misai/.env — MISAI_ENCRYPTION_KEY, MISAI_AGENT_SECRET, ANTHROPIC_API_KEY, RESEND_API_KEY
- **Crypto utils:** /opt/misai/crypto-utils.js — AES-256-GCM encrypt/decrypt for private key storage
- **Endpoints:**
  - `POST /api/signup` — { wallet_address, email } → waitlist (rate limited 3/hr/IP)
  - `POST /api/verify-invite` — { invite_code } → { valid, wallet_address } (code-only lookup, no wallet needed)
  - `POST /api/admin/login` — { username, password } → { token }
  - `GET /api/admin/signups?status=` — list signups (Bearer auth)
  - `GET /api/admin/stats` — { total, pending, approved, rejected, platform_revenue_kx } (Bearer auth)
  - `POST /api/admin/approve` — { wallet_address } → generates MISAI-XXXX-XXXX invite code (Bearer auth)
  - `POST /api/admin/reject` — { wallet_address } (Bearer auth)
  - `GET /api/leaderboard` — top 20 agents by % return (public, cached 10s)
  - `GET /api/decisions/recent` — last 50 decisions across all agents (public, cached 5s)
  - `GET /api/agent/:id/decisions` — last 20 decisions for agent (public)
  - `GET /api/prices` — current market price snapshot (public)
  - `GET /api/kx-rate` — { rate, source, kx_per_decision, platform_margin } (public)
  - `POST /api/agent/register` — { invite_code, agent_name, strategy_prompt, kx_deposit, decision_interval_minutes } → creates agent with $1,000 USD + KX fuel (invite-gated)
  - `GET /api/agent/:id/status` — full agent status (name, portfolio, return %, KX balance, positions, next decision, has_private_key, mode) (public)
  - `PUT /api/agent/:id/connect-wallet` — { wallet_address, private_key } → encrypts and stores private key, sets mode='real' (ownership check: wallet must match agent owner)
  - `POST /api/agent/:id/resume` — resumes paused agent (sets status='active')
  - `DELETE /api/admin/signup/:wallet_address` — deletes signup + agents (Bearer auth)
  - `GET /api/admin/revenue` — { total_kx } sum of platform_revenue (Bearer auth)
- **Invite code format:** MISAI-XXXX-XXXX (alphanumeric, no O/0/I/1 ambiguity)

### MISAI Agent Engine
- **Market data:** /opt/misai/market.js + /opt/misai/fetch_prices.py
  - Stocks (SPY, AAPL, TSLA, NVDA, MSFT) via yfinance Python helper (execSync)
  - Crypto (BTC, ETH, SOL, BNB) via CoinGecko free API (axios)
  - Polls every 30 seconds, stores in price_history table (auto-purge >24hrs)
  - Cached in memory; merges new data with previous (preserves stale values on fetch failure)
- **XChan price module:** /opt/misai/xchan.js — manages KX/USD rate. Currently returns ICO fallback ($0.00055). Post March 11: live rate from xchan.io API.
- **Decision engine:** /opt/misai/engine.js
  - Runs via node-cron every minute, checks each active agent's `decision_interval_minutes`
  - Builds portfolio in USD: `cash_usd` + position values (quantity × live price)
  - **Real mode** (agent has `encrypted_private_key`): checks on-chain balance via `chronx_getAccountInfo` RPC. If balance >= 1.1 KX: transfers KX on-chain to treasury wallet via chronx-wallet CLI. Logs tx_hash. Syncs kx_balance from on-chain. On insufficient balance: pauses agent, sends out-of-fuel email via Resend.
  - **Demo mode** (no private key): unlimited decisions, kx_burned=0, no platform_revenue logged.
  - Treasury wallet: `BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT` (Founder wallet)
  - Wallet CLI path: `/home/josep/chronx/target/release/chronx-wallet`
  - Calls Claude Sonnet (`claude-sonnet-4-20250514`) via `@anthropic-ai/sdk`
  - AI returns JSON: `{ action: BUY|SELL|HOLD, symbol, percent_of_cash: 0-100, reasoning }`
  - BUY: converts % of cash_usd → asset quantity, SELL: liquidates position to cash_usd
  - Logs every decision with usd_before, usd_after, kx_burned, price_usd, market_snapshot
- **Schema (agents):** `starting_usd` (default $1,000), `current_usd`, `cash_usd`, `kx_balance`, `kx_per_decision` (0.4), `status` (active/paused)
- **Schema (positions):** `agent_id`, `symbol`, `quantity`, `avg_cost_usd`
- **Schema (decisions):** `action`, `symbol`, `quantity`, `price_usd`, `usd_before`, `usd_after`, `kx_burned`, `reasoning`, `market_snapshot`
- **Schema (platform_revenue):** `agent_id`, `kx_amount`, `decision_id`, `created_at`
- **Trading currency:** Simulated USD ($1,000 default portfolio)
- **KX role:** Compute fuel ONLY at 0.4 KX/decision (~$0.00128 at ICO price)
- **Platform margin:** 12% (0.048 KX per decision → treasury wallet)
- **xchan.io pricing:** GET /api/kx-rate returns ICO price $0.00319; live rate activates post March 11
- **Robinhood/Alpaca:** Phase 2 (signposted in arena.html UI)
- **Decision interval options:** 5 / 15 / 60 minutes

### RPC Endpoint (Public)
- **URL:** https://api.chronx.io/rpc (routed via api.chronx.io nginx /rpc location -> http://127.0.0.1:8545)
- **Old URL:** https://rpc.chronx.io — DNS A record missing from Hostinger, not resolving. nginx config + SSL cert exist on Vultr but unusable until DNS added.
- **rpc.js updated:** `RPC_URL = 'https://api.chronx.io/rpc'` (was `https://rpc.chronx.io`)

### GitHub Repos
| Repo | URL | Local Path |
|---|---|---|
| Protocol (node) | https://github.com/Counselco/chronx | C:\Users\Josep\chronx |
| Wallet | https://github.com/Counselco/wallet-gui | C:\Users\Josep\chronx\wallet-gui-temp |
| Docs | https://github.com/Counselco/chronx-docs | C:\Users\Josep\chronx-docs |

---

## 3. GENESIS ALLOCATIONS (Re-genesis v7.0, 2026-03-08)

**Genesis date:** January 1, 2026 00:00:00 UTC (Unix: 1,735,689,600)
**Total supply:** 8,270,000,000 KX = 8,270,000,000,000,000 Chronos

| # | Allocation | KX Amount | % | Lock Condition |
|---|---|---|---|---|
| 1 | Public Sale | 6,268,000,000 | 75.79% | Spendable at genesis |
| 2 | Treasury | 1,000,000,000 | 12.09% | 100 annual harmonic locks 2027-2126 |
| 3 | Node Rewards | 1,000,000,000 | 12.09% | 100 annual harmonic locks 2029-2128 |
| 4 | Humanity Stake | 1,000,000 | 0.012% | Locked until 2126-01-01 (100 years) |
| 5 | Milestone 2076 | 500,000 | 0.006% | Locked until 2076-01-01 |
| 6 | Protocol Reserve | 500,000 | 0.006% | Locked until 2036-01-01 |

### Genesis 7 — Zero-balance protocol wallets (created at genesis, 0 KX)
| Wallet | Account ID | Purpose |
|---|---|---|
| Verifas Vault | `JBeezsxWKiuupPmfCtKLWCYbppgABcGS4fhPLQpHrYEo` | Receives activation deposits on Day 91 |
| Activation Escrow | `8LBw5upLaTfWN92rDtmYzoVtRX14jSim9RotYTmGwrGQ` | Transient escrow during Day 91 processing |
| Humanity Stake Pool | `9zj9CyNrxVwMvwV7Kuq69RBsrXThYjXzd6YtJLztknJW` | Receives unclaimed promises at maturity + 100 years |

### Post-genesis transfers (from Public Sale)
| Allocation | KX | Recipient |
|---|---|---|
| Founder | 175,000,000 | `BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT` |
| Faucet | 3,000,000 | `CkBgP1mYQVFrLThM1VTqMLNXjqwW5RP7iKS4x3LouRN3` |
| Relay | 10 | `8Nodc3F2HwUjPMLaFfTJ6WKuSvjEa4fTeopLUK52y5EE` |
| MISAI Bond | 10,000,000 | `AG15CUEyMQcbBTf1stvrT52RJ1URxV2bRLFoPUgrh4C5` |
| Verifas Bond | 10,000,000 | `ERt5ZuYU3WMLEpZQtRxzftApRi5pSr7vcW3WaDV4y5LK` |
| MISAI Executor | 1 | `RbSYrExT6vjZKhXiEMTYZQKB8sPMcVixGLCXcBwtMui` |

**v7.0 changes from v5.0:** Founder/MISAI/Verifas moved from genesis-level to post-genesis transfers. Public Sale restored to full 6,268M. Three new zero-balance Genesis 7 protocol wallets. Promise Axioms + AI Trading Axioms stored as separate metadata keys. Genesis 7 constants stored as auditable JSON metadata. Governance wallet (Founder) recorded for VerifierRegister governance transactions.

### Treasury & Node Rewards Harmonic Series
- Formula: release_k = floor(POOL_CHRONOS / (H_100 x k))
- H_100 = 5.187377517639621
- 100 annual releases, Jan 1, 2029 through Jan 1, 2128
- Year 1 (k=1): largest release; Year 100 (k=100): smallest
- Rounding dust added to k=1 so sum is exactly 1,000,000,000,000,000 Chronos

### Chain Stats (2026-03-08, post re-genesis v7.0)
- Total genesis accounts: 7 (Public Sale, Treasury, Node Rewards, Verifas Vault, Activation Escrow, Humanity Stake Pool, + genesis allocator)
- Post-genesis accounts: 6 (Founder, Faucet, Relay, MISAI Bond, Verifas Bond, MISAI Executor)
- Total timelocks: 203 (100 treasury + 100 node rewards + 3 special)
- DAG vertices: 7 (genesis + 6 funding transfers)
- Total supply: 8,270,000,000 KX (verified)
- Registered verifiers: 1 (ChronX Verifas Placeholder, role=VerifasVault, bond=1M KX)
- Genesis metadata: promise_axioms, trading_axioms, genesis_7_constants, genesis_7_governance_wallet, genesis_7_humanity_stake_pool

---

## 4. TOKENOMICS & ICO

### Pre-ICO (LIVE NOW)
| Period | Price per KX | Discount |
|---|---|---|
| Now to June 22, 2026 (Early) | $0.001755 | 45% off ICO |
| June 22 to Sep 22, 2026 (Standard) | $0.002297 | 28% off ICO |

### Payment Addresses
| Currency | Address |
|---|---|
| BTC | bc1qftz4ut7vyeulz9e9k6nsuljdjjxszxhms3tmjh |
| ETH / USDC | 0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54 |
| SOL | 3owKW4ppK76np6um86yd45AzNtLLQVyYoD2iDAGSES7p |

### Official ICO (Sep 22, 2026)
| Detail | Value |
|---|---|
| ICO Price | $0.00319 per KX |
| Raise Target | ~$20M (public sale) |
| Fully Diluted Market Cap | ~$26.4M |
| Public Sale Allocation | 6,268,000,000 KX |
| Total Supply | 8,270,000,000 KX |

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
9. If unclaimed in 72 hours -> background sweep auto-reverts to Alice (or Alice can manually Reclaim)

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
- Memo: "Welcome to ChronX"
- Stage 1: 100 KX — immediately (lock_seconds: 0)
- Stage 2: 250 KX — 7 days (lock_seconds: 604800)
- Stage 3: 350 KX — 14 days (lock_seconds: 1209600)
- Stage 4: 500 KX — 21 days (lock_seconds: 1814400)
- Stage 5: 800 KX — 30 days (lock_seconds: 2592000)
- Stage 6: 1,000 KX — 60 days (lock_seconds: 5184000)
- Total: 3,000 KX per recipient

### Cascade Sends Completed (2026-03-04)
| Recipient | Claim Code | Status |
|---|---|---|
| cabfone11@gmail.com | KX-CEQT-9D0T-M14R-ETK3 | Sent + email delivered |
| sadieprincesspea@gmail.com | KX-HDYF-7HR6-LQOY-1H5T | Sent + email delivered |
| kevin@whiteashlab.com | KX-L3T1-941V-EI79-6Z6L | Sent + email delivered |
| yvettedaquiz@gmail.com | KX-IPT8-R7O3-RC9O-WK60 | Sent + email delivered |
| usmanuah9@gmail.com | KX-OM3Y-7ZKN-ZHQG-9HQH | Sent + email delivered |
| careyknightm@icloud.com | KX-N62F-B3W8-Y9MZ-I31C | Sent (2026-03-04) |
| patie39@gmail.com | KX-OF2P-UP09-YB61-X86V | Sent (2026-03-04) |
| michellehumphrey1313@gmail.com | KX-114I-BL08-15LV-9FOU | Failed to confirm on chain (2026-03-04) |
| usmanuah9@gmail.com (2nd) | KX-3AEM-NKHQ-D3DM-TZ0Z | Sent + email delivered (2026-03-05) |
| michellehumphrey1313@gmail.com (resend) | KX-76YV-3JFW-SRTK-MVVA | Sent + email delivered (2026-03-05) |

---

## 6. WALLET STATUS

**Current version:** v2.2.2 (Windows + Android)
**Platform:** Windows x64, Android (Google Play)
**Installer:** https://chronx.io/dl/chronx-wallet-setup.exe
**Google Play:** https://play.google.com/store/apps/details?id=com.chronx.wallet
**Framework:** Tauri v2 + Leptos 0.7 CSR

### APK Signing
- Keystore: `C:\Users\Josep\chronx\chronx-release.keystore`
- Password: `ChronX2026`
- Always sign APK after every Android build: `zipalign -f 4 input.apk aligned.apk && apksigner sign --ks chronx-release.keystore aligned.apk`

### Features (v1.4.33)
- PIN login (4/6/8 digit toggle), Change PIN
- **Tab layout: Mobile Receive|Send|Promises|Settings (3+1). Desktop Receive|Send|Promises|Request|History|Settings (5+1).**
- Receive tab (AccountPanel): balance, Public Key with copy, QR modal, Claim Code, incoming promise summary
- Send tab: Simple Send (KX/Email, Send Now/Send Later) + **Cascade Send (desktop)** with stage builder, Standard Friend Template, live preview
- Promises tab: incoming time-locked payments, auto-refresh, node auto-delivers
- Request tab (desktop): poke/request system, trusted contacts management
- **8-language translations:** EN, FR, DE, ZH, ES, RU, AR, UR with globe picker in Settings
- **History tab: merged transaction history + incoming promises**, type filter (All/Sent/Received/Incoming Promise/Outgoing Promise), colored type badge labels, email addresses shown for email sends
- **RevertToSender (v1.4.27):** Expired email locks show "Expired — Reclaiming" while sweep pending, "Expired — Reverted" after funds returned
- **Reclaim button (v1.4.27):** Manual fallback on any expired email lock — calls `reclaim_expired_lock`
- **Cascade cancel with promise protection (v1.4.27):** "Cancel Series" for fully-unclaimed cascades; "Promised ✓" blocks cancel when any lock is claimed
- **Claim by code only (v1.4.29):** No email registration required — `claim_by_code` uses `getCascadeDetails(BLAKE3(code))` directly. Removed "Set up claim emails in Settings" nudge.
- **Clearer error messages (v1.4.29):** "Code not found" with format hint, "already claimed", "expired — returned to sender" (status-aware detection)
- **Android keyboard fix (v1.4.29):** `windowSoftInputMode: adjustPan` + PIN screen padding (300px) for keyboard overlap
- **Live notices system (v1.4.30):** Fetches notices from api.chronx.io/notices (version-filtered). Urgent notices show as non-dismissible red banner at top. Message notices show in Settings with dismiss button. Reports seen/dismissed counts to server. Auto-generated update notice still works (type="message", dismissible).
- **Balance polling after claim/send (v1.4.31→v1.4.32):** All claim and send handlers poll `get_account_info` for up to 15 seconds until balance OR nonce changes. v1.4.31 used nonce-only detection which missed new-user claims. v1.4.32 uses balance comparison.
- **Auto-refresh balance (v1.4.32):** Silent `setInterval(10000)` refreshes balance every 10 seconds without loading spinner. Uses `web_sys::window().set_interval()` with leaked `Closure` (lives for app lifetime).
- **History shows received transactions (v1.4.32):** `getIncomingTransfers` RPC now returns email/cascade claim receipts for the claimer (not just direct transfers). Node fix: step 3 scans DAG vertices for `TimeLockClaimWithSecret` from this account.
- **Gold primary buttons (v1.4.32):** `button.primary` changed from blue (#1d4ed8) to gold (#d4a84b) to match wallet theme.
- **Claim code display fix (v1.4.32):** Success message uses `\n` + `white-space: pre-line` CSS to show claim code on separate line (no mid-code line break).
- **Form clears after send (v1.4.32):** Email, amount, memo fields reset after successful email send (Email+Send Now path). KX Send and Email+Send Later already cleared fields.
- **Cold-start deep link fix (v1.4.44):** Managed state `PendingDeepLink(Mutex<Option<String>>)` replaces file-based approach. Uses `app.deep_link().get_current()` for cold start + `on_open_url` for warm start.
- **Version checker fix (v1.4.45):** Switched from GitHub API to `chronx.io/version.json`. Numeric segment-by-segment comparison. Platform-aware version field (`version` for Windows, `android_version` for Android). Platform-aware download URL (Google Play on Android, .exe on Windows).
- **Google Play integration (v1.4.45):** Update button links to Play Store on Android. Website wallet.html shows Google Play badge.
- **Trusted contact checkbox fix (v1.4.45):** "Add as Trusted Contact" checkbox hidden when recipient is already trusted (`email_confirm_already_trusted` signal).
- **Node URL in Advanced Settings (v1.4.46):** Collapsed "Advanced Settings" section in Settings tab with edit-locked Node URL input, Edit button, and warning note.
- **Cascade preview layout fix (v1.4.47):** Fixed preview sidebar overflow on 520px window — cascade-layout uses `flex-wrap: wrap` instead of `min-width: 700px`. Preview panel stacks below form on narrow windows.
- **Amount formatting fix (v1.4.47):** Cascade confirm modal and preview panel now use `format_kx_display()` — strips trailing zeros (e.g., "100 KX" instead of "100.000000 KX").
- **Memo privacy hint (v1.4.47):** Both Simple Send and Cascade Send memo fields now show italic grey hint: "Note: memos are stored on the blockchain and are publicly visible."
- **Poke trust gate gold color (v1.4.45):** Trust gate message uses `.msg.warning` class (gold #d4a84b) instead of green.
- **Cascade "Immediately" fix (v1.4.48):** `create_email_timelock_series` now maps `unlock_at_unix <= 0` to `now` (matching single email send behavior). Previously rejected "Immediately" stages with "unlock date must be in the future". Also removed 24-hour minimum lock duration check for series entries.
- **Cascade preview reactivity fix (v1.4.48):** `stage_display_date()` changed from `get_untracked()` to `get()` so preview updates live when user changes unlock mode or date. Previously showed stale "Immediately" for stages changed to "On date...".
- **Cascade decimal amount fix (v1.4.48):** Stage amount input changed from `step="0.01" min="0.01"` to `step="any" min="0.000001"` — accepts any fractional KX amount.
- **Cascade decimal cursor jump fix (v1.4.49):** Changed amount input from `type="number"` to `type="text" inputmode="decimal"`. Number inputs normalize the `.value` property (stripping trailing dots like "1." → "1"), so `prop:value` writing back triggers cursor jump. Text inputs preserve the exact string, preventing cursor reset.
- **Email delivery notification fix (v1.4.49):** Notify API (`/opt/chronx-notify/index.js`) was sending "automatically added to your wallet" email to verified recipients on lock CREATION. But node `sweep_matured_timelocks()` skips ALL email locks (0xC5 marker) — email locks require `TimeLockClaimWithSecret`. Fix: verified recipients now receive the standard claim code email, same as unverified.
- **Verified Delivery (v1.4.50):** Server-side relay wallet (`8Nodc3F2HwUjPMLaFfTJ6WKuSvjEa4fTeopLUK52y5EE`) on Vultr claims email locks and forwards KX to verified recipients automatically. Wallet CLI gained `claim-by-code` subcommand. Notify API `autoDeliverToVerifiedWallet()` orchestrates claim+forward. Verified+immediate recipients get "added to your wallet" email. Unverified recipients still get claim code email.
- **AI Economy section (v1.4.50):** Homepage gains "Built for the AI Economy" section with 3 feature cards (Agent-to-Agent Payments, Programmable Escrow, Zero-Fee Micropayments). All 7 languages translated.
- **Relay all-stages fix (v1.4.51):** CLI `claim-by-code` now outputs total KX claimed; relay parses and forwards full combined amount instead of just first stage.
- **Cascade preview duration fix (v1.4.51):** Preview stage lines now use individual `move ||` reactive closures for amount and date display, fixing "8 days" showing when "8 minutes" selected.
- **Promises Coming To Me (v1.4.56):** Gold section header on Promises tab showing incoming delayed sends. All 8 languages translated.
- **SCHEDULED badge (v1.4.56):** Gold badge on History tab for outgoing delayed sends with future unlock dates. CSS class `.history-type-badge.scheduled` with gold styling.
- **Sender identity fix (v1.4.56):** Wallet now includes sender_email + sender_wallet in /notify payload. Emails show sender identity instead of "Someone".
- **Play Store update button fix (v1.4.52):** `open_url` Tauri command was no-op on Android. Replaced with `tauri-plugin-opener` (works on all platforms). Frontend uses `market://details?id=com.chronx.wallet` on mobile with https fallback.
- Cold storage wallet generator
- Private key export (copy + save to file)
- Cancel button on pending sends (with email-specific modal text, cascade-aware series cancel)
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
- `check_for_updates`, `fetch_notices`, `get_seen_notices`, `mark_notice_seen`, `mark_notice_dismissed`
- `open_url`, `get_app_version`
- `generate_cold_wallet`, `get_cold_wallets`, `save_cold_wallet`
- `reclaim_expired_lock` (v1.4.27) — manual reclaim of expired email locks

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
| getNetworkInfo() | P2P multiaddr + peer_count + node_version + uptime_secs |
| getEmailLockStats() | Aggregate email lock stats (pending/claimed/reverted counts + chronos) |
| sendCascade(hex) | Submit cascade transaction |
| getCascadeDetails(hashHex) | All locks sharing a claim_secret_hash |
| getRecentTransactionsDetailed(limit) | Enriched tx list: type, amounts, recipients, status |
| getVerifierRegistry() | All active verifiers (Genesis 7) |
| getPromiseTriggerStatus(lockId) | Day 91 trigger status for a lock (Genesis 7) |
| getGenesis7Constants() | All Genesis 7 protocol constants as JSON |
| getHumanityStakeBalance() | Humanity Stake Pool balance |
| getPromiseAxioms() | Promise Axioms + AI Trading Axioms text |

**IMPORTANT — These RPC methods do NOT exist on the ChronX node (DAG-based, no blocks):**
- `chronx_getBlockHeight` — use `chronx_getChainStats` (returns `dag_depth`)
- `chronx_getBlock` — no equivalent (ChronX uses a DAG, not a linear blockchain)
- `chronx_getNodeInfo` — not implemented
- `chronx_getNetworkStats` — use `chronx_getNetworkInfo`
- `chronx_getSupplyInfo` — use `chronx_getChainStats` (returns `total_supply_kx`)
- `chronx_getPendingTransactionCount` — not implemented
- `chronx_getTimeLockContracts` — requires account_id param (not zero-param); use `chronx_getGlobalLockStats` for aggregates

---

### Security Hardening (implemented 2026-03-05)

**Engine-level validation (already existed):**
- Memo max 256 bytes (`MAX_MEMO_BYTES`)
- Zero-value transfer rejection (`ZeroAmount`)
- Self-send rejection (`SelfTransfer`)
- Insufficient balance check (`InsufficientBalance`)

**Engine-level validation (v3.5 — new):**
- Memo control character rejection (`MemoInvalidChars`): bytes 0x00-0x1F rejected except 0x09 (tab) and 0x0A (newline)
- Auto-create accounts for `TimeLockClaimWithSecret` (prevents silent claim failure for new users)

**RPC-level rate limiting (v3.5 — new):**
- Per-wallet: 10 tx per wallet per 60 seconds. In-memory `RateBucket` struct in `RpcServerState`. Returns `-32603: "Rate limit exceeded. Try again in X seconds"`.
- `send_cascade` delegates to `send_transaction` → same rate limit applies.

**nginx-level hardening (rpc.chronx.io):**
- IP rate limiting: `limit_req_zone $binary_remote_addr zone=rpc:10m rate=30r/m` in nginx.conf http block
- Burst: `limit_req zone=rpc burst=10 nodelay` + `limit_req_status 429`
- Request size: `client_max_body_size 10k` (legitimate txs are always small)
- Config: `/etc/nginx/sites-available/rpc.chronx.io`

---

## 8. WEBSITE PAGES

| Page | URL | Status |
|---|---|---|
| Home | /index.html | LIVE -- landing, stats bar (no distribution section), faucet modal, Windows + Android downloads |
| Wallet | /wallet.html | LIVE -- download page (Windows + Android). Smart device detection: auto-detects OS, shows banner with direct download, reorders platform cards. |
| Download | /download.html | LIVE -- platform cards |
| Claim | /claim.html | LIVE -- faucet claim + email lock claim (7 languages). v1.4.29: primary Copy button + secondary Open in Wallet App + 5-step how-to-claim |
| Pre-ICO | /preico.html | LIVE |
| Token Sale | /tokensale.html | LIVE |
| Exchange | /exchange.html | LIVE -- wKX on Base via 1inch, email notify, how-it-works cards, pre-ICO callout |
| Explorer | /explorer.html | LIVE -- Recent Transactions table (DAG, no blocks), Growing Scarcity bar, tx ID + address search. Uses getRecentTransactionsDetailed + getGlobalLockStats. |
| Run a Node | /node.html | LIVE -- Windows installer + Linux one-liner install, manual tar.gz downloads, Quick Start, FAQ (6 Q&As) |
| Install Script | /install-node.sh | LIVE -- one-line Linux install: `curl -sSL https://chronx.io/install-node.sh \| sudo bash` |
| Analytics | /analytics.html | LIVE -- 5 KPIs (height, txns, locks, locked, connected nodes) |
| Team | /team.html | LIVE |
| Rewards | /rewards.html | LIVE |
| Support | /support.html | LIVE |
| FAQ | /faq.html | LIVE -- includes cold storage FAQ |
| Disclaimer | /disclaimer.html | LIVE |
| Admin | /admin/index.html | LIVE -- 11 tabs: Faucet, Pre-ICO, Transactions, Downloads, Network, Economy, Calendar, Notices, Alerts, Signups, Export |
| Download Tracker | /dl/track.php | LIVE -- tracks downloads by file + Cloudflare country, redirects to actual file |
| version.json | /version.json | v1.4.52 (Android) / v1.4.51 (Windows) |
| bootstrap.json | /bootstrap.json | Stable bootstrap peer address for node operators |

### Website Deploy
- **Deploy script:** `cd C:\Users\Josep && python deploy_website.py`
- **TRUE web root:** /domains/chronx.io/public_html (NEVER use /public_html — that's stale)
- **Cache:** Hostinger cache OFF as of 2026-03-04 — no purge needed after deploy
- **Cloudflare:** Active on chronx.io — CF-IPCountry header available for download tracking
- **Download tracking:** All /dl/ download links go through /dl/track.php?file=X which increments download-counts.json + download-log.json then redirects to actual file
- **Translations:** js/translations.js — 7 languages (EN, FR, DE, ZH, ES, RU, AR)

---

## 9. KEY TECHNICAL DETAILS

- Consensus: PoW, SHA3-256, 20-bit difficulty
- Cryptography: CRYSTALS-Dilithium2 (post-quantum, NIST FIPS 204)
- Account IDs: BLAKE3(Dilithium2 public key), Base58 encoded
- Networking: libp2p (Ed25519 identity, persistent via --identity-file) | Storage: sled | Structure: DAG
- Minimum lock: 1 second (wallet enforces user-facing minimums)
- Locks >= 1 year: 24-hour cancellation window
- Email locks: 72-hour claim window, auto-revert via background sweep (UnclaimedAction::RevertToSender, active since v3.4)
- **Background sweep (v3.4):** Node runs `sweep_expired_email_locks()` every 5 minutes. Scans all Pending email locks (0xC5 marker) where `now > created_at + claim_window_secs` and `unclaimed_action == RevertToSender`. Credits sender balance, sets status to `Reverted`.
- **ReclaimExpiredLock (v3.4):** Manual fallback transaction. Sender submits to reclaim expired email lock. Validates: sender match, Pending status, expired window, RevertToSender action.
- **TimeLockStatus::Reverted (v3.4):** New terminal status. `reverted_at` timestamp records when funds returned.
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

## 10. KEY BUGS FIXED (2026-03-03 / 2026-03-04 / 2026-03-05)

1. **Claim false success** — `sendTransaction` is fire-and-forget (returns TxId before engine executes). Wallet showed "Claimed!" even when node rejected. Fixed by pre-validating lock maturity via `getTimeLockById` RPC before submitting claim transaction.

2. **Email Send Now 24-hour delay** — Three-layer fix:
   - Frontend: `unlock_at = now + 86400` changed to `unlock_at = 0` (sentinel for Send Now)
   - Backend: Removed 24-hour minimum enforcement, maps `unlock_at <= 0` to server's `now`
   - Engine: Skips `UnlockTimestampInPast` check for email locks (0xC5 marker in extension_data)

3. **Notify API falsy-value bug** — JavaScript `!unlock_at` is true when `unlock_at = 0`. Line 321 of index.js: changed `!unlock_at` to `unlock_at == null`. Email delivery now works for Send Now emails.

4. **Engine multi-action lock ID collision** — All `TimeLockCreate` actions in one transaction used `tx_id` as lock ID, causing later locks to overwrite earlier ones in sled DB. Fixed: action_idx=0 uses tx_id, action_idx>0 uses `BLAKE3(tx_id || idx)`.

5. **Cascade email template bugs (fixed twice):**
   - **v1 fix:** `buildSeriesEmail()` read `e.amount` but cascade payload uses `amount_kx`. Fixed to `e.amount_kx || e.amount`.
   - **v2 fix (2026-03-05):** Two remaining bugs: (a) "Invalid Date" in Unlocks At column — `new Date(e.unlock_at * 1000).toUTCString()` failed when `unlock_at` was 0 or missing. Fixed: shows "Immediately" for timestamps within 1 hour of now, `toLocaleDateString('en-US', ...)` for future dates. (b) Amount normalization — added `getKx()` helper that auto-detects chronos vs KX (if raw > 100000, divide by 1M). Also added `toLocaleString()` for comma formatting.

6. **Balance not updating after claim (v1.4.31)** — All 7 claim/send handlers did one immediate `get_account_info` which returned stale balance (node hadn't confirmed yet). Fixed by adding `poll_balance_update()` which polls every 1s for up to 10s until nonce changes. Same pattern as timelock creation which already worked.

---

## 11. TODO LIST

### Completed in v1.4.26-v1.4.27 + Website Updates
- [x] Disable Android pinch-to-zoom (lock UI scaling) — v1.4.26
- [x] RevertToSender background sweep — v1.4.27/v3.4
- [x] ReclaimExpiredLock manual fallback — v1.4.27/v3.4
- [x] Cascade cancel with promise protection — v1.4.27
- [x] Build + publish node binaries (Linux x64, Linux ARM64, Windows x64) — 2026-03-04
- [x] node.html: real download links + Quick Start + FAQ — 2026-03-04
- [x] exchange.html: rewrite with wKX/Base/1inch flow — 2026-03-04
- [x] analytics.html: Connected Nodes KPI — 2026-03-04
- [x] Whitepaper v3.0 published to GitHub — 2026-03-06 (KX as compute fuel, MISAI AI Arena, full ecosystem)
- [x] Admin Transactions tab (chronx_getRecentTransactionsDetailed RPC + proxy + frontend) — 2026-03-04
- [x] Windows NSIS node installer (ChronX-Node-Setup.exe) — 2026-03-04
- [x] Linux one-line install script (install-node.sh) — 2026-03-04
- [x] node.html rewrite: Windows installer + Linux one-liner + manual downloads in details — 2026-03-04
- [x] Download tracking (dl/track.php with Cloudflare country) — 2026-03-04
- [x] Admin Downloads tab (country map, breakdown, recent log) — 2026-03-04
- [x] Admin Network Health tab (node status, peers, chain activity, sweep) — 2026-03-04
- [x] Admin Economy tab (supply, locked, faucet, reverted, pre-ICO, distribution bar) — 2026-03-04
- [x] Admin Alerts tab (RPC offline, faucet low, stale locks, chain stalled) — 2026-03-04
- [x] All download links routed through tracker (wallet.html, node.html) — 2026-03-04

### Completed in v1.4.47
- [x] Cascade preview panel cut off on right side — flex-wrap layout fix
- [x] Cascade confirm modal trailing zeros — format_kx_display() helper
- [x] Memo privacy warning hint — both Simple Send and Cascade Send
- [x] wallet.html: Desktop Features moved above download cards
- [x] wallet.html: Feature badges (Advanced Features / Core features) on platform cards
- [x] Verified: Node engine cascade "Immediately" (lock_seconds=0) — already working, no code change needed
- [x] Verified: Poke badge polling — working correctly (10s interval + initial fetch after PIN unlock)
- [x] Verified: Version comparison — numeric segment-by-segment, no bug
- [x] Verified: Deep link chronx:// URI registration — NSIS installer already registers correctly

### Next Build (v1.4.48+)
- [ ] QR code button broken on BOTH Windows and Android -- fix
- [ ] "Convert KX<->USDC" Coming Soon page
- [ ] Change PIN if missing

### Active Infrastructure
- [x] Fix stats bar / analytics KPIs -- rpc.chronx.io DNS missing, rerouted to api.chronx.io/rpc
- [ ] Fix support form submission
- [ ] Verify Resend domain (chronx.io) at resend.com/domains
- [x] Android wallet release to Play Store — LIVE on Google Play

### Completed in v1.4.56 (2026-03-07)
- [x] Promises tab — "Promises Coming To Me" section header (gold h4, all 8 languages)
- [x] History tab — gold "SCHEDULED" badge for outgoing delayed sends with future unlock
- [x] Sender identity in notify payload (sender_wallet + sender_email from WalletConfig)
- [x] Re-genesis v5.0 with MISAI Bond, Verifas Bond, MISAI Executor wallets
- [x] Homepage rewrite: new hero + 9-panel comic + "What Makes ChronX Different" + Protocol Promise
- [x] MISAI.io reframe: "The AI That Keeps Promises" (removed arena/leaderboard)
- [x] Pre-ICO invite-only (removed payment addresses, self-service purchase flow)
- [x] Whitepaper v3.3: Foundation section, claim-on-maturity, executor model, strategy immutability
- [x] translations.js: 14 new i18n keys across 7 languages (hero, comic, diff cards, protocol promise)

### Pending (from 2026-03-07 session)
- [ ] HOMEPAGE: Comic embed is inline — consider extracting to separate .js for caching
- [x] WHITEPAPER: v3.4 — created with v5.0 tokenomics + AI Trading Axioms appendix
- [ ] WHITEPAPER: v3.4 — publish to GitHub chronx-docs repo
- [ ] FOUNDATION: Legal structure (nonprofit) — needs lawyer before ICO Sep 22 2026
- [ ] EXECUTOR MODEL: on-chain implementation of executor_eligible status + 90-day flag + fee deduction — Phase 2
- [ ] 7-DAY CANCELLATION WINDOW: Confirm node enforces 7-day (604,800s) irrevocability window for AI Promise locks
- [ ] CASCADE RE-SENDS: 10 recipients need fresh cascade sends after genesis wipe (requires wallet GUI)
- [ ] PLAY STORE: Upload internal (1004056) + production (2004056) AABs — manual task
- [x] GOVERNANCE PAGE: governance.html with AI Trading Axioms, Genesis vs Governance table, Foundation info
- [x] GOVERNANCE NAV: Added to all 17 HTML pages + i18n for all 7 languages
- [x] TOKENOMICS UPDATE: tokensale.html and preico.html updated to 6,093,000,000 KX Public Sale
- [x] 10-PANEL COMIC: Added Panel 10 "Try It Yourself" with faucet CTA
- [ ] BACKUP: misai-wallet.json and verifas-wallet.json — store securely offline
- [ ] FAUCET FUND: Transfer 3M KX from Founder to faucet wallet post-genesis

### Key Decisions (2026-03-07)
- Claim-on-maturity confirmed as canonical model (not auto-push)
- 90-day executor eligibility window (Foundation-governable)
- Open race model for executors (no exclusivity window — prevents griefing)
- 7% genesis-level ceiling, Foundation governs downward only
- Bob sets nothing about executor fees — protocol default, zero UX burden
- "ChronX Protocol Foundation" is the public name for the governance body
- Foundation governs delivery layer only; genesis constants are untouchable
- Promise and delivery mechanism are explicitly decoupled by design
- 7-day cancellation window (not 30) — biblical, astral, proportionate to short promises
- AI Trading Axioms (6 axioms) encoded as immutable genesis metadata
- Re-genesis v5.0: Founder/MISAI/Verifas as genesis-level allocations (not post-genesis transfers)
- Public Sale reduced 6,268M → 6,093M KX to accommodate genesis-level bond allocations
- governance.html added as dedicated page for Foundation + Axioms

### WEBSITE REWRITE (pre-ICO) — NOT URGENT, do after wallet v2.4.x stable + Play Store upload
- [ ] Condense top nav bar — too many items
- [ ] Pre-ICO page: invitation only for accredited investors OR up to $100 of KX via XChan for testing purposes only
- [ ] XChan auto-shutoff: if cumulative volume exceeds $100 (sales + purchases combined), automatically disable the exchange UI and show "Exchange temporarily paused" message. Prevents liquidity pool crash from large orders. Joseph has additional liquidity to add — cap will be raised manually after adding it.

### Future (Phase 2+)
- [ ] IMPORTANT: Node operator incentive/distribution model -- must design before ICO Sep 22 2026
- [ ] Cascade Send web UI for businesses
- [x] wKX ERC-20 on Base + Uniswap v3 pool (DONE 2026-03-11) — 1inch listing pending
- [ ] CMC + CoinGecko listing (apply now — pool is live)
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
11. Default RPC: https://api.chronx.io/rpc (rpc.chronx.io DNS missing — use api.chronx.io/rpc)
12. PIN: shared PinInput, keydown-first, never set_value() in input handler
13. ICO date: September 22, 2026 -- Autumnal Equinox -- never change
14. Founder wallet NEVER left on Vultr -- SCP temporarily, use, DELETE immediately
15. CRITICAL GIT SAFETY RULE: After ANY git rebase or merge on the chronx repo, ALWAYS do ALL of the following before building:
  a) `wc -l crates/chronx-core/src/transaction.rs`  (expect 400+)
  b) `wc -l crates/chronx-state/src/engine.rs`      (expect 1000+)
  c) `git status`  (check for uncommitted changes on Vultr)
  d) SCP transaction.rs from Vultr dirty tree if node has uncommitted changes that differ from git
Never trust git log alone. The running Vultr binary may include uncommitted changes not reflected in git history.
16. RULE #16 — NEVER run `git clean -fd` on the chronx repo. This command permanently deletes untracked files bypassing the Recycle Bin. The Android signing keystore (chronx-release.keystore) is untracked and will be permanently deleted. If repo cleanup is needed, use `git clean -n` first (dry run) to see what would be deleted, then manually delete only safe files.
17. RULE #17 — KEYSTORE BACKUP IS MANDATORY. The Android signing keystore lives at: `C:\Users\Josep\chronx\chronx-release.keystore` (Password: ChronX2026, Alias: chronx). It was recovered from a Windows shadow copy on 2026-03-18 after being deleted by `git clean -fd`. It MUST be backed up in ALL three locations after every wallet session: (1) `C:\Users\Josep\OneDrive\Desktop\ChronX Vital\` (2) Email to josephrsanchez@gmail.com as attachment (3) Mac Mini at `~/chronx-release.keystore`. Without this keystore, Android Play Store updates are impossible — Google will reject a new signing key.
18. RULE #18 — MAC MINI SCP USES minty_sync KEY. All SCP/SSH commands from the Mac Mini to Vultr MUST use `-i ~/.ssh/minty_sync`, NOT `-i ~/.ssh/id_ed25519`. Example: `scp -i ~/.ssh/minty_sync root@45.63.22.189:/home/Josep/chronx/crates/chronx-core/src/transaction.rs ./`
19. RULE #19 — VERSION BUMP MUST UPDATE ALL THREE FILES (discovered 2026-03-20). Every version bump MUST update: (1) `wallet-gui-temp/src-tauri/Cargo.toml` → `version = "X.X.X"` (2) `wallet-gui-temp/src-tauri/tauri.conf.json` → `"version": "X.X.X"` (3) `chronx-website/version.json` → `"version": "X.X.X"`. The Tauri backend reads version from Cargo.toml via `env!("CARGO_PKG_VERSION")`. The NSIS installer reads from tauri.conf.json. The update checker reads from version.json. ALL THREE must match. Checklist: `grep version src-tauri/Cargo.toml && grep version src-tauri/tauri.conf.json && curl -s https://chronx.io/version.json | grep version`

---

## 12B. KXGO.IO — GAMING PLATFORM (built 2026-03-16)

**Domain:** kxgo.io
**Server:** Vultr 45.63.22.189 (same as ChronX node)
**SSL:** certbot, expires 2026-06-14, auto-renews
**Nginx:** /etc/nginx/sites-available/kxgo.io — static from /var/www/kxgo.io/public_html/, API proxied to :4043
**Backend:** /opt/kxgo/index.js (Node.js, Express, port 4043)
**Service:** kxgo-api (systemd)
**Database:** MySQL database "kxgo" — 14 tables (players, badges, leaderboard_snapshots, realm_*, castle_*)

**Platform design (NON-NEGOTIABLE):**
- Flat entry fee per room — wallet size irrelevant to outcome
- Skill 70% + luck 30% — no pay-to-win
- Practice Room (fake KX, free) + Battle Room (real KX, TYPE V conditional)
- House edge: 2.5% to KXGO reserve wallet
- KXGO server wallet = bonded attestor for game outcomes
- Entry fee rooms: Novice 10 KX, Standard 100 KX, Elite 1,000 KX, Champion 10,000 KX

**Games built:**
- **Castle Wars** (castle.html) — PixiJS flagship game, 5,889 lines across 4 files
  - Two castles, 3 unit types (Archer/Knight/Siege Engineer), 8 random events
  - AI opponent in practice mode, full combat system, cooldown management
  - castle.js (2,429 lines), castle.css (1,351), castle.html (393), routes/castle.js (1,716)
- **Battle for the Realm** (realm.html) — SVG hex map strategy game, 1,082 lines JS
  - 25-territory map, 6 mock players, alliances, betrayals, 5 action types
  - Random events (plague/treasure/dragon/storm/rebellion/harvest)
  - Win condition: control 13/25 territories for 6 consecutive hours
  - realm.js (1,082 lines), realm.css, realm.html, routes/realm.js (~850 lines)

**Other pages built:**
- Landing page (index.html) — hero, 2 game cards, how-it-works, rooms comparison, leaderboard preview
- Leaderboard (leaderboard.html) — top 10 by ROE, 3 tabs (All-Time/Month/Week)
- Profile (profile.html) — stats, badges with SVG crowns, game history

**Games removed (do NOT build):**
- KX Markets — too close to regulated prediction markets. Removed entirely, no references.

**KXGO Badge system:**
- Server-side, stored in wallet_badges MySQL table (chronx database on Vultr)
- Three tiers: KXGO_BRONZE (#CD7F32) / KXGO_SILVER (#C0C0C0) / KXGO_GOLD (#D4A84B)
- Displayed in ChronX wallet v2.2.2+ via GET /wallet/badges/:wallet
- Future: may graduate to on-chain TYPE L IdentityVerified

**Deploy procedure:**
```bash
# Static files
scp -r public/* root@45.63.22.189:/var/www/kxgo.io/public_html/
# Backend
scp index.js db.js package.json routes/*.js middleware/*.js root@45.63.22.189:/opt/kxgo/
su - josep -c 'cd /opt/kxgo && npm install --production'
systemctl restart kxgo-api
```

---

## 12C. WALLET v2.2.2 (built 2026-03-16)

**Feature 1 — Verified Identity Checkmark:**
- When displaying wallet addresses in Promises tab, queries `get_verified_identity` command
- If verified: shows gold ✓ + display_name (e.g., "✓ ChronX Founder")
- If unverified: shows truncated address as before (no change to existing behavior)
- `identity_or_short()` helper function with HashMap<String, IdentityRecord> cache
- Cache populated per-panel on data load (not per-render — avoids hammering API)
- Tauri backend: `get_verified_identity(wallet_address)` → fetches from `/avatar/{wallet}/meta`

**Feature 2 — KXGO Badges:**
- KXGO_BRONZE / KXGO_SILVER / KXGO_GOLD badge pills in AccountPanel header
- Displayed alongside existing Founder/Genesis/Patron badges
- Fetched from `GET api.chronx.io/wallet/badges/:wallet` (new endpoint)
- `get_wallet_badges(wallet_address)` Tauri command returns `Vec<WalletBadge>`
- Badge data from wallet_badges MySQL table on Vultr

**Feature 3 — Commitments Section:**
- New section at top of Promises tab (above incoming promises)
- Hidden entirely when no commitments exist (no visual bloat)
- TYPE V conditionals: 🔒 icon, amount, description, countdown timer, Cancel button
  - Cancel sends POST to /wallet/commitment-cancel (attestor notification)
  - Countdown: normal color, amber < 30 min, red < 5 min
- TYPE C credits: 🤝 icon, beneficiary (identity-aware), drawn/ceiling, Revoke button
  - Revoke calls `revoke_credit` command (on-chain immediate)
- TYPE Y deposits: 📋 icon, obligor (identity-aware), amount, maturity date (view only)
- `get_commitments()` Tauri command fetches from RPC: getPendingConditionals, getOpenCredits, getActiveDeposits
- `cancel_commitment(id, type, wallet, reason)` Tauri command

**Build outputs:**
- Windows .exe: `ChronX Wallet_2.2.2_x64-setup.exe` — deployed to chronx.io via deploy_website.py
- Android APK: `ChronX_Android_v2.2.2.apk` — signed, deployed to chronx.io/dl/
- Internal AAB: `chronx-internal-v2.2.2.aab` — signed, on Desktop
- Production AAB: `chronx-production-v2.2.2.aab` — signed, on Desktop
- version.json: updated to 2.2.2, deployed

**New Tauri commands (registered in src-tauri/src/lib.rs):**
- `get_verified_identity` — identity lookup via avatar meta API
- `get_wallet_badges` — KXGO badge list from notify API
- `get_commitments` — TYPE V/C/Y active commitments from node RPC
- `cancel_commitment` — TYPE V cancel request to notify API, TYPE C redirect to revoke_credit

**New frontend types (src/lib.rs):**
- `IdentityRecord { wallet_address, display_name, verified }`
- `WalletBadge { badge_type, color, issued_by }`
- `CommitmentsData { active_locks, active_credits, active_deposits }`
- `ConditionalRecord`, `CreditRecord`, `DepositRecord`

---

## 13. SESSION LOG

### 2026-03-18 — Major Session (Genesis 9 + Wallet v2.3.x)

**COMPLETED TODAY:**
- **Genesis 9: Node v9.0.0** built and deployed on Vultr. Binary-only upgrade from Genesis 8 (no re-genesis). Added TYPE_G wallet groups (5 new Action variants: CreateGroup, AddGroupMember, RemoveGroupMember, DissolveGroup, TransferGroupOwnership), AuthorizedSet for lock claim authorization, succession_group/backup_executors/executor_threshold fields on TimeLockCreate, Humanity Stake pool infrastructure.
- **Node v9.0.1:** peer_count RPC fix (AtomicU64 shared counter between P2P and RPC layers) + gossipsub mesh stability (mesh_n=2, mesh_n_low=1, mesh_n_high=4, mesh_outbound_min=1, idle_connection_timeout=300s).
- **Node auto-update system:** Checks chronx.io/version.json every 24h. Desktop notification via notify-rust with one-click update (Windows PowerShell BitsTransfer).
- **Windows node v9.0.1:** Installed with quoted --bootstrap flag. Registry run key updated. NSIS installer rebuilt and deployed.
- **Mac Mini node:** Docker downloading, ARM64 binary ready.
- **Explorer:** Now correctly shows 2 connected nodes (peer_count was missing from RPC response entirely).
- **Wallet v2.3.3:** Enum tag bug fixed — SCP'd transaction.rs from Vultr dirty working tree (git log alone was insufficient).
- **Wallet v2.3.4:** Contacts in email send, ToS consent, edge-to-edge fix, seed phrase UI wired into Settings.
- **Mnemonic:** 24-word BIP39 seed phrase system live. Settings: View Seed Phrase (PIN gate + reveal), Create New Wallet (emergency flow), Restore from Seed Phrase (auto-detects mnemonic vs legacy key).
- **Email formatting:** formatKx() helper — "50,000 KX" with commas. USD language changed to "at the time of this email".
- **api.verifas.io SSL:** Live, cert expires 2026-06-16.
- **terms.html:** Live at chronx.io/terms, all 8 languages.
- **Pre-ICO notice:** Updated to $0.001755/$0.002297.
- **Whitepaper:** GitHub now has ONLY v5.0 (all old versions removed).
- **ai-brief rules:** #15 git safety, #16 no git clean -fd, #17 keystore backup mandatory.

**ANDROID STATUS:**
- AABs built: chronx-internal-v2.3.4.aab (29.5MB, versionCode 2002004) and chronx-production-v2.3.4.aab (29.5MB, versionCode 3002004) — both on Desktop.
- Upload keystore LOST via `git clean -fd`, RECOVERED via new keystore + Google Play upload key reset request.
- New keystore: `C:\Users\Josep\chronx\chronx-release.keystore` (Password: ChronX2026, Alias: chronx, PKCS12). SHA-256: CE:BE:CE:6D:B0:25:28:39:A4:5F:31:A4:C4:95:98:3F:BE:58:76:56:AE:6A:EE:15:20:07:F9:05:D3:C8:6A:05. Backed up: `OneDrive\Desktop\ChronX Vital\`.
- Upload key reset approved: Mar 20, 2026 at 22:46 UTC. CANNOT upload AABs until after that time.
- Upload cert PEM: `C:\Users\Josep\chronx\upload-cert.pem`.

#### Enum Tag Bug (2026-03-18) — 3 failed builds
Root cause: bad `git rebase --ours` dropped 1,100 lines from transaction.rs, engine.rs, query.rs. Vultr binary was unaffected (pre-compiled) but wallet compiled against broken source. Three builds failed:
- v2.3.1: enum mismatch, tag 40
- v2.3.2: git pull got broken source, tag 141
- v2.3.3: FIXED — SCP'd transaction.rs directly from Vultr dirty working tree. Wallet now matches node exactly.

Action enum (44 variants, tags 0-43):
- 0: Transfer, 1: TimeLockCreate (35 fields including 12 new Genesis 9), 2: TimeLockClaim, 3: TimeLockSell, 4: CancelTimeLock, 5-9: Recovery/Verifier, 10-14: Claims state machine, 15-19: Provider/Schema registry, 20: SubmitOraclePrice, 21: TimeLockClaimWithSecret, 22: ReclaimExpiredLock, 23-26: VerifierRegister/Agent*, 27: ExecutorWithdraw, 28-38: 11 payment type actions, 39-43: 5 Group actions.

Key lesson: ALWAYS SCP transaction.rs from Vultr and compare with local before any wallet build.

**PENDING FROM TODAY:**
- Mac Mini node: install Docker, run one command.
- Smart address book (v2.3.5): email registration check with green/yellow indicators — CC-B has the command ready.
- Play Console upload: after Mar 20 22:46 UTC.
- Uniswap pool rebalance: add ~10,188 wKX to position.
- CoinGecko listing: pending.
- 1inch token list: pending.

**OPEN BUGS CARRIED FORWARD:**
- Cascade Send "Immediately" — believed fixed, not yet confirmed on Android.
- Convert via XChan Base address input: still missing.
- History date format on mobile: not yet confirmed fixed.
- Mnemonic restore: needs testing on fresh wallet.

### 2026-03-16 (KXGO.io Gaming Platform + Wallet v2.2.2)
- **KXGO.io built and deployed:** Full gaming platform at kxgo.io on Vultr. Dark navy/gold theme. Landing page, Castle Wars (PixiJS flagship), Battle for the Realm (SVG hex map), leaderboard, profile pages. Nginx + SSL + systemd service (kxgo-api, port 4043). MySQL database "kxgo" with 14 tables. KX Markets removed entirely — too close to regulated prediction markets.
- **Castle Wars:** 5,889 lines. Two castles face each other. 3 unit types (Archer ranged, Knight melee blocked by moat, Siege Engineer 2x wall damage). 9 action types with cooldowns. 8 random events (dragon, gold mine, earthquake, reinforcements, plague, blessing, meteor, sabotage). AI opponent in practice mode. Gold economy with passive income.
- **Battle for the Realm:** 1,082 lines JS. 25-territory hex map with SVG rendering. 12 player colors. Alliance system with betrayal mechanic. 5 action types (attack 500 KX, defend 200 KX, recruit 300 KX, fortify 100 KX, claim free). Win: control 13/25 territories for 6 consecutive hours. Random events every 12 hours.
- **Wallet v2.2.2 built:** 3 features added to 8,800-line Leptos Rust codebase. (1) Identity checkmarks — gold ✓ + display_name for verified wallets in Promises tab. (2) KXGO badges — Bronze/Silver/Gold pills in AccountPanel alongside Founder badge. (3) Commitments section in Promises tab — TYPE V locks with countdown + Cancel, TYPE C credits with Revoke, TYPE Y deposits view-only. Hidden when empty.
- **chronx-notify updated:** 2 new endpoints live — GET /wallet/badges/:wallet (public, cached 300s) and POST /wallet/commitment-cancel (stores cancellation request). 2 new MySQL tables: wallet_badges, commitment_cancellations.
- **Windows v2.2.2 .exe deployed:** Built, signed, uploaded to chronx.io via deploy_website.py.
- **Android v2.2.2 APK deployed:** Built (aarch64), zipaligned, signed (chronx alias), uploaded to chronx.io/dl/.
- **AABs signed on Desktop:** chronx-internal-v2.2.2.aab and chronx-production-v2.2.2.aab (jarsigner, chronx alias).
- **version.json updated:** Serving v2.2.2 at chronx.io/version.json.
- **Deploy procedure:** deploy_website.py from C:\Users\Josep\chronx\ (FTP to Hostinger 82.29.199.47, user u507945893).

### 2026-03-08 (Genesis 7 — Verified Delivery Protocol Implementation)
- **Node v7.0:** Full Rust implementation of Genesis 7 Verified Delivery Protocol across 13 source files.
- **New constants (13):** VERIFAS_TRIGGER_DAYS=91, ACTIVATION_DEPOSIT_BASIS_POINTS=50, GENESIS_7_SHORT_LOCK_THRESHOLD_SECS=604800, etc. in chronx-core/src/constants.rs.
- **New error variants (4):** GovernanceOnly, VerifierBondTooLow, InvalidVerifierRole, VerifasVaultAlreadyRegistered.
- **New Action:** `VerifierRegister` — governance-only transaction to register verifiers. CLI subcommand `verifier-register` added to chronx-wallet.
- **GenesisParams expanded:** 4 new fields (verifas_vault_pubkey, activation_escrow_pubkey, humanity_stake_pool_pubkey, governance_wallet_b58) with serde defaults.
- **StateDb (db.rs):** 3 new sled trees (promise_packages, promise_triggers, verifier_registry). 4 new structs. 9 new accessor methods.
- **Engine behaviors:** (1) VerifierRegister handler validates governance wallet, bond, role, uniqueness. (2) Short-lock skip in sweep_expired_email_locks (locks <= 7 days revert; > 7 days are irrevocable promises). (3) Promise package generation on TimeLockCreate for locks > 7 days. (4) sweep_genesis7_triggers — Day 91 activation deposit. (5) sweep_genesis7_expiry — 100-year transfer to Humanity Stake Pool.
- **RPC (5 new methods):** getVerifierRegistry, getPromiseTriggerStatus, getGenesis7Constants, getHumanityStakeBalance, getPromiseAxioms.
- **Genesis metadata:** Promise Axioms (4) + AI Trading Axioms (4) stored as separate keys. Genesis 7 constants as auditable JSON. Governance wallet + Humanity Stake Pool addresses.
- **Re-genesis v7.0:** Wiped data, new genesis with corrected keys (public_sale_key matched to local wallet). 3 new zero-balance protocol wallets created. All 6 post-genesis funding transfers. Supply verified: 8,270,000,000 KX exact.
- **Verifier registered:** "ChronX Verifas (Placeholder)", VerifasVault role, 1M KX bond, GLOBAL jurisdiction.
- **Keyfile security:** Public-sale-wallet, founder-wallet, and all 3 new Genesis 7 wallet keyfiles shredded from Vultr after use.
- **governance.html updated:** Two separate axiom sections (Promise Axioms + AI Trading Axioms), expanded Genesis vs Governance table with Genesis 7 rows.

### 2026-03-06 (MISAI Agent Engine — Market Data + AI Trading Loop)
- **Market data poller:** /opt/misai/market.js + /opt/misai/fetch_prices.py. Stocks via yfinance (SPY, AAPL, TSLA, NVDA, MSFT), crypto via CoinGecko (BTC, ETH, SOL, BNB). Polls every 30s. Price history stored in SQLite (auto-purge >24hrs). Cached in memory with stale-value preservation on fetch failure.
- **Agent decision engine:** /opt/misai/engine.js using @anthropic-ai/sdk. Cron every minute. For each due agent: builds portfolio (cash_kx + position values via live prices / KX_USD_RATE), calls Claude Sonnet (claude-sonnet-4-20250514), parses JSON {action, symbol, percent_of_cash, reasoning}, executes BUY (% of cash → position) / SELL (full liquidation) / HOLD, logs decision with kx_before, kx_after, price_usd, market_snapshot.
- **Schema:** agents table has separate `cash_kx` (uninvested) and `current_kx` (total portfolio). positions: agent_id, symbol, quantity, avg_cost_kx. decisions: action, symbol, quantity, price_usd, kx_before, kx_after, reasoning, market_snapshot.
- **Beta mode:** All agents use Claude Sonnet via shared ANTHROPIC_API_KEY in /opt/misai/.env. KX_USD_RATE=0.00055 from .env.
- **Public endpoints:** GET /api/leaderboard (cached 10s, recalculates totals with live prices), GET /api/decisions/recent (cached 5s, last 50 across all agents), GET /api/agent/:id/decisions, GET /api/prices, POST /api/agent/register (invite-gated).
- **Verify-invite fix:** Accepts invite_code alone (no wallet needed). Looks up wallet_address from beta_signups table. Frontend stores wallet in sessionStorage.
- **Live leaderboard:** JS fetches /api/leaderboard, auto-refreshes every 30s. Empty state: "Beta begins soon."
- **Live price ticker:** Horizontal bar below nav showing all 9 asset prices with green/red coloring. Auto-refreshes every 10s.
- **Scrolling trade feed:** Shows recent agent decisions (BUY/SELL/HOLD badges with reasoning). Auto-refreshes every 15s.
- **arena.html:** Agent deployment form. Fields: agent name (max 30), strategy prompt (textarea with 500-char counter), starting KX (min 9), decision interval (5/15/60). Beta note: "Powered by Claude Sonnet — no API key needed."
- **Beta gate UX:** Simplified to invite-code-only input (wallet address removed from Mode A). Successful verification redirects to arena.html.
- **End-to-end verified:** TestBot Alpha registered, engine ran, Claude responded with HOLD decision, appeared in leaderboard and trade feed.

### 2026-03-06 (MISAI Homepage Rebuild — Newbie-Friendly Landing Page)
- **Complete index.html rebuild:** Designed for zero-crypto-knowledge visitors. Clean hero ("The AI that trades for you."), single CTA button, no jargon.
- **Section 1 (Hero):** Large headline, subtitle, one "Request Beta Access" button, small "Powered by KX" note.
- **Section 2 (How It Works):** Three large cards: Choose Your AI (Claude/GPT-4/Gemini/Grok), Power It With KX (1.1 KX per decision, xchan.io pricing), It Trades For You (brokerage account).
- **Section 3 (Control):** Two-column layout. Left: typing animation demo of strategy prompt (loops every ~8s). Right: AI response terminal with green LIVE pulse dot.
- **Section 4 (Brokerage):** Robinhood + Alpaca cards (greyed, "Coming Soon"). "MISAI never touches your money" messaging. Beta note: simulated $1,000.
- **Section 5 (What is KX):** Simple gas-in-a-car analogy. Stats: 1.1 KX per decision, 9 KX free to start. Rate from xchan.io.
- **Section 6 (Beta Gate):** Clean Mode A/B toggle. Mode A: invite code → arena. Mode B: email signup → inline success with chronx.io link.
- **Arena content moved to arena-live.html:** Leaderboard, trade feed, price ticker — only linked from inside arena (not from homepage nav).
- **No leaderboard, no trade feed, no jargon on homepage.** No DAG, BLAKE3, time-locked, post-quantum references.

### 2026-03-06 (MISAI Redesign — KX as Compute Fuel, USD Simulated Trading)
- **Core redesign:** KX is now compute fuel only (1.1 KX per AI decision), NOT a trading currency. Trading portfolios are simulated USD ($1,000 default).
- **Schema migration:** agents table: starting_kx/current_kx/cash_kx → starting_usd/current_usd/cash_usd + kx_balance + kx_per_decision. positions: avg_cost_kx → avg_cost_usd. decisions: kx_before/kx_after → usd_before/usd_after + kx_burned. New table: platform_revenue (0.1 KX per decision to treasury).
- **xchan.js module:** /opt/misai/xchan.js — KX/USD rate management. Fallback $0.00055 (ICO). Live xchan.io API integration prepared for March 11.
- **GET /api/kx-rate:** Returns rate, source, kx_per_decision, platform_margin. "Rate supplied by XChan.io Exchange" shown across all UI.
- **Engine.js rewrite:** All portfolio math in USD. Deducts 1.1 KX fuel per decision. Auto-pauses agents when fuel exhausted. Logs kx_burned and platform_revenue.
- **arena.html:** Live compute fuel calculator widget (updates as user types KX/changes interval). Shows decisions count, runtime, USD equivalent. Info box: "KX powers AI brain, portfolio is $1,000 simulated USD." Coming Soon card: Robinhood | Alpaca.
- **index.html:** Hero: "Real AI. Real Strategy." Subtext: "KX powers the AI. USD tracks the score." Leaderboard: Capital/Portfolio/Return %/KX Fuel columns. Trade feed: USD values + KX burn badge. Beta gate: describes simulated USD + KX fuel model.
- **admin.html:** 5th stat card "KX Earned" (gold) showing total platform_revenue.
- **Removed all references to:** "KX wager", "KX returns", "trading with KX", "real KX".

### 2026-03-06 (MISAI Launch + exchanges.html + usecases.html)
- **misai.io deployed:** AI Wager Arena beta website. Animated particle background, beta gate with Mode A (enter with invite code) / Mode B (request access / join waitlist) toggle, how-it-works steps, demo leaderboard, agent transparency cards, beta details section. Outfit + JetBrains Mono fonts, cyan/violet gradient theme.
- **MISAI Beta API:** Express.js + SQLite on Vultr (/opt/misai/), port 4040, systemd `misai-api`. Endpoints: signup (waitlist), verify-invite, admin CRUD, DELETE /api/admin/signup/:wallet_address (deletes signup + agents, logs to admin_log). Proxied at `https://api.chronx.io/misai/*`. Reuses admin-users.json auth.
- **misai.io admin.html:** Admin dashboard with login, stat cards (total/pending/approved/rejected/KX earned), filter tabs, search, approve (generates MISAI-XXXX-XXXX code in modal), reject, delete (red outlined button with confirmation modal, fade animation), CSV export.
- **exchanges.html created:** ChronX page with XCHAN exchange card + leave-site modal popup before navigating to xchan.io. "More exchanges coming soon."
- **usecases.html created:** ChronX page with MISAI use case card (atom icon, beta badge) + leave-site modal popup before navigating to misai.io. "More use cases coming soon."
- **Nav updated on all 16 pages:** Exchanges now points to `exchanges.html` (was direct xchan.io link). Use Cases now points to `usecases.html` (was `#` placeholder with "Soon" badge). Removed ext-arrow and nav-badge-soon spans.
- **Both sites deployed:** chronx.io (51 files, 0 failures) and misai.io (2 files, 0 failures).

### 2026-03-06 (xchan.io About Fix + chronx.io Nav Update)
- **xchan.io About text fix:** Removed ChronX mention from About section. Now reads: "It operates independently and is not affiliated with any specific cryptocurrency project or token issuer."
- **chronx.io nav update:** Added two new nav links to ALL 14 pages (after "Exchange"):
  1. **Exchanges** → https://xchan.io (external, opens in new tab, ↗ arrow indicator)
  2. **Use Cases** → # placeholder with muted gold "Soon" pill badge
- **i18n:** `nav_exchanges` and `nav_usecases` translation keys added to all 7 languages in translations.js. `data-i18n` placed on inner `<span>` to preserve badge/arrow siblings during `textContent` replacement.
- **CSS:** `.ext-arrow` (small muted arrow) and `.nav-badge-soon` (gold pill) styles added to style.css.
- **Use Cases = AI Arena site** — future build, dedicated session.

### 2026-03-06 (MISAI — Agent Dashboard, Real KX Deduction, Connect Wallet)
- **my-agent.html (NEW):** Personal agent dashboard at `my-agent.html?agent_id={id}&wallet={wallet}`. Sticky status bar (name, portfolio, return %, KX balance, next decision timer, auto-refresh 15s). Demo mode banner with "Connect Wallet" button. Paused banner with "Get KX" and "Resume Agent" buttons. Live decision feed with BUY/SELL/HOLD badges, reasoning, USD before/after. "Warming up" animation when no decisions yet. Trading mode toggle (Simulated active, Real Money coming soon). Connect wallet modal (AES-256 encrypted private key storage).
- **GET /api/agent/:id/status:** Returns full agent status including positions array, next_decision_at, has_private_key, mode. No auth required.
- **PUT /api/agent/:id/connect-wallet:** Encrypts private key with AES-256-GCM (MISAI_ENCRYPTION_KEY from .env), stores in agents table, sets mode='real'. Ownership verified by wallet_address match.
- **POST /api/agent/:id/resume:** Resumes paused agents (sets status='active').
- **GET /api/admin/revenue:** Returns { total_kx } sum of platform_revenue table. Bearer auth required.
- **Schema migration:** `ALTER TABLE agents ADD COLUMN encrypted_private_key TEXT`, `ALTER TABLE agents ADD COLUMN mode TEXT DEFAULT 'simulated'`, `ALTER TABLE decisions ADD COLUMN tx_hash TEXT`.
- **Engine.js real KX deduction:** When agent has encrypted_private_key (real mode): checks on-chain balance via `chronx_getAccountInfo` RPC, transfers 1.1 KX to treasury via chronx-wallet CLI, logs tx_hash, syncs kx_balance from on-chain. When no private key (demo mode): unlimited decisions, kx_burned=0, no platform_revenue. Out-of-fuel email via Resend API.
- **crypto-utils.js (NEW):** AES-256-GCM encrypt/decrypt module for private key storage.
- **arena.html fixes:** Post-deploy redirects to my-agent.html (was index.html#leaderboard). Removed visible code comment ("// 10% platform margin..."). Clear error states on page load.
- **CORS updated:** Added PUT and DELETE to allowed methods.
- **Deploy:** misai.io (5 files, 0 failures). misai-api restarted.

### 2026-03-06 (MISAI — KX Branding + Admin Delete Button)
- **KX branding across misai.io:** All first mentions of "KX" on each page now read "ChronX token (KX)" with a one-line explainer: "KX is the native token of the ChronX protocol (chronx.io) — an independent blockchain." Pages updated: index.html (hero note), arena.html (sub text + fuel widget label + info box), arena-live.html (leaderboard section), admin.html (stat card label). All subsequent mentions remain "KX".
- **Specific replacements:** "Powered by KX" → "Powered by ChronX token (KX)", "KX is the only real currency on MISAI" → "ChronX token (KX) is the compute fuel for MISAI", "KX to deposit" → "ChronX token (KX) to deposit".
- **Admin Delete button:** Every row in the signups table now has a red outlined "Delete" button. Clicking shows a custom confirmation modal ("Delete {email}? This cannot be undone." with "Yes, Delete" / "Cancel" buttons). On confirm: calls `DELETE /api/admin/signup/:wallet_address`, fades out the row, refreshes stats.
- **DELETE endpoint:** `DELETE /api/admin/signup/:wallet_address` added to `/opt/misai/index.js`. Requires Bearer auth. Deletes from beta_signups + any agents owned by that wallet. Logs action="deleted" to admin_log. Service restarted.
- **Deploy:** misai.io (4 files, 0 failures).

### 2026-03-06 (MISAI Expanded Decision Cards + Full Trade Transparency)
- **Engine structured JSON:** AI prompt now requests full structured response: market_data_used (price, 24h change, source), trade_details (platform, order type, fill price, fees, spread, units), risk_assessment (stop loss price, confidence, risk level, key risks), time_context (session type). max_tokens increased to 600.
- **decisions.details column:** Stores full JSON blob per decision. Engine builds detailsObj merging AI response with defaults (platform='Simulated', fees=0, spread=0.15%).
- **GET /api/agent/:id/decisions updated:** Returns all fields including parsed details JSON (id, action, symbol, quantity, price_usd, reasoning, usd_before, usd_after, kx_burned, decided_at, tx_hash, details).
- **my-agent.html expanded decision cards:** Most recent card expanded by default, older cards collapsed (click to toggle). Each card has 6 sections: AI Reasoning (italic quote), Market Data (price, 24h change, source), Trade Details (platform, order type, amount, units, fill price, fees, spread), Risk Assessment (stop loss, portfolio impact, confidence/risk dots color-coded), Timing (decision time, market session), Portfolio Impact (before/after, KX burned).
- **Disclosure banner:** Added below status bar — "Simulated trading — no real money. Fees shown are estimates only. Full disclosures." with link to /disclosures.html.
- **Risk dot indicators:** Green (low), Gold (medium), Red (high) for confidence and risk level.
- **Deploy:** misai.io (9 files, 0 failures). misai-api restarted.

### 2026-03-06 (MISAI Risk Management + Controls)
- **DB schema:** 6 new columns on agents table: `trade_duration_hours` (24-168), `trade_end_at` (DATETIME, set at deploy), `stop_loss_pct` (default 15%), `portfolio_floor_pct` (default 20%), `kx_exit_buffer` (default 5 KX), `max_kx_per_day` (default 0 = unlimited).
- **Engine safety checks (engine.js):** 6 checks run every decision cycle in order: (1) Trade duration expired → EXIT_ALL + status='completed', (2) KX safety buffer → EXIT_ALL + status='paused', (3) Portfolio floor → EXIT_ALL + status='paused', (4) Position stop loss → force sell individual position, (5) Daily KX cap → skip cycle, (6) Market close warning → adds "US markets close in 15 min" to AI prompt at 3:45pm EST for stock positions.
- **forceExitAll() helper:** Sells all positions, updates cash/status, sends email notification via Resend (different subject/body per reason: session_expired, kx_buffer, portfolio_floor, abort).
- **abort_requested handling:** Engine picks up agents with status 'abort_requested' and runs forceExitAll → status='aborted'.
- **New API endpoints:** `POST /api/agent/:id/abort` (sets abort_requested), `POST /api/agent/:id/pause` (sets paused, holds positions), `PUT /api/agent/:id/settings` (updates stop_loss_pct, portfolio_floor_pct, max_kx_per_day, decision_interval_minutes).
- **Register updated:** Accepts trade_duration_hours, stop_loss_pct, portfolio_floor_pct, kx_exit_buffer, max_kx_per_day. Calculates trade_end_at = NOW + duration.
- **VALID_INTERVALS:** Now includes 30 min: [5, 15, 30, 60].
- **arena.html Risk & Controls section:** Trading Session Length (24h/48h/72h/1wk), Decision Interval (5/15/30/60 min), Stop Loss per Position, Portfolio Floor, Daily KX Cap, KX Safety Buffer. Live KX estimate calculator shows recommended deposit based on duration + buffer. Wallet connection warning banner for demo mode.
- **my-agent.html Controls panel:** Session progress bar with time remaining, Pause Agent / Abort & Exit buttons, Resume button when paused. Settings rows with inline Edit buttons (stop loss, portfolio floor, daily KX cap). Abort confirmation modal.
- **Status response:** Now includes trade_duration_hours, trade_end_at, stop_loss_pct, portfolio_floor_pct, kx_exit_buffer, max_kx_per_day.
- **Deploy:** misai.io (9 files, 0 failures). misai-api restarted. All endpoints tested.

### 2026-03-06 (MISAI Strategy Display + AI Clarification Flow)
- **my-agent.html strategy section:** Strategy card between status bar and decision feed. Shows current strategy in quotes. [Edit] button toggles inline textarea editor. [Save Strategy] calls `PUT /api/agent/:id/strategy`, shows confirmation "Strategy updated — takes effect on next decision" (auto-hides after 5s). [Cancel] collapses back to display.
- **PUT /api/agent/:id/strategy:** Updates `agents.strategy_prompt` in DB. Validates min 10 chars. Returns `{success: true}`.
- **strategy_prompt in status response:** `GET /api/agent/:id/status` now includes `strategy_prompt` field.
- **arena.html AI strategy clarification:** Pre-deployment flow: "Have AI Review Strategy" button → calls `POST /api/clarify-strategy` (server-side proxy to Anthropic API, claude-sonnet-4-20250514, max 500 tokens). If `STRATEGY_CLEAR`, shows green checkmark. If questions (max 3), shows chat bubble with AI questions + answer textarea. User answers → second API call with REFINE_SYSTEM prompt → shows refined strategy. "Looks good — Deploy" replaces strategy and deploys. "Edit more" pre-fills textarea with refined strategy.
- **POST /api/clarify-strategy:** Server-side proxy to Anthropic API. Uses `ANTHROPIC_API_KEY` from `.env`. Avoids exposing API key in browser. Accepts `{system, messages}`, returns `{text}`.
- **Deploy:** misai.io (9 files, 0 failures). misai-api restarted. All 3 new endpoints tested and verified.

### 2026-03-06 (MISAI Approval Email + Auth Endpoint + Returning User UX)
- **Approval email via Resend:** POST /api/admin/approve now sends styled HTML email to the approved user containing their invite code (cyan monospace, MISAI dark theme). Uses Resend API with `re_WBPPSNo6_CPxYQnp38anmV7BrFqZf52t2` key. From: `yo@chronx.io`.
- **POST /api/auth/verify-invite endpoint:** Validates invite code against `beta_signups` table (status='approved'). Returns `{valid, wallet_address, email}`. Used by frontend gate and returning user flow.
- **Returning user "Enter Arena" button:** `localStorage.misai_invite_code` persists after first successful verify. Navbar shows cyan outlined "Enter Arena →" button linking to `arena.html?code=X`. Hero CTA changes from "Request Beta Access" to "Enter Arena →" for returning users.
- **Service verified:** misai-api restarted successfully. Both `/api/verify-invite` and `/api/auth/verify-invite` endpoints tested and working. Approval email test confirmed (Joseph re-approved, code MISAI-SWQU-ZAPC).
- **Deploy:** misai.io (9 files, 0 failures).

### 2026-03-06 (Guarantee Language Fix — verifas.io + chronx.io)
- **verifas.io:** Removed ALL "guarantee" language — visible text AND CSS class names/IDs. Nav "Guarantee" → "Auto-Revert". "The 365-Day Guarantee" → "The 365-Day Auto-Revert". "That's the guarantee." → "That's how the protocol works." CSS classes `.guarantee` → `.auto-revert`, `.guarantee-text` → `.auto-revert-text`, `.guarantee-highlight` → `.auto-revert-highlight`, `id="guarantee"` → `id="auto-revert"`, anchor links `#guarantee` → `#auto-revert`. Zero instances of "guarant" remain.
- **chronx.io usecases.html:** Verifas card description updated: removed "guarantee" → "365-day window: if conditions aren't confirmed, funds return to sender automatically by protocol."
- **verifas.io hero disclaimer:** Added two lines of small print below hero buttons: ChronX independence disclaimer + wallet download link (`chronx.io/wallet.html`).
- **Deploy:** verifas.io (4 files, 0 failures) × 2 deploys. chronx.io (51 files, 0 failures).
- **Joseph's current MISAI invite code:** MISAI-SWQU-ZAPC (re-approved during approval email test).
- **api.verifas.io SSL:** Still pending — DNS A record `api.verifas.io → 45.63.22.189` not yet added in Hostinger. `dig api.verifas.io +short @8.8.8.8` returns empty. Once DNS propagates, run: `certbot --nginx -d api.verifas.io --non-interactive --agree-tos -m yo@chronx.io`

### 2026-03-06 (v1.4.54 — Version Code Fix for Google Play)
- **Issue:** v1.4.53 AAB had versionCode 1004053, already consumed by Google Play from a previous upload attempt. Google Play rejects duplicate versionCodes.
- **Fix:** Bumped to v1.4.54 (versionCode 1004054) in tauri.conf.json, Cargo.toml, and tauri.properties. No code changes — same 16KB page size fix as v1.4.53.
- **AAB:** Built all 4 architectures, signed with jarsigner. Saved to `C:\Users\Josep\OneDrive\Desktop\chronx-wallet-v1.4.54.aab`.
- **version.json:** android_version bumped to 1.4.54.

### 2026-03-06 (MISAI Disclosures Page + Hero Update)
- **Hero subheadline updated:** Changed from "Tell it your strategy..." to "Your strategy or someone else's. Any AI engine. Fully automatic, live trading on Alpaca or Robinhood (coming soon). See full disclosures." Disclosure link styled muted (rgba(255,255,255,0.4), underline on hover).
- **disclosures.html created:** Full legal disclosures and risk notice page matching MISAI dark theme. 6 sections: No Trading Advice, No Access to Funds, No Guarantee of Performance, Full Assumption of Risk, Beta Software Notice, KX Compute Fuel. CTA box at bottom with "Return to MISAI" button.
- **Disclosure footer link:** Added to all 6 MISAI pages (index.html, arena.html, admin.html, arena-live.html, my-agent.html, disclosures.html). Pages without existing footers got a minimal centered footer with Disclosures + ChronX links.
- **Arena consent line:** Added "By deploying an agent, you confirm you have read and agreed to our full disclosures and risk notice" text with link above the Deploy Agent button in arena.html.
- **Deploy:** misai.io (9 files, 0 failures).

### 2026-03-06 (MISAI Admin Stats + Delete Bug Fix)
- **Stats endpoint SQL error:** Line 248 of `/opt/misai/index.js` had duplicate `WHERE` clause: `WHERE tx_hash IS NOT NULL WHERE tx_hash IS NOT NULL`. Fixed to single `WHERE`.
- **Delete endpoint FOREIGN KEY error:** `DELETE FROM agents` failed because `decisions`, `positions`, and `platform_revenue` tables have foreign keys referencing `agents(id)`. Fix: delete child rows (platform_revenue, decisions, positions) per agent_id before deleting agents row, then delete beta_signups row.
- **Both verified:** Stats returns correct counts. Delete returns `{success: true}` and cascades through all child tables. Service restarted.

### 2026-03-06 (v1.4.53 — 16KB Page Size + Verifas.io + MISAI Treasury + Bug Fixes)
- **v1.4.53 Android AAB:** Added `.cargo/config.toml` with 16KB page size rustflags (`-C link-arg=-Wl,-z,max-page-size=16384`) for all 4 Android targets. Verified LOAD segments have `Align=0x4000` (16KB). AAB: 26.6 MB at `C:\Users\Josep\OneDrive\Desktop\chronx-wallet-v1.4.53.aab`. Ready for Google Play.
- **Verifas.io website created:** `C:\Users\Josep\verifas-website\index.html` — conditional payment relay landing page. Light/institutional theme (Playfair Display + Inter fonts, deep navy #0B1A3B + gold #C9A84C). Sections: Hero, How It Works (3 steps), Use Cases (4 cards), 365-Day Guarantee, Beta Access Gate (waitlist form → api.verifas.io/api/verifas/waitlist), Footer. Responsive. Favicon tags included.
- **deploy_verifas.py created:** `C:\Users\Josep\deploy_verifas.py` — FTP deploy to Hostinger (Host: 82.29.199.47, User: u507945893.verifas.io, Remote: /domains/verifas.io/public_html). **FTP password still needed from Joseph.**
- **chronx.io Verifas nav link:** Added `<a href="https://verifas.io" ... nav_verifas>Verifas ↗</a>` to all 16 HTML pages with navbar. `nav_verifas:'Verifas'` added to all 7 languages in translations.js.
- **usecases.html Verifas card:** Added second use case card (conditional payment relay, "Private Beta" badge, leave-site modal like MISAI card).
- **Favicons generated (PIL):** MISAI: cyan-to-violet gradient "M" on dark bg. Verifas: gold "V" on navy bg. Both: favicon.ico (16+32), favicon-32x32.png, apple-touch-icon.png (180x180). Link tags added to all 5 MISAI HTML pages + Verifas index.html.
- **SVG favicons (2026-03-24):** All 6 sites now have distinct SVG favicons: chronx.io gold diamond, xchan.io teal X, cpnx.com purple checkmark, misai.io green target, hedgekx.io teal shield, verifas.io blue checkmark. 55 HTML files updated with `<link rel="icon" type="image/svg+xml" href="/favicon.svg">`.
- **Governance notices redesigned (2026-03-24):** All EPP sites (xchan.io, hedgekx.io, misai.io) now show ONE consolidated welcome box instead of multiple yellow warning cards. Gold left border, friendly tone ("Welcome — A Note on Our Current Phase"), bullet list of governance parameters, link to governance page. Same information, completely different UX — warm and informative, not alarming.
- **Verifas approval notice removed (2026-03-24):** False "not yet approved" text deleted. Verifas IS an approved EPP with 10M KX bond at genesis. Swiss nonprofit legal structure pending separately.
- **MISAI admin delete button bug:** Root cause: nginx `/misai/` CORS preflight only allowed `POST, GET, OPTIONS`. DELETE was blocked by browser. Fix: Updated to `GET, POST, PUT, DELETE, OPTIONS`. Reloaded nginx.
- **MISAI treasury wallet:** Generated dedicated wallet `Cfg1rRrxeEoYzm8SPL9F6mXDbBCxHCz29DSuZ9sNQPH9` via chronx-wallet keygen. Address stored as `MISAI_TREASURY_WALLET` in `/opt/misai/.env`. Keyfile backed up to `C:\Users\Josep\.chronx\misai-treasury-wallet.json` (private key NOT stored on server). xchan.js TREASURY_WALLET updated.
- **Engine.js revenue integrity:** platform_revenue table: added `tx_hash TEXT` column. Deleted 10 fake revenue rows (demo mode, no tx_hash). INSERT now includes tx_hash. Admin revenue queries filter `WHERE tx_hash IS NOT NULL`. Engine uses `MISAI_TREASURY_WALLET` from .env for transfers.
- **my-agent.html consent notice:** Connect Wallet modal now shows explicit authorization notice: "By connecting your wallet, you authorize MISAI to deduct 1.1 ChronX token (KX)..." with estimated daily cost. Button changed to "I Authorize KX Deductions — Connect".
- **Verifas.io FTP deployed:** deploy_verifas.py updated with correct remote path `/public_html` (FTP user's root is already public_html, not `/domains/verifas.io/public_html`). 4 files uploaded, 0 failures: index.html, favicon.ico, favicon-32x32.png, apple-touch-icon.png.
- **Verifas API deployed on .189:** SSH to 45.63.22.190 denied, so deployed alongside existing services on 45.63.22.189. Express.js + better-sqlite3 at `/opt/verifas-api/`, port 4041. Systemd service: `verifas-api`. nginx vhost: `/etc/nginx/sites-available/api.verifas.io`. Endpoints: POST `/api/verifas/waitlist` (email validation, SQLite storage, Resend confirmation email + admin notify), GET `/api/verifas/waitlist` (admin, X-Admin-Key: VerifasAdmin2026), GET `/api/verifas/health`. SSL pending — needs DNS A record `api.verifas.io → 45.63.22.189` in Hostinger, then run certbot.
- **MISAI treasury private key exported:** Converted raw byte arrays from misai-treasury-wallet.json to base58 string for offline storage.
- **version.json:** Android bumped to 1.4.53.

### 2026-03-06 (v1.4.52 — Android Play Store Update Button Fix)
- **BUG:** "Update on Google Play" button did nothing on Android. Root cause: `open_url` Tauri command was a no-op on Android (`let _ = url;`). Fix: Added `tauri-plugin-opener` dependency, replaced platform-specific `open_url` implementation with `app.opener().open_url()` (works on all platforms). Added `opener:default` to both desktop and mobile capabilities.
- **Play Store intent:** Frontend now uses `market://details?id=com.chronx.wallet` URI on mobile (with `https://play.google.com/store/apps/details?id=com.chronx.wallet` fallback). Desktop continues using GitHub download URL.
- **Android AAB (v1.4.52):** Built all 4 architectures, signed with jarsigner (SHA256withRSA). 26.6 MB at `C:\Users\Josep\OneDrive\Desktop\chronx-wallet-v1.4.52.aab`. Ready for Google Play upload.
- **version.json:** Android bumped to 1.4.52, Windows stays at 1.4.51.

### 2026-03-06 (xchan.io Launch + v1.4.51 Android Production AAB)
- **xchan.io deployed:** Non-custodial exchange interface website. Single-page site with swap widget (demo), FAQ, about section, token cards (KX, USDC, ETH, wBTC, BBP). Powered by 1inch branding. Dark theme, Barlow font, responsive.
- **xchan.io infrastructure:** FTP host `82.29.199.47`, user `u507945893.xchan.io`, remote path `/public_html`. Deploy script: `C:\Users\Josep\deploy_xchan.py`. Local folder: `C:\Users\Josep\xchan-website\`.
- **Android v1.4.51 AAB:** Already built in previous session — all 4 architectures, 16KB page size, jarsigner signed (SHA256withRSA), 26.3 MB. Saved to `C:\Users\Josep\OneDrive\Desktop\chronx-wallet-1.4.51.aab`. Ready for Google Play Production upload.

### 2026-03-06 (v1.4.51 — Relay All-Stages Fix, Cascade Preview Fix)
- **BUG 1 — Relay only delivered first stage:** `autoDeliverToVerifiedWallet()` forwarded only the amount from the single `/notify` call, but `claim-by-code` CLI claims ALL matured locks. Fix: CLI now outputs `"totalling X KX"` in claim output; relay parses total and forwards the full combined amount. Added `amount_kx` field to CLI's `CascadeLock` struct. Rebuilt CLI on Vultr.
- **BUG 2 — Cascade preview "8 days" for "8 minutes":** Preview stage lines used plain String variables (`amt_display`, `date_display`) computed in outer `move || {}` closure. Leptos DOM diffing didn't replace static text nodes when inner signals changed. Fix: wrapped each display in its own `move ||` reactive closure inside the view, ensuring individual reactivity for amount and date.
- **Version bump:** v1.4.51 Windows + Android. version.json updated (both platforms at 1.4.51). Website deployed.
- **Android AAB (v1.4.51):** Built all 4 architectures (arm64-v8a, armeabi-v7a, x86, x86_64), 16KB page size support. Signed with jarsigner (SHA256withRSA). AAB: 26.3 MB at `C:\Users\Josep\OneDrive\Desktop\chronx-wallet-1.4.51.aab`. Ready for Google Play Production release.

### 2026-03-06 (v1.4.50 — Verified Delivery, AI Economy Section)
- **Verified Delivery:** Created relay wallet on Vultr (`8Nodc3F2HwUjPMLaFfTJ6WKuSvjEa4fTeopLUK52y5EE`), funded with 10 KX. Added `claim-by-code` subcommand to chronx-wallet CLI (uses `TimeLockClaimWithSecret` action + `getCascadeDetails` RPC to find locks by BLAKE3 hash of claim code). Added `autoDeliverToVerifiedWallet()` and `getVerifiedWalletAddress()` to Notify API. When verified recipient receives immediate KX, relay claims lock then transfers to recipient's wallet. Env vars: `RELAY_KEYFILE`, `RELAY_ACCOUNT_ID`, `WALLET_CLI` in `/opt/chronx-notify/.env`.
- **AI Economy homepage section:** Added "Built for the AI Economy" section to index.html with 3 feature cards (Agent-to-Agent Payments, Programmable Escrow, Zero-Fee Micropayments). All 7 languages in translations.js.
- **Version bump:** v1.4.50 Windows only. version.json updated. Website deployed.
- **Verified delivery email fix (v1.4.50 patch):** `buildVerifiedRecipientEmail()` showed literal "null" when `sender_email` was missing. Fix: guard with `displaySender = (senderEmail && senderEmail !== 'null') ? senderEmail : 'Someone'`. Also fixed amount trailing zeros ("1.000000 KX" → "1 KX") via `parseFloat(amount).toString()`. Subject line also formatted. Server-side only, no version bump.

### 2026-03-06 (v1.4.49 — Decimal Cursor Fix, Email Delivery Notification Fix)
- **BUG 1 — Cascade decimal cursor jump:** Root cause was `type="number"` on the amount input. Browsers normalize `.value` of number inputs (stripping trailing dots: "1." → "1"), so when `prop:value` wrote back the normalized value, the cursor jumped. Fix: changed to `type="text" inputmode="decimal"`. Text inputs preserve exact string, so `prop:value` write-back is a no-op and cursor stays in place. `inputmode="decimal"` ensures numeric keyboard on mobile.
- **BUG 2 — Auto-delivered KX not appearing:** Investigation found the root cause is in the notify API, not the node engine. `sweep_matured_timelocks()` correctly skips ALL email locks (0xC5 marker) — email locks by design require `TimeLockClaimWithSecret` (manual claim with code). But the notify API was sending a "It has been automatically added to your ChronX Wallet" email to verified recipients on lock CREATION. This email was wrong — the KX was never actually delivered. Fix: changed the verified+immediate branch in `/opt/chronx-notify/index.js` to send the standard claim code email instead, so recipients can claim properly. Restarted `chronx-notify` service.
- **No node changes needed:** The sweep logic is correct as-is. Email locks must be claimed with codes because the node doesn't know the recipient's wallet address (only has email hash).
- **Version bump:** v1.4.49 Windows only. version.json updated. Website deployed.

### 2026-03-06 (v1.4.48 — Cascade Immediately Fix, Preview Reactivity, Decimal Amounts)
- **BUG 1 — Cascade "Immediately" fix:** Root cause was `create_email_timelock_series` in commands.rs rejecting `unlock_at_unix <= now` and requiring 24hr minimum lock. Fix: skip time validation for entries where `unlock_at_unix <= 0` (sentinel for "Immediately"), and map to `now` when building actions. Engine on Vultr already correctly skips time checks for 0xC5 email locks — no server change needed.
- **BUG 2 — Preview reactivity fix:** `stage_display_date()` used `get_untracked()` for all signal reads, meaning the preview never re-rendered when users changed a stage's unlock mode or date. Changed to `get()` so the preview is fully reactive.
- **BUG 3 — Decimal amount fix:** HTML input `step="0.01"` was too restrictive in Tauri WebView. Changed to `step="any" min="0.000001"` to accept any fractional KX amount. Backend already parses as f64 and converts to Chronos correctly.
- **Version bump:** v1.4.48 Windows only. version.json updated. Website deployed. GitHub release pending.

### 2026-03-06 (v1.4.47 — Cascade UI Fixes, Memo Hint, Website Reorganization)
- **GENESIS 10 AUDIT (2026-03-24):** Complete read-only audit saved to `Desktop/chronx-genesis10-audit.txt`. 22 accounts, 210 timelocks, 8.27B KX confirmed. 70+ action types all have engine handlers. 12 governance-disabled actions. 11 gaps identified for Genesis 11 (CPNX bond unfunded, MISAI executor empty, Verifas eligibility window missing from params, etc.). Awaiting Joseph review before Genesis 11.
- **GENESIS 11 BLOCK 2 (2026-03-24):** Master wallet file generated. KXGC bond wallet: `BqjGDbhzLJJgzpVywRxug4wTa2Qqtwipc1hkcLLJsWzF`. KXGC keyfile shredded from Vultr. Joseph confirmed USB backup.
- **GENESIS 11 IS LIVE (2026-03-24):** Final genesis. genesis_version=11.0, final_genesis=true, genesis_lock=true. 10 accounts, 203 timelocks, 0 DAG vertices (fresh). 8,270,000,000 KX total supply confirmed. Public Sale: 6,093,000,000 KX. Treasury: 1B (100 timelocks). Node Rewards: 1B (100 timelocks). Humanity/Milestone/Reserve in 3 timelocks. 13 axioms encoded. No GenesisReset mechanism exists — final by design. Genesis 10 backup: `/home/josep/genesis10-final-backup.tar.gz`. PUBLIC SALE ADDRESS CHANGED: now `B3NZbGxzkNMXgvR6NqvCJGN2UUuiyBMHxXRYs7xRdXg5` (same key, different derivation via BLAKE3).
- **GENESIS 11 — FULLY POPULATED (2026-03-25):** All wallets funded from Public Sale. 18 transfers executed, all verified. Chain stats after repopulation: 24 accounts, 203 timelocks, 18 DAG vertices, 8,270,000,000 KX total supply confirmed.
  - Founder: `BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT` — 188,000,000 KX
  - KXGC Bond: `BqjGDbhzLJJgzpVywRxug4wTa2Qqtwipc1hkcLLJsWzF` — 300,000,000 KX
  - MISAI Bond: `2EY2u8iLXW6KXM6zH2PYcB98WDBzBU7DK4d2PsLL422v` — 10,000,000 KX
  - Verifas Bond: `CNUuEt3kQNAeQtSP9Y9muyCMujxFWq2AfsTecjHvCYtD` — 10,000,000 KX
  - HedgeKX Bond: `DqbgpLvxhobS5FcW71ca85RSYxKxw7Dx2tuogkrrkQ1i` — 10,000,000 KX
  - XChan Bond: `68Y97pWzwT8r5kEfozAjhZd6b4bhrKVmJUr84NAfz129` — 10,000,000 KX
  - CPNX Bond: `5g4Fcn8A9BigH8vvyNvVvTGksC6PVWTsQnvT8adRGfFp` — 1,000,000 KX
  - Faucet: `455fV35X3viK8je1hWoUrMaxzj8iUsZr3a3hvM8GH31T` — 3,000,000 KX
  - wKX Bridge: `FGSemyJdkCU85D4qQNWFd158J44MANAHTAF5Qx974WRR` — 1,000,884 KX
  - MISAI Executor: `64PXAwjapumXadK4e5Zk7f8zAxhaKwJifSJLHHiRsDKb` — 10,000 KX
  - User wallets restored (8 wallets): Relay 10, Usman 999,600, Cabfone11 14,815, Cabfone1999 8,630, Michelle 110, Atif5898 100, Cabfone1999F 25, Iikrudiat20 25 KX
  - Public Sale remaining: `B3NZbGxzkNMXgvR6NqvCJGN2UUuiyBMHxXRYs7xRdXg5` — 5,558,965,801 KX
  - Keyfile note: Genesis 11 uses BLAKE3(pubkey) address derivation. Correct keyfile: `/home/Josep/.chronx/public-sale-wallet-g11.json`. Old keyfile (`public-sale-wallet.json`) has stale account_id.
  - Badge issuance: Not available — no `issue-badge` CLI command or protocol action type exists yet.
  - GENESIS 11: COMPLETE. FINAL GENESIS. genesis_lock: true. No further genesis possible.
- **TYPE A — AUTHORITY GRANT: LIVE (2026-03-25):** Post-genesis protocol upgrade. No chain reset needed.
  - New action types: `AuthorityGrant(AuthorityGrantAction)`, `AuthorityRevoke(AuthorityRevokeAction)` in transaction.rs
  - New enums: `AuthorityType` (Tier1, Tier2), `AuthorityStatus` (Active, PendingRevocation, Revoked, Expired)
  - Engine handlers in engine.rs: Tier1 requires KXGC wallet (`kxgc_bond_wallet` meta key). Tier2 requires active Tier1 grant with `can_subgrant=true`. Sub-grant limits validated against grantor.
  - Revocation: 30-day notice period (configurable per grant via `revocation_notice_seconds`). Status → PendingRevocation → Revoked.
  - New sled tree: `authority_grants` in db.rs. Keyed by tx_id (grant vertex).
  - New RPC methods: `chronx_getAuthorityGrants(wallet)` — returns all grants for a wallet. `chronx_getKXGCCapacity()` — returns KXGC balance, obligations, reserve ratio, warning level (GREEN/YELLOW/RED).
  - Governance params added to genesis-params.json: `kxgc_min_reserve_ratio: 1.00`, `kxgc_investable_fraction: 0.00` (0% — released by governance when MISAI market develops).
  - Node startup: reads `kxgc_bond_wallet_b58` from genesis-params.json, stores as `kxgc_bond_wallet` in meta. KXGC wallet: `BqjGDbhzLJJgzpVywRxug4wTa2Qqtwipc1hkcLLJsWzF`.
  - Compiled, tested, node restarted clean. Chain data preserved (24 accounts, 18 vertices, 8.27B KX).
- **FOUNDER BADGES RESTORED (2026-03-25):** MySQL wallet_badges table updated for Genesis 11. Founder wallet `BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT`: VERIFIED_BUSINESS (green #22c55e, CPNX) + FOUNDER (gold #C9A84C, ChronX Foundation). Usman: FOUNDING_TEAM. Michelle (DX5Y...): NODE_OPERATOR. Verified via `/wallet/badges/` API.
- **GOVERNANCE PAGE UPDATED (2026-03-25):** Immutable constants: 13 axioms across 4 categories (Promise 3, Credit 2, Trigger 1, AI Agent 5) + Genesis 11 FINAL lock. New governed params: `type_pr_requires_type_a`, `kxgc_min_reserve_ratio` (1.0), `kxgc_investable_fraction` (0.0). KXGC added as 6th EPP in governance-directives.json (300M KX bond, fully reserved, GREEN). chronx-notify restarted. Website deployed.
- **WINDOWS NODE: TYPE A SYNCED (2026-03-25):** Git patch applied from Vultr. TYPE A in Windows codebase. Build successful. Node running on Genesis 11 (genesis state synced, post-genesis vertices syncing via P2P). TYPE A RPC confirmed working.
- **BADGE FIX (2026-03-25):** VERIFIED_BUSINESS badge deleted from Founder wallet. Only FOUNDER badge remains (gold #C9A84C). TYPE L IdentityVerified: NOT FOUND on Genesis 11 — verifier registry empty (CPNX not re-registered). Needs: VerifierRegister + CreateLedgerEntry(IdentityVerified). CLI lacks `identity-verified` entry type — needs CLI update or direct RPC submission.
- **Wallet v1.4.47 — Windows build:** Three fixes:
  1. **Cascade preview layout fix:** `.cascade-layout` had `min-width: 700px` but default window is 520px wide, causing preview sidebar to overflow off-screen. Changed to `flex-wrap: wrap` with `flex: 1 1 300px` / `flex: 1 1 200px` so preview stacks below form on narrow windows.
  2. **Cascade confirm modal amount format:** Changed `{total:.6}` to `format_kx_display(total)` — new helper strips trailing zeros (e.g., "100 KX" not "100.000000 KX"). Also fixed preview panel total amount.
  3. **Memo privacy hint:** Added italic grey hint text below memo fields in both Simple Send and Cascade Send: "Note: memos are stored on the blockchain and are publicly visible."
- **Node engine verified (no change needed):** Cascade "Immediately" stages (lock_seconds=0) already work correctly. The `is_email_lock` check at line 306-310 of engine.rs runs independently for each action in `apply_action()`, and all cascade stages carry the 0xC5 marker in extension_data.
- **Other verifications (no changes needed):** Poke badge polling works (10s interval + initial fetch after PIN unlock). Version comparison is correct (segment-by-segment numeric). Deep link chronx:// URI scheme is registered by NSIS installer (lines 625-629).
- **Website updates:**
  - wallet.html: Moved "Desktop Features" section above download cards so users see feature comparison before choosing platform.
  - wallet.html: Added feature badges — gold "Advanced Features" on Windows card, grey "Core features" on Android card.
  - Google Play badge verified working with correct URL.
  - translations.js: Added `wallet_badge_advanced` and `wallet_badge_core` in all 7 languages.
- **version.json:** Windows v1.4.47, Android v1.4.47. (Superseded by v1.4.51)
- **Android build (v1.4.47):** Built AAB (8.9 MB, signed with jarsigner) + APK (17 MB, zipaligned + apksigner). Superseded by v1.4.51 Production AAB.
- **Auto-delivery sweep verified (no change needed):** All 5 matured-pending locks are email cascade locks (0xC5 marker). `sweep_matured_timelocks()` correctly skips these — email locks require recipient to claim with code. No non-email timelocks are stuck.
- **GitHub release:** v1.4.47 published at https://github.com/Counselco/wallet-gui/releases/tag/v1.4.47 with Windows .exe attached.
- **Website deployed:** 49 files, 0 failures.

### 2026-03-05 (v1.4.44–v1.4.46 — Deep Link Fix, Version Checker, Google Play, Node URL)
- **v1.4.44 — Cold-start deep link fix:** Replaced file-based `pending-deep-link.txt` with managed state `PendingDeepLink(Mutex<Option<String>>)`. Uses `app.deep_link().get_current()` on setup for cold start, `on_open_url` for warm start. Fixes Android cold-start deep links (`chronx://claim?code=...`).
- **v1.4.45 — Android build (Google Play):** Version checker switched from GitHub releases API to `chronx.io/version.json` with numeric segment-by-segment comparison. Platform-aware version/download fields. Google Play badge on wallet.html. Trusted contact checkbox hidden when already trusted. Poke trust gate uses gold color. AAB signed and uploaded to Google Play.
- **v1.4.46 — Windows build:** Bumped version. Node URL visible in collapsed "Advanced Settings" section in Settings tab (edit-locked by default, Edit button, warning note). Windows NSIS installer built and deployed to chronx.io/dl/chronx-wallet-setup.exe.
- **version.json:** Windows v1.4.46, Android v1.4.45. Independent version fields per platform.
- **Vultr cascade fix verified:** engine.rs `is_email_lock` check (0xC5 marker) at line 306-310 correctly skips `UnlockTimestampInPast` for ALL email locks including cascade stages with `unlock_at=0`. No code change needed — already working.
- **Server updates:** Conditional notification emails (skip if no Resend key), faucet rate limiting.

### 2026-03-04 (Node Installer + Admin Dashboard Expansion)
- **Windows NSIS installer built:** ChronX-Node-Setup.exe (2.4 MB). Installs chronx-node.exe to Program Files, creates hidden VBScript launcher (no terminal window), optional Task Scheduler autostart, Start Menu shortcuts, Add/Remove Programs entry. Uninstaller stops node, removes task, preserves .chronx data.
- **Linux one-line install script:** install-node.sh auto-detects x86_64/aarch64, downloads binary, creates systemd service, enables + starts. Usage: `curl -sSL https://chronx.io/install-node.sh | sudo bash`
- **Old node removed from laptop:** Killed chronx-node.exe (PID 6740), removed "ChronX Node.lnk" from Startup folder. start-node.bat still exists at C:\Users\Josep\chronx\start-node.bat for reference.
- **Download tracking system:** dl/track.php with whitelist, flock-safe counters (download-counts.json), country tracking via CF-IPCountry, download log (max 1000 entries), always-redirect design. All download links on wallet.html and node.html now go through tracker.
- **4 new admin API endpoints:** GET /admin/downloads (fetches counters from website), GET /admin/network-health (RPC status, uptime, DAG, sweep), GET /admin/token-economy (supply, locked, faucet, email claims, reverted), GET /admin/alerts (checks 7 conditions). All use existing adminAuth middleware.
- **4 new admin tabs:** Downloads (total counter, country flag cards, breakdown table, recent log), Network (2x2 status cards), Economy (6 KPI cards + distribution bar), Alerts (auto-refreshing alert cards with badge).
- **node.html rewritten:** Windows installer as primary download, Linux one-liner with copy button, manual tar.gz in collapsible details section. Updated Quick Start steps for installer flow.
- **RPC method added:** `chronx_getRecentTransactionsDetailed(limit)` — enriched tx data with type classification (Send/TimeLock/EmailLock/Cascade/Claim/Cancel/ReclaimExpired), amounts, recipients, status. Fixed TimeLockId→TxId type mismatch (4 occurrences, using `&lock_id.0`).
- **Website deployed:** 46 files, 0 failures. All endpoints verified through public API.
- **Pending:** Installer requires manual run on laptop (UAC elevation needed). File at C:\Users\Josep\Downloads\ChronX-Node-Setup.exe.

### 2026-03-04 (Node Binaries + Website Updates + Whitepaper v2.6)
- **Node binaries built on Vultr:** Cross-compiled ChronX node for 3 platforms: Linux x64 (3.4M .tar.gz), Linux ARM64 (3.2M .tar.gz), Windows x64 (3.2M .zip). Each package contains the binary + README.txt with bootstrap command. Published to chronx.io/dl/.
- **node.html rewritten:** Replaced "Coming soon" placeholders with 3 real download cards (Linux x64, Linux ARM64, Windows x64). Added Quick Start section with copy-to-clipboard command block. Added FAQ section with 6 Q&As (uptime, cost, rewards, Raspberry Pi, port forwarding, storage).
- **exchange.html rewritten:** New structure: hero, description (wKX on Base via 1inch), email notify box, 3 "How It Works" cards (Bridge KX→wKX, Trade on 1inch, Withdraw to Wallet), Pre-ICO callout, footer note. Removed old placeholder trade cards.
- **analytics.html: Connected Nodes KPI:** Added 5th KPI card using `chronx_getNetworkInfo` RPC (peer_count + 1 for self). Added `getNetworkInfo()` to rpc.js.
- **translations.js: 30+ new keys** in all 7 languages (EN, FR, DE, ZH, ES, RU, AR) for node FAQ, ARM64 download, quickstart, exchange rewrite, analytics nodes KPI. Updated existing keys for exchange title/subtitle, node download buttons, step text.
- **Whitepaper v2.6 published to GitHub** (chronx-docs repo, commit 777132e). README.md updated.
- **Website deployed:** 43 files, 0 failures. All node binaries, updated HTML/JS live.

### 2026-03-04 (v1.4.27 — RevertToSender + Cascade Cancel + Reclaim)
- **Node v3.4 — RevertToSender live:** Added `TimeLockStatus::Reverted` (terminal status with `reverted_at` timestamp). Added `Action::ReclaimExpiredLock` transaction type for manual reclaim of expired email locks. Added `sweep_expired_email_locks()` to StateEngine — scans all Pending email locks (0xC5 marker) where claim window expired and `unclaimed_action == RevertToSender`, credits sender balance, sets Reverted. Background sweep runs every 5 minutes via tokio::spawn in node main.rs. 4 new error types: NoClaimWindow, ClaimWindowNotExpired, NotRevertToSender, ReclaimNotBySender.
- **RPC enrichment:** `RpcTimeLock` now exposes `claim_window_secs: Option<u64>` and `unclaimed_action: Option<String>`. `tlc_status_str()` handles Reverted.
- **Wallet v1.4.27 — backend:** Added `reclaim_expired_lock` Tauri command. `TxHistoryEntry` now includes `claim_secret_hash` for cascade awareness. Backend detects expired-but-not-swept email locks and returns "Expired — Reclaiming" status.
- **Wallet v1.4.27 — frontend:** Reclaim button on expired email sends (gold, calls `reclaim_expired_lock`). Cascade-aware cancel: builds `cascade_claimed` and `cascade_lock_ids` maps, blocks cancel if any lock claimed ("Promised ✓"), allows "Cancel Series" via `cancel_timelock_series` if none claimed. Cancel modal dynamically switches between single/series cancel. New `.email-badge.reclaiming` CSS class (orange theme).
- **Builds:** Windows NSIS + MSI, Android APK (signed). Both deployed to chronx.io/dl/. GitHub release v1.4.27 with both assets.
- **Node committed and rebuilt on Vultr.** Chain stats preserved (5 accounts, 246 timelocks).

### 2026-03-04 (v1.4.26 — Android Viewport Scaling Fix)
- **Android viewport fix:** Disabled pinch-to-zoom (setSupportZoom=false, builtInZoomControls=false, displayZoomControls=false), locked font scaling (textZoom=100) in MainActivity.kt onWebViewCreate override.
- **Viewport meta tag:** Added `maximum-scale=1.0, user-scalable=no` to index.html viewport meta.
- **Edge-to-edge theming:** Added transparent statusBarColor, navigationBarColor, and shortEdges displayCutoutMode to both themes.xml variants.
- **CSS body lock:** Added `html { width:100%; height:100%; overflow:hidden; touch-action:manipulation; }` and `body { width:100%; height:100%; overflow:hidden; }`. Inner `.app` container set to `height:100%; overflow-y:auto;` for scrollable content.
- **Version bumped to 1.4.26.** Android APK built, signed, deployed to chronx.io/dl/chronx-wallet.apk. version.json updated.

### 2026-03-04 (Whitepaper v2.5 + Node Page + Bootstrap.json)
- **Whitepaper v2.5 published to GitHub:** Governance section, updated tokenomics and pricing. v2.3 removed (v2.4 kept for reference). chronx-docs README updated.
- **bootstrap.json created:** Published at https://chronx.io/bootstrap.json — stable bootstrap peer address `12D3KooWMsFQDZhqAFnkcj1XjPrjjVFwsQ6UqgvffvA6HFt6MfFU` for future node clients to discover bootstrap peer dynamically.
- **node.html created:** "Run a Node" page with bootstrap peer (copy button + dynamic load from bootstrap.json), download placeholders (Windows/Linux), quick setup steps, system requirements. Full 7-language i18n support.
- **Navigation updated:** "Run a Node" link added to all 14 site pages (after Explorer, before Exchange). `nav_node` translation key added to all 7 languages in translations.js.
- **Website deployed:** 40 files, 0 failures. New files: node.html, bootstrap.json.

### 2026-03-04 (v1.4.25 — UX Simplification + Persistent P2P Identity)
- **Wallet UX simplification (v1.4.25):** Reduced from 5 tabs to 4 tabs (Account|History|Rewards|Settings). Promises Made tab merged into History with type filter buttons (All/Sent/Received/Incoming Promise/Outgoing Promise) and colored type badges. Receive tab restructured: Public Key with copy button, QR Code in modal overlay, Claim Code section, incoming promise count link. Email addresses shown in History rows for email sends.
- **Persistent P2P identity:** Added `--identity-file <path>` CLI flag to chronx-node. If file exists, loads Ed25519 keypair from protobuf-encoded bytes. If missing, generates and saves new keypair. Vultr node now has permanent peer ID `12D3KooWMsFQDZhqAFnkcj1XjPrjjVFwsQ6UqgvffvA6HFt6MfFU` stored at `/home/josep/.chronx/p2p-identity.key`. Laptop `start-node.bat` updated with new peer ID and `--identity-file`. No more need to update bootstrap peer ID after Vultr restarts.
- **Windows + Android builds:** Both rebuilt with v1.4.25. NSIS installer + signed APK deployed to chronx.io/dl/.
- **Website deployed:** version.json updated to 1.4.25. All 38 files deployed via FTP, 0 failures.
- **Laptop node peering:** Fixed MSYS path conversion issue (`MSYS_NO_PATHCONV=1`). Created `start-node.bat` with bootstrap peer. Added to Windows Startup folder for auto-start on login.

### 2026-03-05 (Cascade Email Template v2 Fix)
- **Cascade email date formatting:** `buildSeriesEmail()` used `toUTCString()` which showed "Invalid Date" for unlock_at=0. Fixed: "Immediately" for timestamps within 1 hour, `toLocaleDateString('en-US', {month:'long', day:'numeric', year:'numeric'})` for future dates. Also accepts `unlock_at_unix` field name.
- **Cascade email amount normalization:** Added `getKx()` helper — if raw amount > 100,000, auto-divides by 1,000,000 (chronos→KX). All amounts now display with `toLocaleString()` comma formatting. Totals in header and table also formatted.
- **Notify API log fix:** Series notifications logged "undefined KX" because `totalKx` was scoped inside if-block. Hoisted `let totalKx` to outer scope. Log now shows correct total.
- **Test cascade sent:** 2 test emails to cabfone11@gmail.com — 6x1 KX + standard 100/250/350/500/800/1000 KX format. Both display correct dates and amounts.

### 2026-03-04 (Cascade Sends + Bug Fixes)
- **Notify API email fix:** `unlock_at: 0` treated as falsy in JavaScript. Changed `!unlock_at` to `unlock_at == null` on line 321 of /opt/chronx-notify/index.js. Email delivery restored for Send Now.
- **Cascade email template fix (v1):** `buildSeriesEmail()` referenced `e.amount` but cascade payload uses `amount_kx`. Changed to `e.amount_kx || e.amount`.
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
- **Favicon:** Red-halo variant (admin/favicon-admin.ico)
- **Auth:** Multi-user bcrypt + session token (replaced X-Admin-Key in v2, 2026-03-04)
  - **Users file:** /home/josep/admin-users.json (chmod 600, bcrypt hashes)
  - **Sessions file:** /home/josep/admin-sessions.json (24hr TTL, hourly cleanup)
  - **Audit log:** /home/josep/admin-audit.log (JSON lines: login_success, login_failed, login_blocked, logout, password_changed)
  - **Rate limiting:** 5 failed logins in 10 min = 30 min IP block (in-memory Map)
  - **Forced password change:** must_change_password: true on first login
  - **Endpoints:** POST /admin/login, POST /admin/logout, GET /admin/verify, POST /admin/change-password, GET /admin/login-history
  - **Frontend auth:** Bearer token in Authorization header (legacy X-Admin-Key still accepted as fallback)
  - **Login history panel:** Bottom of every tab, last 10 events, IP geolocation via ip-api.com, auto-refresh 60s
  - **Change password:** Modal accessible from header button
  - **Role infrastructure:** ROLE_PERMISSIONS object (owner/staff, both identical for now)
  - **Users:** joseph (owner), usman (staff)
  - **nginx CORS:** Authorization header added to Access-Control-Allow-Headers
- **11 tabs:**
  1. **Faucet:** Pending claims, approve/reject buttons (only show for awaiting_approval), auto-refresh 8s, filter by status
  2. **Pre-ICO:** TX hash required, MySQL storage, admin approve/reject, auto-refresh 8s
  3. **Transactions:** Chain transactions via `chronx_getRecentTransactionsDetailed` RPC, sortable columns, type filter, "Show own wallets" toggle (checked by default), auto-refresh 30s toggle
  4. **Downloads:** Total downloads counter, country map (flag cards), file breakdown table with trend arrows, recent download log, auto-refresh 60s toggle. Data from dl/track.php counters.
  5. **Network:** 2x2 grid: Node Status (online/offline, RPC ms, uptime, version), Peers (count), Chain Activity (DAG tips, last tx relative time), Sweep Status (healthy/delayed/stalled). Auto-refresh 30s on by default.
  6. **Economy:** 6 KPI cards: Circulating Supply, Locked in Timelocks, Pending Email Claims, Faucet Balance (color-coded), Reverted Today, Pre-ICO Progress. Two-section distribution: Protocol Reserves (static genesis info) + Consumer Activity bar (user timelocks / email pending / spendable, excludes genesis locks).
  7. **Calendar:** Reminders/deadlines with list view (grouped by overdue/due soon/upcoming/completed) + monthly calendar grid view. Summary badges (overdue/due soon/upcoming). Add/edit/delete/complete reminders via modal. Priority-colored left borders (critical=red, high=orange, medium=blue). Category badges (website/launch/protocol/infrastructure). Pre-loaded with 6 reminders (price update, ICO prep, node rewards, code signing, wKX bridge, Mac Mini). Data stored in /home/jose/admin-reminders.json.
  8. **Notices:** Push notices to all wallets. Notice cards with LIVE/INACTIVE/EXPIRED + URGENT/MESSAGE badges. Compose/edit modal with type toggle, title (60 char), body (300 char), character counters, expires date, min/max version, live preview. Stats: seen/dismissed counts. Alerts integration: urgent notice active >7 days = ERROR, no active notices = INFO. Data: /home/josep/notices.json.
  9. **Alerts:** Auto-checks: RPC offline (error), faucet low (warning), stale email locks (warning), chain stalled (warning), large transactions (info). Also injects reminder-based alerts and notice-based alerts. Badge on tab with warning count. Always auto-refresh 60s.
  10. **Signups:** Three tables: Exchange notify signups (from POST /exchange-notify), Support tickets (with Resolve/Reopen actions via POST /admin/support/resolve), Rewards registrations (confirmed status). Data from GET /admin/signups.
  11. **Export:** CSV download cards for: Exchange signups, Support tickets, Rewards registrations, Pre-ICO purchases, Faucet claims. Pure client-side CSV generation.

### Node Installer (Windows NSIS) — v2 (2026-03-04)
- **Installer:** ChronX-Node-Setup.exe (2.4 MB, NSIS, LZMA compressed)
- **NSIS script:** /home/josep/chronx-node-installer.nsi on Vultr
- **Installs to:** C:\Program Files\ChronX Node\ (uses $PROGRAMFILES64)
- **Files:** chronx-node.exe, node-config.txt, README.txt, LICENSE.txt (NO VBScript)
- **Autostart:** HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run\ChronXNode registry key (replaces Task Scheduler + VBScript to avoid Defender Behavior:Win32/Persistence.A!ml)
- **Start Menu:** "ChronX Node" and "Uninstall ChronX Node" in Start Menu\Programs\ChronX
- **Uninstaller:** Kills process, removes Run registry key, cleans up old schtasks, removes files, preserves %USERPROFILE%\.chronx\
- **Build:** `makensis /home/josep/chronx-node-installer.nsi` on Vultr (requires `apt install nsis`)
- **Note:** Console window eliminated via `windows_subsystem = "windows"` attribute (added 2026-03-04). No flash on login.
- **Reminder storage:** /home/Josep/admin-reminders.json (6 pre-loaded reminders)

### Linux One-Line Install
- **URL:** https://chronx.io/install-node.sh
- **Usage:** `curl -sSL https://chronx.io/install-node.sh | sudo bash`
- **Auto-detects:** x86_64 or aarch64, downloads correct binary
- **Installs:** /usr/local/bin/chronx-node + systemd service (chronx-node)
- **Service:** Enabled + started automatically, restarts on crash

---

## 15. FAUCET

- **Wallet:** CkBgP1mYQVFrLThM1VTqMLNXjqwW5RP7iKS4x3LouRN3
- **Funded:** 3,000,000 KX from Public Sale
- **Amount per claim:** 9 KX
- **Endpoints:** POST /faucet/register, GET /faucet/check, POST /faucet/claim, GET /faucet/stats
- **Tank graphic:** /faucet/stats returns JSON with level percentage; website renders as animated tank
- **Security:** Server NEVER stores wallet addresses. Token-based flow only.

---

### Session: 2026-03-04 (cont.) — Pricing Fixes, Distribution Redesign, Installer v2
- **Pricing updated everywhere:** $0.00030→$0.00040, $0.00033→$0.00050, removed third tier ($0.00036). Updated: index.html, preico.html, faq.html, exchange.html, notices.json, js/translations.js (all 7 languages), ai-brief.md.
- **KX distribution redesign:** Replaced single bar with two displays: Protocol Reserves (static genesis legend) + Consumer Activity (dynamic bar: user timelocks / email pending / spendable, excludes genesis locks). Added to: index.html (homepage), analytics.html, admin/index.html Economy tab.
- **"Explore Data" right-justified** on homepage (was left-aligned).
- **Exchange notify flow fixed:** exchange.html now POSTs to api.chronx.io/exchange-notify instead of redirecting to support.html. Emails stored in MySQL notify_signups table.
- **Admin Signups + Export tabs:** Signups tab shows exchange notifys, support tickets (with resolve/reopen), rewards registrations. Export tab provides CSV downloads for all data types.
- **Node installer v2:** Replaced VBScript + Task Scheduler with HKCU Run registry key to avoid Defender false positive. Uses $PROGRAMFILES64. No VBScript in install.
- **Genesis locks count fixed:** analytics.html now shows 203 (was 103, missing 100 Node Rewards Harmonic locks).
- **rpc.js:** Added getEmailLocks() and getChainStats() methods.

### Session: 2026-03-04 (cont.) -- Multi-User Admin Auth + RPC Enhancements
- **Multi-user admin authentication system:**
  - Replaced single X-Admin-Key auth with bcrypt + session token auth (Bearer token)
  - Two users: joseph (owner), usman (staff). Credentials in /home/josep/admin-users.json (bcrypt, chmod 600)
  - 5 new API endpoints: POST /admin/login, POST /admin/logout, GET /admin/verify, POST /admin/change-password, GET /admin/login-history
  - Session tokens in /home/josep/admin-sessions.json (24hr TTL, hourly cleanup)
  - Audit logging to /home/josep/admin-audit.log (JSON lines per event)
  - Rate limiting: 5 failed logins in 10 min = 30 min IP block (in-memory)
  - Forced password change on first login (must_change_password: true)
  - Legacy X-Admin-Key still accepted as fallback for backward compat
  - Frontend: Username/password login form, forced password change screen, change password modal, user badge in header, login history panel at bottom of every tab (last 10 events, IP geolocation via ip-api.com, 60s auto-refresh)
  - ROLE_PERMISSIONS object in admin.html JS (owner/staff identical for now)
  - nginx CORS updated: Authorization header added to Access-Control-Allow-Headers
  - bcryptjs npm package installed in /opt/chronx-notify/
  - Red-halo admin favicon (admin/favicon-admin.ico) created with Python+Pillow
- **RPC enhancements (node v3.4 rebuild):**
  - `chronx_getNetworkInfo` now returns: peer_multiaddr, peer_count (live from libp2p swarm), node_version ("3.4"), uptime_secs (from Instant::now() at startup)
  - P2P peer tracking: Arc<AtomicU64> shared between P2pNetwork and RpcServer, incremented on ConnectionEstablished, decremented on ConnectionClosed
  - New RPC: `chronx_getEmailLockStats` -- aggregate stats for all email-based time-locks (pending_count, pending_chronos, pending_kx, claimed_count, reverted_count). Scans locks with 0xC5 extension_data marker.
  - New types: RpcEmailLockStats in chronx-rpc types.rs
  - Admin /admin/network-health endpoint updated: peer_count and uptime_secs now from RPC (was hardcoded 0 and systemd fallback)
- **Website updates:**
  - rpc.js: Added getEmailLockStats() method
  - index.html + analytics.html: Replaced broken getEmailLocks() (required email_hash param) with getEmailLockStats() (zero params, returns aggregate)
  - Node rebuilt and deployed on Vultr, all RPC methods verified
- **Temp credentials (both must be changed on first login):**
  - joseph (owner): ChronX-WgXC-4188
  - usman (staff): ChronX-fuST-7422

### 2026-03-04 (v1.4.28 APK + Calendar Tab + Homepage Cleanup + Cascade Sends)
- **Wallet v1.4.28 Android APK built and signed.** GitHub release v1.4.28 created. APK uploaded to chronx.io/dl/chronx-wallet.apk. version.json already at 1.4.28.
- **Homepage cleanup:** Removed Protocol Reserves legend and Consumer Activity bar from index.html. KPI bar (Total Supply, Circulating, KX Locked, Active Promises, Genesis Date) unchanged. analytics.html retains full distribution display. Cleaned up orphaned JS (GENESIS_LOCKED_CHRONOS, emailStats fetch, consumer bar DOM manipulation).
- **Admin Calendar tab added (tab #7, between Economy and Alerts):**
  - Backend: 4 new API endpoints on Vultr (GET/POST/PATCH/DELETE /admin/reminders). Data stored in /home/Josep/admin-reminders.json. CORS updated for PATCH/DELETE methods.
  - Frontend: List view (grouped by overdue/due soon/upcoming/completed) + monthly calendar grid view. Summary badges. Add/edit/delete modal. Priority borders, category badges, expand/collapse detail text.
  - Alerts integration: loadAlerts() now also fetches reminders; overdue = ERROR alert, within 7 days = INFO alert.
  - Pre-loaded 6 reminders: Price Update (Jun 15), ICO Launch Prep (Sep 15), Node Rewards (Jan 1 2029), Code Signing Cert (Jun 1), wKX Bridge (Apr 1), Mac Mini (Mar 15).
- **Cascade sends (2 recipients, 3,000 KX each, 6,000 KX total):**
  - careyknightm@icloud.com: TX 2eadbe69..., Claim Code KX-N62F-B3W8-Y9MZ-I31C
  - patie39@gmail.com: TX de5be4a8..., Claim Code KX-OF2P-UP09-YB61-X86V
  - Both use standard friend cascade: 100/250/350/500/800/1000 KX at 0/7d/14d/21d/30d/60d
  - Founder wallet SCP'd to Vultr, used, deleted immediately after.
- **Founder balance:** ~99,973,300 KX (was ~99,979,300 before these sends)
- **Website deployed:** 47 files, 0 failures.

### 2026-03-04 (Faucet Tab Actions Fix)
- **Faucet claim flow clarified:** `pending` = user registered email but hasn't entered wallet yet (via claim.html). `awaiting_approval` = user entered wallet, waiting for admin. Approve/Reject buttons now only show for `awaiting_approval`. Pending claims show "Awaiting wallet" label instead.
- **Faucet flow:** POST /faucet/register → status=`pending` → user clicks email link → claim.html → enters wallet → POST /faucet/claim → status=`awaiting_approval` → admin approves → status=`claimed`.

### 2026-03-04 (RPC Route Fix — Analytics KPIs Now Working)
- **Root cause 1:** `rpc.chronx.io` DNS A record missing from Hostinger. Added `/rpc` location block to `api.chronx.io` nginx config proxying to `http://127.0.0.1:8545`. Updated `rpc.js` RPC_URL to `https://api.chronx.io/rpc`.
- **Root cause 2:** Duplicate `Access-Control-Allow-Origin: *` headers — nginx `/rpc` block added `add_header` on proxied responses but ChronX node already sets its own CORS header. Chrome silently blocks duplicate CORS. Fixed by removing the `add_header` from nginx `/rpc` block (keep it only in the OPTIONS block).
- **Cache busting:** Bumped `rpc.js?v=3` → `rpc.js?v=4` on analytics.html, explorer.html, index.html.
- **Result:** All KPI cards on analytics.html and stats bar on index.html now show live data. All 4 RPC methods verified: getGlobalLockStats, getChainStats, getNetworkInfo, getEmailLockStats.
- **TODO:** Add `rpc` A record pointing to `45.63.22.189` in Hostinger DNS when convenient (for backward compat). Not urgent since api.chronx.io/rpc works.

### 2026-03-04 (Admin Transactions Tab Fix)
- **Root cause:** "Show own wallets" checkbox unchecked by default. `KNOWN_WALLETS` includes Founder, Faucet, Public Sale, Node Rewards. Since ALL current transactions originate from Founder wallet, 100% of rows were filtered out → "No transactions found."
- **Fix:** Set `checked` attribute on `#tx-show-own` checkbox so own-wallet transactions are visible by default.
- **CORS note for /rpc:** The `/rpc` nginx location must NOT add `add_header 'Access-Control-Allow-Origin'` on non-OPTIONS responses — the ChronX node already sends this header. Only add CORS headers inside the `if ($request_method = OPTIONS)` block. Same pattern as the `/` location block for the notify API.

### 2026-03-04 (Admin Transactions Date Fix)
- **Root cause:** Transaction Time and Lock Until columns showed "Invalid Date". The rendering code did `new Date(tx.timestamp * 1000).toISOString()` then passed the ISO string to `fmtDate` — double-wrapping that sometimes failed. Also, `fmtDate` only showed date without time.
- **Fix:** Pass raw Unix seconds directly to `fmtDate(tx.timestamp, true)` and `fmtDate(tx.lock_until, !farFuture)`. Updated `fmtDate` to accept optional `showTime` param. Numbers auto-detected as Unix seconds (< 1e12) vs milliseconds (> 1e12). Far-future locks (>1yr away) show date only: "Jan 1, 2029". Recent dates show time: "Mar 4, 2026, 07:50 PM".
- **Duplicate fmtDate fix:** Calendar tab had its own `fmtDate(s)` that shadowed the main one. Renamed to `fmtCalDate(s)` — only used by calendar card rendering and day detail view. Prevents future shadowing bugs.
- **fmtDate signature:** `fmtDate(dt, showTime)` — handles: numbers (Unix sec/ms), ISO strings, MySQL datetime strings, null/undefined. Always UTC. All admin tabs (Faucet, Pre-ICO, Transactions, Downloads, Alerts, Signups) use this single function.

### 2026-03-04 (Remove Email Requirement from Claim)
- **Investigation:** Node engine `TimeLockClaimWithSecret` handler in `chronx-state/src/engine.rs` NEVER checked email — only validates BLAKE3(claim_secret) matches stored hash, lock is Pending, matured, and within claim window. No `chronx_claimEmailLock` RPC exists; claims go through `chronx_sendTransaction` with signed `TimeLockClaimWithSecret` action.
- **Actual blocker:** Wallet GUI `claim_by_code` in `commands.rs` discovered locks via 3 sources: (1) `chronx_getEmailLocks(BLAKE3(email))` — required registered claim email, (2) `getPendingIncoming(wallet)` — only wallet-addressed locks, (3) own timelocks. Email locks sent to external recipients were only discoverable via Source 1, requiring email registration.
- **Fix:** Replaced all 3 sources with single call to `chronx_getCascadeDetails(BLAKE3(code))` which looks up locks by `claim_secret_hash` directly. No email needed. Error message changed from "Make sure your claim email is set in Settings" to "No pending locks found for this code."
- **Privacy benefit:** Email/wallet mappings no longer required for claim. Possession of claim code alone is sufficient.
- **No node changes needed.** Wallet cargo check passes. Requires wallet rebuild (v1.4.29) to deploy.
- **claim_by_code flow (NEW):** `BLAKE3(uppercase(code))` → `chronx_getCascadeDetails(hash)` → filter Pending → maturity check → build `TimeLockClaimWithSecret` actions → `sendTransaction`.

### 2026-03-04 (wallet.html Smart Device Detection)
- **Device detection on wallet.html:** Added `navigator.userAgent` detection for Android, iOS, Mac, and Windows. On page load, shows a prominent gold-bordered banner above the platform cards with device-specific message and download button (for Android/Windows) or "coming soon" message (for iOS/Mac). Detected platform's card is reordered to appear first in the grid via `insertBefore`.
- **Banner content:** Android gets direct APK download button; Windows gets direct .exe download button; iOS/Mac get "coming very soon" with alternative suggestion text.
- **All 7 languages updated** in translations.js: 6 new keys (`detect_android_title`, `detect_ios_title`, `detect_ios_alt`, `detect_mac_title`, `detect_mac_alt`, `detect_win_title`) in EN, FR, DE, ZH, ES, RU, AR.
- **Platform card IDs added:** `card-windows`, `card-android`, `card-mac`, `card-ios` for DOM reordering.
- **CSS:** New `.device-banner` class with gold border, centered layout, large download button.
- **Website deployed:** 47 files, 0 failures.

### 2026-03-05 (Cascade Resend — michellehumphrey1313@gmail.com)
- **Replacement cascade:** Previous send KX-114I-BL08-15LV-9FOU failed to confirm on chain.
- **TX:** a1589e846a64d60676db7280fd6ea7554332ffe48c886a5fd39184cdf1a37ab4
- **Claim Code:** KX-76YV-3JFW-SRTK-MVVA
- **Email delivered:** Resend ID cd96ab41-484e-4527-93e0-5c12c17a065d
- **Founder balance:** ~99,964,300 KX (was ~99,967,300)
- **Founder wallet SCP'd to Vultr, used, deleted immediately.**

### 2026-03-05 (Cascade Send — usmanuah9@gmail.com, 2nd)
- **Cascade sent:** 3,000 KX total (6 stages: 100/250/350/500/800/1000 KX at 0/7d/14d/21d/30d/60d)
- **TX:** fa153e08de150f1b92b9a8a8fbbe7162d4bd6d6c09da85fe1e5e04131238d6c5
- **Claim Code:** KX-3AEM-NKHQ-D3DM-TZ0Z
- **Email delivered:** Resend ID c7901c9b-6089-4b55-8a62-ae70d78afac6
- **Founder balance:** ~99,967,300 KX (was ~99,970,300)
- **Founder wallet SCP'd to Vultr, used, deleted immediately.**

### 2026-03-05 (v1.4.33 — Tab Restructure, Cascade Send, Poke/Request, i18n)
- **Tab restructure:** Mobile 3+1 tabs (Receive|Send|Promises|Settings). Desktop 5+1 (+Request+History). Settings on mobile includes History and Rewards as sub-views.
- **Cascade Send UI (desktop only):** New `CascadeSendPanel` component. Mode toggle in Send tab: Simple Send / Cascade Send. Stage builder table with per-stage unlock options (Immediately, After X time, On date). "Use Standard Friend Template" pre-fills 6 stages (100→1000 KX over 60 days). Live preview sidebar. Confirmation modal. Uses existing `create_email_timelock_series` backend.
- **Poke/Request system:** `RequestPanel` component with email/amount/note form. Trusted contacts CRUD (stored in `~/.chronx/trusted_contacts.json`). Notify API endpoints: POST /poke, GET /poke/pending/:email, POST /poke/decline, POST /poke/paid. Deep link: `chronx://poke/pay?request_id=...`.
- **7-language translations:** EN, FR, DE, ZH, ES, RU, AR. Compile-time JSON via `include_str!()`. Globe picker in Settings. `t(lang, key)` function with English fallback.
- **Node v3.6 auto-delivery sweep:** `sweep_matured_timelocks()` in engine.rs. Runs every 5 min alongside existing email sweep. Auto-credits recipients for matured non-email timelocks. New RPC: `chronx_getMaturedDeliveries`.
- **Build split scaffold:** `mobile` feature flag in Tauri backend Cargo.toml. Runtime `is_desktop()` in WASM frontend.
- **Builds:** Windows NSIS + Android APK (signed). Both deployed. GitHub release v1.4.33. version.json updated.

### 2026-03-05 (v1.4.32 — Auto-refresh, History Fix, Security Hardening)
- **CRITICAL FIX — New user claims:** `engine.rs:apply()` returned `UnknownAccount` for new users trying to claim email/cascade locks (their account never existed on chain). Fix: auto-create account when tx contains `TimeLockClaimWithSecret` and provides valid `sender_public_key` (derives to `tx.from`). Deployed as node v3.5.
- **History shows received:** `get_incoming_transfers` RPC now scans DAG for `TimeLockClaimWithSecret` transactions FROM the queried account (step 3). Previously only found direct transfers and locks where `recipient_account_id` matched, which missed email claim receipts.
- **Balance-based polling:** `poll_balance_update()` now detects balance OR nonce change (was nonce-only). 15s timeout (was 10s).
- **Auto-refresh:** Silent `setInterval(10000)` on app mount refreshes `get_account_info` every 10 seconds without loading spinner.
- **UI fixes:** Gold primary buttons (#d4a84b), claim code on separate line (`white-space: pre-line`), form clears after email send.
- **Security hardening (node v3.5):**
  - Memo character validation: reject control chars (0x00-0x1F) except tab (0x09) and newline (0x0A)
  - Per-wallet rate limiting: 10 tx per wallet per 60 seconds (in-memory RateBucket in RPC server)
  - nginx IP rate limiting: `limit_req_zone $binary_remote_addr zone=rpc:10m rate=30r/m` + `burst=10 nodelay`
  - nginx request size limit: `client_max_body_size 10k` on rpc.chronx.io
  - Already existed: memo 256-byte limit, zero-value rejection, self-send rejection, insufficient balance check
- **Builds:** Windows NSIS + Android APK (signed). Both deployed. GitHub release v1.4.32. version.json updated.
- **Usman's claim confirmed on chain:** Account `7xbB5n2rVfW4bx8goKscNpUWWtac7YGfshv7fW1UDaER` created (auto-create fix worked). Total accounts: 6.

### 2026-03-05 (v1.4.31 — Balance Not Updating After Claim)
- **Root cause:** `sendTransaction` is fire-and-forget — node returns TxId before processing. All 7 claim/send handlers did one immediate `get_account_info` call which returned stale balance (node hadn't confirmed yet). The "Claimed 100 KX!" message appeared but balance stayed at 0.
- **Fix:** Added `poll_balance_update()` helper in `src/lib.rs` — polls `get_account_info` every 1 second for up to 10 seconds, comparing nonce to detect when node has confirmed the transaction. Falls back to a final refresh if nonce doesn't change. Applied to all 7 sites:
  1. Account panel `claim_by_code` (line ~1711)
  2. Promises panel `claim_timelock` (line ~2616)
  3. Promises panel `claim_by_code` (line ~2761)
  4. Promises panel `claim_email_timelock` (line ~2700) — previously had NO balance refresh at all
  5. My Timelocks `claim_timelock` (line ~2897)
  6. History incoming `claim_timelock` (line ~3378)
  7. KX Send Now `send_transfer` (line ~1909) — same single-refresh issue
- **Pattern matches existing code:** Timelock creation (lines 1943-1953) already used nonce-polling. Now all state-changing operations use the same pattern.
- **Build:** Version bumped to 1.4.31. Windows NSIS + Android APK (signed). Both deployed to chronx.io/dl/. version.json updated.
- **Website deployed:** 46 files, 0 failures.

### 2026-03-04 (Block Explorer Fix — "Node unreachable" resolved)
- **Root cause:** explorer.html called `chronx_getBlockHeight` and `chronx_getBlock` — neither exists on ChronX node (DAG-based, no blocks). Caused "Node unreachable" error on every page load.
- **FIX 1 — rpc.js:** `getBlockHeight()` now calls `chronx_getChainStats` and returns `dag_depth`. Removed `getBlock()`, `getRecentBlocks()`, `getTimeLocks()`, `getEmailLocks()` (all broken or unused). Added `getRecentTransactions(n)` calling `chronx_getRecentTransactionsDetailed`. Bumped cache buster to `?v=5` on explorer.html, analytics.html, index.html.
- **FIX 2 — explorer.html:** Replaced "Recent Blocks" table (Height/Hash/Txs/Time) with "Recent Transactions" table (Tx ID/Type/Amount/Status/Time). Color-coded type badges (Send=green, TimeLock=blue, EmailLock=orange, Cascade=purple, Claim=cyan, Cancel=red). Click tx row → detail panel with actions. Search: hex string → tx lookup, else → account lookup (removed block height search). Auto-refresh 20s.
- **FIX 3 — Growing Scarcity:** Replaced broken `Rpc.getTimeLocks()` (requires account_id param) with `Rpc.getGlobalLockStats()` which returns `total_locked_kx` directly. Now shows "2,002.03M" (2B KX locked). Auto-refresh 60s.
- **Translations updated:** All 7 languages (EN, FR, DE, ZH, ES, RU, AR) — new keys: `explorer_col_txid`, `explorer_col_type`, `explorer_col_amount`, `explorer_col_status`. Updated `explorer_recent` from "Recent Blocks" to "Recent Transactions". Updated `explorer_search_ph` to remove "block height".
- **RPC method audit (Vultr):** `chronx_getBlockHeight` = Method not found. `chronx_getBlock` = Method not found. `chronx_getTransaction` = works (needs valid hex). `chronx_getAccount` = works. `chronx_getChainStats` = works. `chronx_getGlobalLockStats` = works. `chronx_getRecentTransactionsDetailed` = works.
- **Website deployed:** 46 files, 0 failures. Explorer verified working.

### 2026-03-04 (v1.4.30 — Live Notices System)
- **Notices API backend (Vultr):** Created /opt/chronx-notify/notices-routes.js (separate Express route module). Public: GET /notices (version-filtered via semver), POST /notices/:id/seen, POST /notices/:id/dismissed. Admin: full CRUD (GET/POST/PATCH/DELETE). Data stored in /home/josep/notices.json. Wired into index.js via require(). Pre-loaded with "Pre-ICO is Live!" message notice.
- **Admin Notices tab (#8, between Calendar and Alerts):** Notice cards with status badges (LIVE/INACTIVE/EXPIRED), type badges (URGENT/MESSAGE), stats (seen/dismissed/expires/version/author). Compose/edit modal: type toggle, title (60 char max), body (300 char max), character counters, expires date, min/max version, live preview panel. Alerts integration: urgent notice active >7 days = ERROR, no active notices = INFO.
- **Wallet notice display (v1.4.30):** Updated Notice struct with `notice_type` (serde rename from JSON "type") and `dismissible` fields. `fetch_notices` now hits api.chronx.io/notices?version=X (was static chronx.io/notices.json). Maps `notice_type` → `severity` for backward compat. Urgent notices: non-dismissible red banner at top (filters severity=="urgent"||"critical" AND dismissible!=true). Message notices: dismissible gold cards in Settings (excludes urgent from count + list). New `mark_notice_dismissed` command reports to server + persists locally.
- **Build:** Version bumped to 1.4.30 (tauri.conf.json, Cargo.toml). Windows NSIS built. Android APK built + signed (zipalign + apksigner). Both deployed to chronx.io/dl/. version.json updated.
- **Cleanup:** Deleted static notices.json from website (api.chronx.io/notices is now source of truth).
- **Website deployed:** 46 files, 0 failures.

### 2026-03-04 (Cascade Send — michellehumphrey1313@gmail.com)
- **Cascade sent:** 3,000 KX total (6 stages: 100/250/350/500/800/1000 KX at 0/7d/14d/21d/30d/60d)
- **TX:** 790400e6a85cbfa51915ab44d1a5ab3afb995403e6a6a4fd9ddccfe2a0f56303
- **Claim Code:** KX-114I-BL08-15LV-9FOU
- **Email delivered:** Resend ID 640ebc87-bc3f-45b0-839a-bac928f61015
- **Founder balance:** ~99,970,300 KX (was ~99,973,300)
- **Founder wallet SCP'd to Vultr, used, deleted immediately.**

### 2026-03-04 (v1.4.29 — Claim by Code Only + UX Fixes)
- **FIX 1+2 — claim.html redesign:** Replaced single "Open in ChronX Wallet" button with primary "Copy Claim Code" gold button + secondary "Open in Wallet App" outline button. Added `#copy-hint` message after copy: "Now open ChronX Wallet → tap Receive → paste your code → tap Claim Now". Updated how-to-claim from 4 to 5 steps matching v1.4.28 wallet UI (Receive tab, "Got a claim code?" box). Fixed `copyCode()` with regex extraction (`KX-XXXX-XXXX-XXXX-XXXX` pattern) to prevent copying garbage after the code. Updated all 7 i18n languages (EN, ES, FR, DE, JA, KO, ZH): added `copyCode`, `copyHint`, `step5` keys; updated `step3`/`step4`.
- **FIX 3 — Claim without email:** `claim_by_code` in commands.rs now uses single `chronx_getCascadeDetails(BLAKE3(code))` call instead of 3 email-based sources. No email registration needed. Removed "Set up claim emails in Settings" nudge from lib.rs.
- **FIX 4 — Clearer error messages:** `claim_by_code` and `claim_email_timelock` in commands.rs now detect lock status: "Code not found" with format hint, "This code has already been claimed", "This code has expired — the KX was automatically returned to the sender". Status-aware via Claimed/Reverted checks on candidate locks.
- **FIX 5 — Android keyboard:** Added `android:windowSoftInputMode="adjustPan"` to AndroidManifest.xml. Added `padding-bottom: 300px; overflow-y: auto;` to `.pin-screen` CSS.
- **FIX 6 — Whitepaper v2.7:** Created `PRIVACY_ADDENDUM_v2.7.md` in chronx-docs repo (markdown since .docx can't be text-edited). Documents claim code privacy: no email-to-wallet mapping stored. Committed + pushed to GitHub.
- **BUILD:** Version bumped to 1.4.29 (tauri.conf.json, Cargo.toml, version.json). Android APK built (4 architectures), signed with chronx-release.keystore, deployed to chronx.io/dl/chronx-wallet.apk.
- **Release notes:** "Claim by code only (no email required), fix claim.html copy button, clearer error messages, Android keyboard fix, whitepaper v2.7 privacy update."

### 2026-03-04 (Node Silent Window + Admin Faucet Fix + Audit)
- **Node silent window:** Added `#![cfg_attr(target_os = "windows", windows_subsystem = "windows")]` to crates/chronx-node/src/main.rs. Cross-compiled for Windows. Rebuilt NSIS installer. New ChronX-Node-Setup.exe deployed to chronx.io/dl/. Windows node binary no longer shows console window.
- **Admin faucet fix:** Approve/Reject buttons only show for `awaiting_approval` status (not `pending` — that means user hasn't entered wallet yet). `pending` shows "Awaiting wallet" label. Added status-specific labels for claimed/rejected/expired. Fixed `fmtDate` to handle null values, MySQL datetime format, and Unix timestamps. "Invalid Date" no longer appears.
- **Wallet.json audit:** Confirmed founder wallet at `C:\Users\Josep\.chronx\wallet.json` matches `BCwHsGLPzSGqjpG7Ptqp3qVRNrqEKdW9Dt4g7NEQpwLT`. On-chain balance confirmed 99,973,300 KX. All B-checks passed (RPC, .exe, wallet UI, analytics labels, Humanity date).

### 2026-03-06 (v1.4.45 — Version Checker Fix + Google Play + Poke Fixes)
- **Version checker fix:** `check_for_updates` now uses `https://chronx.io/version.json` instead of GitHub releases API (which had stale v1.4.35 tag). Numeric version comparison replaces string equality — compares each segment as integers (1.4.45 > 1.4.35). On Android reads `android_version` field; on Windows reads `version` field.
- **Google Play update link:** Android update button now says "Update on Google Play" and opens Play Store URL. Download URL on Android set to `https://play.google.com/store/apps/details?id=com.chronx.wallet`. Windows still uses chronx.io/dl/chronx-wallet-setup.exe.
- **Poke bug fix — Trusted Contact checkbox:** Email send confirmation modal now checks if recipient is already a trusted contact before showing the "Add as Trusted Contact" checkbox. If already trusted, checkbox is hidden. Applies to both Send Now and Send Later paths.
- **Website Android card:** Replaced APK download button with official Google Play badge image linking to Play Store. Removed "Install from unknown sources" note. Updated device-detection banner for Android users. All 7 website languages updated.
- **version.json:** Independent platform versions — `android_version: "1.4.45"`, `version: "1.4.43"` (Windows). `android_download_url` points to Play Store.
- **Builds:** Android AAB (signed with jarsigner, jar verified) + APK (signed with apksigner, v2+v3 verified). Deployed to chronx.io/dl/. Website deployed with Google Play links.

### 2026-03-05 (v1.4.44 — Cold-Start Deep Link Root Cause Fix)
- **Root cause found:** `on_open_url` does NOT fire on Android cold start. The Android launch Intent URL must be retrieved via `app.deep_link().get_current()` in `setup()`. All file-based approaches (v1.4.40–v1.4.43) failed because they depended on `on_open_url` writing files.
- **Fix — Managed state approach:** Replaced all file-based deep link storage with Tauri managed state (`PendingDeepLink(Mutex<Option<String>>)`). In `setup()`, `app.deep_link().get_current()` retrieves the launch Intent URL and stores it in managed state. New `get_launch_deep_link` command reads and clears managed state. Removed `get_pending_deep_link`, `get_pending_poke_link`, `get_deep_link_debug` commands and all file I/O (`pending-deep-link.txt`, `pending-poke-link.txt`, `deep-link-debug.txt`).
- **Frontend routing:** New `route_deep_link_url()` function parses the raw URL and routes to the correct handler: `chronx://claim` → extract code + tab 0, `chronx://pay`/`chronx://decline` → normalize to `chronx://poke/` prefix + `process_poke_link()`. Used in both PinSetup and PinUnlock cold-start paths.
- **Warm-start unchanged:** `on_open_url` still fires for warm-start deep links and emits `deep-link-poke`/`deep-link-claim` events. Also updates managed state as fallback.
- **Independent platform versions:** `version.json` now has `android_version` and `android_release_notes` fields separate from Windows `version`. `wallet.html` updated to show platform-specific version chips.
- **Builds:** Android APK only (signed, v2+v3 verified). Deployed to chronx.io/dl/. version.json updated (Windows stays v1.4.43, Android v1.4.44).

### 2026-03-06 (Server — Conditional Notification Emails + Rate Limiting)
- **Task 1 — Conditional notification emails:** `/notify` endpoint now checks if recipient email has a verified wallet (via `verified_emails` table or `wallet_registry` confirmed=1). Three email variants: (1) **Verified recipient**: "You've got KX!" email with auto-claimed message + "Open Wallet App" button (chronx://receive deep link), no claim code shown. (2) **Future unlock (promise)**: "A KX Promise is waiting for you" email with unlock date, sender email, memo, claim code for later use, and "Download Wallet" button. (3) **Unverified + immediate**: Existing claim code email unchanged. Accepts optional `sender_email` in request body for personalized subjects.
- **Verified emails persistence:** `/verify-email/confirm` now persists successful verifications to `verified_emails` MySQL table (email UNIQUE, wallet_address, verified_at). Upsert on duplicate. New helper `isEmailVerified(email)` checks both `verified_emails` and `wallet_registry` (confirmed=1).
- **Task 2 — Faucet claim rate limiting:** `/faucet/claim` now rate-limits to 10 attempts per IP per hour. Uses in-memory Map (no external deps). Returns 429 "Too many attempts. Please try again later." on exceed. Hourly cleanup interval prevents memory leaks.
- **Database:** New `verified_emails` table: `id, email (UNIQUE), wallet_address, verified_at`. Auto-created on startup.
- **Deploy:** Backed up index.js, uploaded patched version, restarted chronx-notify service. Health check passed.

### 2026-03-05 (v1.4.43 — Deep Link Debug + Email Verify Fix)
- **FIX 1 — Deep link debug logging:** Added `deep-link-debug.txt` file written by `on_open_url` handler showing: raw URL, matched branch, normalized URL, and which files exist after routing. New `get_deep_link_debug` Tauri command reads+consumes this file. Frontend displays debug info as `[DL DEBUG]` message after PIN unlock when a deep link was received. Reverted v1.4.42's aggressive file deletion — `get_pending_poke_link` and `get_pending_deep_link` now only delete their own file (the v1.4.42 change made `get_pending_poke_link` delete the claim file before `get_pending_deep_link` could read it).
- **FIX 2 — Email verification code invalid:** Root cause: `confirm_verify_email` Tauri command read `wallet_id` from keyfile, while `send_verify_email` got it from the frontend. If they differed, the server's `wallet_id !== wallet_id` check silently rejected with generic "Invalid or expired code" error. Fixed: (a) `confirm_verify_email` now accepts optional `walletId` param from frontend (same pattern as `send_verify_email`); (b) frontend passes `info.account_id` to both send and confirm calls; (c) server returns specific error messages ("No verification code found", "Code expired", "Wallet mismatch", "Incorrect code") instead of generic "Invalid or expired code"; (d) server debug logging added (`[VERIFY DEBUG]`) to see exactly which check fails; (e) backend returns `Err(specific_message)` instead of `Ok(false)` so frontend shows the actual error.
- **Builds:** Android APK (signed, v2+v3 verified). Deployed to chronx.io/dl/. Server-side changes deployed to api.chronx.io.

### 2026-03-05 (v1.4.42 — Deep Link Population Fix)
- **PROBLEM A — Claim code not populating:** `AccountPanel` read `deep_link_code` signal with `get_untracked()` at component init. On cold start, the signal is set AFTER `AccountPanel` mounts (async PIN flow sets `app_phase=Wallet` first, then calls `get_pending_deep_link` later). Fix: replaced one-time `get_untracked()` with a reactive `Effect::new` that watches `deep_link_code` and sets `home_claim_code` whenever it changes. Effect consumes the signal by clearing it after copy.
- **PROBLEM B — Stale files persisting:** Both `get_pending_deep_link` and `get_pending_poke_link` backend commands now delete BOTH pending files (claim + poke) immediately after reading, before returning data. This ensures no stale file can fire on the next cold start regardless of which link type was tapped.
- **Warm-start claim listener:** Added `deep-link-claim` event listener in frontend (mirrors existing `deep-link-poke` listener). On warm start, claim deep links now set `deep_link_code` signal and navigate to Receive tab.
- **Builds:** Android APK (signed, v2+v3 verified). Deployed to chronx.io/dl/.

### 2026-03-05 (v1.4.41 — Deep Link Routing Fix)
- **Root cause:** Three bugs caused cross-contamination between deep link types: (1) Backend used independent `if` blocks instead of `if/else if`, allowing a URL to match multiple handlers; (2) Stale `pending-poke-link.txt` from a previous decline would persist and trigger the decline modal on a subsequent claim link cold start; (3) `process_poke_link` pattern matching (`url.contains("poke/pay")`) wouldn't match the simplified `chronx://pay` format.
- **Backend fix (lib.rs):** Rewrote `on_open_url` as strict `if/else if` chain with three routes: `chronx://pay` OR `chronx://poke/pay` → writes normalized `chronx://poke/pay` URL to `pending-poke-link.txt`; `chronx://decline` OR `chronx://poke/decline` → same file with normalized decline URL; `chronx://claim` → writes code to `pending-deep-link.txt`. Each route **deletes the other pending file** to prevent stale data.
- **Frontend fix (process_poke_link):** Updated pattern matching to detect `/pay` or `chronx://pay` (and same for decline) so both URL formats work.
- **Frontend fix (cold-start paths):** Changed both PinSetup and PinUnlock paths from independent `if`/`if` to `if`/`else if` — only ONE deep link type is processed per cold start. Poke links checked first (higher priority), then claim links.
- **Builds:** Android APK (signed, v2+v3 verified). Deployed to chronx.io/dl/.

### 2026-03-05 (v1.4.40 — Pre-Play Store Fixes)
- **Claim code deep link (FIX 1):** Fixed PinUnlock path `active_tab.set(1)` → `active_tab.set(0)`. Claim codes now navigate to Receive tab where the claim code field lives.
- **PAY NOW deep link (FIX 2):** `process_poke_link` now sets `active_tab.set(1)` (Send tab) BEFORE the `get_poke_by_id` network call, so navigation works even if API is slow on cold start.
- **Decline button (FIX 3a):** Notify API poke email Decline button changed from `#333` (gray) to `#dc2626` (red). Restart chronx-notify service.
- **Decline deep link (FIX 3b):** `process_poke_link` decline path now sets `decline_request_id` from URL immediately and opens modal even if `get_poke_by_id` fails. No navigation — stays on current screen with modal overlay.
- **Email verify wallet ID (FIX 4):** `send_verify_email` backend now accepts optional `walletId` param. Frontend passes `info.account_id` from app state. Falls back to keyfile read if not provided.
- **version.json (FIX 5):** Updated to 1.4.40 and verified via curl.
- **Trust gate message color (FIX 6):** Added `.msg.warning` CSS class (gold border/text on dark bg). RequestPanel trust gate message uses "msg warning" instead of "msg success".
- **v1.4.39:** Email send confirmation modal with "Add as Trusted Contact" checkbox (desktop only).
- **Builds:** Windows .exe + Android APK (signed). Both deployed to chronx.io/dl/.

### 2026-03-05 (v1.4.38 — Desktop Fixes)
- **Cascade Send layout (FIX 1):** Restructured to 60/40 two-column layout (min 700px). Left column: form (email, memo, stage builder, + Add Stage, template). Right column: preview card with border/background, Send Cascade button (gold, full width), fee-free line, status messages.
- **Request tab trust gate (FIX 2):** Before calling `send_poke_request`, checks `is_trusted_contact` for recipient email. If not trusted, blocks send with message: "You can only request money from Trusted Contacts. Send them KX first to add them as a contact."
- **Node URL in Advanced (FIX 3):** Moved Node URL to collapsed "Advanced Settings" section at bottom of desktop Settings. Collapsed by default. Shows tooltip "Only change this if you know what you're doing." Input is read-only until Edit button clicked.
- **Poke badge on app load (FIX 4):** Added initial poke count fetch immediately after PIN unlock (both PinSetup and PinUnlock paths), same logic as 10s interval poll. Badge shows on Send tab from first render.
- **Admin dashboard balance fix (FIX 5):** Changed `data.result.balance` to `data.result.balance_kx` (with `balance_chronos` fallback) in admin/index.html.
- **Website:** Added "Desktop Version — Additional Features" section to wallet.html (Cascade Send, Request Money, Full Transaction History, Cold Storage Generator, Export Private Key, AI Agent Auto Payments, Node URL Configuration). All 7 languages translated.
- **Builds:** Windows .exe only. Deployed to chronx.io/dl/.

### 2026-03-05 (v1.4.37 — Deep Link Cold Start Fix)
- **Root cause: Android cold start event timing.** On Android, deep link URLs fire during native `setup()` before WASM frontend loads. Events emitted by `handle.emit()` were lost. Fixed by writing poke deep link URL to `pending-poke-link.txt` file (same pattern as claim codes with `pending-deep-link.txt`).
- **PAY NOW deep link (FIX 1):** File-based `get_pending_poke_link` command reads and consumes the pending URL after PIN unlock. Shared `process_poke_link()` function handles both file-based (cold start) and event-based (warm start) paths. Navigates to Send tab (tab 1) and pre-fills Email + Send Now form.
- **Decline deep link (FIX 2):** Same file-based approach. Opens decline modal (red header, block sender checkbox) instead of navigating. poke.html Decline button changed from `#333` (black) to `#ef4444` (red).
- **Email input width (FIX 3a):** Replaced flex layout with stacked block layout: input `width:100%` on its own line, button `width:100%` below. No flex = no RTL collapse.
- **Email verify wallet_id (FIX 3b):** Added empty check for `wallet_id` in `send_verify_email` — returns clear error instead of sending empty string to API (which caused "Missing required fields" server error).
- **Android deep link path fix:** Both `pending-deep-link.txt` and `pending-poke-link.txt` now use `app.path().app_data_dir()` on Android instead of `HOME`/`USERPROFILE` env vars (which aren't set on Android).
- **Builds:** Android APK (signed). Deployed to chronx.io/dl/.

### 2026-03-05 (v1.4.36 — Pre-Play Store Fixes)
- **Poke PAY NOW pre-populate:** Deep link `chronx://poke/pay?request_id=X` fetches poke details via new `GET /poke/:request_id` API endpoint, navigates to Send tab, switches to Email + Send Now, and pre-fills recipient email, amount, and memo. After successful send, calls `confirm_poke_paid`.
- **Poke Decline red + modal + block:** Decline deep link opens modal with red "Request Declined" header, shows sender email, includes "Block this sender" checkbox. Blocking adds sender to `blocked_senders` in WalletConfig. Blocked senders' pokes are filtered from badge count.
- **Email verification input RTL fix:** Root cause was `body dir="rtl"` for Arabic/Urdu collapsing flex input. Fixed with `dir="ltr"` + `direction:ltr` on both the flex container and input. Input uses `flex:1 1 0%;min-width:50px;width:0` to prevent collapse. Email list rows also get explicit `dir="ltr"` + `direction:ltr` on container.
- **Poke badge on all platforms:** Removed desktop-only guard — poke count now polls on mobile too.
- **New backend commands:** `get_blocked_senders`, `add_blocked_sender`, `is_sender_blocked`, `get_poke_by_id`.
- **Notify API:** Added `GET /poke/:request_id` endpoint returning single poke details.
- **Builds:** Android APK (signed). Deployed to chronx.io/dl/.

### 2026-03-05 (v1.4.35 — Critical Email Send Fix + UI Fixes)
- **CRITICAL FIX — Email send restored:** `create_email_timelock` was broken on both platforms since v3.5 security hardening added a 10KB nginx body limit on rpc.chronx.io. Dilithium2 TimeLockCreate transactions (signature 2420B + public key 1312B + recipient key 1312B) hex-encode to ~10,900 bytes, exceeding the limit. Nginx returned 413 HTML error, which reqwest couldn't parse as JSON → "Bad RPC response: error decoding response body". Fix: increased `client_max_body_size` from 10k to 64k on rpc.chronx.io nginx config.
- **RPC error diagnostics:** `rpc_call()` now reads response as text first, checks HTTP status, and includes status code + body preview in error messages. Timeout increased from 5s to 15s.
- **Email verification input CSS fix:** Input was ~1 character wide on mobile. Added `min-width:0;width:100%;box-sizing:border-box` alongside `flex:1`.
- **Empty email validation:** "Send Verification Code" now shows "Please enter an email address" / "Please enter a valid email address" instead of silently failing.
- **RTL text bleed fix:** Email addresses now render with `dir="ltr"` and `unicode-bidi:embed` to prevent Arabic/Urdu RTL direction from reversing email text.
- **Poke request badge on Send tab:** Red badge showing pending poke count appears on the Send tab button. Polls `get_pending_pokes` every 10 seconds alongside balance refresh.
- **Privacy Policy page:** Created `privacy.html` with full GDPR-style privacy policy. Added "Privacy Policy" footer link to all 14 site pages. Added `footer_privacy` i18n key in all 7 website languages.
- **Builds:** Windows NSIS, Android APK (signed). Both deployed to chronx.io/dl/. GitHub release v1.4.35.

### 2026-03-05 (v1.4.34 — Settings i18n + Email Verification + Urdu + UI Polish)
- **Complete Settings i18n:** ~55 new translation keys across all 8 languages (EN, FR, DE, ZH, ES, RU, AR, UR). All hardcoded Settings panel strings now use `t()`.
- **Email verification security fix:** New API endpoints `POST /verify-email` and `POST /verify-email/confirm` on Vultr (in-memory, 6-char code, 10-min expiry, rate limited 3/hour). Three new Tauri commands: `send_verify_email`, `confirm_verify_email`, `get_verified_emails`. `WalletConfig` gains `verified_emails` field. UI: "+ Add Email" triggers verification code send; 6-char code input; verified emails show green checkmark; unverified show amber warning with "Send Verification Code" link.
- **Urdu (8th language):** Full ur.json with 115 keys. RTL support (same as Arabic). Added to language picker with Pakistani flag.
- **Desktop-only gating:** Node URL and Cold Storage sections hidden on mobile via runtime `if desktop {}` check.
- **View Promises fix:** Navigation link now goes to Promises tab (was Send tab). Text uses translated `view_promises` key. `lang` param added to AccountPanel.
- **QR code modal:** Converted from inline toggle to fixed centered overlay with close button.
- **Cascade Send layout:** 60/40 two-column split (flex: 3/2) with sticky preview sidebar.
- **Promises empty state:** Centered package icon with translated title/subtitle.
- **Builds:** Windows NSIS + MSI, Android APK (signed). Both deployed to chronx.io/dl/. GitHub release v1.4.34.

### 2026-03-06 (ICO Pricing Update — $0.00319/KX, $20M Raise Target)
- **ICO price corrected:** $0.00055 → $0.00319 per KX. Raise target: $20M from 6,268,000,000 KX public sale. Fully diluted market cap: ~$26.4M.
- **Pre-ICO Early (live now):** $0.00040 → $0.001755 (45% off ICO). Pre-ICO Standard (Jun 22): $0.00050 → $0.002297 (28% off ICO).
- **chronx.io updated:** All price references across index.html, preico.html, faq.html, tokensale.html, exchange.html, disclaimer.html, js/translations.js (all 7 languages). ICO tiers replaced with single ICO price model.
- **xchan.io updated:** KX/USDC rate display → 0.00319. Rate constant in JavaScript.
- **misai.io updated:** KX per decision 1.1 → 0.4 (~$0.00128). All calculators, info boxes, homepage. Server: xchan.js KX_USD_RATE_FALLBACK → 0.00319, KX_PER_DECISION_WITH_MARGIN → 0.4, PLATFORM_MARGIN → 0.12 (12%).
- **Whitepaper v3.1:** Created from v3.0. Updated: compute fuel table (flat 0.4 KX), pricing table (Pre-ICO Early/Standard/ICO), KX/USD rate, Pre-ICO Pricing section content, roadmap ICO target, MISAI margin note, expanded legal disclaimer. Committed to chronx-docs.
- **All three sites deployed:** chronx.io (51 files), misai.io (9 files), xchan.io (1 file). All 0 failures. misai-api restarted.

### 2026-03-06 (v1.4.55 Dual AAB Build — Internal + Production)
- **Version bump:** 1.4.54 → 1.4.55 in tauri.conf.json, src-tauri/Cargo.toml.
- **Internal AAB:** `chronx-wallet-v1.4.55-internal.aab` — versionCode 1004055 (auto-generated from Tauri version "1.4.55"). For Play Console Internal Testing track.
- **Production AAB:** `chronx-wallet-v1.4.55-production.aab` — versionCode 2004055 (hardcoded in build.gradle.kts during build). For Play Console Production track.
- **Version code convention locked:** 1XXXXXX = internal testing, 2XXXXXX = production. Tauri auto-generates 1XXXXXX from version string; production builds must hardcode versionCode in build.gradle.kts (then restore after build).
- **16KB page size:** Confirmed via `.cargo/config.toml` rustflags `-Wl,-z,max-page-size=16384` on all 4 Android targets (aarch64, armv7, i686, x86_64).
- **Tauri auto-gen caveat:** `tauri.properties` is auto-regenerated on every build from `tauri.conf.json`. Cannot rely on editing this file for custom versionCodes. Must edit `build.gradle.kts` directly.
- **Both AABs signed:** jarsigner with `chronx-release.keystore`, alias `chronx`.
- **version.json updated:** android_version → "1.4.55".

### 2026-03-06 (Admin Portal — Usman Password Reset)
- **Password reset:** Usman's admin password reset to temporary `ChronX-Usman-2026` in `/home/josep/admin-users.json` on Vultr.
- **must_change_password:** Set to `true` — Usman will be prompted to change on next login.
- **Admin users file:** `/home/josep/admin-users.json` — bcrypt-hashed passwords, roles (owner/staff), shared by ChronX admin and MISAI admin portals.

### 2026-03-06 (MISAI — Binance API Integration)
- **Binance spot trading:** International users (Pakistan, HK, 180+ countries) can connect Binance API keys. Crypto only, no stocks. Not available in US.
- **Server DB:** Added columns `binance_api_key` (AES-256 encrypted), `binance_secret_key` (AES-256 encrypted), `binance_mode` (default 'spot') to agents table.
- **Server endpoints (index.js):**
  - `POST /api/agent/verify-binance` — verifies keys against `api.binance.com/api/v3/account` (HMAC-SHA256 signed), returns `{ valid, balances }`.
  - `POST /api/agent/:id/connect-binance` — verifies, encrypts with AES-256-GCM, stores in DB. Returns `{ success, balances }`.
  - `GET /api/agent/:id/binance-status` — fetches live Binance account, returns `{ connected, balances, total_usdt_value }`.
- **Engine (engine.js):** `executeBinanceTrade()` — executes MARKET orders on Binance. BUY uses `quoteOrderQty` (dollar amount). SELL fetches position from Binance account, adjusts for LOT_SIZE filter precision. Errors logged, never crash engine.
- **arena.html:** Binance connection section with API key/secret inputs, verify button, green checkmark + balances on success. Credentials passed to deploy request. "Coming Soon" card updated to "US Brokerages" (Robinhood | Alpaca).
- **my-agent.html:** Trading Mode selector now has 4 options: Simulated (active), Binance (check status), Alpaca (coming soon), Robinhood (coming soon). Binance panel shows USDT balance, positions, connection status.
- **MISAI service name:** `misai-api` (systemctl restart misai-api). Port 4040.
- **misai.io deployed:** 9 files, 0 failures.

### 2026-03-06 (MISAI Debug — Multi-Agent API + Tab Bar Fix)
- **Root cause:** `GET /api/agents?wallet=X` endpoint did not exist on server. Frontend call returned 404, so tabs never rendered.
- **Server patches (index.js on Vultr):**
  - Added `GET /api/agents?wallet=X` — returns array of agent objects with agent_id, agent_name, status, current_usd, starting_usd, return_pct, kx_balance, decision_interval_minutes, trade_duration_hours.
  - Added `POST /api/agents/exit-all` — accepts `{ wallet }`, pauses all active agents, sells all positions to cash at market price.
  - Added `trade_duration_hours` support in `PUT /api/agent/:id/settings` — recalculates trade_end_at from now.
- **Frontend fix (my-agent.html):** Tab bar and portfolio summary now show with >= 1 agent (was > 1). Added "+ New Agent" link tab pointing to arena.html. Fixed agentId string vs number comparison for active tab highlighting. Added fallback for no wallet param (builds single-agent tab from current page data).
- **Service name:** `misai-api` (not `misai`). Systemd unit: `/etc/systemd/system/misai-api.service`. Port: 4040 on 127.0.0.1. Nginx proxy: api.chronx.io/misai/ → localhost:4040/.
- **misai.io redeployed:** 9 files, 0 failures.

### 2026-03-06 (MISAI Major Features — Multi-Agent Tabs, Asset Selector, Session/Interval Editing)
- **Asset selector (arena.html):** Multi-select chip/pill UI for choosing tradeable assets. Categories: Crypto (BTC, ETH, SOL, DOGE, ADA, XRP, AVAX, LINK, DOT, MATIC), Stocks (AAPL, MSFT, NVDA, TSLA, GOOGL, AMZN, META, AMD, NFLX, JPM), ETFs (SPY, QQQ, IWM, VTI, ARKK, GLD). Full names shown. Toggle all per category. BTC/ETH/AAPL/MSFT/NVDA selected by default. Included as `selected_assets` in deploy request.
- **Session length options (arena.html):** Added 8h, 1 month, Custom (shows hours input). Removed 48h.
- **Editable session length (my-agent.html):** Session Length setting row with Edit button. Dropdown: 8h/24h/3d/1wk/1mo. Saves via PUT /api/agent/:id/settings.
- **Adjustable interval with KX calculator (my-agent.html):** Interval setting now has Edit button. Dropdown: 5/15/30/60 min. Live KX cost calculator shows decisions/day, KX/day, USD/day.
- **Multi-agent tabs (my-agent.html):** Loads all agents for wallet via GET /api/agents?wallet=X. Tab bar below portfolio summary. Each tab shows agent name + P&L%. Click switches active agent. URL updated via history.replaceState.
- **P&L tab colors:** Green bottom-border for profitable, red for losing, muted for neutral. Applies to both tab border and P&L text.
- **Pulse animation:** When a new decision is detected (decision count increases), the tab briefly glows cyan (0.6s ease, 2 cycles).
- **Portfolio summary bar (my-agent.html):** Shows total portfolio value, weighted return, total KX across all agents. Only visible when >1 agent.
- **Exit All to Cash button:** In portfolio summary bar. Confirmation modal. Calls POST /api/agents/exit-all with wallet address.
- **misai.io deployed:** 9 files, 0 failures.

### 2026-03-06 (MISAI Content Additions — Why MISAI, Transparency, Trust Line)
- **"Why MISAI?" section:** Added to index.html after hero. 3 cards: Always Watching (⚡), Never Emotional (🧠), Always Current (📡). CSS grid layout with `.why-misai`, `.why-grid`, `.why-card` classes.
- **Transparency disclaimer box:** Added to both index.html and arena.html. Cyan left-border box with "Radical Transparency" header explaining AI decision cost breakdown (0.4 KX ≈ $0.00128, ~88% API costs, ~12% platform margin).
- **Hero trust line:** Added `🔒 MISAI never touches your money` below hero CTA on index.html. Also added bold trust statement on arena.html.
- **"Daily KX Cap" renamed:** → "Daily KX Spending Cap (AI fuel)" across my-agent.html (label, tooltip, all references).
- **misai.io deployed:** 9 files, 0 failures.

### 2026-03-06 (Auto-Delivery System — Matured Timelock Pre-Registration)
- **New MySQL table:** `claim_registrations` — stores wallet pre-registrations against claim codes (claim_code UNIQUE, wallet_address, amount_kx, unlock_at, is_series, status, delivered_at, tx_hash, error_msg)
- **POST /claim/register endpoint:** Recipients register wallet address for a claim code. Validates code against on-chain locks via `chronx_getCascadeDetails` RPC. If locks already matured, triggers immediate delivery. Returns lock details with amounts and unlock dates.
- **GET /claim/status/:code endpoint:** Check registration and delivery status for a claim code.
- **Auto-delivery cron (every 5 min):** Scans `claim_registrations` for matured locks (status='registered' AND unlock_at <= now). Uses relay wallet to claim-by-code then transfer to registered wallet. For series, re-registers with next unlock_at after partial delivery.
- **Delivery confirmation email:** New `buildAutoDeliveryConfirmEmail()` template — notifies recipients when KX is auto-delivered to their wallet.
- **claim.html redesign:** Primary flow changed from "copy claim code" to "Register Wallet for Auto-Delivery". Wallet address input form, success state with lock details table showing amounts/dates/status. Manual claim (copy code / open in app) moved to secondary section below. Status check on page load shows if already registered.
- **Email template updates:** Promise email CTA changed from "Download Wallet" to "Register Wallet for Auto-Delivery" with explanation. Series email how-to updated with auto-delivery option. Single claim email updated with registration link.
- **i18n updated:** All 7 languages (EN, ES, FR, DE, JA, KO, ZH) updated with new `emailClaimDesc` and `registerDesc` keys.
- **blake3 v2.1.4 installed:** npm package for BLAKE3 hashing (matches Rust-side claim code hashing).
- **Cascade/series handling:** Registration stores is_series flag. Cron checks for remaining pending locks after delivery, re-registers with next unlock_at for ongoing series.
- **CORS updated:** chronx-notify now accepts requests from both `chronx.io` and `www.chronx.io`.
- **Files modified:** `/opt/chronx-notify/index.js` (server), `C:\Users\Josep\chronx-website\claim.html` (frontend)
- **Deployed:** chronx-notify restarted, claim.html deployed to chronx.io via FTP

### 2026-03-07 (Promise Email System — Immediate Notification on Delayed Send)
- **Immediate Promise email on delayed send:** /notify endpoint now sends a "You've Been Made a Promise" email immediately when unlock_at is in the future (>60s from now). Fires for BOTH verified and unverified recipients. Subject: "You just received a Promise of X KX 🔒". Body includes: amount in KX, USD equivalent (amount × 0.00319), unlock date (formatted), gold info box "You don't need to do anything — KX will arrive automatically on [date], guaranteed by the blockchain", sender identity (email > ....last6 wallet > Someone), memo if present, CTA button to chronx.io/wallet.html.
- **Delivery confirmation email upgraded:** Auto-delivery success email now reads "A Promise made to you on [original send date] just delivered ✅". References created_at from claim_registrations as original promise date. Body includes "This Promise was kept by the ChronX blockchain — exactly as guaranteed." and memo from original send if available.
- **Sender identity wired end-to-end:** commands.rs updated — notify_email_recipient now includes sender_wallet (from keypair) and sender_email (from WalletConfig) in /notify POST payload. Server builds senderDisplay: email > ....last6 > "Someone". Stored in claim_registrations.sender_display for delivery email retrieval. NOTE: requires wallet rebuild to activate — existing wallet versions still omit sender fields.
- **"Someone" bug confirmed and fixed in code:** Delayed sends currently show "Someone just sent you a Promise" until next wallet build. Fix is in commands.rs, pending rebuild.

### 2026-03-07 (MISAI — Deploy Form Redesign + Engine Intelligence Upgrade)
- **arena.html deploy form — full redesign:** Removed broker connection section (Binance API inputs, Coming Soon brokerages) and individual ticker chip selector (30 chips). Replaced with 4 smart option grids:
  - Asset Universe: Crypto (24/7) / US Stocks (NYSE·NASDAQ) / ETFs / Full Universe — single select
  - Time Horizon: Day Trader (minutes-hours) / Swing Trader (days-weeks) / Long-Term (weeks-months) — single select
  - Risk Profile: Conservative / Balanced / Aggressive — single select
  - Decision Interval: 5/15/30/60 min with KX/day cost shown — single select
  - Session Length: 1 Day / 1 Week / 1 Month / No Limit — single select
- **Smart market hours note:** When Asset Universe = Stocks, ETFs, or Full Universe, a cyan info box appears: "Smart market hours enabled — AI pauses automatically when US markets are closed. KX only burns during trading hours."
- **Deploy button:** Now reads "Deploy in Demo Mode →" with note "Starts in demo mode. Connect a live broker from your agent dashboard anytime." Broker setup is intentionally deferred to agent dashboard.
- **New DB columns on agents table:** asset_universe TEXT DEFAULT 'crypto', time_horizon TEXT DEFAULT 'swing_trader', risk_profile TEXT DEFAULT 'balanced', market_hours_smart INTEGER DEFAULT 1.
- **engine.js — strategy-aware system prompt:** universeMap, horizonMap, riskMap objects injected into Claude system prompt per agent settings. Universe constrains which asset classes AI may trade. Horizon defines holding style (day/swing/long-term). Risk profile sets position sizing limits (20%/40%/unlimited max per position).
- **engine.js — NYSE market hours smart-pause:** Before executing decision for stocks/ETFs agents, checks if current UTC time is Mon-Fri 13:30-20:00 UTC (NYSE hours). Outside hours: skips decision, logs "Market closed — resuming at next open", does NOT burn KX. Crypto and full-universe agents run 24/7 for crypto positions.
- **misai.io deployed:** 9 files, 0 failures. misai-api restarted.

### 2026-03-07 (MISAI — Agent Tabs UI Polish)
- **my-agent.html tabs:** Redesigned to look unmistakably like browser-style tabs. Raised tab style with border on top/sides, bottom border matches surface background (creates "connected to content" illusion). Active tab: cyan agent name, rgba(0,229,255,0.08) tint, border-bottom-color matches surface. Hover: surface2 background. Tabs sit flush against content panel below. "+ New Agent" tab styled with dashed cyan border.

### 2026-03-07 (Whitepaper v3.2 — Full Rebuild from JS)
- **Whitepaper v3.2:** Built from scratch using docx JS library (not XML editing — eliminates corruption risk). 347 paragraphs, all validations PASSED. Output: chronx-whitepaper-v3.2.docx.
- **Changes from v3.1:** Version bump + subtitle "· The AI Promise". Abstract: expanded to introduce AI Promise + third-party notice for XCHAN/MISAI/Verifas. MISAI overview (7.1) + XCHAN overview (10): both now open with "independent third-party... not operated by or affiliated with ChronX". New Section 11 — The AI Promise (4 subsections: 11.1 Four-Step Flow, 11.2 No Protocol Change Required, 11.3 Use Cases, 11.4 Risk Disclosure). Sections renumbered: Security→12, Governance→13, Roadmap→14, Risk→15. Roadmap: new row "2028+ · AI Promise · AI-managed time-locked value transfer".
- **AI Promise custody decision (IMPORTANT — DO NOT BUILD YET):** Current AI Promise design (KX→XCHAN→USDC→MISAI→USDC→XCHAN→KX) has real legal/custody problems: unclear custody during MISAI trading, no mechanism for court orders, death/estate issues, no strategy modification after lock. Correct path: KX-native trading pairs only (KX/USDC, KX/WBTC on Uniswap), funds never leave ChronX protocol. Requires wKX liquidity on Base — 2028 feature. Simple time-locked Promise (no AI, no USDC) is ready now and has zero custody ambiguity. DO NOT ship AI Promise until KX-native pairs exist and a lawyer reviews.
- **Whitepaper committed to chronx-docs locally.** GitHub push: run `cd C:\Users\Josep\chronx-docs && git push origin main`

---

## GENESIS 7 — VERIFIED DELIVERY PROTOCOL
Status: IMPLEMENTED AND LIVE (v7.0, re-genesis 2026-03-08)
Specified: 2026-03-07 | Implemented: 2026-03-08

### What This Is
Genesis 7 adds the Verified Delivery Protocol to the
ChronX node. Implemented across 13 Rust source files.
Re-genesis v7.0 completed 2026-03-08. All RPC methods live.
Placeholder Verifas verifier registered on-chain.

### Files To Modify
- crates/chronx-core/src/constants.rs
  Add all immutable compile-time constants below

- crates/chronx-genesis/src/params.rs
  Add new fields to GenesisParams struct
  Add HUMANITY_STAKE_POOL, VERIFAS_REGISTRY wallets

- engine.rs
  New logic:
  - 91-day consensus trigger transaction
  - Activation deposit collection (0.5% per promise,
    min 100 KX, max 10,000 KX)
  - Promise never-revert (replaces 72-hour revert)
  - 100-year unclaimed expiry → humanity stake pool
  - Encrypted package generation at promise creation
  - Verifier registry management

- db.rs
  New state:
  - Verifier registry (empty at genesis)
  - Promise tracking for trigger
  - Humanity stake pool routing

### New Transaction Types
TYPE_V_TRIGGER — consensus system transaction
  fires automatically on day 91 for unclaimed promises
  sends encrypted package + activation deposit to
  registered Verifas wallet

TYPE_V_EXPIRY — automatic transfer
  fires at maturity + 100 years for unclaimed promises
  routes KX to humanity stake pool

VERIFIER_REGISTER — governance transaction
  adds approved verifier to registry
  requires Foundation governance vote
  records: name, wallet, bond amount, public key,
  jurisdiction

### Immutable Constants (constants.rs)
VERIFAS_TRIGGER_DAYS: 91
ACTIVATION_DEPOSIT_BASIS_POINTS: 50
ACTIVATION_DEPOSIT_MINIMUM_KX: 100
ACTIVATION_DEPOSIT_MAXIMUM_KX: 10_000
PROMISE_REVERT_ENABLED: false
UNCLAIMED_EXPIRY_YEARS: 100
EXPIRY_DESTINATION: humanity_stake_pool
VERIFAS_OBLIGATION: custody_only
VERIFAS_PUBLIC_INTERFACE: false
FINDER_VERIFIER_SAME_ENTITY: prohibited
SELF_CLAIM_FEE: zero
KEY_SHARES_TOTAL: 5
KEY_SHARES_REQUIRED: 3
KEY_ROTATION_COSIGNERS_REQUIRED: 2
KEY_ROTATION_MAX_INTERVAL_DAYS: 365
BENEFICIARY_TYPES: [email, person, organization, governance]

### Governable Parameters (Foundation vote, downward only)
FINDER_FEE_MAX: 6.5%
VERIFAS_RELEASE_FEE_MAX: 0.5%
MINIMUM_VERIFIER_BOND_KX: 1_000_000
SELF_CLAIM_WINDOW_DAYS: 90
FINDER_CONTACT_PERIOD_DAYS: 10

### Required Package Contents (sent to Verifas day 91)
1. Claim credential — complete encrypted unlock
2. Promise value — in KX
3. Beneficiary domicile at creation — optional
4. Beneficiary type — email/person/organization/governance
5. Beneficiary identifier — matching type above

### Beneficiary Types
A = email address
B = person — legal name + date of birth
C = organization — legal name + registration number
    + jurisdiction + successor clause
D = governance — Foundation vote + distribution mechanism

### Verifas Legal Requirements (pre-genesis 7)
Must be completed BEFORE Genesis 7 launches:
- Swiss nonprofit foundation incorporated
- HSM procured and configured
- Keypair generated on HSM — never leaves hardware
- 5-share Shamir split across:
    Share 1: Verifas HSM — Zurich
    Share 2: ChronX Foundation HSM — Geneva
    Share 3: Independent escrow — Singapore
    Share 4: Independent escrow — Cayman Islands
    Share 5: Time-locked on ChronX blockchain
- Foundation governance transaction registers Verifas
  as first approved verifier with public key + bond
- NO NEW GENESIS REQUIRED after this step —
  verifier registry is a governable on-chain structure

### Humanity Stake
Amount: 1,000,000 KX
Lock: until 2126-01-01
Release: Foundation governance vote
Receives: unclaimed promises at maturity + 100 years
New wallet generated at Genesis 7 — not before

---

### 2026-03-11 (wKX Bridge Setup + Contract Deployment — ERC-20 on Base)
- **wKX Bridge KX wallet generated:** `/home/josep/.chronx/wkx-bridge-wallet.json` — Account ID: `FGSemyJdkCU85D4qQNWFd158J44MANAHTAF5Qx974WRR`. This wallet holds KX reserves backing all minted wKX tokens.
- **wKX Bridge ETH wallet generated:** `0x569EAea5F00B1f554790778d14934817bc00e733` — private key stored securely. This wallet signs mint transactions on Base network. Mnemonic: given to Joseph.
- **WrappedKX.sol contract:** Source at `/opt/wkx-deploy/WrappedKX.sol` (also `/home/josep/WrappedKX.sol`). ERC-20 "Wrapped KX" (wKX) on Base (chain 8453). Features: `mint()` (bridge-only, nonReentrant), `unwrap()` (burn + emit event for ChronX release, nonReentrant), `setBridge()` (owner-only). Uses OpenZeppelin ERC20 + Ownable + ReentrancyGuard. 18 decimals.
- **CONTRACT DEPLOYED TO BASE MAINNET:** `0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677` — https://basescan.org/address/0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677. Deployed via solc + ethers from `/opt/wkx-deploy/deploy.js`. ABI saved to `/opt/wkx-deploy/WrappedKX.abi.json`. Bridge address: `0x569EAea5F00B1f554790778d14934817bc00e733`. Owner: `0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54`.
- **Bridge daemon LIVE:** systemd service `wkx-bridge` on Vultr. Source: `/opt/wkx-bridge/index.js` (286 lines). Polls `chronx_getIncomingTransfers` every 30s for KX deposits to bridge wallet, mints wKX on Base to sender's registered Base address. Polls Base for `Unwrapped` events, releases KX from bridge wallet via CLI. SQLite DB: `/opt/wkx-bridge/bridge.db` (tables: deposits, unwraps, address_registry). HTTP API on `localhost:3002`: `POST /register` (map KX address to Base address), `GET /lookup/:kx_addr`, `GET /status`. Env: `/opt/wkx-bridge/.env` (chmod 600). Dependencies: ethers, better-sqlite3, dotenv.
- **Compiler:** solc 0.8.34+commit.80d5c536, optimizer 200 runs, evmVersion paris. Standard JSON input saved at `/opt/wkx-deploy/standard-input.json`. Constructor args: `/opt/wkx-deploy/constructor-args.txt`.
- **BaseScan VERIFIED:** Source code verified via Etherscan V2 API (GUID: xmhanbcavtcnefkuidx7acdkjr4sqd9e69ncw5atmaiuvpwgka). Green checkmark live at https://basescan.org/address/0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677#code. Etherscan API key: `ANVVES9RXQV2ZM224J35BXHJ5C6ZYJPNX4`.
- **Seed mint:** 10,190 wKX minted to Joseph's TrustWallet (`0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54`) for Uniswap pool seeding. TX: `0xfc76a60538968d42c1b7589c0b62b4a7b7e1a3458cf64a5a619a3321185b691d`. chronxTxId: `SEED-LIQUIDITY-2026-03-11`.
- **Uniswap v3 wKX/USDC pool LIVE on Base:** Fee tier 1%, full range, initial price 0.00319 USDC/wKX (ICO price). Seeded with 32.50 USDC + 0.104 wKX. Joseph's TrustWallet: `0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54`.
- **XChan swap UI LIVE at xchan.io:** Full wKX/USDC swap interface with wallet connect, Uniswap v3 quotes, swap execution, wallet registration, unwrap section. Uses ethers.js v6, direct Uniswap v3 Router + Quoter contracts on Base. Pool fee: 1% (10000). API at `api.chronx.io/api/xchan/*` (systemd `xchan-api` on port 4042, nginx proxied).
- **Pool rebalance (2026-03-11):** Initial pool had wrong ratio (~$0.0325/wKX instead of $0.00319). Two seed mints totaling 20,380 wKX. Joseph has ~20,380 wKX in TrustWallet. PENDING: Joseph adds ~10,188 wKX to existing Uniswap position to correct price to $0.00319. Second mint TX: `0x68e78e0ff3b35ab1ebf4871389355195776b7e3940d07223adc64d019f579e94`.
- **Next steps (in order):**
  1. Joseph: add ~10,188 wKX to Uniswap position via https://app.uniswap.org/positions
  2. Apply to CoinMarketCap: https://coinmarketcap.com/application-form/listing/
  3. Apply to CoinGecko: https://www.coingecko.com/en/coins/new
  4. Apply to 1inch token list

---

### 2026-03-13 (Robot Wallet SDK + wallet.html Revamp + iOS/macOS Notify Signups)

#### Wallet Updates
- **Wallet v1.4.82 shipped:** Address book, mobile send restrictions (email-only on mobile, direct wallet address on desktop), convert widget, 8th language (Urdu with RTL).
- **Wallet v1.4.83 built:** Bug fixes — Base address field display, send lockup fix, email-only mobile enforcement.
- **Android versionCodes:** Internal 1004083, Production 2004083.
- **Google Play:** Internal testing v1.4.82 live. Production track still pending review.
- **Next build:** v1.4.84, Internal versionCode 1004084, Production 2004084.

#### Bot API & Robot Wallet SDK
- **Bot API portal LIVE:** `chronx.io/bot.html` — registration form, dashboard link, code examples, docs.
- **Bot API endpoints (Vultr):** POST `/bot/register` (email+wallet→API key), POST `/bot/cashout` (KX→USDC auto-conversion via XChan), GET `/bot/status` (balance+history), PUT `/bot/update-address` (change USDC payout address). All on `api.chronx.io`.
- **bot_accounts table:** SQLite on Vultr (`/opt/chronx-notify/bot.db`). Fields: api_key, email, wallet_address, usdc_address, created_at.
- **chronx-robot-wallet SDK deployed:** `chronx.io/dl/chronx-robot-wallet/` — chronx-bot.js (v1.1.0), config.json, package.json, README.txt, setup.js. ZIP at `chronx.io/dl/chronx-robot-wallet.zip`.

#### Website Changes
- **wallet.html revamped:** New 3-card download layout (Mobile Android, Desktop Windows, macOS & iOS coming soon). Green checkmark feature lists. Bot API section with code snippet. Horizontal "Why ChronX Wallet" cards (Zero Fees, Post-Quantum, Open Source). Full 8-language i18n (~48 new `wdl_*` keys in translations.js).
- **iOS/macOS notify signup form:** AJAX POST to `api.chronx.io/notify-signup` → MySQL `notify_signups` table (email, platform, ip_address, created_at). Deduplication by email+platform. Replaces old mailto link.
- **Admin panel updated:** iOS/macOS Notify Signups section added to Signups tab. Fetches from GET `/admin/notify-signups` (X-Admin-Token protected). Shows count, email, platform, date.
- **Notify API endpoints added:** POST `/notify-signup` (public, validates email, stores with platform+IP), GET `/admin/notify-signups` (admin-only, returns ios-macos signups with count).

#### Infrastructure
- **xchan-api LIVE:** Vultr port 4042, systemd `xchan-api`. `/api/xchan/quote` endpoint for KX/USDC price quotes.
- **wkx-bridge updated:** FallbackProvider for Base RPC reliability + memo routing for deposit identification.
- **Discord LIVE:** https://discord.gg/Nwxrsk4g
- **Cashback extension + rewards.html LIVE:** Amazon Associates tag `chronx-20`.
- **wKX on Base confirmed:** Contract `0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677`, Uniswap v3 pool active.

#### URGENT Reminders
1. **BaseScan verification** needs Etherscan API key (ANVVES9RXQV2ZM224J35BXHJ5C6ZYJPNX4) — verify source code is showing green checkmark.
2. **Uniswap pool rebalance** — Joseph needs to add ~10,188 wKX to correct price to $0.00319.
3. **Google Play production** — submit v1.4.82 or v1.4.83 AAB for production review.
4. **CoinMarketCap / CoinGecko listings** — applications pending.

#### Open Bugs (v1.4.83)
- QR code display broken (blank modal)
- Windows deep link (`chronx://`) not triggering wallet
- Cascade Send `lock_seconds=0` rejected by node
- Import Base64 private key crashes wallet
- version.json triggers false update notifications

---

*Maintained by Claude instances working on ChronX. Last updated: 2026-03-13.*

### 2026-03-14 — Cascade Auto-Delivery Fix (usmanuah9@gmail.com)

#### Problem
usmanuah9@gmail.com was not receiving auto-delivery of incoming cascade promises. A 4-stage cascade (4 × 250,000 KX) was sent from the Public Sale wallet. Only stage 1 (immediately claimable) was delivered; stages 2-4 remained as unclaimed Pending locks on-chain.

#### Root Cause (3 bugs)
1. **Inline relay delivery did not check for remaining cascade locks.** When /notify auto-delivered stage 1 via `autoDeliverToVerifiedWallet()`, it marked the `claim_registrations` entry as `delivered` and never checked if more locks shared the same `claim_secret_hash`. The cron only processes `status=registered` entries, so stages 2-4 were invisible.
2. **CLI output format mismatch in `deliverRegisteredClaim`.** The relay parsed CLI output with regex `/totalling\s+([\d.]+)\s+KX/` but the CLI now outputs `Claimed N lock(s): <txid>` without the "totalling" line. Fallback used `amountKx` from the registration, which for cascades was the total remaining (not per-lock), causing the forward transfer to attempt more KX than actually claimed.
3. **`l.amount` vs `l.amount_chronos` in cron series check.** The crons remaining-locks code used but the RPC returns , resulting in after re-registration.


### 2026-03-14 — Cascade Auto-Delivery Fix (usmanuah9@gmail.com)

#### Problem
usmanuah9@gmail.com was not receiving auto-delivery of incoming cascade promises. A 4-stage cascade (4 x 250,000 KX) was sent from the Public Sale wallet. Only stage 1 (immediately claimable) was delivered; stages 2-4 remained as unclaimed Pending locks on-chain.

#### Root Cause (3 bugs)
1. **Inline relay delivery did not check for remaining cascade locks.** When /notify auto-delivered stage 1 via autoDeliverToVerifiedWallet(), it marked the claim_registrations entry as 'delivered' and never checked if more locks shared the same claim_secret_hash. The cron only processes status='registered' entries, so stages 2-4 were invisible.
2. **CLI output format mismatch in deliverRegisteredClaim.** The relay parsed CLI output with regex /totalling\s+([\d.]+)\s+KX/ but the CLI now outputs "Claimed N lock(s): txid" without the "totalling" line. Fallback used amountKx from the registration, which for cascades was the total remaining (not per-lock), causing the forward transfer to attempt more KX than actually claimed.
3. **l.amount vs l.amount_chronos in cron series check.** The cron's remaining-locks code used l.amount but the RPC returns amount_chronos, resulting in amount_kx=0 after re-registration.

#### Bonus fix
- MySQL ENUM for claim_registrations.status was missing 'pending_claim' — unverified recipients hit "Data truncated" errors on INSERT.

#### Fixes Applied
1. **Data fix:** Re-registered KX-FCC3-BA8F-935A-23D2 with status='registered', is_series=1, unlock_at=next matured lock.
2. **Inline delivery cascade check:** After relay delivers, code now queries chronx_getCascadeDetails for remaining Pending locks and re-registers with status='registered', is_series=1, unlock_at=next maturity.
3. **Pre-claim amount query in deliverRegisteredClaim:** Before claiming, queries cascade details to compute exact matured KX amount instead of relying on CLI output parsing.
4. **Fixed l.amount to l.amount_chronos || l.amount** in all 3 occurrences in the cron/cascade code.
5. **Added 'pending_claim' to MySQL ENUM.**
6. **Manual transfer:** 250,000 KX forwarded from relay to usmanuah9 wallet (tx e09a5efa...).

#### Verification
- usmanuah9 balance: 518,501 KX (correct: 270,001 original + 250,000 stage 2 - sends)
- 2 locks remaining: unlock at 2026-03-15 20:48:00 and 2026-03-16 20:49:00
- claim_registrations ID 34: status='registered', is_series=1, unlock_at=1773607680
- Cron will auto-deliver next lock at ~20:48 Mar 15, then re-register for final lock


### 2026-03-14 (late) — Email Template Fixes (FIX 1/2/3)

#### FIX 1: "Someone" instead of sender email
- **Root cause:** `buildEmail` (claim code template) and `buildSeriesEmail` had "Someone" hardcoded. They did not accept a `senderDisplay` parameter.
- **Fix:** Added `senderDisplay` parameter to both functions. Updated all call sites to pass `senderDisplay`. Also updated `buildVerifiedRecipientEmail` call to use `senderDisplay` instead of `sender_email || 'Someone'`.
- **Subject lines updated:** Claim code email now shows "from senderDisplay". Verified delivery email now shows "from senderDisplay".
- `buildPromiseEmail` was already correct (used `senderEmail` parameter).
- Removed duplicate `buildVerifiedRecipientEmail` function definition (was defined twice, lines 522 and 621).

#### FIX 2: Unlock date shows "Thu, 01 Jan 1970" (epoch zero)
- **Root cause:** `buildEmail` and `buildPromiseEmail` formatted `unlock_at=0` as a date (`new Date(0)`), producing "Thu, 01 Jan 1970 00:00:00 UTC".
- **Fix:** Added guard in both functions: if `unlock_at` is falsy, <= 0, or < 1,000,000,000 (year 2001), display "Available immediately" instead of formatting as date.
- `buildSeriesEmail` was already correct (had an existing `if (!unlockTs || unlockTs === 0)` check that showed "Immediately").

#### FIX 3: Verified recipient still receiving claim code email
- **Finding:** josephrsanchez@gmail.com was NOT in the `verified_emails` table. The code logic is correct: verified emails get auto-delivery + "KX added to wallet" email; unverified get claim code. Joseph was simply unverified.
- **Action:** Added josephrsanchez@gmail.com to `verified_emails` (wallet: 6AyvnXZkLXA95gTBN2aG39h81R5gUZ42MPZsuwAjxeNf).
- **Tested:** Sent 1 KX email-timelock to josephrsanchez@gmail.com via relay wallet. Verified: sender shows "test@chronx.io", not "Someone". Verified recipient got auto-delivery email (not claim code). Relay delivered 1 KX to founder wallet (tx: 9e83a1ec...).

#### Additional fix: ENUM mismatch from prior session
- Confirmed `pending_claim` was added to MySQL ENUM in prior session. No more "Data truncated" errors for unverified recipients.

#### POST /notify field names (for reference)
- `to` (recipient email), `amount` (KX), `unlock_at` (Unix seconds, 0=immediate), `memo`, `claim_code`, `sender_email`, `sender_wallet`, `series` (array for cascade)
- The test curl in the task used `recipient_email` and `amount_kx` which are WRONG field names. Correct names above.


### 2026-03-14 — v1.5.5 (Win) — Hide claim code for verified, hide promised when claimed

#### FIX 1: Hide claim code when recipient is verified/registered
- In History tab expanded detail, the "Claim code (share with recipient): KX-XXXX..." section with Copy Code button is now hidden when `recipient_registered = true`.
- Uses `entry.recipient_registered` with fallback to cascade sibling data via `cascade_email` map (same pattern as registration badge elsewhere).
- Rationale: Verified recipients get auto-delivery; they never need the claim code.

#### FIX 2: Hide "Promised — cannot cancel" when already Claimed
- The "Promised — cannot cancel" text in History detail now only shows when the entry's own status is still Pending-ish.
- Added guards: `entry_status != "Claimed" && !entry_status.contains("Expired") && entry_status != "Cancelled"`.
- Rationale: Showing "cannot cancel" on an already-Claimed entry is redundant and confusing.

#### Build
- Version bumped to 1.5.5 in tauri.conf.json and src-tauri/Cargo.toml.
- Windows .exe built and deployed via deploy_website.py.
- version.json updated: version=1.5.5, release_notes updated.
- Git pushed to Counselco/wallet-gui main (48567ea).


#### CRITICAL: .exe deploy requires manual FTP upload
- `deploy_website.py` uploads ALL files in `chronx-website/` but the .exe in `dl/` must be manually copied from the build output first.
- Build output: `wallet-gui-temp/src-tauri/target/release/bundle/nsis/ChronX Wallet_X.Y.Z_x64-setup.exe`
- Must copy to BOTH: `chronx-website/chronx-wallet-setup.exe` AND `chronx-website/dl/chronx-wallet-setup.exe`
- Then run `deploy_website.py` (or FTP upload directly).
- v1.5.5 .exe confirmed uploaded (5,237,767 bytes) to both `/dl/chronx-wallet-setup.exe` and `/chronx-wallet-setup.exe`.

---

### 2026-03-26 — YubiHSM 2 Security Migration Plan

#### SECURITY HARDWARE ORDERED
- **YubiHSM 2** from yubico.com — ~$650
- **Arriving**: ~March 29-31, 2026

#### MIGRATION PLAN (CC-Mac session when HSM arrives)
1. Install yubihsm-shell on Mac Mini
2. Generate oracle + bridge keys ON YubiHSM 2 hardware (never exist in plaintext anywhere)
3. Move bridge daemon from Vultr to Mac Mini
4. Update wKX contract oracle address to new key
5. Update Vultr node to call Mac Mini signing service
6. Retire /opt/wkx-bridge/.env private key
7. Mac Mini becomes signing server (Vultr is public relay only — holds no keys)

#### SAVINGS GOVERNANCE CAPS (active until YubiHSM migration)
```
savings_max_per_wallet_usd: 50
savings_max_total_exposure_usd: 1500
```
Joseph backstops losses manually up to $1,500.

POST-MIGRATION caps can be raised by governance vote.

#### SECURITY CONSTRAINT: PROMISES_CANNOT_BE_LOST
Savings yield (savings_hedgekx_yield_enabled) MUST NOT activate until:
1. Oracle private key moved to HSM or multi-sig
2. HedgeKX escrow contract audited by third party
3. Vultr node hardened / multi-node consensus
4. Explicit governance vote
5. Security disclosure in whitepaper accepted

Default states for all locked KX:
- Option 1: Clean lock — no yield, no risk, no mechanism
- Option 2: MISAI managed — explicit user choice, MISAI bonded
- Option 3: Savings yield — FUTURE, not at launch

**Nothing that touches a hot server can be in the critical path of a locked promise.**

### 2026-03-26 — EPP Governance Dashboard

- **Endpoint**: GET https://api.chronx.io/governance/epp-status — returns live status for all 5 EPPs
- **Dashboard**: https://api.chronx.io/governance/ — dark theme, auto-refresh 30s
- **Admin page**: chronx.io/admin/ now has EPP status lights in header (polls every 30s)
- **Rejected request logging**: xchan_rejected_swaps + hedgekx_rejected_deposits MySQL tables
- **Status logic**: BURST (rejected demand > 0), CRITICAL (cap > 100% or pool empty + active), WARNING (cap > 75% or action_required), OK (normal)
- HedgeKX shows WARNING because pool is $0 (hedging enabled but unfunded = latent risk)

### 2026-03-26 — Superseding Hedger Architecture (designed, not yet built)

Genesis params to add:
```json
{
  "superseding_hedger_duration_days": 7,
  "superseding_hedger_min_commitment_usd": 1600,
  "superseding_hedger_daily_capacity_usd": 250,
  "superseding_hedger_yield_pct_annual_max": 5.0,
  "savings_risk_free_rate_source": "hedgekx_overnight",
  "misai_benchmark_rate_source": "savings_risk_free_rate",
  "promises_savings_yield_enabled": false
}
```
- Risk-free rate = HedgeKX overnight yield
- MISAI benchmark = risk-free rate (must generate alpha above this)
- Superseding hedger: $1,600 USDC → 7-day escrow → $250/day capacity
- Promises earn interest: governance vote required before activation

### 2026-03-26 — HedgeKX Flywheel on Homepage

- New section on chronx.io between AI Economy and Support box
- Inline SVG: 6 nodes orbiting gold HedgeKX center (Savings → Liquidity → Stable KX → PAY_AS → Hedge Demand → Yield → Savings)
- Translated in 7 languages (en, fr, de, zh, es, ru, ar)
- Flow labels on arcs describe the self-reinforcing loop

### 2026-03-26 — Whitepaper Edits (chronx-docs repo)

Three additions to chronx-whitepaper-version-one.docx:
1. HedgeKX flywheel paragraph (Section 4.4, after mandate)
2. Credit assessment sentence (CREDIT AXIOMS section, after Axiom V)
3. L.9 Principal-Protected Savings (Appendix L, after L.8)

---
## END OF DAY 2026-03-26 — FINAL STATE

CHAIN: 24 accounts, 28 vertices, 8,270,000,000 KX intact
FOUNDER: 187,986,901 KX | MOBILE: 21,314 KX
XCHAN: $262.28 USDC reserve (OK)
WALLET: v2.5.43 desktop live | v2.5.42 Android on Play Store
VERSION.JSON: version=2.5.43, android_version=2.5.42

YUBIHSM 2 FIPS ORDERED ($950, yubico.com, arriving ~March 29-31 2026)
  Migration plan: Mac Mini becomes signing server
  Bridge daemon moves from Vultr to Mac Mini
  Keys generated on YubiHSM, never in plaintext
  After migration: raise savings governance caps

SAVINGS PHASE 2 (CC v2.5.44 building as of end of day):
  Three wallet buckets: Spendable / Savings / Loan Reserve
  Auto-Sweep only touches Spendable
  Savings earns HedgeKX overnight yield (0-5% annual)
  Superseding hedger: Joseph deposits $1,600 USDC/week
  Governance caps: $50/wallet, $1,500 total (Joseph backstop)
  savings_hedgekx_yield_enabled: true (governance capped)

SUPERSEDING HEDGER INSIGHT:
  $1,600/week USDC → $250/day hedge capacity
  At ICO phase KX price stable (Joseph maintains via XChan)
  Hedges expire clean → Joseph collects premiums, near-zero risk
  You are paid to maintain stability you were doing anyway

MISAI BENCHMARK:
  Risk-free rate = HedgeKX overnight savings yield
  MISAI must beat this rate to justify existence
  misai_benchmark_rate_source: savings_risk_free_rate

PROMISES CANNOT BE LOST — ABSOLUTE RULE:
  Nothing on a hot server in critical path of locked KX
  Default = clean lock (no yield, no risk)
  Savings yield = governance capped, Joseph backstop
  Full hardening requires: YubiHSM + audit + multi-node + governance vote

PENDING NEXT SESSION:
  1. Restart Mac Mini node (git pull + systemctl restart)
  2. v2.5.44 savings wallet — verify CC finished
  3. Android AAB v2.5.44 build (versionCode 4005040 internal, 5005040 production)
  4. Loan testing: auto-pay, late payment, cancellation, default
  5. XChan Buy KX endpoint (USDC→KX, currently missing)
  6. Wallet UI Leptos session (full-screen loan acceptance, Activity refresh)
  7. YubiHSM migration (when device arrives)



---

## wKX V3 DEPLOYMENT COMPLETE (2026-03-26)

### Contracts Deployed to Base (Chain 8453)

**WrappedKXv3**: `0x72D312b0386EEBd63a0B1734488DD81B3350717a`
  - ERC-20 "Wrapped KX" (wKX), 18 decimals
  - Provenance-enforced: every mint() requires authorized lock_id + non-expired lock. Public burn() for any holder.
  - Two-key model ready: minter + node attestation (attestation dormant until YubiHSM)
  - Owner: `0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54` (Joseph)
  - Minter: `0x569EAea5F00B1f554790778d14934817bc00e733` (bridge wallet, software key)
  - Source: `/opt/wkx-deploy/WrappedKXv3.sol`
  - ABI: `/opt/wkx-deploy/WrappedKXv3.abi.json` + `/opt/wkx-bridge/WrappedKXv3.abi.json`

**ChronXHeartbeatOracle**: `0x6Dfcd09ae500cC34FAFB574F92De2ED9a9B41a62`
  - trustedSigner: `0x569EAea5F00B1f554790778d14934817bc00e733` (bridge wallet, software key)
  - maxAge: 120 seconds
  - enforcementEnabled: **false** (enable after YubiHSM migration)
  - Owner: `0xF5fD6Da90cCaeE370bE7065D5A28e1C9da4d3a54`
  - Source: `/opt/wkx-deploy/HeartbeatOracle.sol`

**Uniswap V3 Pool (wKX v3 / USDC, 1% fee)**:
  - Pool: `0x33128a8fC17869897dcE68Ed026d694621f6FDfD`
  - Position NFT: #4867340 (held by bridge wallet `0x569E...`)
  - Price: $0.00319/wKX (ICO price)
  - Liquidity: 3,135 wKX + ~$10 USDC
  - Full range position

### RETIRED Contracts (do NOT use)
  - **wKX v3 (no burn)**: `0xcD2BB6DEA83298edABd5B1be16fdf3c3Eb2D0a30` -- RETIRED 2026-03-27 (replaced by v3+burn)
  - **wKX v2**: `0x0BBC24a0cBBC5d3fF1B9b90ce5195fC04FE0dD56` -- RETIRED 2026-03-26
  - **wKX v1**: `0xD21176adCEA2Fee38E7Ca2E4c94E7cd10C538677` -- RETIRED (auto-mint accident)
  - **Old Uniswap pool**: `0x0B1865E9519EFf7De80539d986C5abCC5e8667De` -- RETIRED (liquidity removed)

### Bridge Daemon Updated
  - `/opt/wkx-bridge/index.js` uses v3 contract with authorizeLock() + mint() flow
  - `/opt/wkx-bridge/.env` WKX_CONTRACT updated to v3 address
  - `/opt/wkx-bridge/WrappedKXv3.abi.json` in place
  - `/opt/wkx-bridge/xchan-api.js` updated to v3 contract address
  - Both services restarted and running clean

### Known Issues / TODOs
  - **LP wallet dust**: `0xF5fD...` holds 6,272 wKX from OLD v3 contract (0xcD2BB6..., now retired). These tokens are on the retired contract and effectively dead. New v3 contract (0x72D312...) has burn() function. Joseph should burn any dust on the new contract from MetaMask.
  - **BaseScan verification**: VERIFIED. Both contracts have green checkmarks on BaseScan. API key: `ANVVES9RXQV2ZM224J35BXHJ5C6ZYJPNX4`.
  - **CMC/CoinGecko**: Update with new pool address `0x33128a...`. TODO next session.
  - **Heartbeat enforcement**: OFF. Enable after YubiHSM arrives (~Mar 29-31): call setEnforcement(true) on oracle, setTrustedSigner(hsm_address) on oracle, setMinter(hsm_address) on wKX v3.

### YubiHSM Migration Checklist (when hardware arrives)
  1. `setTrustedSigner(hsm_eth_address)` on HeartbeatOracle
  2. `setMinter(hsm_eth_address)` on WrappedKXv3
  3. `setEnforcement(true)` on HeartbeatOracle
  4. Start heartbeat daemon on Mac Mini (30s interval)
  5. Test mint cycle end-to-end
  6. Retire bridge wallet private key from `.env`

### EPP Governance Dashboard (also deployed 2026-03-26)
  - Endpoint: GET https://api.chronx.io/governance/epp-status
  - Dashboard: https://api.chronx.io/governance/
  - Admin page: chronx.io/admin/ has EPP status lights in header
  - MySQL tables: xchan_rejected_swaps, hedgekx_rejected_deposits, epp_governance_log

### Vultr Git Repo Synced
  - Commit `2d30052`: savings protocol (CreateSavingsDeposit, WithdrawSavings, getSavingsBalance RPC)
  - 8 files committed, working tree clean

### Whitepaper Updated (chronx-docs commits 78512c0 + 02a61f3)
  - Section 4.7 Savings (principal guarantee)
  - L.10 wKX Provenance Architecture
  - L.11 Friendly Loans
  - Appendix M (Savings Lock Technical Reference + M.6 HSM Heartbeat Oracle)
  - Appendix N (Savings Guarantee Technical and Legal Basis)
