import random

questions = [
    ["What is the 2nd degree of the C major scale?", "D"],
    ["What is the 3rd degree of the C major scale?", "E"],
    ["What is the 4th degree of the C major scale?", "F"],
    ["What is the 5th degree of the C major scale?", "G"],
    ["What is the 6th degree of the C major scale?", "A"],
    ["What is the 7th degree of the C major scale?", "B"],
    ["What is the 9th degree of the C major scale?", "D"],
    ["What is the 11th degree of the C major scale?", "F"],
    ["What is the 13th degree of the C major scale?", "A"],
    ["What is the 2nd degree of the A minor scale?", "B"],
    ["What is the 3rd degree of the A minor scale?", "C"],
    ["What is the 4th degree of the A minor scale?", "D"],
    ["What is the 5th degree of the A minor scale?", "E"],
    ["What is the 6th degree of the A minor scale?", "F"],
    ["What is the 7th degree of the A minor scale?", "G"],
    ["What is the 9th degree of the A minor scale?", "B"],
    ["What is the 11th degree of the A minor scale?", "D"],
    ["What is the 13th degree of the A minor scale?", "F"],
    ["What is the 2nd degree of the G major scale?", "A"],
    ["What is the 3rd degree of the G major scale?", "B"],
    ["What is the 4th degree of the G major scale?", "C"],
    ["What is the 5th degree of the G major scale?", "D"],
    ["What is the 6th degree of the G major scale?", "E"],
    ["What is the 7th degree of the G major scale?", "F#"],
    ["What is the 9th degree of the G major scale?", "A"],
    ["What is the 11th degree of the G major scale?", "C"],
    ["What is the 13th degree of the G major scale?", "E"],
    ["What is the 2nd degree of the E minor scale?", "F#"],
    ["What is the 3rd degree of the E minor scale?", "G"],
    ["What is the 4th degree of the E minor scale?", "A"],
    ["What is the 5th degree of the E minor scale?", "B"],
    ["What is the 6th degree of the E minor scale?", "C"],
    ["What is the 7th degree of the E minor scale?", "D"],
    ["What is the 9th degree of the E minor scale?", "F#"],
    ["What is the 11th degree of the E minor scale?", "A"],
    ["What is the 13th degree of the E minor scale?", "C"],
    ["What is the 2nd degree of the D major scale?", "E"],
    ["What is the 3rd degree of the D major scale?", "F#"],
    ["What is the 4th degree of the D major scale?", "G"],
    ["What is the 5th degree of the D major scale?", "A"],
    ["What is the 6th degree of the D major scale?", "B"],
    ["What is the 7th degree of the D major scale?", "C#"],
    ["What is the 9th degree of the D major scale?", "E"],
    ["What is the 11th degree of the D major scale?", "G"],
    ["What is the 13th degree of the D major scale?", "B"],
    ["What is the 2nd degree of the B minor scale?", "C#"],
    ["What is the 3rd degree of the B minor scale?", "D"],
    ["What is the 4th degree of the B minor scale?", "E"],
    ["What is the 5th degree of the B minor scale?", "F#"],
    ["What is the 6th degree of the B minor scale?", "G"],
    ["What is the 7th degree of the B minor scale?", "A"],
    ["What is the 9th degree of the B minor scale?", "C#"],
    ["What is the 11th degree of the B minor scale?", "E"],
    ["What is the 13th degree of the B minor scale?", "G"],
    ["What is the 2nd degree of the A major scale?", "B"],
    ["What is the 3rd degree of the A major scale?", "C#"],
    ["What is the 4th degree of the A major scale?", "D"],
    ["What is the 5th degree of the A major scale?", "E"],
    ["What is the 6th degree of the A major scale?", "F#"],
    ["What is the 7th degree of the A major scale?", "G#"],
    ["What is the 9th degree of the A major scale?", "B"],
    ["What is the 11th degree of the A major scale?", "D"],
    ["What is the 13th degree of the A major scale?", "F#"],
    ["What is the 2nd degree of the F# minor scale?", "G#"],
    ["What is the 3rd degree of the F# minor scale?", "A"],
    ["What is the 4th degree of the F# minor scale?", "B"],
    ["What is the 5th degree of the F# minor scale?", "C#"],
    ["What is the 6th degree of the F# minor scale?", "D"],
    ["What is the 7th degree of the F# minor scale?", "E"],
    ["What is the 9th degree of the F# minor scale?", "G#"],
    ["What is the 11th degree of the F# minor scale?", "B"],
    ["What is the 13th degree of the F# minor scale?", "D"],
    ["What is the 2nd degree of the E major scale?", "F#"],
    ["What is the 3rd degree of the E major scale?", "G#"],
    ["What is the 4th degree of the E major scale?", "A"],
    ["What is the 5th degree of the E major scale?", "B"],
    ["What is the 6th degree of the E major scale?", "C#"],
    ["What is the 7th degree of the E major scale?", "D#"],
    ["What is the 9th degree of the E major scale?", "F#"],
    ["What is the 11th degree of the E major scale?", "A"],
    ["What is the 13th degree of the E major scale?", "C#"],
    ["What is the 2nd degree of the C# minor scale?", "D#"],
    ["What is the 3rd degree of the C# minor scale?", "E"],
    ["What is the 4th degree of the C# minor scale?", "F#"],
    ["What is the 5th degree of the C# minor scale?", "G#"],
    ["What is the 6th degree of the C# minor scale?", "A"],
    ["What is the 7th degree of the C# minor scale?", "B"],
    ["What is the 9th degree of the C# minor scale?", "D#"],
    ["What is the 11th degree of the C# minor scale?", "F#"],
    ["What is the 13th degree of the C# minor scale?", "A"],
    ["What is the 2nd degree of the B major scale?", "C#"],
    ["What is the 3rd degree of the B major scale?", "D#"],
    ["What is the 4th degree of the B major scale?", "E"],
    ["What is the 5th degree of the B major scale?", "F#"],
    ["What is the 6th degree of the B major scale?", "G#"],
    ["What is the 7th degree of the B major scale?", "A#"],
    ["What is the 9th degree of the B major scale?", "C#"],
    ["What is the 11th degree of the B major scale?", "E"],
    ["What is the 13th degree of the B major scale?", "G#"],
    ["What is the 2nd degree of the G# minor scale?", "A#"],
    ["What is the 3rd degree of the G# minor scale?", "B"],
    ["What is the 4th degree of the G# minor scale?", "C#"],
    ["What is the 5th degree of the G# minor scale?", "D#"],
    ["What is the 6th degree of the G# minor scale?", "E"],
    ["What is the 7th degree of the G# minor scale?", "F#"],
    ["What is the 9th degree of the G# minor scale?", "A#"],
    ["What is the 11th degree of the G# minor scale?", "C#"],
    ["What is the 13th degree of the G# minor scale?", "E"],
    ["What is the 2nd degree of the F# major scale?", "G#"],
    ["What is the 3rd degree of the F# major scale?", "A#"],
    ["What is the 4th degree of the F# major scale?", "B"],
    ["What is the 5th degree of the F# major scale?", "C#"],
    ["What is the 6th degree of the F# major scale?", "D#"],
    ["What is the 7th degree of the F# major scale?", "E#"],
    ["What is the 9th degree of the F# major scale?", "G#"],
    ["What is the 11th degree of the F# major scale?", "B"],
    ["What is the 13th degree of the F# major scale?", "D#"],
    ["What is the 2nd degree of the D# minor scale?", "E#"],
    ["What is the 3rd degree of the D# minor scale?", "F#"],
    ["What is the 4th degree of the D# minor scale?", "G#"],
    ["What is the 5th degree of the D# minor scale?", "A#"],
    ["What is the 6th degree of the D# minor scale?", "B"],
    ["What is the 7th degree of the D# minor scale?", "C#"],
    ["What is the 9th degree of the D# minor scale?", "E#"],
    ["What is the 11th degree of the D# minor scale?", "G#"],
    ["What is the 13th degree of the D# minor scale?", "B"],
    ["What is the 2nd degree of the F major scale?", "G"],
    ["What is the 3rd degree of the F major scale?", "A"],
    ["What is the 4th degree of the F major scale?", "Bb"],
    ["What is the 5th degree of the F major scale?", "C"],
    ["What is the 6th degree of the F major scale?", "D"],
    ["What is the 7th degree of the F major scale?", "E"],
    ["What is the 9th degree of the F major scale?", "G"],
    ["What is the 11th degree of the F major scale?", "Bb"],
    ["What is the 13th degree of the F major scale?", "D"],
    ["What is the 2nd degree of the D minor scale?", "E"],
    ["What is the 3rd degree of the D minor scale?", "F"],
    ["What is the 4th degree of the D minor scale?", "G"],
    ["What is the 5th degree of the D minor scale?", "A"],
    ["What is the 6th degree of the D minor scale?", "Bb"],
    ["What is the 7th degree of the D minor scale?", "C"],
    ["What is the 9th degree of the D minor scale?", "E"],
    ["What is the 11th degree of the D minor scale?", "G"],
    ["What is the 13th degree of the D minor scale?", "Bb"],
    ["What is the 2nd degree of the Bb major scale?", "C"],
    ["What is the 3rd degree of the Bb major scale?", "D"],
    ["What is the 4th degree of the Bb major scale?", "Eb"],
    ["What is the 5th degree of the Bb major scale?", "F"],
    ["What is the 6th degree of the Bb major scale?", "G"],
    ["What is the 7th degree of the Bb major scale?", "A"],
    ["What is the 9th degree of the Bb major scale?", "C"],
    ["What is the 11th degree of the Bb major scale?", "Eb"],
    ["What is the 13th degree of the Bb major scale?", "G"],
    ["What is the 2nd degree of the G minor scale?", "A"],
    ["What is the 3rd degree of the G minor scale?", "Bb"],
    ["What is the 4th degree of the G minor scale?", "C"],
    ["What is the 5th degree of the G minor scale?", "D"],
    ["What is the 6th degree of the G minor scale?", "Eb"],
    ["What is the 7th degree of the G minor scale?", "F"],
    ["What is the 9th degree of the G minor scale?", "A"],
    ["What is the 11th degree of the G minor scale?", "C"],
    ["What is the 13th degree of the G minor scale?", "Eb"],
    ["What is the 2nd degree of the Eb major scale?", "F"],
    ["What is the 3rd degree of the Eb major scale?", "G"],
    ["What is the 4th degree of the Eb major scale?", "Ab"],
    ["What is the 5th degree of the Eb major scale?", "Bb"],
    ["What is the 6th degree of the Eb major scale?", "C"],
    ["What is the 7th degree of the Eb major scale?", "D"],
    ["What is the 9th degree of the Eb major scale?", "F"],
    ["What is the 11th degree of the Eb major scale?", "Ab"],
    ["What is the 13th degree of the Eb major scale?", "C"],
    ["What is the 2nd degree of the C minor scale?", "D"],
    ["What is the 3rd degree of the C minor scale?", "Eb"],
    ["What is the 4th degree of the C minor scale?", "F"],
    ["What is the 5th degree of the C minor scale?", "G"],
    ["What is the 6th degree of the C minor scale?", "Ab"],
    ["What is the 7th degree of the C minor scale?", "Bb"],
    ["What is the 9th degree of the C minor scale?", "D"],
    ["What is the 11th degree of the C minor scale?", "F"],
    ["What is the 13th degree of the C minor scale?", "Ab"],
    ["What is the 2nd degree of the Ab major scale?", "Bb"],
    ["What is the 3rd degree of the Ab major scale?", "C"],
    ["What is the 4th degree of the Ab major scale?", "Db"],
    ["What is the 5th degree of the Ab major scale?", "Eb"],
    ["What is the 6th degree of the Ab major scale?", "F"],
    ["What is the 7th degree of the Ab major scale?", "G"],
    ["What is the 9th degree of the Ab major scale?", "Bb"],
    ["What is the 11th degree of the Ab major scale?", "Db"],
    ["What is the 13th degree of the Ab major scale?", "F"],
    ["What is the 2nd degree of the F minor scale?", "G"],
    ["What is the 3rd degree of the F minor scale?", "Ab"],
    ["What is the 4th degree of the F minor scale?", "Bb"],
    ["What is the 5th degree of the F minor scale?", "C"],
    ["What is the 6th degree of the F minor scale?", "Db"],
    ["What is the 7th degree of the F minor scale?", "Eb"],
    ["What is the 9th degree of the F minor scale?", "G"],
    ["What is the 11th degree of the F minor scale?", "Bb"],
    ["What is the 13th degree of the F minor scale?", "Db"],
    ["What is the 2nd degree of the Db major scale?", "Eb"],
    ["What is the 3rd degree of the Db major scale?", "F"],
    ["What is the 4th degree of the Db major scale?", "Gb"],
    ["What is the 5th degree of the Db major scale?", "Ab"],
    ["What is the 6th degree of the Db major scale?", "Bb"],
    ["What is the 7th degree of the Db major scale?", "C"],
    ["What is the 9th degree of the Db major scale?", "Eb"],
    ["What is the 11th degree of the Db major scale?", "Gb"],
    ["What is the 13th degree of the Db major scale?", "Bb"],
    ["What is the 2nd degree of the Bb minor scale?", "C"],
    ["What is the 3rd degree of the Bb minor scale?", "Db"],
    ["What is the 4th degree of the Bb minor scale?", "Eb"],
    ["What is the 5th degree of the Bb minor scale?", "F"],
    ["What is the 6th degree of the Bb minor scale?", "Gb"],
    ["What is the 7th degree of the Bb minor scale?", "Ab"],
    ["What is the 9th degree of the Bb minor scale?", "C"],
    ["What is the 11th degree of the Bb minor scale?", "Eb"],
    ["What is the 13th degree of the Bb minor scale?", "Gb"],
    ["What is the 2nd degree of the Gb major scale?", "Ab"],
    ["What is the 3rd degree of the Gb major scale?", "Bb"],
    ["What is the 4th degree of the Gb major scale?", "Cb"],
    ["What is the 5th degree of the Gb major scale?", "Db"],
    ["What is the 6th degree of the Gb major scale?", "Eb"],
    ["What is the 7th degree of the Gb major scale?", "F"],
    ["What is the 9th degree of the Gb major scale?", "Ab"],
    ["What is the 11th degree of the Gb major scale?", "Cb"],
    ["What is the 13th degree of the Gb major scale?", "Eb"],
    ["What is the 2nd degree of the Eb minor scale?", "F"],
    ["What is the 3rd degree of the Eb minor scale?", "Gb"],
    ["What is the 4th degree of the Eb minor scale?", "Ab"],
    ["What is the 5th degree of the Eb minor scale?", "Bb"],
    ["What is the 6th degree of the Eb minor scale?", "Cb"],
    ["What is the 7th degree of the Eb minor scale?", "Db"],
    ["What is the 9th degree of the Eb minor scale?", "F"],
    ["What is the 11th degree of the Eb minor scale?", "Ab"],
    ["What is the 13th degree of the Eb minor scale?", "Cb"],
    [
        "What is the tonality of the chord built on the 1st degree of a major scale?",
        "major",
    ],
    [
        "What is the tonality of the chord built on the 2nd degree of a major scale?",
        "minor",
    ],
    [
        "What is the tonality of the chord built on the 3rd degree of a major scale?",
        "minor",
    ],
    [
        "What is the tonality of the chord built on the 4th degree of a major scale?",
        "major",
    ],
    [
        "What is the tonality of the chord built on the 5th degree of a major scale?",
        "major",
    ],
    [
        "What is the tonality of the chord built on the 6th degree of a major scale?",
        "minor",
    ],
    [
        "What is the tonality of the chord built on the 7th degree of a major scale?",
        "diminished",
    ],
    [
        "What is the tonality of the chord built on the 1st degree of a natural minor scale?",
        "minor",
    ],
    [
        "What is the tonality of the chord built on the 2nd degree of a natural minor scale?",
        "dimiinished",
    ],
    [
        "What is the tonality of the chord built on the 3rd degree of a natural minor scale?",
        "major",
    ],
    [
        "What is the tonality of the chord built on the 4th degree of a natural minor scale?",
        "minor",
    ],
    [
        "What is the tonality of the chord built on the 5th degree of a natural minor scale?",
        "minor",
    ],
    [
        "What is the tonality of the chord built on the 6th degree of a natural minor scale?",
        "major",
    ],
    [
        "What is the tonality of the chord built on the 7th degree of a natural minor scale?",
        "minor",
    ],
    ["A to A# ascending is a  interval", "m2"],
    ["A to B ascending is a  interval", "M2"],
    ["A to C ascending is a  interval", "m3"],
    ["A to C# ascending is a  interval", "M3"],
    ["A to D ascending is a  interval", "P4"],
    ["A to D# ascending is a  interval", "TT"],
    ["A to E ascending is a  interval", "P5"],
    ["A to F ascending is a  interval", "m6"],
    ["A to F# ascending is a  interval", "M6"],
    ["A to G ascending is a  interval", "m7"],
    ["A to G# ascending is a  interval", "M7"],
    ["A to Ab descending is a  interval", "m2"],
    ["A to G descending is a  interval", "M2"],
    ["A to Gb descending is a  interval", "m3"],
    ["A to F descending is a  interval", "M3"],
    ["A to E descending is a  interval", "P4"],
    ["A to Eb descending is a  interval", "TT"],
    ["A to D descending is a  interval", "P5"],
    ["A to Db descending is a  interval", "m6"],
    ["A to C descending is a  interval", "M6"],
    ["A to B descending is a  interval", "m7"],
    ["A to Bb descending is a  interval", "M7"],
    ["The major key with one sharp note?", "G"],
    ["The major key with two sharp notes?", "D"],
    ["The major key with three sharp notes?", "A"],
    ["The major key with four sharp notes?", "E"],
    ["The major key with five sharp notes?", "B"],
    ["The major key with six sharp notes?", "F#"],
    ["The minor key with one sharp note?", "E"],
    ["The minor key with two sharp notes?", "B"],
    ["The minor key with three sharp notes?", "F#"],
    ["The minor key with four sharp notes?", "C#"],
    ["The minor key with five sharp notes?", "G#"],
    ["The minor key with six sharp notes?", "D#"],
    ["The major key with one flat note?", "F"],
    ["The major key with two flat notes?", "Bb"],
    ["The major key with three flat notes?", "Eb"],
    ["The major key with four flat notes?", "Ab"],
    ["The major key with five flat notes?", "Db"],
    ["The major key with six flat notes?", "Gb"],
    ["The minor key with one flat note?", "D"],
    ["The minor key with two flat notes?", "G"],
    ["The minor key with three flat notes?", "C"],
    ["The minor key with four flat notes?", "F"],
    ["The minor key with five flat notes?", "Bb"],
    ["The minor key with six flat notes?", "Eb"],
    ["The flat note in the key of F major?", "Bb"],
    # ["The flat note in the key of G minor?", "Bb"],
    ["The flat notes in the key of Bb major are ", "Bb, Eb"],
    ["The flat notes in the key of Eb major are ", "Bb, Eb, Ab"],
    ["The flat notes in the key of Ab major are ", "Bb, Eb, Ab, Db"],
    ["The flat notes in the key of Db major are ", "Bb, Eb, Ab, Db, Gb"],
    ["The flat notes in the key of Gb major are ", "Bb, Eb, Ab, Db, Gb, Cb"],
    ["The sharp note in the key of G major?", "F#"],
    # ["The sharp note in the key of e minor?", "F#"],
    ["The sharp notes in the key of D major are ", "F#, C#"],
    ["The sharp notes in the key of A major are ", "F#, C#, G#"],
    ["The sharp notes in the key of E major are ", "F#, C#, G#, D#"],
    ["The sharp notes in the key of B major are ", "F#, C#, G#, D#, A#"],
    ["The sharp notes in the key of F# major are ", "F#, C#, G#, D#, A#, E#"],
    ["This mode has a b3 and a b7 relative to the major scale", "dorian"],
    [
        "This mode has a b2, a b3, a b6, and a b7 relative to the major scale",
        "phrygian",
    ],
    ["This mode has a #4 relative to the major scale", "lydian"],
    ["This mode has a b7 relative to the major scale", "mixolydian"],
    ["This mode has a b3, a b6, and a b7 relative to the major scale", "aeolian"],
    [
        "This mode has a b2, a b3, a b5, a b6, and a b7 relative to the major scale",
        "lochrian",
    ],
    ["The relative minor of C major?", "A"],
    ["The relative minor of G major?", "E"],
    ["The relative minor of D major?", "B"],
    ["The relative minor of A major?", "F#"],
    ["The relative minor of E major?", "C#"],
    ["The relative minor of B major?", "G#"],
    ["The relative minor of F# major?", "D#"],
    ["The relative major of A minor?", "C"],
    ["The relative major of E minor?", "G"],
    ["The relative major of B minor?", "D"],
    ["The relative major of F# minor?", "A"],
    ["The relative major of C# minor?", "E"],
    ["The relative major of G# minor?", "B"],
    ["The relative major of D# minor?", "F#"],
    ["The relative minor of F major?", "D"],
    ["The relative minor of Bb major?", "G"],
    ["The relative minor of Eb major?", "C"],
    ["The relative minor of Ab major?", "F"],
    ["The relative minor of Db major?", "Bb"],
    ["The relative minor of Gb major?", "Eb"],
    ["The relative major of D minor?", "F"],
    ["The relative major of G minor?", "Bb"],
    ["The relative major of C minor?", "Eb"],
    ["The relative major of F minor?", "Ab"],
    ["The relative major of Bb minor?", "Db"],
    ["The relative major of Eb minor?", "Gb"],
    ["The Ionian mode is built on this degree of the major scale", "first"],
    ["The Dorian mode is built on this degree of the major scale", "second"],
    ["The Phrygian mode is built on this degree of the major scale", "third"],
    ["The Lydian mode is built on this degree of the major scale", "fourth"],
    ["The Mixolydian mode is built on this degree of the major scale", "fifth"],
    ["The Aeolian mode is built on this degree of the major scale", "sixth"],
    ["The Lochrian mode is built on this degree of the major scale", "seventh"],
    ["The Dorian mode contains ", "b3, b7"],
    ["The Phrygian mode contains ", "b2, b3, b6, b7"],
    ["The Lydian mode contains ", "#4"],
    ["The Mixolydian mode contains ", "b7"],
    ["The Aeolian mode contains ", "b3, b6, b7"],
    ["The Lochrian mode contains ", "b2, b3, b5, b6, b7"],
    ["The third of a Ab major chord?", "C"],
    ["The third of a A major chord?", "C#"],
    ["The third of a Bb major chord?", "D"],
    ["The third of a B major chord?", "D#"],
    ["The third of a C major chord?", "E"],
    ["The third of a Db major chord?", "F"],
    ["The third of a D major chord?", "F#"],
    ["The third of a Eb major chord?", "G"],
    ["The third of a E major chord?", "G#"],
    ["The third of a F major chord?", "A"],
    ["The third of a F# major chord?", "A#"],
    ["The third of a Gb major chord?", "Bb"],
    ["The third of a G major chord?", "B"],
    ["The fifth of a Ab major chord?", "Eb"],
    ["The fifth of a A major chord?", "E"],
    ["The fifth of a Bb major chord?", "F"],
    ["The fifth of a B major chord?", "F#"],
    ["The fifth of a C major chord?", "G"],
    ["The fifth of a Db major chord?", "Ab"],
    ["The fifth of a D major chord?", "A"],
    ["The fifth of a Eb major chord?", "Bb"],
    ["The fifth of a E major chord?", "B"],
    ["The fifth of a F major chord?", "C"],
    ["The fifth of a F# major chord?", "C#"],
    ["The fifth of a Gb major chord?", "Db"],
    ["The fifth of a G major chord?", "D"],
    ["The third of a A minor chord?", "C"],
    ["The third of a Bb minor chord?", "Db"],
    ["The third of a B minor chord?", "D"],
    ["The third of a C minor chord?", "Eb"],
    ["The third of a C# minor chord?", "E"],
    ["The third of a D minor chord?", "F"],
    ["The third of a D# minor chord?", "F#"],
    ["The third of a Eb minor chord?", "Gb"],
    ["The third of a E minor chord?", "G"],
    ["The third of a F minor chord?", "Ab"],
    ["The third of a F# minor chord?", "A"],
    ["The third of a G minor chord?", "Bb"],
    ["The third of a G# minor chord?", "B"],
    ["The fifth of a A minor chord?", "E"],
    ["The fifth of a Bb minor chord?", "F"],
    ["The fifth of a B minor chord?", "F#"],
    ["The fifth of a C minor chord?", "G"],
    ["The fifth of a C# minor chord?", "G#"],
    ["The fifth of a D minor chord?", "A"],
    ["The fifth of a D# minor chord?", "A#"],
    ["The fifth of a Eb minor chord?", "Bb"],
    ["The fifth of a E minor chord?", "B"],
    ["The fifth of a F minor chord?", "C"],
    ["The fifth of a F# minor chord?", "C#"],
    ["The fifth of a G minor chord?", "D"],
    ["The fifth of a G# minor chord?", "D#"],
    ["The third of a A diminished chord?", "C"],
    ["The third of a A# diminished chord?", "C#"],
    ["The third of a B diminished chord?", "D"],
    ["The third of a C diminished chord?", "Eb"],
    ["The third of a C# diminished chord?", "E"],
    ["The third of a D diminished chord?", "F"],
    ["The third of a D# diminished chord?", "F#"],
    ["The third of a E diminished chord?", "G"],
    ["The third of a F# diminished chord?", "A"],
    ["The third of a G diminished chord?", "Bb"],
    ["The third of a G# diminished chord?", "B"],
    ["The fifth of a A diminished chord?", "Eb"],
    ["The fifth of a A# diminished chord?", "E"],
    ["The fifth of a B diminished chord?", "F"],
    ["The fifth of a C diminished chord?", "Gb"],
    ["The fifth of a C# diminished chord?", "G"],
    ["The fifth of a D diminished chord?", "Ab"],
    ["The fifth of a D# diminished chord?", "A"],
    ["The fifth of a E diminished chord?", "Bb"],
    ["The fifth of a F# diminished chord?", "C"],
    ["The fifth of a G diminished chord?", "Db"],
    ["The fifth of a G# diminished chord?", "D"],
    # ["There are  semitones in a perfect fourth interval", ""],
    # ["The note a perfect fifth above D?", "A"],
    # ["The major key where the chords Em and F#m are diatonic?", "D"],
    # ["The minor key where the chords the chords Em and F#m are diatonic is", "B"],
    # ["The major key where F#m is the 6th chord?", "A"],
    # ["The minor key where F is the 6th chord is", "A"],
    # ["The seventh of a Ab major chord?", "D"],
    # ["The seventh of a A major chord?", ""],
    # ["The seventh of a Bb major chord?", ""],
    # ["The seventh of a B major chord?", ""],
    # ["The seventh of a C major chord?", ""],
    # ["The seventh of a Db major chord?", ""],
    # ["The seventh of a D major chord?", ""],
    # ["The seventh of a Eb major chord?", ""],
    # ["The seventh of a E major chord?", ""],
    # ["The seventh of a Fmajor chord?", ""],
    # ["The seventh of a F# major chord?", ""],
    # ["The seventh of a Gb major chord?", ""],
    # ["The seventh of a G major chord?", ""],
    # ["The seventh of a A minor chord?", ""],
    # ["The seventh of a Bb minor chord?", ""],
    # ["The seventh of a B minor chord?", ""],
    # ["The seventh of a C minor chord?", ""],
    # ["The seventh of a C# minor chord?", ""],
    # ["The seventh of a D minor chord?", ""],
    # ["The seventh of a D# minor chord?", ""],
    # ["The seventh of a Eb minor chord?", ""],
    # ["The seventh of a E minor chord?", ""],
    # ["The seventh of a F minor chord?", ""],
    # ["The seventh of a F# minor chord?", ""],
    # ["The seventh of a G minor chord?", ""],
    # ["The seventh of a G# minor chord?", ""],
    # ["The seventh of a A diminished chord?", ""],
    # ["The seventh of a A# diminished chord?", ""],
    # ["The seventh of a B diminished chord?", ""],
    # ["The seventh of a C diminished chord?", ""],
    # ["The seventh of a C# diminished chord?", ""],
    # ["The seventh of a D diminished chord?", ""],
    # ["The seventh of a D# diminished chord?", ""],
    # ["The seventh of a E diminished chord?", ""],
    # ["The fifth of a F diminished chord?", ""],
    # ["The seventh of a F# diminished chord?", ""],
    # ["The seventh of a G diminished chord?", ""],
    # ["The seventh of a G# diminished chord?", ""],
]

questions = sorted(questions, key=lambda _: random.random())
