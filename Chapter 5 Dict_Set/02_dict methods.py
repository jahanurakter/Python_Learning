marks = {
    "Maya": 99,
    "Jahan": 80,
    "Jeffy": 50
}
print(marks.items())
print(marks.get("Daisy")) #prints None
print(marks["Daisy"]) #Returns Error
marks.update({"Maya": 80})
print(marks)
print(marks.keys())
print(marks.values())
print(marks.popitem())
print(marks.clear)
marks.setdefault("Daisy", 25)
print(len(marks))
print(sorted(marks))