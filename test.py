import json

with open("test_set.json", "r") as f:
    test_set = json.load(f)
with open("dtangira.json", "w") as f:
    json.dump(test_set, f, ensure_ascii=False, indent=4)

print(test_set[0]['predicted_label'])