"""Auditable passage matching; accent folding is for alignment, not source editing."""
import re
import unicodedata as ud

POLICY = 'long_unique_accent_alignment_v1'


def spaced(text):
    chars, spans = [], []
    last = None
    for token in re.finditer(r'\S+', text):
        if last is not None:
            chars.append(' '); spans.append((last, token.start()))
        for i in range(token.start(), token.end()):
            chars.append(text[i]); spans.append((i,i+1))
        last=token.end()
    return ''.join(chars),spans


def folded(text, spans):
    chars, positions = [], []
    i=0
    while i<len(text):
        end=i+1
        while end<len(text) and ud.combining(text[end]):
            end+=1
        cluster=text[i:end]
        name=ud.name(text[i],'')
        eligible=any(script in name for script in ('LATIN','CYRILLIC','GREEK'))
        value=ud.normalize('NFD',cluster) if eligible else cluster
        if eligible:
            value=''.join(c for c in value if ud.category(c)!='Mn')
        for c in value:
            chars.append(c);positions.append((spans[i][0],spans[end-1][1]))
        i=end
    return ''.join(chars),positions


def match(quotation, block, allow_accents=False):
    if not quotation.strip():
        return None
    start=block.find(quotation)
    if start>=0:
        return {'kind':'verbatim','source_start':start,'source_end':start+len(quotation),
                'source_quotation':quotation,'submitted_quotation':quotation}
    q,_=spaced(quotation);s,spans=spaced(block)
    start=s.find(q)
    if start>=0:
        a,b=spans[start][0],spans[start+len(q)-1][1]
        return {'kind':'whitespace','source_start':a,'source_end':b,
                'source_quotation':block[a:b],'submitted_quotation':quotation}
    # Fallback is deliberately confined to substantial passages, not words.
    if not allow_accents or len(q)<40 or len(q.split())<6:
        return None
    fq,_=folded(q,[(i,i+1) for i in range(len(q))]);fs,mapping=folded(s,spans)
    start=fs.find(fq)
    if start<0 or fs.find(fq,start+1)>=0:
        return None
    a,b=mapping[start][0],mapping[start+len(fq)-1][1]
    source=block[a:b]
    nq=ud.normalize('NFC',q);ns=ud.normalize('NFC',spaced(source)[0])
    if len(nq)!=len(ns):
        return None
    differences=[{'quotation_character':x,'source_character':y,'normalized_position':i}
                 for i,(x,y) in enumerate(zip(nq,ns)) if x!=y]
    letters=sum(c.isalpha() for c in nq)
    if not differences or len(differences)>2 or len(differences)>letters*0.05:
        return None
    return {'kind':'accent_alignment','policy':POLICY,'source_start':a,'source_end':b,
            'source_quotation':source,'submitted_quotation':quotation,'differences':differences}
