#!/usr/bin/env python3
"""Build whitepaper v6.4 from v6.3 unpacked docx."""
import zipfile, os, shutil, re

UNPACK = "unpacked_v6_3"
OUTPUT = "chronx-whitepaper-v6_4.docx"
ORIGINAL = "chronx-whitepaper-v6_3.docx"

# Helper: make a normal paragraph
def para(text, bold=False, color=None, size=24, italic=False):
    rpr = '<w:rPr><w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/>'
    if bold: rpr += '<w:b/><w:bCs/>'
    if italic: rpr += '<w:i/><w:iCs/>'
    if color: rpr += f'<w:color w:val="{color}"/>'
    rpr += f'<w:sz w:val="{size}"/><w:szCs w:val="{size}"/></w:rPr>'
    escaped = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('"', '&quot;')
    return f'<w:p><w:pPr><w:spacing w:before="120" w:after="120"/></w:pPr><w:r>{rpr}<w:t xml:space="preserve">{escaped}</w:t></w:r></w:p>'

def heading1(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Heading1"/><w:spacing w:before="360" w:after="120"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/><w:b/><w:bCs/><w:sz w:val="32"/><w:szCs w:val="32"/></w:rPr><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'

def heading2(text):
    return f'<w:p><w:pPr><w:pStyle w:val="Heading2"/><w:spacing w:before="280" w:after="80"/></w:pPr><w:r><w:rPr><w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/><w:b/><w:bCs/><w:sz w:val="26"/><w:szCs w:val="26"/></w:rPr><w:t xml:space="preserve">{text}</w:t></w:r></w:p>'

def table_row(cells, bold=False, bg=None):
    """Build a table row with 3 cells."""
    row = '<w:tr>'
    for cell_text in cells:
        tc = '<w:tc><w:tcPr><w:tcW w:w="0" w:type="auto"/>'
        if bg:
            tc += f'<w:shd w:val="clear" w:color="auto" w:fill="{bg}"/>'
        tc += '</w:tcPr>'
        rpr = '<w:rPr><w:rFonts w:ascii="Arial" w:cs="Arial" w:eastAsia="Arial" w:hAnsi="Arial"/><w:sz w:val="18"/><w:szCs w:val="18"/>'
        if bold:
            rpr += '<w:b/><w:bCs/>'
        rpr += '</w:rPr>'
        escaped = cell_text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        tc += f'<w:p><w:r>{rpr}<w:t xml:space="preserve">{escaped}</w:t></w:r></w:p></w:tc>'
        row += tc
    row += '</w:tr>'
    return row

# Read document.xml
doc_path = os.path.join(UNPACK, "word", "document.xml")
with open(doc_path, 'r', encoding='utf-8') as f:
    content = f.read()

changes = 0

# 1. Update version: v6.2 -> v6.4 and v6.3 -> v6.4
content = content.replace('Whitepaper v6.2', 'Whitepaper v6.4')
content = content.replace('Whitepaper v6.3', 'Whitepaper v6.4')
content = content.replace('whitepaper v6.2', 'whitepaper v6.4')
content = content.replace('whitepaper v6.3', 'whitepaper v6.4')
changes += 1
print("1. Version updated to v6.4")

# 2. Build Appendix B XML
page_break = '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'

appendix = page_break
appendix += heading1("Appendix B — Loan Status Flag Reference")
appendix += para(
    "Lenders may optionally record status flags on their loan records. "
    "Flags are the unilateral declaration of the recording party and represent their position only. "
    "Flags are permanent but may be superseded by subsequent flags. The current loan status reflects "
    "the most recently recorded flag. The complete flag history is always visible on-chain. Borrowers "
    "retain the right to record a DISPUTED flag at any time. ChronX Protocol makes no independent "
    "verification of any flag, takes no position on its accuracy, and expressly disclaims any role in "
    "credit reporting, debt collection, or dispute resolution."
)

# Flag table
flags = [
    ("OFFERED", "Protocol", "Offer created, awaiting acceptance"),
    ("ACTIVE", "Protocol", "Funds disbursed, payments current"),
    ("PAID_OFF", "Protocol", "Fully repaid"),
    ("EARLY_EXIT", "Protocol", "Exited before term end"),
    ("COLLATERAL_CALLED", "Protocol", "Collateral lock triggered"),
    ("EXPIRED", "Protocol", "Offer expired before acceptance"),
    ("WITHDRAWN", "Protocol", "Lender withdrew before acceptance"),
    ("LATE", "Lender", "Payment past due within grace period"),
    ("DELINQUENT", "Lender", "Payment significantly overdue"),
    ("DEFAULT", "Lender", "Formal default declared"),
    ("ACCELERATED", "Lender", "Full balance called due immediately"),
    ("WRITTEN_OFF", "Lender", "Declared uncollectable"),
    ("REINSTATED", "Lender", "Restored to good standing after default"),
    ("SETTLED", "Lender", "Resolved for less than full balance"),
    ("FORGIVEN", "Lender", "Remaining balance forgiven"),
    ("TRANSFERRED", "Lender", "Assigned to new lender"),
    ("REFINANCED", "Lender", "Replaced by new loan"),
    ("BANKRUPTCY", "Borrower", "Self-reported bankruptcy filing"),
    ("BANKRUPTCY_DISCHARGED", "Borrower", "Bankruptcy case closed"),
    ("INSOLVENCY", "Borrower", "Self-reported insolvency"),
    ("DISPUTED", "Borrower", "Contests an adverse lender flag"),
    ("LITIGATION_PENDING", "Either party", "Legal proceedings initiated"),
    ("JUDGMENT", "Either party", "Court ruling self-reported"),
    ("GARNISHMENT", "Either party", "Court-ordered collection"),
    ("AMENDED", "Both parties", "Terms modified by mutual consent"),
    ("FORBEARANCE", "Both parties", "Temporary payment relief"),
    ("DEFERRAL", "Both parties", "Specific payments postponed"),
    ("FROZEN", "Governance", "Suspended by Foundation action"),
    ("UNDER_REVIEW", "Governance", "Flagged for administrative review"),
]

table_xml = '<w:tbl><w:tblPr><w:tblW w:w="5000" w:type="pct"/><w:tblBorders>'
for border in ['top', 'left', 'bottom', 'right', 'insideH', 'insideV']:
    table_xml += f'<w:{border} w:val="single" w:sz="4" w:space="0" w:color="999999"/>'
table_xml += '</w:tblBorders></w:tblPr>'

# Header row
table_xml += table_row(["Flag", "Set By", "Description"], bold=True, bg="1A1A2E")

# Data rows
for flag, setter, desc in flags:
    table_xml += table_row([flag, setter, desc])

table_xml += '</w:tbl>'
appendix += table_xml

# Signing authority disclaimer
appendix += para("")  # spacer
appendix += heading2("Signing Authority")
appendix += para(
    "Status flags are cryptographically signed by the posting wallet. The protocol enforces signing "
    "rules at the engine level \u2014 certain flags may only be posted by the lender, others only by "
    "the borrower, and some require both signatures. Automatic flags are generated by the protocol "
    "engine and cannot be posted by any wallet. A lender may optionally record various flags on loans "
    "they have issued. Borrowers may post one DISPUTED flag in response to any adverse lender flag. "
    "All flags are permanent but may be superseded. Jurisdiction-gated credit history publication is "
    "disabled by default and requires Foundation governance activation.",
    size=20
)

changes += 1
print("2. Appendix B built")

# 3. Insert before </w:body> but AFTER the sectPr
# The sectPr belongs to the last section. We insert appendix before the sectPr.
sect_idx = content.rfind('<w:sectPr>')
if sect_idx >= 0:
    content = content[:sect_idx] + appendix + content[sect_idx:]
    print("3. Appendix B inserted before final sectPr")
    changes += 1
else:
    # Fallback: insert before </w:body>
    body_end = content.rfind('</w:body>')
    content = content[:body_end] + appendix + content[body_end:]
    print("3. Appendix B inserted before </w:body> (fallback)")
    changes += 1

# Write updated document.xml
with open(doc_path, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"4. document.xml written ({len(content)} chars)")

# 4. Repack as docx (ZIP)
if os.path.exists(OUTPUT):
    os.remove(OUTPUT)

with zipfile.ZipFile(OUTPUT, 'w', zipfile.ZIP_DEFLATED) as zout:
    for root, dirs, files in os.walk(UNPACK):
        for fname in files:
            full_path = os.path.join(root, fname)
            arc_name = os.path.relpath(full_path, UNPACK)
            zout.write(full_path, arc_name)

size_kb = os.path.getsize(OUTPUT) / 1024
print(f"5. {OUTPUT} created ({size_kb:.1f} KB)")
print(f"Total changes: {changes}")

# Cleanup
shutil.rmtree(UNPACK)
print("6. Cleanup done")
