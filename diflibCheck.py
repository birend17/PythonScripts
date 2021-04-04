import difflib
text1 = """Lorem ipsum dolor sit amet, consectetuer adipiscing elit."""
text2 = """Lorem ipsum dolor sit amet, birend consectetuer adipiscing elit."""

seq=difflib.SequenceMatcher(None,text2, text1,autojunk=True)
# d=seq.ratio()*100
# print (d)

seq1 = seq.get_matching_blocks()

print(seq1)
