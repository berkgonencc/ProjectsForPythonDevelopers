"""
Mad Libs game

Ask the user for an input.

This could be anything such as a name, an adjective, a pronoun or even an action.
Once you get the input, you can rearrange it to build up your own story."""

noun = input("Noun: ")
noun2 = input("Plural noun: ")
noun3 = input("Noun: ")
place = input("Name a place: ")
adj = input("Adjective: ")
noun4 = input("Noun: ")

madlibs = f"Be kind your {noun} - footed {noun2}.\n" \
          f"For a duck may be somebody's {noun3},\n" \
          f"Be kind to your {noun2} in {place}\n" \
          f"Where the weather is always {adj}.\n" \
          f"\n" \
          f"You may think that is this the {noun},\n" \
          f"Well it is."

print(madlibs)
