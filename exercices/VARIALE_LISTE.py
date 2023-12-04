def saisir_notes():
    notes = []

    while True:
        note = float(input("entrer une note (ou une note negative pour arreter la saisie): "))
        while note > 20:
            note = float(input("error ! saisir une note valise : "))
        if note < 0:
            break
        notes.append(note)
        return notes
    
def note_maximal(notes):
    max_note = float
    for note in notes:
        if note < max_note:
            max_note = note

        return notes

def note_minimal(notes):
    min_note = 21
    for note in notes :
        if note < min_note:
            min_note = note
        
        return min_note
    
def moyenne_notes(notes):
    total = 0
    total_notes = 0
    for note in notes: 
        total += note

        return total / total_notes
    
def main():
    notes = saisir_notes

    print(f"la note maximale est {note_maximal(notes)}")
    print(f"la note minimale est : {note_minimal(notes)}")
    print(f"la moyenne dess notes est : {moyenne_notes(notes)}")

main()