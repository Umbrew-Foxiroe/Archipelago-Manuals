# Object classes from AP that represent different types of options that you can create
from Options import FreeText, NumericOption, Toggle, DefaultOnToggle, Choice, TextChoice, Range, NamedRange

# These helper methods allow you to determine if an option has been set, or what its value is, for any player in the multiworld
from ..Helpers import is_option_enabled, get_option_value



####################################################################
# NOTE: At the time that options are created, Manual has no concept of the multiworld or its own world.
#       Options are defined before the world is even created.
#
# Example of creating your own option:
#
#   class MakeThePlayerOP(Toggle):
#       """Should the player be overpowered? Probably not, but you can choose for this to do... something!"""
#       display_name = "Make me OP"
#
#   options["make_op"] = MakeThePlayerOP
#
#
# Then, to see if the option is set, you can call is_option_enabled or get_option_value.
#####################################################################


# To add an option, use the before_options_defined hook below and something like this:
#   options["total_characters_to_win_with"] = TotalCharactersToWinWith
#

class TotalCharactersToWinWith(Range):
    """Instead of having to beat the game with all characters, you can limit locations to a subset of character victory locations."""
    display_name = "Number of characters to beat the game with before victory"
    range_start = 10
    range_end = 50
    default = 50

class mario_party_1(Toggle):
    """Enable or disable Mario Party 1"""
    display_name: "Mario Party 1"
class mario_party_2(DefaultOnToggle):
    """Enable or disable Mario Party 2"""
    display_name: "Mario Party 2"
class mario_party_3(DefaultOnToggle):
    """Enable or disable Mario Party 3"""
    display_name: "Mario Party 3"
class mario_party_4(DefaultOnToggle):
    """Enable or disable Mario Party 4"""
    display_name: "Mario Party 4"
class mario_party_5(DefaultOnToggle):
    """Enable or disable Mario Party 5"""
    display_name: "Mario Party 5"
class mario_party_6(DefaultOnToggle):
    """Enable or disable Mario Party 6"""
    display_name: "Mario Party 6"
class mario_party_7(DefaultOnToggle):
    """Enable or disable Mario Party 7"""
    display_name: "Mario Party 7"
class mario_party_8(DefaultOnToggle):
    """Enable or disable Mario Party 8"""
    display_name: "Mario Party 8"
class mario_party_ds(Toggle):
    """Enable or disable Mario Party DS (NOT YET IMPLEMENTED)"""
    display_name: "Mario Party DS"
class minigame_sanity(DefaultOnToggle):
    """Makes every minigame a check. (Up to roughly 563 extra locations.)"""
    display_name: "Mario Party Minigames"
class bonus_sanity(DefaultOnToggle):
    """Toggles the bonus / side minigames, typically found in the Extra menu."""
    display_name: "Mario Party Bonus Minigames"
class mic_sanity(DefaultOnToggle):
    """Toggle the Mic Game checks."""
    display_name: "Mario Party Mic Games"
class story_sanity(DefaultOnToggle):
    """Toggle the story modes of the games."""
    display_name: "Mario Party Story Mode"
class item_sanity(DefaultOnToggle):
    """Every item obtained is a check. (Roughly 138 locations.)"""
    display_name: "Mario Party Itemsanity"
class rare_item_sanity(DefaultOnToggle):
    """Add items that cannot be obtained through the shop or other reliable ways to item_sanity. Does nothing with it off."""
    display_name: "Mario Party Rare Items"
class mp3_partner_sanity(DefaultOnToggle):
    """Obtaining a partner is a check. Does nothing with MP3 off."""
    display_name: "Mario Party 3 Partners"
class mp7_character_orb_sanity(Toggle):
    """Add character specific orbs to itemsanity. Does nothing with it or MP7 off."""
    display_name: "Mario Party 7 Character Orbs"
# This is called before any manual options are defined, in case you want to define your own with a clean slate or let Manual define over them
def before_options_defined(options: dict) -> dict:
    options["mario_party_1"] = mario_party_1
    options["mario_party_2"] = mario_party_2
    options["mario_party_3"] = mario_party_3
    options["mario_party_4"] = mario_party_4
    options["mario_party_5"] = mario_party_5
    options["mario_party_6"] = mario_party_6
    options["mario_party_7"] = mario_party_7
    options["mario_party_8"] = mario_party_8
    options["mario_party_ds"] = mario_party_ds
    options["minigame_sanity"] = minigame_sanity
    options["bonus_sanity"] = bonus_sanity
    options["mic_sanity"] = mic_sanity
    options["story_sanity"] = story_sanity
    options["item_sanity"] = item_sanity
    options["rare_item_sanity"] = rare_item_sanity
    options["mp3_partner_sanity"] = mp3_partner_sanity
    options["mp7_character_orb_sanity"] = mp7_character_orb_sanity
    return options
# This is called after any manual options are defined, in case you want to see what options are defined or want to modify the defined options
def after_options_defined(options: dict) -> dict:
    return options