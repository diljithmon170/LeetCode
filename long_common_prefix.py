# strs=["flower","flow","flowight"]
# pref=strs[0]
# pref_len=[len(pref)]
# for s in strs[1:]:
#     while pref != s[0:pref_len]:
#         pref_len -= 1
#         if pref_len == 0:
#             print()
#         pref = pref[0:pref_len]
# print(pref)


strs = ["flower", "flow", "flowight"]
pref = strs[0]
pref_len = len(pref)  # Fix: Change to integer, not a list

for s in strs[1:]:
    while pref != s[0:pref_len]:  # Fix: pref_len should be an integer
        pref_len -= 1
        if pref_len == 0:
            # print("")  # This means no common prefix
            pref = ""   # Fix: Assign empty string when no common prefix
            break       # Exit while loop when no common prefix
        pref = pref[0:pref_len]  # Shorten the prefix as we find a match
print()
print(pref)


