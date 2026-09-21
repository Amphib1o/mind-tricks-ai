import pretty_midi

print("Mind Tricks AI iniciado")

midi = pretty_midi.PrettyMIDI()

piano = pretty_midi.Instrument(program=0)

acordes = {
2
"trance": [57, 60, 64], # Am
3
"techno": [54, 57, 61], # F#m
4
"melodic": [52, 55, 59] # Em
5
} 

for nota in acorde:
    piano.notes.append(
        pretty_midi.Note(
            velocity=100,
            pitch=nota,
            start=0,
            end=2
        )
    )

midi.instruments.append(piano)

midi.write("generated_midis/primer_acorde.mid")

print("MIDI creado correctamente")